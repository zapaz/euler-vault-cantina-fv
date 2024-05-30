import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/deposit.spec";
import "./unit/withdraw.spec";
import "./unit/skim.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";
import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/definitions.spec";
import "./common/reverts.spec";

use rule dustFavorsTheHouse;
use rule underlyingCannotChange;
use rule redeemingAllValidity;
use rule reclaimingProducesAssets;
use invariant totalSupplyIsSumOfBalances;

use rule conversionOfZero;
use rule conversionWeakIntegrity;
use rule conversionWeakMonotonicity;
use rule convertToAssetsWeakAdditivity;
use rule convertToCorrectness;
use rule convertToSharesWeakAdditivity;
use rule zeroDepositZeroShares;

use rule onlyEVC;
use rule deposit;
use rule depositSharesWeak;
use rule depositSharesByVault;
use rule depositSatisfy;

use rule withdraw;
use rule withdrawSatisfyIncrease;
use rule withdrawSatisfyDecrease;

use rule depositWithdraw;

use rule skim;
use rule skimOk;
use rule skimWithdrawUnchanged;
use rule skimIdemDeposit;

use rule zeroAddressUnchanged;

use rule vaultBalanceChanged;

use rule assetsSharesCVL;
use rule sharesAssetsCVL;
use rule assetsSharesAssets;

use rule mustNotAlwaysReverts;
