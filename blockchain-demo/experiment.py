import subprocess
import time
import random
from host import Host
from switch import Switch
from controller import Controller


def sendTransaction(_node, _from, _to, _value, _gas):
    try:
        sendTransactionCommand = '''geth attach --exec 'eth.sendTransaction({from: "'''+_from+'''",to: "'''+_to+'''", value: '''+str(_value)+''', gas: '''+str(_gas)+'''})' /home/.ethereum/data/geth.ipc'''
        print(sendTransactionCommand)
        subprocess.run('''docker exec '''+ _node + ''' ''' + sendTransactionCommand, shell=True)
        return True
    except Exception as e:
        print(e)
        return False


print("create signer and nodes")

h1 = Host('signer')
h2 = Host('node1')
h3 = Host('node2')
h4 = Host('node3')
h5 = Host('node4')

print("create swtich and controller")

s1 = Switch('s1')
c1 = Controller('c1')

print("instatiate the images, all blockchain nodes are the same, only the command to start the bc changes")

h1.instantiate(dockerImage='eth-node')
h2.instantiate(dockerImage="eth-node")
h3.instantiate(dockerImage="eth-node")
h4.instantiate(dockerImage="eth-node")
h5.instantiate(dockerImage="eth-node")
s1.instantiate()
c1.instantiate(dockerImage="eth-controller")

print("connects hosts to Switch S1")
time.sleep(10)

h1.connect(s1)
h2.connect(s1)
h3.connect(s1)
h4.connect(s1)
h5.connect(s1)
s1.connect(c1)

print("Set their IPs")

h1.setIp('10.1.1.1',24,s1)
h2.setIp('10.1.1.2',24,s1)
h3.setIp('10.1.1.3',24,s1)
h4.setIp('10.1.1.7',24,s1)
h5.setIp('10.1.1.8',24,s1)

s1.setIp('10.1.1.4', 24)
c1.setIp('10.1.1.5', 24, s1)

print("create the SDN controller")

c1.initController('10.1.1.5', 9001)
s1.setController('10.1.1.5', 9001)

print("estabilish network conecction")

s1.connectToInternet('10.1.1.6', 24)

print("set default gateways")

h1.setDefaultGateway('10.1.1.6', s1)
h2.setDefaultGateway('10.1.1.6', s1)
h3.setDefaultGateway('10.1.1.6', s1)
h4.setDefaultGateway('10.1.1.6', s1)
h5.setDefaultGateway('10.1.1.6', s1)

c1.setDefaultGateway('10.1.1.6', s1)

#s1.enableNetflow('10.0.0.6', 9001)

print("init signer")

try:
    signerCommand = "nohup sh /home/command-signer.sh 10.1.1.1 &"
    #signerCommand = "nohup sh /home/command-signer.sh &"
    #> /home/.ethereum/geth.log"
    #subprocess.run(f'docker exec signer nohup tcpdump -s 65535 -w signer.pcap &', shell=True)
    subprocess.run(f'docker exec signer '+signerCommand, shell=True)
    #h1.run(signerCommand)
except Exception as e:
    print(e) 

print("waiting for signer to start...")
time.sleep(10)

#input("press enter to init nodes")
print("init nodes")

nodeCommand = "nohup sh /home/command-node.sh 10.1.1.2 &"
#subprocess.run(f'docker exec node1 nohup tcpdump -s 65535 -w node1.pcap &', shell=True)
subprocess.run(f'docker exec node1 '+nodeCommand, shell=True)

nodeCommand = "nohup sh /home/command-node.sh 10.1.1.3 &"
#subprocess.run(f'docker exec node2 nohup tcpdump -s 65535 -w node2.pcap &', shell=True)
subprocess.run(f'docker exec node2 '+nodeCommand, shell=True)

nodeCommand = "nohup sh /home/command-node.sh 10.1.1.7 &"
#subprocess.run(f'docker exec node2 nohup tcpdump -s 65535 -w node2.pcap &', shell=True)
subprocess.run(f'docker exec node3 '+nodeCommand, shell=True)

nodeCommand = "nohup sh /home/command-node.sh 10.1.1.8 &"
#subprocess.run(f'docker exec node2 nohup tcpdump -s 65535 -w node2.pcap &', shell=True)
subprocess.run(f'docker exec node4 '+nodeCommand, shell=True)

peers = subprocess.run('docker exec node1 geth attach --exec "eth.getBalance(eth.accounts[0])" /home/.ethereum/data/geth.ipc', shell=True)
while (peers == "[]"):
    peers = subprocess.run('docker exec node1 geth attach --exec "eth.getBalance(eth.accounts[0])" /home/.ethereum/data/geth.ipc', shell=True)
    print (peers)
    time.sleep(1)

time.sleep(10)

for i in range(0,1):
    sendTransaction('node1','0x0b913e0F6093819aff423254AaA8cAd82FDa9b02',
                    '0x84564ba949a198f5e0f09bfe7233760f29d3a1d0',
                    50000000000000,21000)

print("waiting for block creation...\n")
time.sleep(10)


print("checking balance\n")
subprocess.run('docker exec node1 geth attach --exec "eth.getBalance(eth.accounts[0])" \
                /home/.ethereum/data/geth.ipc', shell=True)

#try:
#    while True:
#        subprocess.run('docker exec node1 geth attach --exec "eth.getBalance(eth.accounts[0])" /home/.ethereum/data/geth.ipc', shell=True)
#        time.sleep(1)
#except KeyboardInterrupt:
#    pass
#addPeerCommand = 'geth attach /home/.ethereum/data/geth.ipc -- exec admin.addPeer("enode://2adeac6710220735cf6c4737e752644b93a4102ea388e77c3196666326cebc68bfd02472630e300018a22c3e9952d09d915e29c693ca4dcd9231e3407d86b9c4@10.1.1.1:30303")'
#subprocess.run(f'docker exec node1 '+addPeerCommand, shell=True)

#h2.run(nodeCommand)
#h3.run(nodeCommand)


input("Press enter to end experiment...\n")

s1.clearNetflow()

h1.delete()
h2.delete()
h3.delete()

s1.delete()
c1.delete()