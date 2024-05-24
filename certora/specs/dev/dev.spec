import "../Vault.spec";
import "./deposit.spec";
import "./withdraw.spec";
import "./evc.spec";
// import "./ko.spec";

use rule onlyEVC;

use rule deposit;
use rule depositSatisfyDecrease;
use rule depositSatisfyIncrease;

use rule withdraw;
use rule withdrawSatisfyIncrease;
use rule withdrawSatisfyDecrease;

// use rule depositWithdraw;

