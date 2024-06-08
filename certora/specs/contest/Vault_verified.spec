import "../VaultFull.spec";

import "./access/evc.spec";

import "./unit/deposit.spec";
import "./unit/withdraw.spec";
import "./unit/skim.spec";
import "./unit/mint.spec";
import "./unit/redeem.spec";

import "./compose/depositWithdraw.spec";
import "./compose/assetsShares.spec";
import "./invariant/zeroAddress.spec";
import "./invariant/vault.spec";

import "./common/definitions.spec";
import "./common/reverts.spec";
import "./common/nonReentrant.spec";

methods {
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
}


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

use rule onlyEVC;
use rule deposit;
use rule depositShares;
use rule depositSatisfy;
use rule depositWithdraw;
use rule depositMonotonicity;

use rule vaulAssetsChanged;
use rule vaulSharesChanged;
use rule vaultBalanceGreaterThanTotalAssets;

use rule mintMaxEqual;
use rule depositMax;
use rule mintMax;
use rule redeemMax;
use rule withdrawMax;

use rule withdraw;
use rule withdrawSatisfyDecrease;

use rule skim;
use rule skimIdemDeposit;
use rule skimSatisfy;
use rule skimWithdrawUnchanged;


use rule assetsSharesCVL;
use rule sharesAssetsCVL;
use rule assetsSharesAssets;

use invariant reentrantLockInvariant;
use rule nonReentrantCheck;
use rule nonReentrantViewCheck;
