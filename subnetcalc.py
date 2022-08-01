from sys import exit

def ip_valid(ip):
	'''This functions tests if IPv4 address is valid. If yes, it returns IPv4 address.
	Function will accept IP address from classes A, B and C except:
		- 127.0.0.0/8 - uses for loopback addresses (RFC 5735 - https://datatracker.ietf.org/doc/html/rfc5735)
		- 169.254.0.0/16 - used for link-local addresses (RFC 5735 - https://datatracker.ietf.org/doc/html/rfc5735)'''
	ip_octets = ip.split(".")
	
	if len(ip_octets) == 4 and 1 <= int(ip_octets[0]) <= 223 and int(ip_octets[0]) != 127 and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) \
	and 0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255:
		return ip

def subnet_mask_valid(subnet_mask):
	'''This function tests if subnet mask is valid. If yes, it returns subnet mask.
	Valid subnet masks are in range /8 - /32.'''
	subnet_octets = subnet_mask.split(".")
	valid_masks = (255, 254, 252, 248, 240, 224, 192, 128, 0)

	if len(subnet_octets) == 4 and int(subnet_octets[0]) == 255 and int(subnet_octets[1]) in valid_masks and int(subnet_octets[2]) in valid_masks  \
	and int(subnet_octets[3]) in valid_masks and int(subnet_octets[0]) >= int(subnet_octets[1]) >= int(subnet_octets[2]) \
	and int(subnet_octets[2]) >= int(subnet_octets[3]):
		if int(subnet_octets[0]) != 255 and int(subnet_octets[1]) ==0 and int(subnet_octets[2]) == 0 and int(subnet_octets[3]) == 0:
			return subnet_mask
		elif int(subnet_octets[0]) == 255:
			if int(subnet_octets[1]) != 255 and int(subnet_octets[2]) == 0 and int(subnet_octets[3]) == 0:
				return subnet_mask
			elif int(subnet_octets[1]) == 255:
				if int(subnet_octets[2]) != 255 and int(subnet_octets[3]) == 0:
					return subnet_mask
				elif int(subnet_octets[2]) == 255:
					return subnet_mask 

def ip_binary(ip):
	'''This function returns IP address in binary format.'''

	ip_octets = ip.split(".")
	ip_addr_binary = [(8 - len(bin(int(octet)).lstrip("0b"))) * "0" + bin(int(octet)).lstrip("0b") for octet in ip_octets]
	ip_addr_binary = "".join(ip_addr_binary)
	return ip_addr_binary 

def subnet_mask_binary(subnet_mask):
	'''This function returns subnet mask in binary format'''
	subnet_octets = subnet_mask.split(".")
	subnet_binary = [(8 - len(bin(int(octet)).lstrip("0b"))) * "0" + bin(int(octet)).lstrip("0b") for octet in subnet_octets]
	subnet_binary = "".join(subnet_binary)
	return subnet_binary

def network_address(ip, subnet_mask):
	'''This function returns network address for given IP address if subnet mask is not /31 or /32'''

	count_ones = subnet_mask_binary(subnet_mask).count("1")
	count_zeros = 32 - count_ones
	
	if count_zeros > 2: 
		network_addr_bin = ip_binary(ip)[:count_ones] + count_zeros * "0"
		network_addr_bin = [network_addr_bin[i:i+8] for i in range(0, 32, 8)]
		network_addr = [str(int(octet, 2)) for octet in network_addr_bin]
		network_addr = ".".join(network_addr)
		return network_addr 

def broadcast_address(ip, subnet_mask):
	'''This function returns broadcast address for given IP address if subnet mask is not /31 or /32.'''
	count_ones = subnet_mask_binary(subnet_mask).count("1")
	count_zeros = 32 - count_ones

	if count_zeros > 2: 
		broadcast_addr_bin = ip_binary(ip)[:count_ones] + count_zeros * "1"
		broadcast_addr_bin = [broadcast_addr_bin[i:i+8] for i in range(0, 32, 8)]
		broadcast_addr = [str(int(octet, 2)) for octet in broadcast_addr_bin]
		broadcast_addr = ".".join(broadcast_addr)
		return broadcast_addr 

def first_ip_address(ip, subnet_mask):
	'''This function returns first IP address in the subnet if subnet mask is not /31 or /32.'''
	count_ones = subnet_mask_binary(subnet_mask).count("1")
	count_zeros = 32 - count_ones

	if count_zeros > 2:
		first_addr_bin = ip_binary(ip)[:count_ones] + (count_zeros - 1) * "0" + "1"
		first_addr_bin = [first_addr_bin[i:i+8] for i in range(0, 32, 8)]
		first_addr = [str(int(octet, 2)) for octet in first_addr_bin]
		first_addr = ".".join(first_addr)
		return first_addr 

def last_ip_address(ip, subnet_mask):
	'''This function returns last IP address in the subnet if subnet mask is not /31 or /32.'''
	count_ones = subnet_mask_binary(subnet_mask).count("1")
	count_zeros = 32 - count_ones

	if count_zeros > 2:
		last_addr_bin = ip_binary(ip)[:count_ones] + (count_zeros - 1) * "1" + "0"
		last_addr_bin = [last_addr_bin[i:i+8] for i in range(0, 32, 8)]
		last_addr = [str(int(octet, 2)) for octet in last_addr_bin]
		last_addr = ".".join(last_addr)
		return last_addr

def wildcard_mask(subnet_mask):
	'''This function returns wildcard mask for a given subnet mask.'''
	subnet_octets = subnet_mask.split(".")
	wildcard_mask = [str(255 - int(octet)) for octet in subnet_octets]
	wildcard_mask = ".".join(wildcard_mask)
	return wildcard_mask

def cidr_notation(subnet_mask):
	'''This function returns subnet mask in CIDR notation.'''
	count_ones = subnet_mask_binary(subnet_mask).count("1")
	count_zeros = 32 - count_ones

	cidr = "/" + str(count_ones)
	return cidr

def usable_hosts_per_subnet(subnet_mask):
	'''This function returns number of usable hosts per subnet if if subnet mask is not /31 or /32.'''
	count_ones = subnet_mask_binary(subnet_mask).count("1")
	count_zeros = 32 - count_ones

	if count_zeros > 2:
		hosts_per_subnet = (2 ** count_zeros - 2)
		return hosts_per_subnet

def main():

	while True:
		try:
			ip_input = input("Enter an IP address: ")
			if ip_valid(ip_input):
				ip = ip_input
				break
			else:
				print("IP address is invalid.")
		except ValueError:
			print("IP address is invalid.")
		except KeyboardInterrupt:
			print("\nGoodbye.")
			exit()

	while True:
		try:
			subnet_input = input("Enter a subnet mask: ")
			if subnet_mask_valid(subnet_input):
				subnet_mask = subnet_input
				break
			else:
				print("Subnet mask is invalid.")
		except ValueError:
			print("Subnet mask is invalid.")
		except KeyboardInterrupt:
			print("\nGoodbye.")	
			exit()

	print("-" * 50)
	

	#print(f"IP address: {ip}") - not needed
	#print(f"Subnet mask: {subnet_mask}") - not needed
	print(f"CIDR notation:       {cidr_notation(subnet_mask) + ' (' + subnet_mask + ')'}")
	print(f"First usable IP:     {first_ip_address(ip, subnet_mask)}")
	print(f"Last usable IP:      {last_ip_address(ip, subnet_mask)}")
	print(f"Broadcast:           {broadcast_address(ip, subnet_mask)}")
	print(f"Usable hosts:        {usable_hosts_per_subnet(subnet_mask)}")
	print(f"Network:             {network_address(ip, subnet_mask)}")
	print(f"Wildcard mask:       {wildcard_mask(subnet_mask)}")

if __name__ == "__main__":
	main()

