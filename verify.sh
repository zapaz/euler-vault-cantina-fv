#! /bin/sh

CONFS_DIR=certora/confs
MUTATIONS_DIR=certora/mutations
CONTRACTS_DIR=src

function verify_contract() {
    confName=$(basename $conf)
    echo Verify conf $confName

    certoraRun $conf --msg "'Verify $confName'"
}

# loop on every conf in certora confs dir
for conf in $CONFS_DIR/*_verified.conf; do
    verify_contract
done

function verify_public_mutations() {
    mv $CONTRACTS_DIR/$solName.sol  /tmp/$solName.sol

    for file in $MUTATIONS_DIR/$solName/*.sol; do
      cp "$file" "$CONTRACTS_DIR/$solName.sol"

      echo "Catch $solName mutation"

      certoraRun $CONFS_DIR/"$solName"_contest_verified.conf --msg "'Catch $solName mutation'"
    done

    mv /tmp/$solName.sol $CONTRACTS_DIR/$solName.sol
}

