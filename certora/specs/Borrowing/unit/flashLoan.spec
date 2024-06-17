// not include in verified rules...
rule flashLoan(env e, uint256 amount, address receiver, address user){
  address caller = actualCaller(e);
}