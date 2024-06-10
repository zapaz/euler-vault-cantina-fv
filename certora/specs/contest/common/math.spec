definition max(uint256 a, uint256 b) returns uint256 = a > b ? a : b;
definition min(uint256 a, uint256 b) returns uint256 = a < b ? a : b;
definition min3(uint256 a, uint256 b, uint256 c) returns uint256 = a < b ? min(a, c) : min(a, b);
definition min4(uint256 a, uint256 b, uint256 c, uint256 d) returns uint256 = a < b ? min3(a, c, d) : min3(b, c, d);
definition min5(uint256 a, uint256 b, uint256 c, uint256 d, uint256 e)
  returns uint256 = a < b ? min4(a, c, d, e) : min4(b, c, d, e);