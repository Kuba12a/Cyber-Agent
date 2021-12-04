import subprocess

def execute_command(command):    
    message = subprocess.check_output(command.split(" "))
    return str(message).lstrip("b'").rstrip("'").replace("\\n", '\n')

def get_configuration():
    message = subprocess.check_output(['ifconfig','-a'])
    message += (subprocess.check_output(['cat','/etc/network/interfaces']))
    message += (subprocess.check_output(['cat','/etc/hosts']))
    return str(message).replace("\\n", '\n')
#test 
print(execute_command("echo siema"))