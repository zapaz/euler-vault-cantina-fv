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
