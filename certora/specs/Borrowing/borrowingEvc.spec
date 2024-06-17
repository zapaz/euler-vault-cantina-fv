// check borrowingEvcUpdater functions can only be called by EVC
rule borrowingEvcOnly(method f, env e, calldataarg args) filtered {
  f ->  borrowingEvcUpdater(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}

// check non borrowingEvcUpdater functions can be called by non EVC sender
rule borrowingEvcOnlySatisfy(method f, env e, calldataarg args) filtered {
  f ->  !( borrowingEvcUpdater(f) || borrowingIsHarness(f) )
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}



