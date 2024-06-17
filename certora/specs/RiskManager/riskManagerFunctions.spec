// identify RiskManager functions that are harnessed
definition riskManagerIsHarness(method f) returns bool = baseIsHarness(f)
      ||  f.selector == sig:checkAccountLiquidity(address,address[]).selector;

// identify RiskManager functions that can update state
definition riskManagerEvc(method f) returns bool =
          f.selector == sig:checkVaultStatus().selector
      ||  f.selector == sig:checkAccountStatus(address, address[]).selector;

// identify RiskManager functions that can only be called by EVC
definition riskManagerUpdateState(method f) returns bool =
          f.selector == sig:checkVaultStatus().selector
      ||  f.selector == sig:disableController().selector;


