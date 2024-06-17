// not used in verified rules

rule riskManagerAccountStatus(method f, env e, calldataarg args, address account, address[] collaterals) {
  checkAccountLiquidity(e, account,  collaterals);
  // liquidity is ok, not reverted

  f@withrevert(e, args);

  checkAccountLiquidity@withrevert(e, account,  collaterals);

  // liquidity should stil be ok!  not last reverted
  assert !lastReverted;
}
