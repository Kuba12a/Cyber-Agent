from scapy.all import *
import os
import time

def process_pcap(interface, timeout, filtr):
    print("Sniffing network traffic")
    t = AsyncSniffer(prn=None, store=True, filter=filtr)
    t.start()
    time.sleep(int(timeout))
    t.stop()
    current_time = time.ctime().replace(":","-")
    current_time=current_time.replace(" ", "_")
    name = "pcap_" + current_time + ".pcapng"
    name = os.path.join("Captures", name)
    wrpcap(name, t.results, append=True)
    print("Sniffing network traffic finished")
    #return t.results
    
    

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
 

def get_configuration():
    message = subprocess.check_output(['ifconfig','-a'])
    message += (subprocess.check_output(['cat','/etc/network/interfaces']))
    message += (subprocess.check_output(['cat','/etc/hosts']))
    return str(message).replace("\\n", '\n')