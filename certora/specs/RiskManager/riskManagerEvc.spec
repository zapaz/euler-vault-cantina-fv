// check riskManagerEvc functions can only be called by EVC
rule riskManagerEvcOnly(method f, env e, calldataarg args) filtered {
  f -> riskManagerEvc(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}

// check non riskManagerEvc functions can be called by non EVC sender
rule riskManagerEvcOnlySatisfy(method f, env e, calldataarg args) filtered {
  f -> !( riskManagerEvc(f) || riskManagerIsHarness(f) )
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}

