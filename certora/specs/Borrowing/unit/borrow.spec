///
// On borrow:
// - assets borrowed is as expected
// - only vault can decrease it's assets balance, by borrowed amount
// - only actualCaller can decrease it's assets balance, by borrowed amount
///
rule borrow(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);

  mathint borrowed = (amount == max_uint256) ? cash(e) : amount;

  mathint _userAssets = userAssets(e, user);
  mathint assets = borrow(e, amount, receiver);
  mathint userAssets_ = userAssets(e, user);

  assert assets == borrowed;
  assert userAssets_ < _userAssets => (user == currentContract) && (userAssets_ == _userAssets - borrowed);
  assert userAssets_ > _userAssets => (user == receiver)        && (userAssets_ == _userAssets + borrowed);
}

// check owed amount is increased by assets amount return by borrow
rule borrow2(env e, address receiver){
  address caller = actualCaller(e);

  mathint _owedReceiver =  getCurrentOwedExt(e, receiver);
  mathint assets = borrow(e, _, receiver);
  mathint owedReceiver_ =  getCurrentOwedExt(e, receiver);

  assert  owedReceiver_ == _owedReceiver + assets;
}

// check more borrow return more assets
rule borrowMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  uint256 _assets = borrow(e, amount, _);

  uint256 assets_ = borrow(e, require_uint256(amount + more), _) at initialStorage;

  assert assets_ >= assets_;
}
