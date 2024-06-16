import "./Vault.spec";

// all rules not used in verified spec
// due to timeoute when all rules verified together
// rules split in 5 files

// slow
// use invariant assetsMoreThanSupply;
// use invariant noAssetsIfNoSupply;
// use invariant noSupplyIfNoAssets;
// use invariant vaultSolvency;
// use rule mintMonotonicity;

use rule conversionOfZero;
use rule conversionWeakIntegrity;
use rule conversionWeakMonotonicity;
use rule convertToAssetsWeakAdditivity;
use rule convertToCorrectness;
use rule convertToSharesWeakAdditivity;
use rule zeroDepositZeroShares;

use rule dustFavorsTheHouse;
use rule underlyingCannotChange;
use rule redeemingAllValidity;
use rule reclaimingProducesAssets;

use invariant totalSupplyIsSumOfBalances;

use rule deposit;
use rule depositMax;
use rule depositShares;
use rule depositSatisfy;
use rule depositPreview;
use rule depositWithdraw;
use rule depositMonotonicity;

use rule mint;
use rule mintMax;
use rule mintPreview;
use rule mintSatisfy;

use rule redeem;
use rule redeemMax;
use rule redeemPreview;
use rule redeemMaxSatisfy;
use rule redeemFromShares;

use rule withdrawMax;
use rule withdrawBalance;
use rule withdrawPreview;
use rule withdrawMonotonicity;
use rule withdrawSatisfyDecrease;

use rule withdrawSatisfyIncrease;
use rule zeroAddressUnchanged;

use rule vaultNonReentrantCheck;
use rule vaultNonReentrantViewCheck;
use rule vaultMustNotAlwaysReverts;

use rule assetsSharesCVL;
use rule sharesAssetsCVL;
use rule assetsSharesAssets;

use rule vaulAssetsChanged;
use rule vaulSharesChanged;
use rule vaultBalanceGreaterThanTotalAssets;

use invariant vaultReentrantLockInvariant;

use rule vaultUpdate;
use rule vaultUpdateSatisfy;
use rule vaultEvcOnly;
use rule vaultEvcOnlySatisfy;

use rule skim;
use rule skimSupply;
use rule skimSatisfy;
use rule skimIdemDeposit;
use rule skimMonotonicity;
use rule skimWithdrawUnchanged;
