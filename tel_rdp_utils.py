
import json
import configparser
import os,time


path    = "bb_setting.ini"


def return_datetime_str():
    return time.strftime('%H:%M:%S')

def removeFix(mString=""):
    goodLetter = '0123456789.'
    result = ''
    for let in mString:
        for blet in goodLetter:
            if let == blet:
                result += let

    return result


def retutr_float(par: str):
    result = 0
    par = removeFix(par)
    try:
        result = float(par)
    except:
        pass
    return result

class setting():
    def __init__(self):
        
        # if not os.path.isdir(folder):
        #     print('создание папки :',folder)
        #     os.mkdir(folder)
        
        self.path = path
        self.setting = {}
        self.readConfig()

    def createConfig(self):
        """
        Create a config file
        """
        config = configparser.ConfigParser()

        config.add_section("server")        
        config.set("server", "hostName"     , "192.168.21.145")
        config.set("server", "serverPort"   , "8888")        


        with open(self.path, "w") as config_file:
            config.write(config_file)

    def readConfig(self):
        if not os.path.exists(self.path):
            self.createConfig()

        config = configparser.ConfigParser()
        config.read(self.path)

        self.hostName = config.get("server", "hostName")
        self.serverPort = config.get("server", "serverPort")


        self.setting = {
            'hostName'  : self.hostName,
            'serverPort': self.serverPort,
        }

    def print_setting(self):
        print(self.setting)

def remove_files(ext:str,exept_file:str):    
    for file in os.listdir(os.getcwd()):
        if file.endswith(ext):
            if file!=exept_file:
                print('del:',file)
                os.remove(file) 

# добавил сохранение файла и текс. данных 05-06-20
def save_file_txt(name_file:str,text_str:str):
    with open(name_file,'w') as f:
        f.write(text_str)