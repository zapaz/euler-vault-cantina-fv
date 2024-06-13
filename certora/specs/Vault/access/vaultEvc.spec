rule onlyVaultEVC (method f, env e, calldataarg args) filtered {
    f ->  f.selector == sig:transfer(address,uint256).selector
      ||  f.selector == sig:transferFrom(address,address,uint256).selector
      ||  f.selector == sig:transferFromMax(address,address).selector
      ||  f.selector == sig:deposit(uint256,address).selector
      ||  f.selector == sig:mint(uint256,address).selector
      ||  f.selector == sig:withdraw(uint256,address,address).selector
      ||  f.selector == sig:redeem(uint256,address,address).selector
      ||  f.selector == sig:skim(uint256,address).selector
  }{
  f(e, args);

  assert e.msg.sender == evc;
}



