rule withdrawBalance(env e, uint256 amount, address receiver, address user){
  mathint _balance = userAssets(e, user);
  mathint shares = withdraw(e, amount, receiver, _);
  mathint balance_ = userAssets(e, user);

  assert balance_ < _balance => (user == currentContract) && (balance_ == _balance - amount);
  assert balance_ > _balance => (user == receiver) && (balance_ == _balance + amount);
}

rule withdrawMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  mathint _shares = withdraw(e, amount, _, _);

  mathint shares_ = withdraw(e, require_uint256(amount + more), _, _) at initialStorage;

  assert shares_ >= _shares;
}

rule withdrawFromAssets(env e, uint256 amount){
  assert withdraw(e, amount, _, _) >= convertToShares(e, amount);
}

rule withdrawPreview(env e, uint256 amount){
  assert previewWithdraw(e, amount) == withdraw(e, amount, _, _);
}

rule withdrawSatisfyIncrease(env e, uint256 amount, address receiver, address owner){
  mathint _balance = userAssets(e, owner);
  mathint shares   = withdraw(e, amount, receiver, owner);
  mathint balance_ = userAssets(e, owner);

  satisfy balance_ > _balance;
  satisfy shares > 0;
}

rule withdrawSatisfyDecrease(env e, calldataarg args, address user){
  mathint _balance = userAssets(e, currentContract);
  mathint shares   = withdraw(e, args);
  mathint balance_ = userAssets(e, currentContract);

  satisfy balance_ < _balance;
  satisfy shares > 0;
}

rule withdrawMax(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxAssets1 = convertToAssets(e, convertToShares(e, cash(e)));
  uint256 maxAssets2 = convertToAssets(e, userShares(e, owner));
  uint256 maxAssets3 = isWithdrawDisabled(e) ? 0 : max_uint256;
  uint256 maxAssets4 = controllerEnabled(e, owner) ? 0 : max_uint256;

  uint256 maxWithdraw = maxWithdraw(e, owner);

  assert  maxWithdraw == min4(maxAssets1, maxAssets2, maxAssets3, maxAssets4);
}