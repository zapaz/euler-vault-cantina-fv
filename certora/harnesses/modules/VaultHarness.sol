// SPDX-License-Identifier: GPL-2.0-or-later

pragma solidity ^0.8.0;
// import {IERC20} from "../../lib/ethereum-vault-connector/lib/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol";

import "../../../certora/harnesses/AbstractBaseHarness.sol";
import "../../../src/EVault/modules/Vault.sol";
import "../../../src/EVault/modules/Token.sol";

contract VaultHarness is VaultModule, TokenModule, AbstractBaseHarness {
    constructor(Integrations memory integrations) Base(integrations) {}

    function controllerEnabled(address account) public view returns (bool) {
        return hasAnyControllerEnabled(account);
    }

    function userAssets(address user) public view returns (uint256) {
        return IERC20(asset()).balanceOf(user);
    }

    function userShares(address user) public view returns (uint256) {
        return vaultStorage.users[user].getBalance().toUint();
    }

    function cash() public view returns (uint256) {
        return vaultStorage.cash.toUint();
    }

    function updateVault() internal override returns (VaultCache memory vaultCache) {
        // initVaultCache is difficult to summarize because we can't
        // reason about the pass-by-value VaultCache at the start and
        // end of the call as separate values. So this harness
        // gives us a way to keep the loadVault summary when updateVault
        // is called
        vaultCache = loadVault();
        if (block.timestamp - vaultCache.lastInterestAccumulatorUpdate > 0) {
            vaultStorage.lastInterestAccumulatorUpdate = vaultCache.lastInterestAccumulatorUpdate;
            vaultStorage.accumulatedFees = vaultCache.accumulatedFees;

            vaultStorage.totalShares = vaultCache.totalShares;
            vaultStorage.totalBorrows = vaultCache.totalBorrows;

            vaultStorage.interestAccumulator = vaultCache.interestAccumulator;
        }
        return vaultCache;
    }

    // VaultStorage Accessors:
    function storage_lastInterestAccumulatorUpdate() public view returns (uint48) {
        return vaultStorage.lastInterestAccumulatorUpdate;
    }

    function storage_cash() public view returns (Assets) {
        return vaultStorage.cash;
    }

    function storage_supplyCap() public view returns (uint256) {
        return vaultStorage.supplyCap.resolve();
    }

    function storage_borrowCap() public view returns (uint256) {
        return vaultStorage.borrowCap.resolve();
    }

    function storage_hookTarget() external view returns (address) {
        return vaultStorage.hookTarget;
    }

    function storage_reentrancyLocked() external view returns (bool) {
        return vaultStorage.reentrancyLocked;
    }

    // reentrancyLocked seems not direclty used in loadVault
    function storage_hookedOps() public view returns (Flags) {
        return vaultStorage.hookedOps;
    }

    function storage_snapshotInitialized() public view returns (bool) {
        return vaultStorage.snapshotInitialized;
    }

    function storage_totalShares() public view returns (Shares) {
        return vaultStorage.totalShares;
    }

    function storage_totalBorrows() public view returns (Owed) {
        return vaultStorage.totalBorrows;
    }

    function storage_accumulatedFees() public view returns (Shares) {
        return vaultStorage.accumulatedFees;
    }

    function storage_interestAccumulator() public view returns (uint256) {
        return vaultStorage.interestAccumulator;
    }

    function storage_configFlags() public view returns (Flags) {
        return vaultStorage.configFlags;
    }

    function cache_cash() public view returns (Assets) {
        return loadVault().cash;
    }
}
