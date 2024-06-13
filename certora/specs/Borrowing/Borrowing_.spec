import "../Borrowing.spec";

import "../Common/math.spec";

import "./borrowingBalance.spec";
import "./borrowingFunctions.spec";
import "./borrowingReverts.spec";
import "./borrowingNonReentrant.spec";
import "./borrowingEvc.spec";

import "./unit/borrow.spec";
import "./unit/repay.spec";
import "./unit/pullDebt.spec";


methods {
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
}