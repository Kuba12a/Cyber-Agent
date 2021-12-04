import os



def capture_traffic():
    print("Pobieram kaptury tak jak kazesz ziomek")


#Get list of filenames from directory
def get_captures_list():
    return os.listdir("Captures")
        
 

#Get file content as binary
def get_capture(filename):
    path = os.path.join("Captures",filename)
    file = open(path,'rb')
    content = file.read()
    file.close()
    return content
