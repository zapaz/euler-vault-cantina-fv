rule onlyGovernanceEVC (method f, env e, calldataarg args) filtered {
    f ->  f.selector == sig:liquidate(address,address,uint256,uint256).selector
      ||  f.selector == sig:convertFees().selector
  }{
  f(e, args);

  assert e.msg.sender == evc;
}



