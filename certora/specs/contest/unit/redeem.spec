rule redeemMax(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxShares1 = convertToShares(e, cash(e));
  uint256 maxShares2 = userShares(e, owner);
  uint256 maxShares3 = isRedeemDisabled(e)         ? 0 : max_uint256;
  uint256 maxShares4 = controllerEnabled(e, owner) ? 0 : max_uint256;

  uint256 maxRedeem  = maxRedeem(e, owner);

  assert  maxRedeem  <= min4(maxShares1, maxShares2, maxShares3, maxShares4);
  // not equal, is it a bug ?
}