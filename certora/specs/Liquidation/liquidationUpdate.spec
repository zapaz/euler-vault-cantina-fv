rule liquidationUpdate(method f, env e, calldataarg args) filtered {
  f -> !(liquidationIsHarness(f) || f.isView)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  assert storage_ != _storage => liquidationUpdateState(f);
}


rule liquidationUpdateSatisfy(method f, env e, calldataarg args) filtered {
  f -> liquidationUpdateState(f)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  satisfy storage_ != _storage;
}
