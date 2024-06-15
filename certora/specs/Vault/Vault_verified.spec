import "./Vault.spec";

use rule dustFavorsTheHouse;

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

use rule vaultEvcOnly;
use rule deposit;
use rule depositMax;
use rule depositShares;
use rule depositSatisfy;
use rule depositPreview;
use rule depositWithdraw;
use rule depositMonotonicity;

use rule vaulAssetsChanged;
use rule vaulSharesChanged;
use rule vaultBalanceGreaterThanTotalAssets;

use rule vaultUpdate;

use rule mint;
use rule mintMax;
use rule mintPreview;
use rule mintSatisfy;
use rule mintMonotonicity;

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

use rule skim;
use rule skimSupply;
use rule skimSatisfy;
use rule skimIdemDeposit;
use rule skimMonotonicity;
use rule skimWithdrawUnchanged;

use rule assetsSharesCVL;
use rule sharesAssetsCVL;
use rule assetsSharesAssets;

use invariant vaultReentrantLockInvariant;
use rule vaultNonReentrantCheck;
use rule vaultNonReentrantViewCheck;

use rule vaultMustNotAlwaysReverts;
