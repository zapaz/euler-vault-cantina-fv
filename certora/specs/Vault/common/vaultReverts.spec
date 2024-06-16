// check these vault view functions never reverts (unless if eth sent to them)
rule vaultMustNeverRevertsView(method f, env e, calldataarg arg) filtered { f -> vaultNeverRevertsView (f) } {
  if (!f.isPayable) { require e.msg.value == 0; }
  require !storage_reentrancyLocked();

	f@withrevert(e, arg);

	assert !lastReverted;
}

// check that vault functions not allways reverts
rule vaultMustNotAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !vaultIsHarness(f) } {
	f@withrevert(e, arg);
	satisfy !lastReverted;
}
