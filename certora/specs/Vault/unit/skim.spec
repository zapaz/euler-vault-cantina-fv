// skim should only take surplus
// cash after skim must be strictly equal to cash before + amount transfered
rule skim(env e, uint256 amount, address receiver){
  address caller = actualCaller(e);
  require caller != currentContract;
  require ERC20a == asset();

  require cash(e) == userAssets(e, currentContract);
  ERC20a.transferFrom(e, caller, currentContract, amount);
  mathint _shares = convertToShares(e, amount);

  mathint _cash = cash(e);

  mathint _callerAssets = userAssets(e, caller);
  mathint _vaultAssets = userAssets(e, currentContract);
  mathint _receiverShares = userShares(e, receiver);

  mathint shares = skim(e, amount, receiver);

  mathint cash_ = cash(e);
  mathint callerAssets_ = userAssets(e, caller);
  mathint vaultAssets_ = userAssets(e, currentContract);
  mathint receiverShares_ = userShares(e, receiver);

  assert shares == _shares;
  assert shares > 0 <=> amount > 0;
  assert callerAssets_ == _callerAssets;
  assert vaultAssets_ == _vaultAssets;
  assert cash_ == _cash + amount;
  assert receiverShares_ == _receiverShares + shares;
}

rule skimMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  mathint _shares = skim(e, amount, _);

  mathint shares_ = skim(e, require_uint256(amount + more), _) at initialStorage;

  assert shares_ >= _shares;
}


// with no borrow
rule skimSupply(env e) {
  require actualCaller(e) != currentContract;
  require storage_totalBorrows(e) == 0;

  require userAssets(e, currentContract) >= totalAssets(e);

  skim(e, _, _);

  assert userAssets(e, currentContract) >= totalAssets(e);
}

// skim and deposit should have same effect
// shares via deposit should be equal to shares via skim
// (no borrow here)
rule skimIdemDeposit(env e, uint256 amount, address receiver){
  address caller = actualCaller(e);
  require caller != currentContract;

  require ERC20a == asset();
  require cash(e) == userAssets(e, currentContract);

  storage initialStorage = lastStorage;

  ERC20a.transferFrom(e, caller, currentContract, amount);
  mathint _shares = skim(e, max_uint256, receiver);
  mathint _receiverShares = userShares(e, receiver);

  mathint shares_ = deposit(e, amount, receiver) at initialStorage;
  mathint receiverShares_ = userShares(e, receiver);

  assert shares_ == _shares;
  assert receiverShares_ == _receiverShares;
}

///
// shares can be returned while
// - actual caller balance decrease
// - actual Vault balance increase
///
rule skimSatisfy(env e, address receiver){
  address caller = actualCaller(e);

  mathint _receiverShares = userShares(e, receiver);
  mathint shares = skim(e, _, receiver);
  mathint receiverShares_ = userShares(e, receiver);

  satisfy shares > 0;
  satisfy receiverShares_ > _receiverShares;
}

rule skimWithdrawUnchanged(env e, uint256 amount, address user){
  address caller = actualCaller(e);
  require ERC20a == asset();

  mathint _balance = userAssets(e, user);
  ERC20a.transferFrom(e, caller, currentContract, amount);
  skim(e, max_uint256, caller);
  withdraw(e, amount, caller, caller);
  mathint balance_ = userAssets(e, user);

  assert balance_ == _balance;
}

// KO

// catch mutation Vault_0 ?
// with no transfer balance sould not move
rule skimRedeemUnchanged(env e, uint256 amount, address user){
  address caller = actualCaller(e);
  require caller != currentContract;
  require ERC20a == asset();
  require cash(e) == userAssets(e, currentContract);

  mathint _balance = userAssets(e, user);
  ERC20a.transferFrom(e, caller, currentContract, amount);
  skim(e, max_uint256, caller);
  redeem(e, max_uint256, caller, caller);
  mathint balance_ = userAssets(e, user);

  assert balance_ == _balance;
}

// CVL ko ?
// Found different values for ghost function newInterestBorrows(0):
rule skimIdemDeposit2(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);
  require caller != currentContract;
  require ERC20a == asset();
  require cash(e) == userAssets(e, currentContract);

  storage initialStorage = lastStorage;

  ERC20a.transferFrom(e, caller, currentContract, amount);
  skim(e, max_uint256, caller);
  storage skimStorage = lastStorage;

  deposit(e, amount, caller) at initialStorage;
  storage depositStorage = lastStorage;

  assert skimStorage == depositStorage;
}