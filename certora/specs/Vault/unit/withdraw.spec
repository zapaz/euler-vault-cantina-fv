// on withdraw
// - vault balance decrease by withdrawn amount
// - receiver balance increase by withdrawn amount
rule withdrawBalance(env e, uint256 amount, address receiver, address user){
  mathint _balance = userAssets(e, user);
  mathint shares = withdraw(e, amount, receiver, _);
  mathint balance_ = userAssets(e, user);

  assert balance_ < _balance => (user == currentContract) && (balance_ == _balance - amount);
  assert balance_ > _balance => (user == receiver) && (balance_ == _balance + amount);
}

// more withdraw amount requested gives more shares
rule withdrawMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  mathint _shares = withdraw(e, amount, _, _);

  mathint shares_ = withdraw(e, require_uint256(amount + more), _, _) at initialStorage;

  assert shares_ >= _shares;
}

// withdraw amount is as expected convertToShares
rule withdrawFromAssets(env e, uint256 amount){
  assert withdraw(e, amount, _, _) >= convertToShares(e, amount);
}
// withdraw amount is as expected withdrawPreview
rule withdrawPreview(env e, uint256 amount){
  assert previewWithdraw(e, amount) == withdraw(e, amount, _, _);
}

// strictly positive withdraw is possible, with owner assets increase
rule withdrawSatisfyIncrease(env e, uint256 amount, address receiver, address owner){
  mathint _balance = userAssets(e, owner);
  mathint shares   = withdraw(e, amount, receiver, owner);
  mathint balance_ = userAssets(e, owner);

  satisfy balance_ > _balance;
  satisfy shares > 0;
}

// strictly positive withdraw is possible, with vault assets decrease
rule withdrawSatisfyDecrease(env e, calldataarg args, address user){
  mathint _balance = userAssets(e, currentContract);
  mathint shares   = withdraw(e, args);
  mathint balance_ = userAssets(e, currentContract);

  satisfy balance_ < _balance;
  satisfy shares > 0;
}

// withdrawMax is less than these 2 max values
// and equal to 0 if withdraw is disabled or controller enabled
rule withdrawMax(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxAssets1 = convertToAssets(e, convertToShares(e, cash(e)));
  uint256 maxAssets2 = convertToAssets(e, userShares(e, owner));

  uint256 maxWithdraw = maxWithdraw(e, owner);

  assert isWithdrawDisabled(e)       => maxWithdraw == 0;
  assert controllerEnabled(e, owner) => maxWithdraw == 0;
  assert maxWithdraw <= min(maxAssets1, maxAssets2);
}