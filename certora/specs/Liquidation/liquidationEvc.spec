rule liquidationEvcOnly (method f, env e, calldataarg args) filtered {
    f ->  liquidationEvcOnly(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}



rule liquidationEvcOnlySatisfy (method f, env e, calldataarg args) filtered {
    f ->  !liquidationEvcOnly(f)
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}



