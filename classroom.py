import ipaddress
import time
#Classroom 1 - 14 computers
#Classroom 2 - 14 computers
#Small Classroom 3 - 6 computers
#Small Classroom 4 - 6 computers
#Small Classroom 5 - 6 computers
#Office 1 - 2 computers
#Office 2 - 2 computers

#Classroom 1 - 30
#Classroom 2 - 30
#Classroom 3 - 14
#Classroom 4 - 14
#Classroom 5 - 14
#Lab 1 - 6
#Lab 2 - 6

ipInterface = ipaddress.ip_interface('138.191.0.0\25')
ipnetwork = ipInterface.network

classroom = (list(ipaddress.ip_network(ipnetwork).subnets(prefixlen_diff=2)))

smcl_1 = (list(ipaddress.ip_network(classroom[2]).subnets()))
smcl_2 = (list(ipaddress.ip_network(classroom[3]).subnets()))

office = (list(ipaddress.ip_network(smcl_2[1]).subnets()))


print('IP addresses and network information for assignment')
print('Office 1:')
print('Network address: {}'.format((office[0]).network_address))
print('Broadcast address: {}'.format((office[0]).broadcast_address))
print('Number of hosts: {}'.format(len(list((office[0]).hosts()))))
print('Valid host range: {0} - {1}'.format((((office[0]).network_address)+1), (((office[0]).broadcast_address)-1)))
print('')
print('Office 2:')
print('Network address: {}'.format((office[1]).network_address))
print('Broadcast address: {}'.format((office[1]).broadcast_address))
print('Number of hosts: {}'.format(len(list((office[1]).hosts()))))
print('Valid host range: {0} - {1}'.format((((office[1]).network_address)+1), (((office[1]).broadcast_address)-1)))
print('')
print('Small Classroom 3')
print('Network address: {}'.format((smlcl_1[0]).network_address))
print('Broadcast address: {}'.format((smlcl_1[0]).broadcast_address))
print('Number of hosts: {}'.format(len(list((smlcl_1[0]).hosts()))))
print('Valid host range: {0} - {1}'.format((((smlcl_1[0]).network_address)+1), (((smlcl_1[0]).broadcast_address)-1)))
print('')
print('Small Classroom 4')
print('Network address: {}'.format((smlcl_1[1]).network_address))
print('Broadcast address: {}'.format((smlcl_1[1]).broadcast_address))
print('Number of hosts: {}'.format(len(list((smlcl_1[1]).hosts()))))
print('Valid host range: {0} - {1}'.format((((smlcl_1[1]).network_address)+1), (((smlcl_1[1]).broadcast_address)-1)))
print('')
print('Small Classroom 5')
print('Network address: {}'.format((smlcl_2[0]).network_address))
print('Broadcast address: {}'.format((smlcl_2[0]).broadcast_address))
print('Number of hosts: {}'.format(len(list((smlcl_2[0]).hosts()))))
print('Valid host range: {0} - {1}'.format((((smlcl_2[0]).network_address)+1), (((smlcl_2[0]).broadcast_address)-1)))
print('')
