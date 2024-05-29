import "../Base.spec";

// rule fails when caller is Vault (caller == currentContract)
// forge test POC available => `depositSelf.t.sol`
rule depositShares(env e, calldataarg args){
  address caller = actualCaller(e);

  mathint _balanceCaller = userAssets(e, caller);
  uint256 shares = deposit(e, args);
  mathint balanceCaller_ = userAssets(e, caller);

  assert shares > 0 <=> balanceCaller_ < _balanceCaller;
}