// check liquidationEvcOnly functions can only be called by EVC
rule liquidationEvcOnly (method f, env e, calldataarg args) filtered {
    f ->  liquidationEvcOnly(f)
}{
  f(e, args);

  assert e.msg.sender == evc;
}


// check  than non liquidationEvcOnly can be called by other sender than EVC
rule liquidationEvcOnlySatisfy (method f, env e, calldataarg args) filtered {
    f ->  !liquidationEvcOnly(f)
}{
  f(e, args);

  satisfy e.msg.sender != evc;
}



