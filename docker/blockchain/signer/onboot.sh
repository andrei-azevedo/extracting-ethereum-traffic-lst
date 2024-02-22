#!/bin/bash

#
# Copyright (C) 2022 Alexandre Mitsuru Kaihara
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#



# Start services
service smbd start
service ssh start
service cron start

# Start blockchain mining
geth  --datadir=/home/.ethereum/data --networkid=3107 --mine  --miner.etherbase=0x6b4F3286fe87612e7Deb71A2FBedA0e948Ad4980 --keystore=/home/.ethereum/keystore  --unlock "0x6b4F3286fe87612e7Deb71A2FBedA0e948Ad4980"  --allow-insecure-unlock  --password "/home/.ethereum/account-password"  --http --http.port=8545 --http.corsdomain="*" --http.api=miner,net,admin,eth --verbosity=3 > /home/.ethereum/geth.log 2>&1

# Keep alive
tail -f /home/.ethereum/geth.log
