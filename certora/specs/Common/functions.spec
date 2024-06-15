definition baseIsHarness(method f) returns bool =
          f.selector == sig:isDepositDisabled().selector
      ||  f.selector == sig:isMintDisabled().selector
      ||  f.selector == sig:isWithdrawDisabled().selector
      ||  f.selector == sig:isRedeemDisabled().selector
      ||  f.selector == sig:isSkimDisabled().selector
      ||  f.selector == sig:isOperationDisabledExt(uint32).selector
      ||  f.selector == sig:vaultCacheOracleConfigured().selector
      ||  f.selector == sig:getLTVConfig(address).selector
      ||  f.selector == sig:isAccountStatusCheckDeferredExt(address).selector
      ||  f.selector == sig:getBalanceAndForwarderExt(address).selector
      ||  f.selector == sig:vaultIsOnlyController(address).selector
      ||  f.selector == sig:vaultIsController(address).selector
      ||  f.selector == sig:getCollateralsExt(address).selector
      ||  f.selector == sig:isCollateralEnabledExt(address, address).selector;