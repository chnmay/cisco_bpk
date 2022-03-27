from netmiko import ConnectHandler
import getpass
import sys
import os
import time
import ctypes  # An included library with Python install.


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year


##initialising device
device = {
    'device_type': 'cisco_ios',
    'ip': '10.255.20.3',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }
##opening IP file
#ipfile=open("E:\Desktop\Script for backup cisco\iplist.txt")
user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
print("Hooray we found your file!")
print ("Script to take backup of devices, Please enter your credential")
device['username']=input("User name ")
device['password']=getpass.getpass()
print("Enter enable password: ")
device['secret']=getpass.getpass()

##taking backup
for line in f:
 try:
     device['ip']=line.strip("\n")
	 
     print ("\n\nConnecting Device ",line)
     net_connect = ConnectHandler(**device)
     net_connect.enable()
     time.sleep(1)
     print ("Reading the running config ")
     output = net_connect.send_command('show run')
     time.sleep(3)
     filename=device['ip']+'-'+today+".txt"
     saveconfig=open(filename,'w+')
     print("Writing Configuration to file")
     saveconfig.write(output)
     saveconfig.close()
     time.sleep(2)
     net_connect.disconnect()
     print ("Configuration saved to file",filename)
 except:
           print ("Access to "+device['ip']+" failed,backup did not taken")

f.close()
print ("\nAll device backup completed")