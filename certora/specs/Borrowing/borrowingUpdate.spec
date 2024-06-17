// check only borrowingUpdateState functions can modify state
rule borrowingUpdate(method f, env e, calldataarg args) filtered {
  f -> !(borrowingIsHarness(f) || f.isView)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  assert storage_ != _storage => borrowingUpdateState(f);
}

// check borrowingUpdateState functions can at least modify state once
rule borrowingUpdateSatisfy(method f, env e, calldataarg args) filtered {
  f -> borrowingUpdateState(f)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  satisfy storage_ != _storage;
}
