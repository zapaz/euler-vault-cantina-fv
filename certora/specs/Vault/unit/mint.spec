rule mint(env e, uint256 amount, address user){
  address caller = actualCaller(e);

  mathint _userAssets = userAssets(e, user);
  mathint assets = mint(e, amount, _);
  mathint userAssets_ = userAssets(e, user);

  assert userAssets_ < _userAssets => (user == caller)          && (userAssets_ == _userAssets - assets);
  assert userAssets_ > _userAssets => (user == currentContract) && (userAssets_ == _userAssets + assets);
}

rule mintPreview(env e, uint256 amount){
  assert previewMint(e, amount) == mint(e, amount, _);
}

rule mintMonotonicity(env e, uint256 amount, uint256 more){
  storage initialStorage = lastStorage;
  uint256 _assets = mint(e, amount, _);

  uint256 assets_ = mint(e, require_uint256(amount + more), _) at initialStorage;

  assert assets_ >= _assets;
}


rule mintSatisfy(env e){
  mathint assets = mint(e, _, _);

  satisfy assets > 0;
}


rule mintMax(env e){
  require storage_totalBorrows(e) == 0;

  uint256 supply     = cash(e);
  uint256 supplyCap  = storage_supplyCap();

  uint256 maxShares1 = convertToShares(e, require_uint256(supplyCap - supply));
  uint256 maxShares2 = convertToShares(e, assert_uint256(max_uint112 - supply));
  uint256 maxShares3 = assert_uint256(max_uint112 - storage_totalShares(e));
  uint256 maxShares4 = isMintDisabled(e)   ? 0 : max_uint256;
  uint256 maxShares5 = supply >= supplyCap ? 0 : max_uint256;

  uint256 maxMint    = maxMint(e, _);

  assert  maxMint    == min5(maxShares1, maxShares2, maxShares3, maxShares4, maxShares5);
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