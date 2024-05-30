import "../Borrowing.spec";

import "./unit/borrow.spec";
import "./invariant/borrowing.spec";
import "./common/definitions.spec";

// OK
use rule borrow;
use rule borrowingBalanceChanged;

