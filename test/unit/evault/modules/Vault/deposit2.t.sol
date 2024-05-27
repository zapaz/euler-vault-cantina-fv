// SPDX-License-Identifier: GPL-2.0-or-later

pragma solidity ^0.8.0;

import {EVaultTestBase} from "../../EVaultTestBase.t.sol";
import {Events} from "src/EVault/shared/Events.sol";
import {SafeERC20Lib} from "src/EVault/shared/lib/SafeERC20Lib.sol";
import {Permit2ECDSASigner} from "../../../../mocks/Permit2ECDSASigner.sol";
import {IAllowanceTransfer} from "permit2/src/interfaces/IAllowanceTransfer.sol";
import {IEVC} from "ethereum-vault-connector/interfaces/IEthereumVaultConnector.sol";

import "src/EVault/shared/types/Types.sol";
import {console2} from "forge-std/Test.sol";

contract VaultTest_Deposit2 is EVaultTestBase {
    using TypesLib for uint256;

    error InvalidNonce();
    error InsufficientAllowance(uint256 amount);

    uint256 userPK;
    address user;
    address user1;

    Permit2ECDSASigner permit2Signer;

    function setUp() public override {
        super.setUp();

        permit2Signer = new Permit2ECDSASigner(address(permit2));

        userPK = 0x123400;
        user = vm.addr(userPK);
        user1 = makeAddr("user1");

        assetTST.mint(user1, type(uint256).max);
        hoax(user1);
        assetTST.approve(address(eTST), type(uint256).max);

        assetTST.mint(user, type(uint256).max);
        startHoax(user);
        assetTST.approve(address(eTST), type(uint256).max);
    }

    function test_ONE() public {
        assetTST.mint(address(eTST), 1e18);
        // hoax(address(eTST));
        // assetTST.approve(address(eTST), type(uint256).max);

        assertEq(assetTST.balanceOf(address(eTST)), 1e18);

        vm.startPrank(address(eTST));
        uint256 shares = eTST.deposit(1e16, address(eTST));
        console2.log("test_ONE ~ shares:", shares);

        assertEq(assetTST.balanceOf(address(eTST)), 1e18);
    }
}
