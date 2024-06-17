// on rePay:
// - check only caller can decrease it's asset balance by asset amount as expected
// - check only vault can increase it's asset balance by amount as expected
rule repay(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);

  mathint _userAssets = userAssets(e, user);

  mathint assets = repay(e, amount, receiver);

  mathint userAssets_ = userAssets(e, user);

  assert userAssets_ < _userAssets => (user == caller)          && (userAssets_ == _userAssets - assets);
  assert userAssets_ > _userAssets => (user == currentContract) && (userAssets_ == _userAssets + assets);
}

// on repayWithShares:
// - check only caller can decrease it's asset balance by asset amount as expected
// - check only vault can increase it's asset balance by amount as expected
rule repayWithShares(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);

  mathint _userAssets = userAssets(e, user);

  mathint shares;
  mathint assets;
  (shares, assets) = repayWithShares(e, amount, receiver);

  mathint userAssets_ = userAssets(e, user);

  assert userAssets_ < _userAssets => (user == caller)          && (userAssets_ == _userAssets - assets);
  assert userAssets_ > _userAssets => (user == currentContract) && (userAssets_ == _userAssets + assets);
}

// check more borrow return more assets
rule repayWithSharesMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  uint256 _assets = borrow(e, amount, _);

  uint256 assets_ = borrow(e, require_uint256(amount + more), _) at initialStorage;

  assert assets_ >= assets_;
}


// not ok rules, not in verifeid rules

rule repay2(env e, address receiver){
  address caller = actualCaller(e);

  mathint _owedReceiver =  getCurrentOwedExt(e, receiver);
  mathint assets = repay(e, _, receiver);
  mathint owedReceiver_ =  getCurrentOwedExt(e, receiver);

  assert  owedReceiver_ == _owedReceiver - assets;
}
