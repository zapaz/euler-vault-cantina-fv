
// check deposit and immediate withdraw returns the same amount
rule depositWithdraw(env e, uint256 amount, address user){
  address caller = actualCaller(e);

  uint256 _balance = userAssets(e, user);
  deposit(e, amount, caller);
  withdraw(e, amount, caller, caller);
  uint256 balance_ = userAssets(e, user);

  assert balance_ == _balance;
}
