rule borrow(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);

  mathint borrowed = (amount == max_uint256) ? cash(e) : amount;

  mathint _balanceUser = userAssets(e, user);
  borrow(e, amount, receiver);
  mathint balanceUser_ = userAssets(e, user);

  assert e.msg.sender == evc;
  assert balanceUser_ < _balanceUser => (user == currentContract) && (balanceUser_ == _balanceUser - borrowed);
  assert balanceUser_ > _balanceUser => (user == receiver)        && (balanceUser_ == _balanceUser + borrowed);
}
