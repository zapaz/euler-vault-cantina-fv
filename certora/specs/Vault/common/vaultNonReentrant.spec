// check that these vault write functions are non-reentrant
rule vaultNonReentrantCheck(method f, env e, calldataarg args) filtered {f -> vaultIsNonReentrant(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert lastReverted;
}

// check that these vault view functions are non-reentrant
rule vaultNonReentrantViewCheck(method f, env e, calldataarg args) filtered {f -> vaultIsNonReentrantView(f)} {
    require storage_reentrancyLocked() == true;

    f@withrevert(e, args);

    assert !lastReverted  => e.msg.sender == storage_hookTarget()
                          || e.msg.sender == currentContract;
}

// check the vault locked state is never locked (unless during a tx)
invariant vaultReentrantLockInvariant(env e)
    storage_reentrancyLocked() == false;

