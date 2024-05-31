rule nonReentrantCheck(method f, env e, calldataarg args) filtered {f -> isNonReentrant(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

rule nonReentrantViewCheck(method f, env e, calldataarg args) filtered {f -> isNonReentrantView(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert !lastReverted  => e.msg.sender == storage_hookTarget()
                          || e.msg.sender == currentContract;
                      // <=> e.msg.sender == storage_hookTarget()
                      //  || (storage_hookTarget() == ProxyUtils.useViewCaller() && e.msg.sender == currentContract);
}

invariant reentrantLockInvariant(env e)
    storage_reentrancyLocked() == false;

