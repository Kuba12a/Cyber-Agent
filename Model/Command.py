from pydantic import BaseModel
import datetime

#actions

#get_captures_list = "get_captures_list"
#get_captures = "get_captures"
#get_logs_list = "get_logs_list"
#get_logs = "get_logs"
get_configuration = "get_configuration"
capture_traffic = "capture_traffic"
execute_command = "execute_command"

'''
action: how data passed to Agent should be interpreted - type of command
names: names of files to be downloaed from agent - default: ""
time: time for pcap generation - default: 30
parameter: parameters for commands - default: ""
        get_configuration: which configuration
        execute_command: command to be executed
        get_captures: BPF filter
        .
        .
        .
'''
class Command(BaseModel):
        action: str 
        names: str 
        time: int 
        parameters: str 

        def __init__(self, action = "n" , names = "n", time=30, parameters="n"):
            self.__action =action
            self.__names = names
            self.__time = time
            self.__parameters = parameters


        def set_action(self, x):
                self.__action= x
        def set_time(self, x):
                self.__time = x
        def set_parameters(self, x):
                self.__parameters = x
        def set_names(self, x):
                self.__names = x


