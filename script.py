
from optparse import OptionParser
from scapy.all import *
conf.L3socket = L3RawSocket

parser = OptionParser()
parser.add_option("-D", dest="dst_addr", help="Destination address")
parser.add_option("-d", dest="dst_port", help="Destination port")
parser.add_option("-S", dest="src_addr", help="Source address")
parser.add_option("-s", dest="src_port", help="Source port")
parser.add_option("-q", dest="seq_nr", help="Sequence number")
parser.add_option("-a", dest="ack_nr", help="Acknowledgment number")

(options, args) = parser.parse_args()
if options.src_port is None or options.src_addr is None or options.dst_addr is None or options.dst_port is None or options.seq_nr is None or options.ack_nr is None:
    parser.print_help()
    exit()

print "%s:%s -> %s:%s # seq=%s ack=%s" % (options.src_addr, options.src_port, options.dst_addr, options.dst_port, options.seq_nr, options.ack_nr)

packet = IP(src=options.src_addr, dst=options.dst_addr)/TCP(sport=int(options.src_port), dport=int(options.dst_port), flags="R", seq = int(options.seq_nr), ack = int(options.ack_nr))

send(packet, verbose=0)

print 'done'
