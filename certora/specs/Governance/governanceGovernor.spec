// check governanceGovernor functions must be called by governor
rule governanceGovernorOnly (method f, env e, calldataarg args) filtered {
  f ->  governanceGovernorOnly(f)
}{
  f(e, args);

  assert governorAdmin(e) == getGovernor(e);
}

// check non governanceGovernor functions mustcan be called by non governor at least once
rule governanceGovernorOnlySatisfy (method f, env e, calldataarg args) filtered {
  f ->  !( governanceGovernorOnly(f) || governanceIsHarness(f) )
}{
  f(e, args);

  satisfy governorAdmin(e) != getGovernor(e);
}

