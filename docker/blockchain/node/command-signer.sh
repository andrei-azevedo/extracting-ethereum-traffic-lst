#!/bin/bash
#--discovery.port=30305 --port=30305 

geth init --datadir /home/.ethereum/data /home/.ethereum/genesis.json
geth --nat=extip:$1 --datadir=/home/.ethereum/data --networkid=3107 --mine  --miner.etherbase=0x6b4F3286fe87612e7Deb71A2FBedA0e948Ad4980 --keystore=/home/.ethereum/keystore  --unlock "0x6b4F3286fe87612e7Deb71A2FBedA0e948Ad4980"  --allow-insecure-unlock  --password "/home/.ethereum/account-password"  --http --http.port=8545 --http.corsdomain="*" --http.api=miner,net,admin,eth --verbosity=5 > /home/geth.log 2>&1