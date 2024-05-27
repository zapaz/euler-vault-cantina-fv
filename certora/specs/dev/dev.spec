import "../VaultFull.spec";

import "./evc.spec";
import "./deposit.spec";
import "./withdraw.spec";
import "./depositWithdraw.spec";
import "./skim.spec";
import "./zeroAddress.spec";
import "./assetsShares.spec";

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

use rule depositBalances;
use rule depositShares;
use rule depositSharesByVault;
use rule depositSatisfyDecrease;
use rule depositSatisfyIncrease;

use rule withdraw;
use rule withdrawSatisfyIncrease;
use rule withdrawSatisfyDecrease;

use rule depositWithdraw;

use rule skim;
use rule skimOk;
use rule skimWithdrawUnchanged;
use rule skimIdemDeposit;

use rule zeroAddressUnchanged;

// DEV

// KO
// use rule assetsSharesAssets;
// use rule skimRedeemUnchanged;
// use rule skimIdemDeposit2;
