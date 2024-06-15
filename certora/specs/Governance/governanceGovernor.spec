rule governanceGovernorOnly (method f, env e, calldataarg args) filtered {
  f ->  governanceGovernorOnly(f)
}{
  f(e, args);

  assert e.msg.sender == governor;
}



