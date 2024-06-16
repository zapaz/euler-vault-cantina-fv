definition riskManagerIsHarness(method f) returns bool = baseIsHarness(f)
      ||  f.selector == sig:checkAccountLiquidity(address,address[]).selector;

definition riskManagerEvc(method f) returns bool =
          f.selector == sig:checkVaultStatus().selector
      ||  f.selector == sig:checkAccountStatus(address, address[]).selector;

definition riskManagerUpdateState(method f) returns bool =
          f.selector == sig:checkVaultStatus().selector
      ||  f.selector == sig:disableController().selector;


