rule withdraw(env e, uint256 amount, address receiver, address owner, address user){
  address caller = actualCaller(e);

  mathint _balance = userAssets(e, user);
  withdraw(e, amount, receiver, owner);
  mathint balance_ = userAssets(e, user);

  assert e.msg.sender == evc;
  assert balance_ < _balance => (user == currentContract) && (balance_ == _balance - amount);
  assert balance_ > _balance => (user == receiver) && (balance_ == _balance + amount);
}

rule withdrawSatisfyIncrease(env e, uint256 amount, address receiver, address owner){
  mathint _balance = userAssets(e, owner);
  withdraw(e, amount, receiver, owner);
  mathint balance_ = userAssets(e, owner);

  satisfy balance_ > _balance;
}

rule withdrawSatisfyDecrease(env e, calldataarg args, address user){
  mathint _balance = userAssets(e, currentContract);
  withdraw(e, args);
  mathint balance_ = userAssets(e, currentContract);

  satisfy balance_ < _balance;
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