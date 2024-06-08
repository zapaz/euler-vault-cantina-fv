import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/mint.spec";
import "./unit/deposit.spec";
import "./unit/skim.spec";
import "./unit/withdraw.spec";
import "./unit/redeem.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";

import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/reverts.spec";
import "./common/definitions.spec";
import "./common/nonReentrant.spec";

methods {
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
    function storage_supplyCap()        external returns (uint256) envfree;
}

use rule depositMax;
use rule mintMax;
use rule redeemMax;
use rule withdrawMax;

// use rule redeemMax;

// KO

// use rule vaultSkim;
// use rule skimRedeemUnchanged;
// use rule skimIdemDeposit2;
