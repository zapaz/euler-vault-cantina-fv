// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.13;

import {Test, console2, stdError} from "forge-std/Test.sol";
import {DeployPermit2} from "permit2/test/utils/DeployPermit2.sol";

import {GenericFactory} from "src/GenericFactory/GenericFactory.sol";

import {ProtocolConfig} from "src/ProtocolConfig/ProtocolConfig.sol";

import {Dispatch} from "src/EVault/Dispatch.sol";

import {Initialize} from "src/EVault/modules/Initialize.sol";
import {Token} from "src/EVault/modules/Token.sol";
import {Vault} from "src/EVault/modules/Vault.sol";
import {Borrowing} from "src/EVault/modules/Borrowing.sol";
import {Liquidation} from "src/EVault/modules/Liquidation.sol";
import {BalanceForwarder} from "src/EVault/modules/BalanceForwarder.sol";
import {Governance} from "src/EVault/modules/Governance.sol";
import {RiskManager} from "src/EVault/modules/RiskManager.sol";

// import {EVault} from "src/EVault/EVault.sol";
// import {ISimpleVault, IERC20} from "src/EVault/ISimpleVault.sol";
import {SimpleVault, ISimpleVault} from "src/EVault/SimpleVault.sol";

import {TypesLib} from "src/EVault/shared/types/Types.sol";
import {Base} from "src/EVault/shared/Base.sol";

import {EthereumVaultConnector} from "ethereum-vault-connector/EthereumVaultConnector.sol";

import {TestERC20} from "test/mocks/TestERC20.sol";
import {MockBalanceTracker} from "test/mocks/MockBalanceTracker.sol";
import {MockPriceOracle} from "test/mocks/MockPriceOracle.sol";
import {IRMTestDefault} from "test/mocks/IRMTestDefault.sol";
import {IHookTarget} from "src/interfaces/IHookTarget.sol";
import {SequenceRegistry} from "src/SequenceRegistry/SequenceRegistry.sol";

import {AssertionsCustomTypes} from "test/helpers/AssertionsCustomTypes.sol";

import "src/EVault/shared/Constants.sol";

contract SimpleVaultTest is AssertionsCustomTypes, Test, DeployPermit2 {
    EthereumVaultConnector public evc;
    address admin;
    address feeReceiver;
    address protocolFeeReceiver;
    ProtocolConfig protocolConfig;
    address balanceTracker;
    MockPriceOracle oracle;
    address unitOfAccount;
    address permit2;
    address sequenceRegistry;
    GenericFactory public factory;

    TestERC20 assetTST;

    ISimpleVault public eTST;

    address initializeModule;
    address tokenModule;
    address vaultModule;
    address borrowingModule;
    address liquidationModule;
    address riskManagerModule;
    address balanceForwarderModule;
    address governanceModule;

    Base.Integrations integrations;
    Dispatch.DeployedModules modules;

    function setUp() public virtual {
        admin = vm.addr(1000);
        feeReceiver = makeAddr("feeReceiver");
        protocolFeeReceiver = makeAddr("protocolFeeReceiver");
        factory = new GenericFactory(admin);

        evc = new EthereumVaultConnector();
        protocolConfig = new ProtocolConfig(admin, protocolFeeReceiver);
        balanceTracker = address(new MockBalanceTracker());
        oracle = new MockPriceOracle();
        unitOfAccount = address(1);
        permit2 = deployPermit2();
        sequenceRegistry = address(new SequenceRegistry());
        integrations =
            Base.Integrations(address(evc), address(protocolConfig), sequenceRegistry, balanceTracker, permit2);

        initializeModule = address(new Initialize(integrations));
        tokenModule = address(new Token(integrations));
        vaultModule = address(new Vault(integrations));
        borrowingModule = address(new Borrowing(integrations));
        liquidationModule = address(new Liquidation(integrations));
        riskManagerModule = address(new RiskManager(integrations));
        balanceForwarderModule = address(new BalanceForwarder(integrations));
        governanceModule = address(new Governance(integrations));

        modules = Dispatch.DeployedModules({
            initialize: initializeModule,
            token: tokenModule,
            vault: vaultModule,
            borrowing: borrowingModule,
            liquidation: liquidationModule,
            riskManager: riskManagerModule,
            balanceForwarder: balanceForwarderModule,
            governance: governanceModule
        });

        address evaultImpl = address(new SimpleVault(integrations, modules));

        vm.prank(admin);
        factory.setImplementation(evaultImpl);

        assetTST = new TestERC20("Test Token", "TST", 18, false);
        eTST = ISimpleVault(
            factory.createProxy(address(0), true, abi.encodePacked(address(assetTST), address(oracle), unitOfAccount))
        );
        eTST.setInterestRateModel(address(new IRMTestDefault()));
        eTST.setMaxLiquidationDiscount(0.2e4);
        eTST.setFeeReceiver(feeReceiver);
    }

    address internal SYNTH_VAULT_HOOK_TARGET = address(new MockHook());
    uint32 internal constant SYNTH_VAULT_HOOKED_OPS = OP_DEPOSIT | OP_MINT | OP_REDEEM | OP_SKIM | OP_REPAY_WITH_SHARES;

    function createSynthEVault(address asset) internal returns (ISimpleVault) {
        ISimpleVault v = ISimpleVault(
            factory.createProxy(address(0), true, abi.encodePacked(address(asset), address(oracle), unitOfAccount))
        );
        v.setInterestRateModel(address(new IRMTestDefault()));

        v.setInterestFee(1e4);

        v.setHookConfig(SYNTH_VAULT_HOOK_TARGET, SYNTH_VAULT_HOOKED_OPS);

        return v;
    }

    function getSubAccount(address primary, uint8 subAccountId) internal pure returns (address) {
        require(subAccountId <= 256, "invalid subAccountId");
        return address(uint160(uint160(primary) ^ subAccountId));
    }
}

contract MockHook is IHookTarget {
    error E_OnlyAssetCanDeposit();
    error E_OperationDisabled();

    function isHookTarget() external pure override returns (bytes4) {
        return this.isHookTarget.selector;
    }

    // deposit is only allowed for the asset
    function deposit(uint256, address) external view {
        address asset = ISimpleVault(msg.sender).asset();

        // these calls are just to test if there's no RO-reentrancy for the hook target
        ISimpleVault(msg.sender).totalBorrows();
        ISimpleVault(msg.sender).balanceOf(address(this));

        if (asset != caller()) revert E_OnlyAssetCanDeposit();
    }

    // all the other hooked ops are disabled
    fallback() external {
        revert E_OperationDisabled();
    }

    function caller() internal pure returns (address _caller) {
        assembly {
            _caller := shr(96, calldataload(sub(calldatasize(), 20)))
        }
    }
}
