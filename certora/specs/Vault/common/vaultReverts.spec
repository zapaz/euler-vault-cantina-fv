rule vaultMustNeverRevertsView(method f, env e, calldataarg arg) filtered { f -> vaultNeverRevertsView (f) } {
  if (!f.isPayable) { require e.msg.value == 0; }
  require !storage_reentrancyLocked();

	f@withrevert(e, arg);

	assert !lastReverted;
}

rule vaultMustNotAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !vaultIsHarness(f) } {
	f@withrevert(e, arg);
	satisfy !lastReverted;
}
