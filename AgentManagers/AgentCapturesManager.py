from scapy.all import *

def process_pcap(interface, timeout, filtr):
    t = AsyncSniffer(iface=interface, prn=None, store=True, filter=filtr)
    t.start()
    time.sleep(int(timeout))
    t.stop()
    return t.results
    
#test (dziala na sudo)
process_pcap("eth0", 10, "tcp").nsummary()