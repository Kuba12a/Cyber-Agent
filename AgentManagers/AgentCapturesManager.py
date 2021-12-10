from scapy.all import *
import os

def process_pcap(interface, timeout, filtr):
    print("Pobieram kaptury tak jak kazesz ziomek")
    t = AsyncSniffer(iface=interface, prn=None, store=True, filter=filtr)
    t.start()
    time.sleep(int(timeout))
    t.stop()
    return t.results
    
    

#Get file content as binary
def get_capture(filename):
    path = os.path.join("Captures",filename)
    file = open(path,'rb')
    content = file.read()
    file.close()
    return content   
    

#Get list of filenames from directory
def get_captures_list():
    return os.listdir("Captures")
 
#test (dziala na sudo)
#process_pcap("eth0", 10, "tcp").nsummary()