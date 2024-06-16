// Vault constant value
definition VIRTUAL_DEPOSIT() returns uint112 = 10^6;

// vault muldiv in CVL
function mulDiv112(uint112 amount, uint112 totalParts, uint112 totalAmount) returns uint256 {
  uint256 mul = require_uint256(amount * totalParts);
  uint256 div = require_uint256(mul / totalAmount);
  return div;
}

// check converToShares calculation is correct
rule assetsSharesCVL(env e, uint112 assets, uint112 totalAssets, uint112 totalShares){
  require totalShares == require_uint112(storage_totalShares(e) + VIRTUAL_DEPOSIT());
  require totalAssets == require_uint112(totalAssets(e) + VIRTUAL_DEPOSIT());

  uint256 _shares = mulDiv112(assets, totalShares, totalAssets);
  uint256 shares_ = convertToShares(e, assets);

  assert shares_ == _shares;
}

// check convertToAssets calculation is correct
rule sharesAssetsCVL(env e, uint112 shares, uint112 totalShares, uint112 totalAssets){
  require totalShares == require_uint112(storage_totalShares(e) + VIRTUAL_DEPOSIT());
  require totalAssets == require_uint112(totalAssets(e) + VIRTUAL_DEPOSIT());

  uint256 _assets = mulDiv112(shares, totalAssets, totalShares);
  uint256 assets_ = convertToAssets(e, shares);

  assert assets_ == _assets;
}

// check convertToshares then convertToAssets never increases assets
// but not exactly equal ("favour the house")
rule assetsSharesAssets(env e){
  uint256 _assets;
  uint256 shares = convertToShares(e, _assets);
  uint256 assets_ = convertToAssets(e, shares);

  assert assets_ <= _assets;
}

// check ratio assets/shares values read in state
// are always the result of the convertToShares
rule assetsShares(method f, env e, calldataarg args, address user)  filtered {
  f -> !(vaultIsHarness(f) || f.isView)
}{
  uint256 _assets = userAssets(e, user);
  uint256 _shares = userShares(e, user);
  require _shares == convertToShares(e, _assets);

  f(e, args);

  uint256 assets_ =  userAssets(e, user);
  uint256 shares_ =  userShares(e, user);
  assert  shares_ == convertToShares(e, assets_);
}