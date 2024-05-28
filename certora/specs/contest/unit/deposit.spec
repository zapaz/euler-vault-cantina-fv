///////////////////////////////////////////////////////////////////////////////////////////////
// deposit associated rules
///////////////////////////////////////////////////////////////////////////////////////////////
// - deposited amount is equal to amount or actuallCaller balance (if amount is max_uint256)
// - deposit must be called by evc
// - only Vault can increase it's balance, by deposited amount
// - only actualCaller can decrease it's balance, by deposited amount
///////////////////////////////////////////////////////////////////////////////////////////////
rule depositBalances(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);

  mathint deposit = (amount == max_uint256) ? userAssets(e, caller) : amount;

  mathint _balanceUser = userAssets(e, user);
  deposit(e, amount, receiver);
  mathint balanceUser_ = userAssets(e, user);

  assert e.msg.sender == evc;
  assert balanceUser_ > _balanceUser => (user == currentContract) && (balanceUser_ == _balanceUser + deposit);
  assert balanceUser_ < _balanceUser => (user == caller)          && (balanceUser_ == _balanceUser - deposit);
}

rule depositSharesWeak(env e, calldataarg args){
  address caller = actualCaller(e);
  require caller != currentContract;

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, args);
  mathint balanceCaller_ = userAssets(e, caller);

  assert shares > 0 <=> balanceCaller_ < _balanceCaller;
}

// bug ??  caller == currentContract et shares > 0
rule depositSharesByVault(env e, calldataarg args){
  address caller = actualCaller(e);
  require caller == currentContract;

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, args);
  mathint balanceCaller_ = userAssets(e, caller);

  satisfy shares > 0;
  satisfy balanceCaller_ == _balanceCaller;
}

rule depositSatisfyDecrease(env e, calldataarg args){
  address caller = actualCaller(e);

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, args);
  mathint balanceCaller_ = userAssets(e, caller);

  satisfy shares > 0;
  satisfy balanceCaller_ < _balanceCaller;
}

rule depositSatisfyIncrease(env e, calldataarg args){
  mathint _balanceVault = userAssets(e, currentContract);
  uint256 shares = deposit(e, args);
  mathint balanceVault_ = userAssets(e, currentContract);

  satisfy shares > 0;
  satisfy balanceVault_ > _balanceVault;
}

