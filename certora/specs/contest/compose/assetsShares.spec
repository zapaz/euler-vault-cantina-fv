function CVLconvertToShares(uint112 assets, uint112 totalShares, uint112 totalAssets) returns uint256 {
  require(totalAssets >= 10^6 && totalShares >= 10^6);
  uint256 mul = require_uint256(assets * totalShares);
  uint256 div = require_uint256(mul / totalAssets);
  return div;
}

function CVLconvertToAssets(uint112 shares, uint112 totalShares, uint112 totalAssets) returns uint256 {
  require(totalAssets >= 10^6 && totalShares >= 10^6);
  uint256 mul = require_uint256(shares * totalAssets);
  uint256 div = require_uint256(mul / totalShares);
  return div;
}

rule assetsSharesCVL(env e, uint112 assets){
  uint112 totalShares = storage_totalShares(e);
  uint112 totalAssets = require_uint112(totalAssets(e));

  uint256 _shares = CVLconvertToShares(assets, totalShares, totalAssets);
  uint256 shares_ = convertToShares(e, assets);

  assert shares_ == _shares;
}

rule sharesAssetsCVL(env e, uint112 shares){
  uint112 totalAssets = require_uint112(totalAssets(e));
  uint112 totalShares = storage_totalShares(e);

  assert convertToAssets(e, shares) == CVLconvertToAssets(shares, totalShares, totalAssets);
}

rule assetsSharesAssets(env e){
  uint256 _assets;
  uint256 shares = convertToShares(e, _assets);
  uint256 assets_ = convertToAssets(e, shares);

  assert assets_ == _assets;
}

