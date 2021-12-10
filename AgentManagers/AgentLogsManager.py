import os




#Get list of filenames from directory
def get_logs_list():
    return os.listdir("Logs")
        
 

#Get file content as binary
def get_log(filename):
    path = os.path.join("Logs",filename)
    file = open(path,'rb')
    content = file.read()
    file.close()
    return content