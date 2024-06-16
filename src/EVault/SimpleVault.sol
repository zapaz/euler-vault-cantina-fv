// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import {EVault} from "src/EVault/EVault.sol";
import {IEVault} from "src/EVault/IEVault.sol";
import {Base} from "src/EVault/shared/Base.sol";

interface ISimpleVaultBase {
    function stake(uint256, address) external returns (uint256);
    function unstake(uint256, address, address) external returns (uint256);
}

interface ISimpleVault is IEVault, ISimpleVaultBase {}

contract SimpleVault is ISimpleVaultBase, EVault {
    constructor(Integrations memory integrations, DeployedModules memory modules) EVault(integrations, modules) {}

    /// Define aliases for 2 main Vault functions
    //  stake == deposit
    function stake(uint256 amount, address receiver) external returns (uint256) {
        return this.deposit(amount, receiver);
    }

    // unstake == withdraw
    function unstake(uint256 amount, address receiver, address owner) external returns (uint256) {
        return this.withdraw(amount, receiver, owner);
    }
}
