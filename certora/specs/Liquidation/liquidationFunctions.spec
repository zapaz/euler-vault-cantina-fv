// identify Liquidation functions that are harnessed
definition liquidationIsHarness(method f) returns bool = baseIsHarness(f);

// identify Liquidation functions that can update state
definition liquidationUpdateState(method f) returns bool = !(liquidationIsHarness(f) || f.isView);

// identify Liquidation functions that can only be called by EVC
definition liquidationEvcOnly(method f) returns bool = liquidationUpdateState(f);
