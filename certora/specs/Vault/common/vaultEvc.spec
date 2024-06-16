// check only EVC can call functions than update the vault
// i.e. vaultUpdater functions
rule vaultEvcOnly (method f, env e, calldataarg args) filtered {
  f -> vaultUpdater(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}

// check other functions (not vaultUpdater ones) can be called by other sender thant the EVC
rule vaultEvcOnlySatisfy (method f, env e, calldataarg args) filtered {
  f -> !(vaultUpdater(f) || vaultIsHarness(f))
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}



