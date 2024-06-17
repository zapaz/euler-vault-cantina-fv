// check borrowingIsNonReentrant functions are actually non reentrant
rule borrowingNonReentrantCheck(method f, env e, calldataarg args) filtered {f -> borrowingIsNonReentrant(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

// check borrowingIsNonReentrantView view functions are actually non reentrant
rule borrowingNonReentrantViewCheck(method f, env e, calldataarg args) filtered {f -> borrowingIsNonReentrantView(f)} {
    require e.msg.sender != storage_hookTarget();
    require e.msg.sender != currentContract;

    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

// check nonReentrant lock is well setted 
invariant borrowingReentrantLockInvariant(env e)
    storage_reentrancyLocked() == false;

