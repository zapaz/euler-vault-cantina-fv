rule vaultNonReentrantCheck(method f, env e, calldataarg args) filtered {f -> vaultIsNonReentrant(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

rule vaultNonReentrantViewCheck(method f, env e, calldataarg args) filtered {f -> vaultIsNonReentrantView(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert !lastReverted  => e.msg.sender == storage_hookTarget()
                          || e.msg.sender == currentContract;
                      // <=> e.msg.sender == storage_hookTarget()
                      //  || (storage_hookTarget() == ProxyUtils.useViewCaller() && e.msg.sender == currentContract);
}

invariant vaultReentrantLockInvariant(env e)
    storage_reentrancyLocked() == false;

