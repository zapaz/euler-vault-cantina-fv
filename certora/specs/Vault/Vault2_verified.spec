import "./Vault.spec";

// vault redeem and withdraw rules

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