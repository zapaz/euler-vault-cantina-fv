rule vaultEvcOnly (method f, env e, calldataarg args) filtered {
  f -> vaultUpdater(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}

rule vaultEvcOnlySatisfy (method f, env e, calldataarg args) filtered {
  f -> !(vaultUpdater(f) || vaultIsHarness(f))
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}



