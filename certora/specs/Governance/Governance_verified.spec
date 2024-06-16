import "../Governance.spec";

import "../Common/math.spec";
import "../Common/functions.spec";

import "./governanceFunctions.spec";
import "./governanceUpdate.spec";
import "./governanceGovernor.spec";

use rule governanceGovernorOnly;
use rule governanceGovernorOnlySatisfy;
use rule governanceUpdate;
use rule governanceUpdateSatisfy;
