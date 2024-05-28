// catch mutation AssetTransfers_0
rule zeroAddressUnchanged(method f, env e, calldataarg args)  filtered { f -> !f.isView } {
  uint256 _balance = userAssets(e, 0);
  f(e, args);
  uint256 balance_ = userAssets(e, 0);

  assert balance_ == _balance;
}
