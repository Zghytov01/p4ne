from pysnmp.hlapi import *

ios = ObjectIdentity('SNMPv2-MIB', "sysDescr", 0 )
interfaces = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")
result_ios = getCmd(SnmpEngine(),
	            CommunityData('public', mpModel=0),
	            UdpTransportTarget(("10.31.70.209" , 161)),
	            ContextData(),
	 	ObjectType(ios ))

for r in result_ios:
	for a in r [3]:
		print(a)

result_interface = nextCmd(SnmpEngine (),
	            CommunityData('public', mpModel=0),
	            UdpTransportTarget(("10.31.70.209" , 161)),
	            ContextData(),
	 	ObjectType(interfaces),lexicographicMode=False)
for i in result_interface:
	for b in i [3]:
		print(b)
