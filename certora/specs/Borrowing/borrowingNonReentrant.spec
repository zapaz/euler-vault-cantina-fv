rule borrowingNonReentrantCheck(method f, env e, calldataarg args) filtered {f -> borrowingIsNonReentrant(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

rule borrowingNonReentrantViewCheck(method f, env e, calldataarg args) filtered {f -> borrowingIsNonReentrantView(f)} {
    require e.msg.sender != storage_hookTarget();
    require e.msg.sender != currentContract;

    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

invariant borrowingReentrantLockInvariant(env e)
    storage_reentrancyLocked() == false;

