// Borrowing verified rules

import "./Borrowing_.spec";

use invariant borrowingReentrantLockInvariant;
use rule borrowingNonReentrantCheck;
use rule borrowingNonReentrantViewCheck;

use rule borrow;
use rule borrowingUpdate;
use rule borrowingEvcOnly;
use rule borrowingBalances;
use rule borrowMonotonicity;
use rule borrowingUpdateSatisfy;
use rule borrowingUpdateBalance;
use rule borrowingEvcOnlySatisfy;
use rule borrowingUpdateBalanceSatisfy;
use rule borrowingMustNotAlwaysReverts;

use rule repay;
use rule repayWithShares;
use rule repayWithSharesMonotonicity;

use rule pullDebt;
