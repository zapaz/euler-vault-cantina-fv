rule vaultUpdate(method f, env e, calldataarg args) filtered {
  f -> !(vaultIsHarness(f) || f.isView)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  assert storage_ != _storage => vaultUpdateState(f);
}

rule vaultUpdateSatisfy(method f, env e, calldataarg args) filtered {
  f -> vaultUpdateState(f)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  satisfy storage_ != _storage;
}
