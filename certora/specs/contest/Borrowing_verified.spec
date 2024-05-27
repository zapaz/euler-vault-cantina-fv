import "../Borrowing.spec";

import "./unit/borrow.spec";
import "./invariant/borrowing.spec";

// OK
use rule borrow;
use rule borrowingBalanceChanged;

