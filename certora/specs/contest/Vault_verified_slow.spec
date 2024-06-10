import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/deposit.spec";
import "./unit/withdraw.spec";
import "./unit/skim.spec";
import "./unit/mint.spec";
import "./unit/redeem.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";
import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/isFunctionType.spec";
import "./common/math.spec";
import "./common/reverts.spec";
import "./common/nonReentrant.spec";

methods {
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
}

use rule mintMaxSatisfy;
use rule withdrawSatisfyIncrease;
use rule zeroAddressUnchanged;
use rule underlyingCannotChange;
use rule mustNotAlwaysReverts;

use rule redeemMax;
