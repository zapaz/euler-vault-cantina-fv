definition isOnlyEVCChecks(method f) returns bool =
          f.selector == sig:checkAccountStatus(address,address[]).selector
      ||  f.selector == sig:checkVaultStatus().selector;


definition isOnlyAdmin(method f) returns bool =
          f.selector == sig:setAdmin(address).selector
      ||  f.selector == sig:setFeeReceiver(address).selector
      ||  f.selector == sig:setProtocolFeeShare(uint16).selector
      ||  f.selector == sig:setInterestFeeRange(uint16,uint16).selector
      ||  f.selector == sig:setVaultInterestFeeRange(address,bool,uint16,uint16).selector
      ||  f.selector == sig:setVaultFeeConfig(address,bool,address,uint16).selector;
