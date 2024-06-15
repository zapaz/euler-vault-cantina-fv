rule riskManagerUpdate(method f, env e, calldataarg args) filtered {
  f -> !(riskManagerIsHarness(f) || f.isView)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  assert storage_ != _storage => riskManagerUpdateState(f);
}

rule riskManagerUpdateSatisfy(method f, env e, calldataarg args) filtered {
  f -> riskManagerUpdateState(f)
}{
  storage _storage = lastStorage;
  f(e, args);
  storage storage_ = lastStorage;

  satisfy storage_ != _storage;
}
