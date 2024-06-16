import "./Vault.spec";

use invariant assetsMoreThanSupply;
use invariant noAssetsIfNoSupply;
use invariant noSupplyIfNoAssets;
use invariant vaultSolvency;

use rule mintMonotonicity;