#!/bin/bash
#-discovery.port=30306 --port=30306 

geth init --datadir /home/.ethereum/data /home/.ethereum/genesis.json
geth  --nat=extip:$1  --datadir=/home/.ethereum/data --networkid=3107  -keystore=/home/.ethereum/keystore  --unlock "0x0b913e0F6093819aff423254AaA8cAd82FDa9b02"  --allow-insecure-unlock  --password "/home/.ethereum/account-password"  --http --http.port=8545 --http.corsdomain="*" --http.api=net,admin,eth --bootnodes enode://2adeac6710220735cf6c4737e752644b93a4102ea388e77c3196666326cebc68bfd02472630e300018a22c3e9952d09d915e29c693ca4dcd9231e3407d86b9c4@10.1.1.1:30303 --verbosity=5 > /home/geth.log 2>&1
