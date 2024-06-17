import "./Vault.spec";

// slow rules, in a separated verified spec

use invariant assetsMoreThanSupply;
use invariant noSupplyIfNoAssets;
// use invariant vaultSolvency;

use rule mintMonotonicity;