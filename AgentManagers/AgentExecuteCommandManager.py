import subprocess

def execute_command(command):    
    message = subprocess.run(command.split(" "))
    print(message)

def get_configuration():
    print()
#test 
execute_command('echo siema')