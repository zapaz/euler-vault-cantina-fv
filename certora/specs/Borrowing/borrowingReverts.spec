// check borrowing functions not allways revert
rule borrowingMustNotAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) } {
	f@withrevert(e, arg);
	satisfy !lastReverted;
}


// rules below bot included in the verfied rules

// check simulation borrowing functions allways revert
rule borrowingMustAlwaysReverts(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) } {
	f@withrevert(e, arg);
	assert lastReverted ;
}

// rules bellow ko
// some implying not ERC2646 compliance, but already stated un Euler doc

rule borrowingMustNeverReverts(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) } {
  if (!f.isPayable) { require e.msg.value == 0; }
	f@withrevert(e, arg);
	assert !lastReverted;
}

rule borrowingMustNeverRevertsView(method f, env e, calldataarg arg) filtered { f -> !borrowingIsHarness(f) && f.isView } {
  if (!f.isPayable) { require e.msg.value == 0; }
  require !storage_reentrancyLocked();

	f@withrevert(e, arg);

	assert !lastReverted;
}


