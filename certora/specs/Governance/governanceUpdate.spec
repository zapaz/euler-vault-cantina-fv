// check only governanceUpdateState functions can modify state
rule governanceUpdate(method f, env e, calldataarg args) filtered {
  f -> !(governanceIsHarness(f) || f.isView)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  assert storage_ != _storage => governanceUpdateState(f);
}

// check governanceUpdateState functions can modify state at least once
rule governanceUpdateSatisfy(method f, env e, calldataarg args) filtered {
  f -> governanceUpdateState(f)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  satisfy storage_ != _storage;
}
