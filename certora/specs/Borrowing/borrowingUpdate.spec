rule borrowingUpdate(method f, env e, calldataarg args) filtered {
  f -> !(borrowingIsHarness(f) || f.isView)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  assert storage_ != _storage => borrowingUpdateState(f);
}

rule borrowingUpdateSatisfy(method f, env e, calldataarg args) filtered {
  f -> borrowingUpdateState(f)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  satisfy storage_ != _storage;
}
