// generic import and methods uses by all Borrowing rules

import "../Borrowing.spec";

import "../Common/math.spec";
import "../Common/functions.spec";

import "./borrowingBalance.spec";
import "./borrowingFunctions.spec";
import "./borrowingReverts.spec";
import "./borrowingNonReentrant.spec";
import "./borrowingUpdate.spec";
import "./borrowingEvc.spec";

import "./unit/borrow.spec";
import "./unit/repay.spec";
import "./unit/pullDebt.spec";


methods {
    function storage_reentrancyLocked() external returns (bool)    envfree;
    function storage_hookTarget()       external returns (address) envfree;
}