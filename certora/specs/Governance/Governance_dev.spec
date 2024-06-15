import "../Governance.spec";

import "../Common/math.spec";
import "../Common/functions.spec";

import "./governanceFunctions.spec";
import "./governanceUpdate.spec";
// import "./governanceGovernor.spec";
// import "./governanceReverts.spec";
// import "./governanceNonReentrant.spec";

// use rule governanceGovernorOnly;
use rule governanceUpdate;
use rule governanceUpdateSatisfy;
