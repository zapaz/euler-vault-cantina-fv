// on pullDebt:
// - check only from can decrease it's asset balance by asset amount as expected
// - check only vault can increase it's asset balance by amount as expected
rule pullDebt(env e, uint256 amount, address from, address user){
  mathint _userAssets = userAssets(e, user);
  mathint assets = pullDebt(e, amount, from);
  mathint userAssets_ = userAssets(e, user);

  assert userAssets_ < _userAssets => (user == from)                   && (userAssets_ == _userAssets - assets);
  assert userAssets_ > _userAssets => (user == currentContract)        && (userAssets_ == _userAssets + assets);
}

