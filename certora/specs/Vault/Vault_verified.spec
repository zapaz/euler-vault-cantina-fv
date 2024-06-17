import "./Vault.spec";

// original certora rules

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
use invariant noAssetsIfNoSupply;
