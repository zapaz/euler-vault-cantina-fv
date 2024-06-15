rule borrowingEvcOnly(method f, env e, calldataarg args) filtered {
  f ->  borrowingEvcUpdater(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}

rule borrowingEvcOnlySatisfy(method f, env e, calldataarg args) filtered {
  f ->  !( borrowingEvcUpdater(f) || borrowingIsHarness(f) )
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}



