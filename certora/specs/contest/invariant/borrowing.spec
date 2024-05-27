rule borrowingBalanceChanged (method f, env e, calldataarg args, address user) {
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  assert balanceUser_ != _balanceUser =>
       f.selector == sig:borrow(uint256,address).selector
    || f.selector == sig:repay(uint256,address).selector
    || f.selector == sig:pullDebt(uint256,address).selector
    || f.selector == sig:flashLoan(uint256,bytes).selector;
}
