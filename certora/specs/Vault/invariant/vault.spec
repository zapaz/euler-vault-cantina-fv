rule vaulAssetsChanged (method f, env e, calldataarg args, address user)  filtered {
  f -> !(f.isView || vaultIsHarness(f))
}{
  require user != currentContract;

  mathint _userAssets = userAssets(e, user);
  f(e, args);
  mathint userAssets_ = userAssets(e, user);

  assert userAssets_ < _userAssets =>
       f.selector == sig:deposit(uint256,address).selector
    || f.selector == sig:mint(uint256,address).selector;

  assert userAssets_ > _userAssets =>
       f.selector == sig:withdraw(uint256,address,address).selector
    || f.selector == sig:redeem(uint256,address,address).selector;
}

rule vaulSharesChanged (method f, env e, calldataarg args, address user)  filtered {
  f -> !(f.isView || vaultIsHarness(f) || isTransfer(f))
}{
  require user != currentContract;

  mathint _userShares = userShares(e, user);
  f(e, args);
  mathint userShares_ = userShares(e, user);

  assert userShares_ > _userShares =>
       f.selector == sig:deposit(uint256,address).selector
    || f.selector == sig:mint(uint256,address).selector
    || f.selector == sig:skim(uint256,address).selector;

  assert userShares_ < _userShares =>
       f.selector == sig:withdraw(uint256,address,address).selector
    || f.selector == sig:redeem(uint256,address,address).selector;
}

// without Borrowing no need to take into account totalBorrowed
rule vaultBalanceGreaterThanTotalAssets(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || vaultIsHarness(f) || f.selector == sig:skim(uint256,address).selector)
}{
  address caller = actualCaller(e);
  require caller != currentContract;

  require userAssets(e, currentContract) >= totalAssets(e);

  f(e, args);

  assert userAssets(e, currentContract) >= totalAssets(e);
}



