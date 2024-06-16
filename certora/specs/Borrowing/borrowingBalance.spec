rule borrowingUpdateBalance(method f, env e, calldataarg args, address user) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  assert balanceUser_ != _balanceUser => borrowingUpdateBalance(f);
}

rule borrowingUpdateBalanceSatisfy(method f, env e, calldataarg args, address user) filtered {
  f -> borrowingUpdateBalance(f)
}{
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  satisfy balanceUser_ != _balanceUser;
}
