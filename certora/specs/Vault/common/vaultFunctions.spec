definition isTransfer(method f) returns bool =
      f.selector == sig:transfer(address,uint256).selector
  ||  f.selector == sig:transferFrom(address,address,uint256).selector
  ||  f.selector == sig:transferFromMax(address,address).selector;

definition vaultIsHarness(method f) returns bool = baseIsHarness(f)
      ||  f.selector == sig:userAssets(address).selector
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

definition vaultIsNonReentrant(method f) returns bool =
          f.selector == sig:deposit(uint256,address).selector
      ||  f.selector == sig:mint(uint256,address).selector
      ||  f.selector == sig:withdraw(uint256,address,address).selector
      ||  f.selector == sig:redeem(uint256,address,address).selector
      ||  f.selector == sig:skim(uint256,address).selector;


definition vaultIsNonReentrantView(method f) returns bool =
          f.selector == sig:totalAssets().selector
      ||  f.selector == sig:convertToAssets(uint256).selector
      ||  f.selector == sig:convertToShares(uint256).selector
      ||  f.selector == sig:maxDeposit(address).selector
      ||  f.selector == sig:previewDeposit(uint256).selector
      ||  f.selector == sig:maxMint(address).selector
      ||  f.selector == sig:previewMint(uint256).selector
      ||  f.selector == sig:maxWithdraw(address).selector
      ||  f.selector == sig:previewWithdraw(uint256).selector
      ||  f.selector == sig:maxRedeem(address).selector
      ||  f.selector == sig:previewRedeem(uint256).selector
      ||  f.selector == sig:accumulatedFees().selector
      ||  f.selector == sig:accumulatedFeesAssets().selector;

definition vaultNeverRevertsView(method f) returns bool =
          f.selector == sig:asset().selector
      ||  f.selector == sig:totalAssets().selector
      ||  f.selector == sig:convertToShares(uint256).selector
      ||  f.selector == sig:convertToAssets(uint256).selector
      ||  f.selector == sig:maxDeposit(address).selector
      ||  f.selector == sig:previewDeposit(uint256).selector
      ||  f.selector == sig:maxMint(address).selector
      ||  f.selector == sig:previewMint(uint256).selector
      ||  f.selector == sig:maxWithdraw(address).selector
      ||  f.selector == sig:previewWithdraw(uint256).selector
      ||  f.selector == sig:maxRedeem(address).selector
      ||  f.selector == sig:previewRedeem(uint256).selector;


definition isOnlyCalledByEVC(method f) returns bool =
          f.selector == sig:transfer(address,uint256).selector
      ||  f.selector == sig:transferFrom(address,address,uint256).selector
      ||  f.selector == sig:transferFromMax(address,address).selector
      ||  f.selector == sig:deposit(uint256,address).selector
      ||  f.selector == sig:mint(uint256,address).selector
      ||  f.selector == sig:withdraw(uint256,address,address).selector
      ||  f.selector == sig:redeem(uint256,address,address).selector
      ||  f.selector == sig:skim(uint256,address).selector;

definition vaultUpdater(method f) returns bool = isTransfer(f) || vaultIsNonReentrant(f);

definition vaultUpdateState(method f) returns bool = vaultUpdater(f) || f.selector == sig:approve(address,uint256).selector;


