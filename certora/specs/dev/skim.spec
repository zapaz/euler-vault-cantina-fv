// OK

rule skimOk(env e, uint256 amount, address user){
  address caller = actualCaller(e);
  require ERC20a == asset();

  storage initialStorage = lastStorage;

  ERC20a.transferFrom(e, caller, currentContract, amount);
  uint256 _shares = skim(e, amount, caller);

  uint256 shares_ = deposit(e, amount, caller) at initialStorage;

  assert shares_ == _shares;
}

// skim should only take surplus
// cash after skim must be strictly equal to cash before + amount transfered
rule skim(env e, uint256 amount, address user){
  address caller = actualCaller(e);
  require caller != currentContract;
  require ERC20a == asset();

  uint256 _cash = cash(e);
  require _cash == userAssets(e, currentContract);

  ERC20a.transferFrom(e, caller, currentContract, amount);
  skim(e, max_uint256, caller);
  uint256 cash_ = cash(e);

  assert cash_ == require_uint256(_cash + amount);
}

// skim and deposit should have same effect
// shares via deposit should be equal to shares via skim
rule skimIdemDeposit(env e, uint256 amount){
  address caller = actualCaller(e);
  require caller != currentContract;
  require ERC20a == asset();
  require cash(e) == userAssets(e, currentContract);

  storage initialStorage = lastStorage;

  ERC20a.transferFrom(e, caller, currentContract, amount);
  uint256 _shares = skim(e, max_uint256, caller);

  uint256 shares_ = deposit(e, amount, caller) at initialStorage;

  assert shares_ == _shares;
}


rule skimWithdrawUnchanged(env e, uint256 amount, address user){
  address caller = actualCaller(e);
  require ERC20a == asset();

  uint256 _balance = userAssets(e, user);
  ERC20a.transferFrom(e, caller, currentContract, amount);
  skim(e, max_uint256, caller);
  withdraw(e, amount, caller, caller);
  uint256 balance_ = userAssets(e, user);

  assert balance_ == _balance;
}

// DEV

// KO

// catch mutation Vault_0 ?
// with no transfer balance sould not move
rule skimRedeemUnchanged(env e, uint256 amount, address user){
  address caller = actualCaller(e);
  require caller != currentContract;
  require ERC20a == asset();
  require cash(e) == userAssets(e, currentContract);

  uint256 _balance = userAssets(e, user);
  ERC20a.transferFrom(e, caller, currentContract, amount);
  skim(e, max_uint256, caller);
  redeem(e, max_uint256, caller, caller);
  uint256 balance_ = userAssets(e, user);

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