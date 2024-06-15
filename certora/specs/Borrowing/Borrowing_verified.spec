import "./Borrowing_.spec";

use invariant borrowingReentrantLockInvariant;
use rule borrowingNonReentrantCheck;
use rule borrowingNonReentrantViewCheck;

use rule borrow;
use rule borrowMonotonicity;
use rule borrowingUpdateBalance;
use rule borrowingMustNotAlwaysReverts;
use rule borrowingEvcOnly;

use rule repay;
use rule repayWithShares;
use rule repayWithSharesMonotonicity;

use rule pullDebt;
