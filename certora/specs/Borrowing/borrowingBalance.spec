rule borrowingBalanceChanged (method f, env e, calldataarg args, address user) filtered {
  f -> !(f.isView || borrowingIsHarness(f))
}{
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  assert balanceUser_ != _balanceUser => borrowingUpdater(f);
}
