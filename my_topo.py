#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import OVSController, OVSSwitch, RemoteController

class SwitchTopo(Topo):
	def build(self, n, m):
		host_list = {}
		switch_list = {}
		
		TopSwitch = self.addSwitch('s0', dailMode = 'secure')

		for s in range(m):
			switch_list[s] = self.addSwitch('s%s' % (s+1), failMode = 'secure')
			#switch_list[s] = self.addSwitch('s%s' % (s), failMode = 'standalone')
			
			for h in range(n):
				host_list[h] = self.addHost('h%s' % (h+s*n))
				self.addLink(host_list[h], switch_list[s])
		
		for s in range(m):
			self.addLink(switch_list[s], TopSwitch)


def my_test():
	topo = SwitchTopo(n=2, m=5)
	net = Mininet(topo=topo, controller=None)
	
	info( '*** Add Controller\n' )
	net.addController(name='c0', controller = RemoteController)
	
	net.start()

	#info("*** Try Connections\n")
	#dumpNodeConnections(net.hosts)

	#info("*** Test ping all\n")
	#net.pingAll()
	CLI(net)
	net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    my_test()
