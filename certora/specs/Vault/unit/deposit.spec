///
// deposit associated rules
///

///
// On deposit:
// - only vault can increase it's assets balance, by deposited amount
// - only actualCaller can decrease it's assets balance, by deposited amount
///
rule deposit(env e, uint256 amount, address user){
  address caller = actualCaller(e);

  mathint deposit = (amount == max_uint256) ? userAssets(e, caller) : amount;

  mathint _userAssets = userAssets(e, user);
  deposit(e, amount, _);
  mathint userAssets_ = userAssets(e, user);

  assert userAssets_ > _userAssets => (user == currentContract) && (userAssets_ == _userAssets + deposit);
  assert userAssets_ < _userAssets => (user == caller)          && (userAssets_ == _userAssets - deposit);
}

// check shares returned on deposit are equal to previewDesposit result
rule depositPreview(env e, uint256 amount){
  assert previewDeposit(e, amount) == deposit(e, amount, _);
}

// check more deposit return more shares
rule depositMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  uint256 _shares = deposit(e, amount, _);

  uint256 shares_ = deposit(e, require_uint256(amount + more), _) at initialStorage;

  assert shares_ >= _shares;
}


///
// Assuming actual caller is not the vault (caller != currentContract)
// on deposit:
// - shares returned are equal to convertToShares of amount
// - some shares are returned if and only if amount is strictly positive
// - caller assets balance decrease by amount
// - receiver shares balance increase by shares
///
rule depositShares(env e, uint256 amount, address receiver){
  address caller = actualCaller(e);
  require caller != currentContract;

  mathint _callerAssets = userAssets(e, caller);
  mathint _receiverShares = userShares(e, receiver);

  mathint _shares = convertToShares(e, amount);

  mathint shares = deposit(e, amount, receiver);

  mathint callerAssets_ = userAssets(e, caller);
  mathint receiverShares_ = userShares(e, receiver);

  assert shares == _shares;
  assert shares > 0 <=> amount > 0;
  assert callerAssets_ + amount == _callerAssets;
  assert receiverShares_ == _receiverShares + shares;
}

///
// shares sould be returned if and only if caller balance decrease
///
// rule violated:
//  - fails when caller is vault
//  - POC available => `test/contest/DepositSelfHack.t.sol`
//  - report => `findings/DepositSelfHack.md`
///
rule depositSharesViolated(env e){
  address caller = actualCaller(e);

  mathint _callerAssets = userAssets(e, caller);
  mathint shares = deposit(e, _, _);
  mathint callerAssets_ = userAssets(e, caller);

  assert shares > 0 <=> callerAssets_ < _callerAssets;
}

// ensure depositMax is less than expected
rule depositMax(env e){
  require storage_totalBorrows(e) == 0;

  uint256 supply     = cash(e);
  uint256 supplyCap  = storage_supplyCap();

  uint256 maxAssets1 = require_uint256(supplyCap - supply);
  uint256 maxAssets2 = assert_uint256(max_uint112 - supply);
  uint256 maxAssets3 = convertToAssets(e, assert_uint256(max_uint112 - storage_totalShares(e)));
  uint256 maxAssets4 = isDepositDisabled(e) ? 0 : max_uint256;
  uint256 maxAssets5 = supply >= supplyCap  ? 0 : max_uint256;

  uint256 maxDeposit = maxDeposit(e, _);

  assert  maxDeposit <= min5(maxAssets1, maxAssets2, maxAssets3, maxAssets4, maxAssets5);
}

///
// ensure shares can be returned
///
rule depositSatisfy(env e){
  mathint shares = deposit(e, _, _);

  satisfy shares > 0;
}


