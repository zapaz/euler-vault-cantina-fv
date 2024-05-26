///////////////////////////////////////////////////////////////////////////////////////////////
// deposit associated rules
///////////////////////////////////////////////////////////////////////////////////////////////
// - deposited amount is equal to amount or actuallCaller balance (if amount is max_uint256)
// - deposit must be called by evc
// - only Vault can increase it's balance, by deposited amount
// - only actualCaller can decrease it's balance, by deposited amount
///////////////////////////////////////////////////////////////////////////////////////////////
rule deposit(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);
  mathint deposit = (amount == max_uint256) ? userAssets(e, caller) : amount;

  mathint _balance = userAssets(e, user);
  deposit(e, amount, receiver);
  mathint balance_ = userAssets(e, user);

  assert e.msg.sender == evc;
  assert balance_ > _balance => (user == currentContract) && (balance_ == _balance + deposit);
  assert balance_ < _balance => (user == caller) && (balance_ == _balance - deposit);
}

rule depositSatisfyDecrease(env e, calldataarg args){
  address caller = actualCaller(e);

  mathint _balance = userAssets(e, caller);
  deposit(e, args);
  mathint balance_ = userAssets(e, caller);

  satisfy balance_ < _balance;
}

rule depositSatisfyIncrease(env e, calldataarg args){
  mathint _balance = userAssets(e, currentContract);
  deposit(e, args);
  mathint balance_ = userAssets(e, currentContract);

  satisfy balance_ > _balance;
}

