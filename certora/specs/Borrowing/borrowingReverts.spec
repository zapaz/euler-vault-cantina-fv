rule borrowingMustNeverRevertsView(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) && f.isView } {
  if (!f.isPayable) { require e.msg.value == 0; }
  require !storage_reentrancyLocked();

	f@withrevert(e, arg);

	assert !lastReverted;
}

rule borrowingMustNotAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) } {
	f@withrevert(e, arg);
	satisfy !lastReverted;
}

rule borrowingMustNeverReverts(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) } {
  if (!f.isPayable) { require e.msg.value == 0; }
	f@withrevert(e, arg);
	assert !lastReverted;
}

rule borrowingMustAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) } {
	f@withrevert(e, arg);
	assert lastReverted ;
}

