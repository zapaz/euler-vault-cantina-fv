// identify if function is harnessed
definition borrowingIsHarness(method f) returns bool = baseIsHarness(f)
      ||  f.selector == sig:initOperationExternal(uint32,address).selector
      ||  f.selector == sig:getTotalBalance().selector
      ||  f.selector == sig:toAssetsExt(uint256).selector
      ||  f.selector == sig:unpackBalanceExt(BorrowingHarness.PackedUserSlot).selector
      ||  f.selector == sig:getUserInterestAccExt(address).selector
      ||  f.selector == sig:getVaultInterestAccExt().selector
      ||  f.selector == sig:getUnderlyingAssetExt().selector
      ||  f.selector == sig:userAssets(address).selector;

// identify if write function has to be non reentrant
definition borrowingIsNonReentrant(method f) returns bool =
          f.selector == sig:borrow(uint256,address).selector
      ||  f.selector == sig:repay(uint256,address).selector
      ||  f.selector == sig:repayWithShares(uint256,address).selector
      ||  f.selector == sig:pullDebt(uint256,address).selector
      ||  f.selector == sig:flashLoan(uint256,bytes).selector
      ||  f.selector == sig:touch().selector;

// identify if view function has to be non reentrant
definition borrowingIsNonReentrantView(method f) returns bool =
          f.selector == sig:totalBorrows().selector
      ||  f.selector == sig:totalBorrowsExact().selector
      ||  f.selector == sig:cash().selector
      ||  f.selector == sig:debtOf(address).selector
      ||  f.selector == sig:debtOfExact(address).selector
      ||  f.selector == sig:interestRate().selector
      ||  f.selector == sig:interestAccumulator().selector;

// identify if function can update debt
definition borrowingUpdateDebt(method f) returns bool =
       f.selector == sig:borrow(uint256,address).selector
    || f.selector == sig:repay(uint256,address).selector
    || f.selector == sig:pullDebt(uint256,address).selector;

// identify if function can update state only via EVC
definition borrowingEvcUpdater(method f) returns bool = borrowingUpdateDebt(f)
    || f.selector == sig:repayWithShares(uint256,address).selector
    || f.selector == sig:touch().selector;

// identify if function can modify balance
definition borrowingUpdateBalance(method f) returns bool =
       f.selector == sig:borrow(uint256,address).selector
    || f.selector == sig:repay(uint256,address).selector;


// identify if function can update state
definition borrowingUpdateState(method f) returns bool = borrowingEvcUpdater(f);


