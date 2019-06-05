#importing the necessary libraries
#!/usr/bin/python
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.link import TCLink

#defining the network
def myNetwork():
    #Creating the network
    net = Mininet(topo=None,link=TCLink,build=False,ipBase='10.0.0.0/8',autoStaticArp=True)
    #Adding controller
    info('*** Adding controller\n')
    c0=net.addController('c0',controller=OVSController,port=6633)
    #adding switches
    info('*** Add switches=s\n')
    s1=net.addSwitch('s1',stp='true')
    s2=net.addSwitch('s2',stp='true')
    s3=net.addSwitch('s3',stp='true')
    s4=net.addSwitch('s4',stp='true')
    s5=net.addSwitch('s5',stp='true')
    s6=net.addSwitch('s6',stp='true')
    s7=net.addSwitch('s7',stp='true')
    s8=net.addSwitch('s8',stp='true')
    s9=net.addSwitch('s9',stp='true')
    s10=net.addSwitch('s10',stp='true')
    s11=net.addSwitch('s11',stp='true')

    #adding hosts
    info('** Add hosts\n')
    h1=net.addHost('h1',ip='10.0.0.1')  #this is the server
    h2=net.addHost('h2',ip='10.0.0.254') #this is server client with the given ip address
    
    #Adding links
    info('*** Add links\n')
    net.addLink(h1,s1,cls=TCLink)
    net.addLink(h2,s11,cls=TCLink)
  
#---------------------------------------------------
    net.addLink(s1,s5,bw=10,cls=TCLink)
    net.addLink(s2,s5,bw=15,cls=TCLink)
    net.addLink(s2,s6,bw=20,cls=TCLink)
    net.addLink(s3,s6,bw=15,cls=TCLink)
    net.addLink(s3,s7,bw=10,cls=TCLink)
    net.addLink(s4,s7,bw=15,cls=TCLink)
    net.addLink(s5,s6,bw=20,cls=TCLink)
    net.addLink(s6,s7,bw=20,cls=TCLink)
    net.addLink(s5,s8,bw=15,cls=TCLink)
    net.addLink(s5,s9,bw=15,cls=TCLink)
    net.addLink(s6,s9,bw=15,cls=TCLink)
    net.addLink(s6,s10,bw=10,cls=TCLink)
    net.addLink(s7,s10,bw=15,cls=TCLink)
    net.addLink(s7,s11,bw=10,cls=TCLink)
   

#---------------------------------------------------
    #Starting network
    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()
    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s11').start([c0])
    
    s1.cmd('ovs-vsctl set bridge s1 stp_enable=true')
    s2.cmd('ovs-vsctl set bridge s2 stp_enable=true')
    s3.cmd('ovs-vsctl set bridge s3 stp_enable=true')
    s4.cmd('ovs-vsctl set bridge s4 stp_enable=true')
    s5.cmd('ovs-vsctl set bridge s5 stp_enable=true')
    s6.cmd('ovs-vsctl set bridge s6 stp_enable=true')
    s7.cmd('ovs-vsctl set bridge s7 stp_enable=true')
    s8.cmd('ovs-vsctl set bridge s8 stp_enable=true')
    s9.cmd('ovs-vsctl set bridge s9 stp_enable=true')
    s10.cmd('ovs-vsctl set bridge s10 stp_enable=true')
    s11.cmd('ovs-vsctl set bridge s11 stp_enable=true')
   
   
    
    info( '*** post configure switches and hosts\n')
    CLI(net)
    net.stop()

if __name__=='__main__':
    setLogLevel('info')
    topo=myNetwork()

    

