import "./Vault.spec";

// vault generic rules

use rule vaultNonReentrantCheck;
use rule vaultNonReentrantViewCheck;
use rule vaultMustNotAlwaysReverts;

use rule assetsSharesCVL;
use rule sharesAssetsCVL;
use rule assetsSharesAssets;

use rule vaulAssetsChanged;
use rule vaulSharesChanged;
use rule vaultBalanceGreaterThanTotalAssets;
