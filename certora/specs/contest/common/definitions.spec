definition isHarnessBase(method f) returns bool =
      f.selector == sig:getLTVConfig(address).selector
  ||  f.selector == sig:vaultCacheOracleConfigured().selector
  ||  f.selector == sig:isAccountStatusCheckDeferredExt(address).selector
  ||  f.selector == sig:getBalanceAndForwarderExt(address).selector
  ||  f.selector == sig:vaultIsOnlyController(address).selector
  ||  f.selector == sig:vaultIsController(address).selector
  ||  f.selector == sig:getCollateralsExt(address).selector
  ||  f.selector == sig:isCollateralEnabledExt(address, address).selector
  ||  f.selector == sig:isOperationDisabledExt(uint32).selector
  ||  f.selector == sig:isDepositDisabled().selector
  ||  f.selector == sig:isMintDisabled().selector
  ||  f.selector == sig:isWithdrawDisabled().selector
  ||  f.selector == sig:isRedeemDisabled().selector
  ||  f.selector == sig:isSkimDisabled().selector;

definition isHarnessVault(method f) returns bool =
          f.selector == sig:userAssets(address).selector
      ||  f.selector == sig:cash().selector
      ||  f.selector == sig:storage_lastInterestAccumulatorUpdate().selector
      ||  f.selector == sig:storage_cash().selector
      ||  f.selector == sig:storage_supplyCap().selector
      ||  f.selector == sig:storage_borrowCap().selector
      ||  f.selector == sig:storage_reentrancyLocked().selector
      ||  f.selector == sig:storage_hookedOps().selector
      ||  f.selector == sig:storage_snapshotInitialized().selector
      ||  f.selector == sig:storage_totalShares().selector
      ||  f.selector == sig:storage_totalBorrows().selector
      ||  f.selector == sig:storage_accumulatedFees().selector
      ||  f.selector == sig:storage_interestAccumulator().selector
      ||  f.selector == sig:storage_configFlags().selector
      ||  f.selector == sig:cache_cash().selector;

definition isHarness(method f) returns bool = isHarnessBase(f) || isHarnessVault(f);