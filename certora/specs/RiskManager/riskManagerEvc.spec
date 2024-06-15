rule riskManagerEvcOnly(method f, env e, calldataarg args) filtered {
  f -> riskManagerEvc(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}

rule riskManagerEvcOnlySatisfy(method f, env e, calldataarg args) filtered {
  f -> !( riskManagerEvc(f) || riskManagerIsHarness(f) )
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}

