import "../Borrowing.spec";

import "./unit/borrow.spec";
import "./invariant/borrowing.spec";
// import "./common/isFunctionType.spec";
import "./common/math.spec";

// OK
use rule borrow;
use rule borrowingBalanceChanged;

