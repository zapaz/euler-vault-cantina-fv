import "../VaultFull.spec";

import "../Common/math.spec";

import "./access/vaultEVC.spec";

import "./unit/mint.spec";
import "./unit/deposit.spec";
import "./unit/skim.spec";
import "./unit/withdraw.spec";
import "./unit/redeem.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";

import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/vaultReverts.spec";
import "./common/vaultFunctions.spec";
import "./common/vaultNonReentrant.spec";

function CVLBoolRandom(env e) returns bool { return (e.block.timestamp  % 2 == 0); }

methods {
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
    function storage_supplyCap()        external returns (uint256) envfree;
    function controllerEnabled(address) external returns (bool) envfree;

    // function Base.isOperationDisabled(VaultHarness.Flags, uint32) internal returns (bool) => NONDET;
    function Base.isOperationDisabled(VaultHarness.Flags, uint32) internal returns (bool)
    with(env e) => CVLBoolRandom(e);
}

