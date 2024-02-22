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


#geth  --datadir=/home/.ethereum/data --networkid=3107  -keystore=/home/.ethereum/keystore  --unlock "0x0b913e0F6093819aff423254AaA8cAd82FDa9b02"  --allow-insecure-unlock  --password "/home/.ethereum/account-password"  --http --http.port=8545 --http.corsdomain="*" --http.api=net,admin,eth --verbosity=3 > /home/.ethereum/geth.log 2>&1

# Keep alive
tail -f /dev/null
