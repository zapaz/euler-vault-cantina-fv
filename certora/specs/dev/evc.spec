rule onlyEVC (method f, env e, calldataarg args) filtered {
    f ->  f.selector == sig:transfer(address,uint256).selector
      ||  f.selector == sig:transferFrom(address,address,uint256).selector
      ||  f.selector == sig:transferFromMax(address,address).selector
      ||  f.selector == sig:deposit(uint256,address).selector
      ||  f.selector == sig:mint(uint256,address).selector
      ||  f.selector == sig:withdraw(uint256,address,address).selector
      ||  f.selector == sig:redeem(uint256,address,address).selector
      ||  f.selector == sig:skim(uint256,address).selector
      // ||  f.selector == sig:borrow(uint256,address).selector
      // ||  f.selector == sig:repay(uint256,address).selector
      // ||  f.selector == sig:repayWithShares(uint256,address).selector
      // ||  f.selector == sig:pullDebt(uint256,address).selector
      // ||  f.selector == sig:touch().selector
      // ||  f.selector == sig:liquidate(address,address,uint256,uint256).selector
      // ||  f.selector == sig:convertFees().selector
  }{
  f(e, args);

  assert e.msg.sender == evc;
}



