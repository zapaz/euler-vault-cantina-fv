// slow rules, in a separated verified spec


import "./Vault.spec";

use invariant assetsMoreThanSupply;
use invariant noSupplyIfNoAssets;
// use invariant vaultSolvency;

// use rule mintMonotonicity;

use rule dustFavorsTheHouse;
use rule reclaimingProducesAssets;
use rule redeemingAllValidity;
use invariant noAssetsIfNoSupply;