rule mustNeverRevertsView(method f, env e, calldataarg arg) filtered { f -> !isHarness(f) && f.isView } {
  if (!f.isPayable) { require e.msg.value == 0; }
  require !storage_reentrancyLocked(e);

	f@withrevert(e, arg);

	assert !lastReverted;
}

rule mustNotAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !isHarness(f) } {
	f@withrevert(e, arg);
	satisfy !lastReverted;
}

rule mustNeverReverts(method f, env e, calldataarg arg) filtered { f -> !isHarness(f) } {
  if (!f.isPayable) { require e.msg.value == 0; }
	f@withrevert(e, arg);
	assert !lastReverted;
}

rule mustAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !isHarness(f) } {
	f@withrevert(e, arg);
	assert lastReverted ;
}
