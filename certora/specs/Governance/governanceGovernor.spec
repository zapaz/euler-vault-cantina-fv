rule governanceGovernorOnly (method f, env e, calldataarg args) filtered {
  f ->  governanceGovernorOnly(f)
}{
  f(e, args);

  assert governorAdmin(e) == getGovernor(e);
}


rule governanceGovernorOnlySatisfy (method f, env e, calldataarg args) filtered {
  f ->  !( governanceGovernorOnly(f) || governanceIsHarness(f) )
}{
  f(e, args);

  satisfy governorAdmin(e) != getGovernor(e);
}

