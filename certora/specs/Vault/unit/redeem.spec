rule redeem(env e, address receiver, address user){
  mathint _balance = userAssets(e, user);
  mathint redeemed = redeem(e, _, receiver, _);
  mathint balance_ = userAssets(e, user);

  assert balance_ < _balance => (user == currentContract) && (balance_ == _balance - redeemed);
  assert balance_ > _balance => (user == receiver) && (balance_ == _balance + redeemed);
}

rule redeemFromShares(env e, uint256 amount){
  assert convertToAssets(e, amount) == redeem(e, amount, _, _);
}

rule redeemPreview(env e, uint256 amount){
  assert previewRedeem(e, amount) == redeem(e, amount, _, _);
}

rule redeemMonotonicity(env e,  address owner, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  mathint _redeemed = redeem(e, amount, _, owner);

  mathint redeemed_ = redeem(e, require_uint256(amount + more), _, owner) at initialStorage;

  assert redeemed_ >= _redeemed;
}

rule redeemMax(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxShares1 = convertToShares(e, cash(e));
  uint256 maxShares2 = userShares(e, owner);

  uint256 maxRedeem  = maxRedeem(e, owner);

  assert isRedeemDisabled(e)         => maxRedeem == 0;
  assert controllerEnabled(e, owner) => maxRedeem == 0;
  assert maxRedeem  <= min(maxShares1, maxShares2);
}

rule redeemMaxSatisfy(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxShares1 = convertToShares(e, cash(e));
  uint256 maxShares2 = userShares(e, owner);

  uint256 maxRedeem  = maxRedeem(e, owner);

  satisfy (maxRedeem > 0) && (maxRedeem <= min(maxShares1, maxShares2));
}
