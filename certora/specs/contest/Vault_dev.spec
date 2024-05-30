import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/deposit.spec";
import "./unit/withdraw.spec";
import "./unit/skim.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";

import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/reverts.spec";
import "./common/definitions.spec";

use rule deposit;
use rule depositSharesWeak;
use rule depositSharesByVault;
use rule depositSatisfy;

// use rule vaultBalanceGreaterThanTotalAssets;
// use rule depositSharesByVault;

// KO
// use rule vaultSkim;
// use rule skimRedeemUnchanged;
// use rule skimIdemDeposit2;

