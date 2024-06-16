import "./Vault.spec";

// vault skim rules and more generic rules

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

