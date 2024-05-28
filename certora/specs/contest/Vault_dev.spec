import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/deposit.spec";
import "./unit/withdraw.spec";
import "./unit/skim.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";

import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

use rule vaultBalanceGreaterThanTotalAssets;
use rule depositSharesByVault;

// KO
// use rule vaultSkim;
// use rule skimRedeemUnchanged;
// use rule skimIdemDeposit2;
