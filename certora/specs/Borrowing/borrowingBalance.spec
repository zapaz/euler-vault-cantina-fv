  // getCurrentOwed(e, _, user);

// check assets in current contract always greater than cash
// (rule could be transformed in an invariant)
rule borrowingBalances(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  require actualCaller(e) != currentContract;

  mathint _assets = userAssets(e, currentContract);
  mathint _cash = cash(e);

  require _assets >= _cash;

  f(e, args);

  mathint assets_ = userAssets(e, currentContract);
  mathint cash_ = cash(e);

  assert assets_ >= cash_;
}

// check assets in current contract equals cash
// with no skim or no borrow for current contract
rule borrowingBalancesEqual(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  require actualCaller(e) != currentContract;

  mathint _assets = userAssets(e, currentContract);
  mathint _cash = cash(e);

  require _assets == _cash;

  if (f.selector == sig:borrow(uint256,address).selector) {
    address receiver;
    require receiver != currentContract;
    borrow(e, _, receiver);
  }else {
    f(e, args);
  }

  mathint assets_ = userAssets(e, currentContract);
  mathint cash_ = cash(e);

  assert assets_ == cash_;
}

rule borrowingBalances4(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  require actualCaller(e) != currentContract;

  require totalAssets(e) == require_uint256(totalBorrows(e) + cash(e));

  f(e, args);

  assert totalAssets(e) == require_uint256(totalBorrows(e) + cash(e));
}



rule borrowingBalances5(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  require actualCaller(e) != currentContract;

  require totalBorrows(e) >= totalBorrowsExact(e);

  if (f.selector == sig:borrow(uint256,address).selector) {
    address receiver;
    require receiver != currentContract;
    borrow(e, _, receiver);
  }else {
    f(e, args);
  }

  assert totalBorrows(e) >= totalBorrowsExact(e);
}


rule borrowingBalances6(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  require actualCaller(e) != currentContract;

  mathint _assets = cash(e) + totalBorrowsExact(e);

  if (f.selector == sig:borrow(uint256,address).selector) {
    address receiver;
    require receiver != currentContract;
    borrow(e, _, receiver);
  }else {
    f(e, args);
  }

  mathint assets_ = cash(e) + totalBorrowsExact(e);

  assert assets_ == _assets;
}





// check user balance is only modified by borrowingUpdateBalance functions
rule borrowingUpdateBalance(method f, env e, calldataarg args, address user) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  assert balanceUser_ != _balanceUser => borrowingUpdateBalance(f);
}

// check all borrowingUpdateBalance functions can modify user balance at least once
rule borrowingUpdateBalanceSatisfy(method f, env e, calldataarg args, address user) filtered {
  f -> borrowingUpdateBalance(f)
}{
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  satisfy balanceUser_ != _balanceUser;
}
