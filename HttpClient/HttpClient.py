import requests
from pprint import pprint
import os




#TODO adres managera w jakimś configu
manager_address = "http://127.0.0.1:8001/uploadFile"




def send_file(filename):   
    ext = filename.split(".")[1]
    try:
        if(ext=="pcapng"):
            path = os.path.join("Captures", filename)
            with open(path,'rb') as filedata:
                r = requests.post(manager_address,  files={'file': filedata})
            status_code = r.status_code
            pprint(r.content)
        elif(ext == "evtx"):
            path = os.path.join("Logs", filename)
            with open(path,'rb') as filedata:
                r = requests.post(manager_address,  files={'file': filedata})
            status_code = r.status_code
            pprint(r.content)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    return r.status_code
