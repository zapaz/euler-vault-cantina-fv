///
// deposit associated rules
///

///
// - deposited amount is equal to amount or actuallCaller balance (if amount is max_uint256)
// - deposit must be called by evc
// - deposit shares are equal to expected depositPreview value
// - only Vault can increase it's balance, by deposited amount
// - only actualCaller can decrease it's balance, by deposited amount
///
rule deposit(env e, uint256 amount, address user){
  address caller = actualCaller(e);

  mathint deposit = (amount == max_uint256) ? userAssets(e, caller) : amount;

  mathint _balanceUser = userAssets(e, user);
  deposit(e, amount, _);
  mathint balanceUser_ = userAssets(e, user);

  assert e.msg.sender == evc;
  assert balanceUser_ > _balanceUser => (user == currentContract) && (balanceUser_ == _balanceUser + deposit);
  assert balanceUser_ < _balanceUser => (user == caller)          && (balanceUser_ == _balanceUser - deposit);
}

///
// shares sould be returned if and only if caller balance decrease
///
// rule fails: that's a bug!
//  - fails when caller is Vault
//  - POC available => `test/contest/DepositSelfHack.t.sol`
//  - report => `findings/DepositSelfHack.md`
///
rule depositShares(env e){
  address caller = actualCaller(e);

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, _, _);
  mathint balanceCaller_ = userAssets(e, caller);

  assert shares > 0 <=> balanceCaller_ < _balanceCaller;
}

///
// weak version of `depositShares` rule
// assuming actual caller is not the Vault (caller != currentContract)
// shares are returned if and only if caller balance decrease
///
rule depositSharesWeak(env e, uint256 amount){
  address caller = actualCaller(e);
  require caller != currentContract;

  mathint _balanceCaller = userAssets(e, caller);
  uint256 _shares = previewDeposit(e, amount);
  uint256 shares_ = convertToShares(e, amount);
  uint256 shares = deposit(e, amount, _);
  mathint balanceCaller_ = userAssets(e, caller);

  assert shares == shares_;
  assert shares == _shares;
  assert balanceCaller_ + amount == _balanceCaller;
  assert shares > 0 <=> balanceCaller_ < _balanceCaller;
}

///
// another rule proving the bug
// shares are returned whereas actual caller balance is unchanged
///
rule depositSharesByVault(env e){
  address caller = actualCaller(e);
  require caller == currentContract;

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, _, _);
  mathint balanceCaller_ = userAssets(e, caller);

  satisfy shares > 0;
  satisfy balanceCaller_ == _balanceCaller;
}

///
// shares can be returned while
// - actual caller balance decrease
// - actual Vault balance increase
///
rule depositSatisfy(env e){
  address caller = actualCaller(e);

  mathint _balanceCaller = userAssets(e, caller);
  mathint _balanceVault = userAssets(e, currentContract);
  uint256 shares = deposit(e, _, _);
  mathint balanceCaller_ = userAssets(e, caller);
  mathint balanceVault_ = userAssets(e, currentContract);

  satisfy shares > 0;
  satisfy balanceCaller_ < _balanceCaller;
  satisfy balanceVault_ > _balanceVault;
}


