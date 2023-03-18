import os
import sys
import webbrowser
def information_gathering():
    print("Welcome to Information Gathereing Tools")
    os.system('nmap')
    print("Enter Your Nmap command By seeing above information")
    command = input()
    os.system(command)
    print("\n\n\n\n")
    tools_hub()
def wordlist():
        print("Welcome to wordlist Generator")
        print("Enter the max number of Words/digits should not be less than 8")
        max_words = input()
        print("Enter all the possible characters")
        possible_charcters = input()
        print("Enter the output txt file path along with name, i.e /home/kali/1.txt")
        out_name = input()
        command = 'crunch 8 '+max_words+' '+possible_charcters+' -o'+' '+out_name
        os.system(command)
        print("\n\n\n\n")
        tools_hub()
def wirless():
        print("Welcome to Wirless Attack Tools")
        print("We are going to use Wifiphisher")
        print("1.To Install\n2.To Run\n99.To Return to previous Menu\n")
        ch = int(input())
        if(ch == 1):        
            print("Enter Y for any prompts")
            os.system('git clone https://github.com/wifiphisher/wifiphisher.git')
            print("Installation Succesfull")
            os.chdir("/home/reddy/Desktop/wifiphisher")
            os.system('python setup.py install')
            wirless()
        elif(ch == 2):
            print('Do you have connected to Wifi. Enter Y or N')
            ch1 = input()
            if(ch1 == 'Y'):
                os.system('wifiphisher -aI wlan0 -jI wlan4 -p firmware-upgrade --handshake-capture handshake.pcap')
            else :
                os.system('wifiphisher -aI eth0 -jI wlan4 -p firmware-upgrade --handshake-capture handshake.pcap')
        else:
             tools_hub()
        print("\n\n\n\n")
        tools_hub()
def phishing():
        print("Welcome to Phishing Tools")
        print("We are using MaxPhisher tool \n\n\n")
        print("1.To Install\n2.To Run\n99.To Return to previous Menu\n")
        ch = int(input())
        if(ch == 1):
            os.system('git clone https://github.com/KasRoudra/MaxPhisher.git')
            phishing()
        elif(ch == 2):
            os.chdir("/home/reddy/Desktop/MaxPhisher")
            os.system('python maxphisher.py')
        else:
             tools_hub()
        print('\n\n\n')
        tools_hub()
def ddos():
         print("Welcome to DDOS TOOLS")
         print("We are using SLOWRIS tool \n\n\n")
         print("1.To Install\n2.To Run\n99.To Return to previous Menu\n")
         ch = int(input())
         if(ch==1):
            os.system('git clone https://github.com/gkbrk/slowloris.git')
            os.chdir("/home/reddy/Desktop/slowloris")
            ddos()
         elif(ch==2):
            print("Enter Url of the website")
            url = input()
            os.system('python slowloris.py '+url)
         else:
              tools_hub()
         print("\n\n\n")
         tools_hub()
def payload():
         print("Welcome to PAYLOAD CREATION TOOLS")
         print("We are using MSFVENOM tool \n\n\n")
         os.system('msfvenom -h')
         print("Enter You Input accordingly to Information Provided")
         x = input()
         os.system(x)
         print("\n\n\n\n")
         tools_hub()
def sql():
        print("Welcome to Sql Injection Tools")
        print("We are using sqlmap tool \n\n\n")
        print("1.To Install \n 2.To Run")
        ch = int(input())
        if(ch==1):
            os.system('sudo apt install sqlmap')
            print("Sucess install sqlmap")
            sql()
        else:
            os.system('sqlmap -h')
            os.system('sqlmap')
        print("\n\n\n")
        tools_hub()
def webattack():
        print("Welcome to webAttack Tools")
        print("We are Using SubDomain Finder tool \n\n\n")
        print("1.To Install\n2.To Run")
        ch = int(input())
        if(ch==1):
            os.system('git clone https://github.com/aboul3la/Sublist3r')
            print("Sucess install")
            webattack()
        else:
            os.chdir("/home/reddy/Desktop/Sublist3r")
            os.system('python sublist3r.py')
        print("\n\n\n")
        tools_hub()
def postexploatitation():
        print("Welcome to PostExploitation Tools")
        print("We are Using Vegile tool \n\n\n")
        print("1.To Install\n2.To Run")
        ch = int(input())
        if(ch == 1):
            os.system('https://github.com/Screetsec/Vegile')
            print("Successfuly Installed")
            postexploatitation()
        else:
            os.chdir("/home/reddy/Desktop/Vegile")
            os.system('chmod +x Vegile')
        print("\n\n\n")
        tools_hub()
def reverse():
        print('welcome to Reverse Engineering Tools')
        print('We are using apk2gold tool')
        print("1.To Install \n 2.To Run")
        ch = int(input())
        if(ch == 1):
            os.system('git clone https://github.com/lxdvs/apk2gold.git')
            print("Successfuly Installed")
            reverse()
        else:
            os.chdir("/home/reddy/Desktop/apk2gold")
            print('Enter Apk name')
            apk = input()
            os.system('apk2gold '+apk+'.apk' )
        print("\n\n\n")
        tools_hub()
def tools_hub():
    tools_list = ["InformationGatheringTools","WordlistGeneratorTools","Wireless Attack Tools","Phishing Attack Tools","DDOS Tools","Payload CreatorTools",
    "Sql Injection Tools","WebAttack Tools","Post Exploitation Tools","Reverse Engineering Tools"]
    c = 1
    for i in tools_list:
        print("[",c,"]"+".  " +i)
        c+=1
    n = int(input())
    if(n == 1):
           information_gathering()
        
    elif(n == 2):
           wordlist()

    elif(n == 3):
           wirless()

    elif(n==4):
       phishing()
    elif(n==5):
        ddos()
    elif(n == 6):
          payload()
         
    elif(n==7):
        sql()
    elif(n==8):
       webattack()
    elif(n==9):
          postexploatitation()
    elif(n == 10):
          reverse()
        

tools_hub()  




