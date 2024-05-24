rule depositWithdraw(env e, uint256 amount){
  require ERC20a == asset();

  uint256 _balance = userAssets(e, e.msg.sender);
  deposit(e, amount, e.msg.sender);
  withdraw(e, amount, e.msg.sender, e.msg.sender);
  uint256 balance_ = userAssets(e, e.msg.sender);

  assert _balance == balance_;
}
