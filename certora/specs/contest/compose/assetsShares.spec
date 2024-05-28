definition VIRTUAL_DEPOSIT() returns uint112 = 10^6;

function mulDiv112(uint112 amount, uint112 totalParts, uint112 totalAmount) returns uint256 {
  uint256 mul = require_uint256(amount * totalParts);
  uint256 div = require_uint256(mul / totalAmount);
  return div;
}

rule assetsSharesCVL(env e, uint112 assets, uint112 totalAssets, uint112 totalShares){
  require totalShares == require_uint112(storage_totalShares(e) + VIRTUAL_DEPOSIT());
  require totalAssets == require_uint112(totalAssets(e) + VIRTUAL_DEPOSIT());

  uint256 _shares = mulDiv112(assets, totalShares, totalAssets);
  uint256 shares_ = convertToShares(e, assets);

  assert shares_ == _shares;
}

rule sharesAssetsCVL(env e, uint112 shares, uint112 totalShares, uint112 totalAssets){
  require totalShares == require_uint112(storage_totalShares(e) + VIRTUAL_DEPOSIT());
  require totalAssets == require_uint112(totalAssets(e) + VIRTUAL_DEPOSIT());

  uint256 _assets = mulDiv112(shares, totalAssets, totalShares);
  uint256 assets_ = convertToAssets(e, shares);

  assert assets_ == _assets;
}

rule assetsSharesAssets(env e){
  uint256 _assets;
  uint256 shares = convertToShares(e, _assets);
  uint256 assets_ = convertToAssets(e, shares);

  assert assets_ <= _assets;
}

