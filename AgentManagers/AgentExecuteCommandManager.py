import subprocess

def execute_command(command):    
    message = subprocess.check_output(command.split(" "))
    return str(message).lstrip("b'").rstrip("'").replace("\\n", '\n')

