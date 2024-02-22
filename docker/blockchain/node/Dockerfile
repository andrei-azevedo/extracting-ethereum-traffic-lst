
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


#FROM ethereum/client-go
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
&&  RUNLEVEL=1 apt-get install -y cron samba openssh-server sudo net-tools iproute2 iputils-ping iptables nano apt-utils

RUN apt-get update \ 
&& RUNLEVEL=1 apt-get install -y software-properties-common \
&& add-apt-repository -y ppa:ethereum/ethereum \
&& apt-get update \
&& apt-get install -y ethereum

RUN apt-get install -y tcpdump


RUN mkdir /home/.ethereum
# copy genesis.json
COPY genesis.json /home/.ethereum/

# copy premade keys
COPY keystore/ /home/.ethereum/keystore

# copy password for keys
COPY account-password /home/.ethereum/

# Init BC
#RUN geth init --datadir /home/.ethereum/data /home/.ethereum/genesis.json

COPY command-signer.sh /home
COPY command-node.sh /home

COPY onboot.sh /home
RUN chmod +x /home/onboot.sh
CMD ["./home/onboot.sh"] 

# For conecting via Open SSL
EXPOSE 22

# Ethereum ports
EXPOSE 30303
EXPOSE 8545
