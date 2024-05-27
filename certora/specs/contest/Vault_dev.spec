import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/deposit.spec";
import "./unit/withdraw.spec";
import "./unit/skim.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";
import "./invariant/zeroAddress.spec";

use rule assetsSharesCVL;
use rule sharesAssetsCVL;

// KO
// use rule assetsSharesAssets;
// use rule skimRedeemUnchanged;
// use rule skimIdemDeposit2;
