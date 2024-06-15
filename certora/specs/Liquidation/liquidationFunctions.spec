definition liquidationIsHarness(method f) returns bool = baseIsHarness(f);

definition liquidationUpdateState(method f) returns bool = !(liquidationIsHarness(f) || f.isView);

definition liquidationEvcOnly(method f) returns bool = liquidationUpdateState(f);
