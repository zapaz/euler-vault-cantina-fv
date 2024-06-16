// generic import and methods uses by all vault rules
// including original vaultFull rules and definitions by certora

// NOTE: all these rules are made on a contract without Borrowing
// meaning that borrow is not possible, owed amount allways 0
// some rules would not be true with borrowing enabled

import "../VaultFull.spec";

import "../Common/math.spec";
import "../Common/functions.spec";

import "./unit/mint.spec";
import "./unit/deposit.spec";
import "./unit/skim.spec";
import "./unit/withdraw.spec";
import "./unit/redeem.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";

import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/vaultEVC.spec";
import "./common/vaultReverts.spec";
import "./common/vaultFunctions.spec";
import "./common/vaultNonReentrant.spec";
import "./common/vaultUpdate.spec";

// return random bool
function CVLBoolRandom(env e) returns bool { return (e.block.timestamp  % 2 == 0); }

methods {
    // added harness functions
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
    function storage_supplyCap()        external returns (uint256) envfree;
    function controllerEnabled(address) external returns (bool) envfree;

    // replace the original function with random bool, original is too slow
    function Base.isOperationDisabled(VaultHarness.Flags, uint32) internal returns (bool)
             with(env e) => CVLBoolRandom(e);
}

