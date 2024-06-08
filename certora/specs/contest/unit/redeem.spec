// idem as deposit with share param instead of assetsShares
// repeat same functions


rule redeemMax(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxShares1 = convertToShares(e, cash(e));
  uint256 maxShares2 = userShares(e, owner);

  uint256 maxRedeem = maxRedeem(e, owner);

  assert isRedeemDisabled(e) => maxRedeem == 0;
  assert maxRedeem <= maxShares1;
  assert maxRedeem <= maxShares2;
}