import requests
import Model.Command as Command



def send_file(URL, command : Command):
    with open('report.xls', 'rb') as f:
        r = requests.post('http://httpbin.org/post', files={'report.xls': f})
    try:
        response = requests.post('http://httpbin.org/post', files={'report.xls': f})
        status_code = response.status_code
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    return response.status_code