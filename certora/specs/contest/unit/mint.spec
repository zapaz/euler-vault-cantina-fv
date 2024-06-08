// idem as deposit with share param instead of assetsShares
// repeat same functions


rule mintMax(env e){
  require storage_totalBorrows(e) == 0;

  uint256 supply = cash(e);
  uint256 supplyCap = storage_supplyCap();
  uint256 maxShares1 = convertToShares(e, require_uint256(supplyCap - supply));
  uint256 maxShares2 =  convertToShares(e, assert_uint256(max_uint112 - supply));
  uint256 maxShares3 = assert_uint256(max_uint112 - storage_totalShares(e));

  uint256 maxMint = maxMint(e, _);

  assert isMintDisabled(e)    => maxMint == 0;
  assert supply  >= supplyCap => maxMint == 0;
  assert maxMint <= maxShares1;
  assert maxMint <= maxShares2;
  assert maxMint <= maxShares3;
}

// maxMint should be less than supply cap
// (no borrow there)
rule mintMaxEqual(env e){
  require storage_totalBorrows(e) == 0;

  uint256 supply = cash(e);
  uint256 supplyCap = storage_supplyCap();
  uint256 maxMint = maxMint(e, _);

  if (isMintDisabled(e)) {
    assert maxMint == 0;
  } else if (supply >= supplyCap) {
    assert maxMint == 0;
  } else {
    uint256 maxAssets1 = require_uint256(supplyCap - supply);
    uint256 maxAssets2 = require_uint256(max_uint112 - cash(e));
    uint256 maxAssets  = min(maxAssets1, maxAssets2);

    uint256 maxShares1 = convertToShares(e, maxAssets);
    uint256 maxShares2 = require_uint256(max_uint112 - storage_totalShares(e));
    uint256 maxShares  = min(maxShares1, maxShares2);
`
    assert maxMint == maxShares;
  }
}

rule mintMaxSatisfy(env e){
  uint256 supply = cash(e);
  uint256 supplyCap = storage_supplyCap();

  require storage_totalBorrows(e) == 0;
  require(!isMintDisabled(e));
  require(supply < supplyCap);

  maxMint(e, _);

  satisfy true;
}