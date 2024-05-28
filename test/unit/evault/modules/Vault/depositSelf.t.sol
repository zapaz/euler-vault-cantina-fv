// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {EVaultTestBase} from "../../EVaultTestBase.t.sol";
import {console2} from "forge-std/Test.sol";

contract VaultTest_DepositSelf is EVaultTestBase {
    uint256 one = 1e18;
    address user = makeAddr("user");
    address robber = makeAddr("robber");

    function _log(string memory label) public view {
        console2.log(label, "| User   Balance :", assetTST.balanceOf(user));
        console2.log(label, "| Vault  Balance :", assetTST.balanceOf(address(eTST)));
        console2.log(label, "| Total  Assets  :", eTST.totalAssets());
        console2.log(label, "| Robber Balance :", assetTST.balanceOf(robber));
        console2.log("------------------------|-------------------------------------");
    }

    function setUp() public override {
        super.setUp();

        assetTST.mint(user, one);
        _log("       User   Mint    1");

        startHoax(user);
        assetTST.approve(address(eTST), one);
    }

    function test_depositSelf() public {
        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == one);
        assert(assetTST.balanceOf(robber) == 0);

        eTST.deposit(one, user);
        _log("       User   Deposit 1");

        startHoax(address(eTST));
        eTST.deposit(one, address(eTST));
        _log("Buggy  Vault  Deposit 1");

        eTST.withdraw(one, robber, address(eTST));
        _log("Robber Vault  Steal   1");

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == 0);
        assert(assetTST.balanceOf(robber) == one);
    }
}
