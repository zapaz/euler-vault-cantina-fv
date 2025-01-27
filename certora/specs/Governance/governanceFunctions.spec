// identity functions that are harnessed
definition governanceIsHarness(method f) returns bool = baseIsHarness(f);

// identity functions that can update state
definition protocolConfigUpdateState(method f) returns bool =
          f.selector == sig:ProtocolConfig.setAdmin(address).selector
      ||  f.selector == sig:ProtocolConfig.setFeeReceiver(address).selector
      ||  f.selector == sig:ProtocolConfig.setProtocolFeeShare(uint16).selector
      ||  f.selector == sig:ProtocolConfig.setInterestFeeRange(uint16,uint16).selector
      ||  f.selector == sig:ProtocolConfig.setVaultInterestFeeRange(address,bool,uint16,uint16).selector
      ||  f.selector == sig:ProtocolConfig.setVaultFeeConfig(address,bool,address,uint16).selector;

// identity functions that can only be called by governor
definition governanceGovernorOnly(method f) returns bool = protocolConfigUpdateState(f)
      ||  f.selector == sig:clearLTV(address).selector
      ||  f.selector == sig:setCaps(uint16,uint16).selector
      ||  f.selector == sig:setConfigFlags(uint32).selector
      ||  f.selector == sig:setFeeReceiver(address).selector
      ||  f.selector == sig:setHookConfig(address,uint32).selector
      ||  f.selector == sig:setInterestFee(uint16).selector
      ||  f.selector == sig:setInterestRateModel(address).selector
      ||  f.selector == sig:setLTV(address,uint16,uint16,uint32).selector
      ||  f.selector == sig:setLiquidationCoolOffTime(uint16).selector
      ||  f.selector == sig:setMaxLiquidationDiscount(uint16).selector;

// identity functions that can modify state
definition governanceUpdateState(method f) returns bool = governanceGovernorOnly(f)
      ||  f.selector == sig:convertFees().selector
      ||  f.selector == sig:setGovernorAdmin(address).selector;
