#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections


class CustomTree(Topo):
    "Create the switches and hosts, then build the tree"

    def build(self):
        # Create the switches
        s9 = self.addSwitch('s9', datapath = None, protocols = None)
        s10 = self.addSwitch('s10', datapath = None, protocols = None)
        s11 = self.addSwitch('s11', datapath = None, protocols = None)
        s12 = self.addSwitch('s12', datapath = None, protocols = None)
        s13 = self.addSwitch('s13', datapath = None, protocols = None)
        s14 = self.addSwitch('s14', datapath = None, protocols = None)
        s15 = self.addSwitch('s15', datapath = None, protocols = None)

        # Create the hosts
        h1 = self.addHost('h1', cls = None, ip = '10.0.0.1', defaultRoute = None)
        h2 = self.addHost('h2', cls = None, ip = '10.0.0.2', defaultRoute = None)
        h3 = self.addHost('h3', cls = None, ip = '10.0.0.3', defaultRoute = None)
        h4 = self.addHost('h4', cls = None, ip = '10.0.0.4', defaultRoute = None)
        h5 = self.addHost('h5', cls = None, ip = '10.0.0.5', defaultRoute = None)
        h6 = self.addHost('h6', cls = None, ip = '10.0.0.6', defaultRoute = None)
        h7 = self.addHost('h7', cls = None, ip = '10.0.0.7', defaultRoute = None)
        h8 = self.addHost('h8', cls = None, ip = '10.0.0.8', defaultRoute = None)
        
        self.addLink(h1, s11)
        self.addLink(h2, s11)
        self.addLink(h3, s12)
        self.addLink(h4, s12)
        self.addLink(h5, s14)
        self.addLink(h6, s14)
        self.addLink(h7, s15)
        self.addLink(h8, s15)
        self.addLink(s11, s10)
        self.addLink(s12, s10)
        self.addLink(s14, s13)
        self.addLink(s15, s13)
        self.addLink(s10, s9)
        self.addLink(s13, s9)


def Test():
    
    # Initialize Mininet
    net = Mininet(topo = CustomTree(), build = False, ipBase = '10.0.0.0/8')

    # Add a Controller
    info( '*** Adding controller\n' )
    c0 = net.addController('c0', controller = None, ip = '127.0.0.1', protocol = 'tcp', port = 6633)

    # Start controller and switches
    info( '*** Starting network\n')
    net.start()

    # Dump all host connections
    info( '*** Dumping host connections\n')
    dumpNodeConnections(net.hosts)

    # Ping all hosts (UDP)
    info( '*** Testing network connectivity\n')
    net.pingAll()

    # Use iperf to check bandwidth between two nodes (TCP)
    info( '*** Testing bandwidth between h1 and h8\n')
    h1, h8 = net.get('h1', 'h8')
    net.iperf((h1, h8))

    # Stop the network
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Test()

