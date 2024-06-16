///
// On redeem:
// - only vault can decrease it's assets balance, by redeemed amount
// - only actualCaller can increase it's assets balance, by redeemed amount
///
rule redeem(env e, address receiver, address user){
  mathint _balance = userAssets(e, user);
  mathint redeemed = redeem(e, _, receiver, _);
  mathint balance_ = userAssets(e, user);

  assert balance_ < _balance => (user == currentContract) && (balance_ == _balance - redeemed);
  assert balance_ > _balance => (user == receiver) && (balance_ == _balance + redeemed);
}

// redeemed amount is what expected by convertToAssets
rule redeemFromShares(env e, uint256 amount){
  assert convertToAssets(e, amount) == redeem(e, amount, _, _);
}

// redeemed amount is what expected by redeemPreview
rule redeemPreview(env e, uint256 amount){
  assert previewRedeem(e, amount) == redeem(e, amount, _, _);
}

// more redeem amount requested gives more redeemed
rule redeemMonotonicity(env e,  address owner, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  mathint _redeemed = redeem(e, amount, _, owner);

  mathint redeemed_ = redeem(e, require_uint256(amount + more), _, owner) at initialStorage;

  assert redeemed_ >= _redeemed;
}

// maxRedeen is less that these 2 values
// maxRedeen is 0 redeeem disable or controller enabled
rule redeemMax(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxShares1 = convertToShares(e, cash(e));
  uint256 maxShares2 = userShares(e, owner);

  uint256 maxRedeem  = maxRedeem(e, owner);

  assert isRedeemDisabled(e)         => maxRedeem == 0;
  assert controllerEnabled(e, owner) => maxRedeem == 0;
  assert maxRedeem  <= min(maxShares1, maxShares2);
}

// maxRedeen is possibly less that these 2 values
rule redeemMaxSatisfy(env e, address owner){
  require storage_totalBorrows(e) == 0;

  uint256 maxShares1 = convertToShares(e, cash(e));
  uint256 maxShares2 = userShares(e, owner);

  uint256 maxRedeem  = maxRedeem(e, owner);

  satisfy (maxRedeem > 0) && (maxRedeem <= min(maxShares1, maxShares2));
}
