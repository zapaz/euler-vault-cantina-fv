rule vaultBalanceChanged (method f, env e, calldataarg args, address user)  filtered {
  f -> !(f.isView || isHarness(f))
}{
  mathint _balanceUser = userAssets(e, user);
  f(e, args);
  mathint balanceUser_ = userAssets(e, user);

  assert balanceUser_ != _balanceUser =>
       f.selector == sig:deposit(uint256,address).selector
    || f.selector == sig:mint(uint256,address).selector
    || f.selector == sig:withdraw(uint256,address,address).selector
    || f.selector == sig:redeem(uint256,address,address).selector;
}

// without Borrowing no need to take into account totalBorrowed
// with Borrowing would need to take into account totalBorrowed
rule vaultBalanceGreaterThanTotalAssets(method f, env e, calldataarg args) filtered {
  f -> !(f.isView || isHarness(f) || f.selector == sig:skim(uint256,address).selector)
}{
  address caller = actualCaller(e);
  require caller != currentContract;

  require userAssets(e, currentContract) >= totalAssets(e);

  f(e, args);

  assert userAssets(e, currentContract) >= totalAssets(e);
}

rule vaultSkim(env e, uint256 amount, address receiver) {
  address caller = actualCaller(e);

  require userAssets(e, currentContract) >= totalAssets(e);

  skim(e, amount, receiver);

  assert userAssets(e, currentContract) >= totalAssets(e);
}

