# Subnet Calculator 

Program takes an IPv4 address and subnet mask as a input and returns following information:
- IPv4 address
- Subnet mask in dotted decimal format and CIDR notation
- Network address
- Broadcast address
- First IP address in the subnet
- Last IP address in the subnet 
- Usable hosts per subnet
- Wildcard mask 

## Usage 
You need Python version 3.6 or later to run the program. 
You can download Python from official website: [https://www.python.org/getit/](https://www.python.org/getit/)

When the program is run, user is prompted to input IP address and subnet mask:
```
Enter an IP address:
```

Program will accept IPv4 address from class A, B, C except: 
- 127.0.0.0/ 8 - used for loopback addresses
- 169.254.0.0/16 - used for link-local addresses

```
Enter a subnet mask:
```
Subnet mask should be entered in dotted decimal format e.g. 255.255.255.0. Program will accept subnet mask from 255.0.0.0.0 to 255.255.255.255. 
If you use subnet mask 255.255.255.254 (/31) or 255.255.255.255 (/32) program returns None for: network and broadcast address, first and last IP address, usable hosts per subnet. 

## Example
```
Enter an IP address: 1.1.1.1
Enter a subnet mask: 255.255.255.0
--------------------------------------------------
IP address: 1.1.1.1
Subnet mask: 255.255.255.0   /24
Network address: 1.1.1.0
Broadcast address: 1.1.1.255
First IP in the subnet: 1.1.1.1
Last IP in the subnet: 1.1.1.254
Usable hosts per subnet: 254
Wildcard mask: 0.0.0.255
```
## Author
Created by [Mario Lechończak](https://github.com//mlechonczak). Feel free to contact me.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
