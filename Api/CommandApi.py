from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import sys 
sys.path.append(".")
import Model.Command as command_model
import Model.Name as name_class
import AgentManagers.AgentCapturesManager as agent_captures_manager
import AgentManagers.AgentLogsManager as agent_logs_manager
import AgentManagers.AgentExecuteCommandManager as agent_execution_command_manager
import HttpClient.HttpClient as http_client
import os
import threading
from fastapi.responses import FileResponse

app = FastAPI()

#Tutaj packet capture, get configuration i execute command
@app.post("/command")
def login(command: command_model.Command):
    if(command.action== command_model.get_configuration):
        result = agent_captures_manager.get_configuration()
        return {"msg" : result}
    elif(command.action== command_model.capture_traffic):
        pcap_thread = threading.Thread(target=agent_captures_manager.process_pcap("eth0",command.time, command.parameters), args=(1,))
        pcap_thread.start()
        return {"msg" : "Packet capture started on agent"}
    elif(command.action == command_model.execute_command):
        result = agent_execution_command_manager.execute_command(command.parameters)
        return {"msg" : result}
    
    return {"msg": "Nothing done"}


@app.post("/file")
def get_file(name : name_class.Name):
    #if filename.endswith(".pcapng"):
    file_path = os.path.join("Captures", name.name)
    #http_client.send_file(name.name)
    return FileResponse(file_path, media_type='application/octet-stream', filename= name.name)


@app.get("/filenames/evtx")
def login():
    logs_list = agent_logs_manager.get_logs_list()
    return logs_list

@app.get("/filenames/pcapng")
def login():
    captures_list = agent_captures_manager.get_captures_list()
    return captures_list
