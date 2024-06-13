definition borrowingIsHarness(method f) returns bool =
          f.selector == sig:initOperationExternal(uint32,address).selector
      ||  f.selector == sig:getTotalBalance().selector
      ||  f.selector == sig:toAssetsExt(uint256).selector
      ||  f.selector == sig:unpackBalanceExt(BorrowingHarness.PackedUserSlot).selector
      ||  f.selector == sig:getUserInterestAccExt(address).selector
      ||  f.selector == sig:getVaultInterestAccExt().selector
      ||  f.selector == sig:getUnderlyingAssetExt().selector
      ||  f.selector == sig:userAssets(address).selector;

definition borrowingIsNonReentrant(method f) returns bool =
          f.selector == sig:borrow(uint256,address).selector
      ||  f.selector == sig:repay(uint256,address).selector
      ||  f.selector == sig:repayWithShares(uint256,address).selector
      ||  f.selector == sig:pullDebt(uint256,address).selector
      ||  f.selector == sig:flashLoan(uint256,bytes).selector
      ||  f.selector == sig:touch().selector;

definition borrowingIsNonReentrantView(method f) returns bool =
          f.selector == sig:totalBorrows().selector
      ||  f.selector == sig:totalBorrowsExact().selector
      ||  f.selector == sig:cash().selector
      ||  f.selector == sig:debtOf(address).selector
      ||  f.selector == sig:debtOfExact(address).selector
      ||  f.selector == sig:interestRate().selector
      ||  f.selector == sig:interestAccumulator().selector;

definition borrowingUpdater(method f) returns bool =
       f.selector == sig:borrow(uint256,address).selector
    || f.selector == sig:repay(uint256,address).selector
    || f.selector == sig:pullDebt(uint256,address).selector
    || f.selector == sig:flashLoan(uint256,bytes).selector;