import os
import configparser

def get_ip():
    path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    path=os.path.join(path,"config.txt")
    config = configparser.ConfigParser()    
    config.read(path)
    ipS=config.get('server','ip')
    return ipS