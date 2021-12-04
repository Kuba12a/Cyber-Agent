import requests
import Model.Command as Command
import json
import datetime


def send_command(URL, command : Command):

    data = json.dumps(command.__dict__)
    status_code = None
    try:
        response = requests.post(url=URL, data=data)
        status_code = response.status_code
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    # extracting data in json format
    
    return status_code