import "../Borrowing.spec";

import "../Common/math.spec";
import "../Common/functions.spec";

import "./riskManagerFunctions.spec";
import "./riskManagerUpdate.spec";
import "./riskManagerStatus.spec";
import "./riskManagerEvc.spec";

// import "./riskManagerNonReentrant.spec";

methods {
}

// use rule riskManagerAccountStatus;
use rule riskManagerUpdate;
use rule riskManagerUpdateSatisfy;
use rule riskManagerEvcOnly;
use rule riskManagerEvcOnlySatisfy;
