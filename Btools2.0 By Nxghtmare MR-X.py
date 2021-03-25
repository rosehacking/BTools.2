#!/usr/bin/python

import sys
import os
import threading
from time import sleep 


if os.getuid() != 0:
	print("\033[1;31m\nError:\033[0;m Este script requiere de privilegios de root (sudo)")
	sys.exit()

os.system("clear")

print('''
\033[96m
+=========================================+
|......... BEST TOOLS (my point)..........|
+-----------------------------------------+
|#Author:   @Samuel3928 edit by nxghtmare |
|#Contact: nxghtmaresoporte@gmail.com     |
|#Date:          25/03/2021               |
|#SI CAMBIAS PARTE DE ESTE CÓDIGO         |
|SOLO TE CONVIERTE EN LAMMER!!!!          |
|Creditos de este banner                  |
|MR-X817 in github                        |
|#I take no responsibilities for the      |
|use of this program !                    |
+=========================================+
|.........BEST TOOLS FOR LINUX!...........|
+-----------------------------------------+
''')

def menu():
	print("""
\033[1;37m(1)\033[0;m \033[0;32mFSociety\033[0;m            \033[1;37m(11)\033[0;m \033[0;32mYoda\033[0;            \033[1;37m(21)\033[0;m \033[0;32mTor-Browser\033[0;m                \033[1;37m(31)\033[0;m \033[0;32mShodanEye\033[0;m
\033[1;37m(2)\033[0;m \033[0;32mAnon-Surf\033[0;m           \033[1;37m(12)\033[0;m \033[0;32mNmap\033[0;m           \033[1;37m(22)\033[0;m \033[0;32mGitTool\033[0;m                    \033[1;37m(32)\033[0;m \033[0;32mPredator-Phishing\033[0;m
\033[1;37m(3)\033[0;m \033[0;32mHackTheWorld\033[0;m        \033[1;37m(13)\033[0;m \033[0;32manonET\033[0;m         \033[1;37m(23)\033[0;m \033[0;32mCoinmon\033[0;m                    \033[1;37m(33)\033[0;m \033[0;32mSqlmap\033[0;m
\033[1;37m(4)\033[0;m \033[0;32mCoronavirus-Stats\033[0;m   \033[1;37m(14)\033[0;m \033[0;32mInshackle\033[0;m      \033[1;37m(24)\033[0;m \033[0;32mGod-Killer\033[0;m                 \033[1;37m(34)\033[0;m \033[0;32mI-See-You\033[0;m
\033[1;37m(5)\033[0;m \033[0;32mCamHackers\033[0;m          \033[1;37m(15)\033[0;m \033[0;32mProxyGen\033[0;m       \033[1;37m(25)\033[0;m \033[0;32mLazyScript\033[0;m                 \033[1;37m(35)\033[0;m \033[0;32mSayChesse\033[0;m
\033[1;37m(6)\033[0;m \033[0;32mHolehe\033[0;m              \033[1;37m(16)\033[0;m \033[0;32mUserScan\033[0;m       \033[1;37m(26)\033[0;m \033[0;32mSherlock\033[0;m                   \033[1;37m(36)\033[0;m \033[0;32mTheFatRat\033[0;m
\033[1;37m(7)\033[0;m \033[0;32mRAASNet\033[0;m             \033[1;37m(17)\033[0;m \033[0;32mFacebook-Ban\033[0;m   \033[1;37m(27)\033[0;m \033[0;32mIPMux\033[0;m                      \033[1;37m(37)\033[0;m \033[0;32mRouterSploit\033[0;m
\033[1;37m(8)\033[0;m \033[0;32mCryDroid\033[0;m            \033[1;37m(18)\033[0;m \033[0;32mWhatsApp-Ban\033[0;m   \033[1;37m(28)\033[0;m \033[0;32mBeeLogger\033[0;m                  \033[1;37m(38)\033[0;m \033[0;32mLockPhish\033[0;m
\033[1;37m(9)\033[0;m \033[0;32mGvngSearch\033[0;m          \033[1;37m(19)\033[0;m \033[0;32mKickThemOut\033[0;m    \033[1;37m(29)\033[0;m \033[0;32mCupp\033[0;m                       \033[1;37m(39)\033[0;m \033[0;32mWishFish\033[0;m
\033[1;37m(10)\033[0;m \033[0;32mDroidFiles\033[0;m         \033[1;37m(20)\033[0;m \033[0;32mEvilTrust\033[0;m      \033[1;37m(30)\033[0;m \033[0;32mWifiJammer-ng\033[0;m              \033[1;37m(0)\033[0;m \033[0;31mSalir\033[0;m\033[0;37m/\033[0;m\033[0;31mLeave\033[0;m
""")
menu()

X = input("\033[1;44;37mEscoge Una Opción:\033[0;m \033[1;36m\n\n>\033[0;m ")


if X == "1":
    tool = os.system("git clone https://github.com/Manisso/fsociety")
elif X == "2":
    tool = os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git")
elif X== "3":
    tool = os.system("git clone https://github.com/Samuel3928/HackTheWorld.git")
elif X== "4":
    tool = os.system("sudo apt install curl")
    tool = os.system("curl https://corona-stats.online")
elif X=="5":
    tool = os.system("apt-get install python3-pip")
    tool = os.system("apt-get install git")
    tool = os.system("pip3 install requests")
    tool = os.system("pip3 install colorama")
    tool = os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
elif X=="6":
    tool = os.system("pip3 install holehe")
    tool = os.system("holehe")
elif X=="7":
    tool = os.system("git clone https://github.com/leonv024/RAASNet.git")
elif X=="8":
    tool = os.system("git clone https://github.com/benniraj25/crydroid.git")
elif X=="9":
    tool = os.system("git clone https://github.com/ByDog3r/GvngSearch")
elif X=="10":
    tool = os.system("git clone https://github.com/mafiamasterhere/droidfiles")
elif X=="11":
    tool = os.system("git clone https://github.com/Monkey-hk4/yoda")
elif X=="12":
    tool = os.system("apt-get install nmap")
elif X=="13":
    tool = os.system("git clone https://github.com/b4rc0d37/AnonET.git")
elif X=="14":
    tool = os.system("git clone https://github.com/xd20111/inshackle")
elif X=="15":
    tool = os.system("git clone https://github.com/tuhin1729/ProxyGen.git")
elif X=="16":
    tool = os.system("git clone https://github.com/JoeTech-Studio/UserScan.git")
elif X=="17":
    tool = os.system("git clone https://github.com/bhikandeshmukh/fbreport")
elif X=="18":
    tool = os.system("git clone https://github.com/Hacking-pch/WHATSAPP-BANEO.git")
elif X=="19":
    tool = os.system("git clone https://github.com/k4m4/kickthemout.git")
    tool = os.system("git clone https://github.com/secdev/scapy.git")
elif X=="20":
    tool = os.system("git clone https://github.com/s4vit4r/eviltrust.git")
elif X=="21":
    tool = os.system("apt-get install tor && service start tor")
elif X=="22":
    tool = os.system("https://github.com/Ha3MrX/GitTool.git")
elif X=="23":
    tool = os.system("sudo apt-get install nodejs")
    tool = os.system("sudo apt-get install npm")
    tool = os.system("sudo npm install –g coinmon")
    tool = os.system("coinmon")
elif X=="24":
    tool = os.system("git clone https://github.com/FDX100/GOD-KILLER.git")
elif X=="25":
    tool = os.system("git clone https://github.com/arismelachroinos/lscript")
elif X=="26":
    tool = os.system("git clone https://github.com/sherlock-project/sherlock")
elif X=="27":
    tool = os.system("apt-get install wget")
    tool = os.system("git clone https://github.com/Amriez/ipmux.git")
elif X=="28":
    tool = os.system("git clone https://github.com/4w4k3/BeeLogger.git")
elif X=="29":
    tool = os.system("git clone https://github.com/Mebus/cupp.git")
elif X=="30":
    tool = os.system("git clone https://github.com/MisterBianco/wifijammer-ng")
elif X=="31":
    tool = os.system("git clone https://github.com/BullsEye0/shodan-eye")
elif X=="32":
    tool = os.system("git clone https://github.com/tony23x/Predator-Phish")
elif X=="33":
    tool = os.system("git clone https://github.com/sqlmapproject/sqlmap")
elif X=="34":
    tool = os.system("git clone https://github.com/Viralmaniar/I-See-You")
elif X=="35":
    tool = os.system("git clone https://github.com/hangetzzu/saycheese")
elif X=="36":
    tool = os.system("git clone https://github.com/Screetsec/TheFatRat")
elif X=="37":
    tool = os.system("git clone https://github.com/threat9/routersploit")
elif X=="38":
    tool = os.system("git clone https://github.com/JasonJerry/lockphish")
elif X=="39":
    tool = os.system("git clone https://github.com/kinghacker0/WishFish")
elif X == "0":
    tool = os.system("exit")
    print("\n\033[1;32mGracias por usar Este script, vuelve Pronto!!\033[0;m\033[1;37m!\033[0;m")
else:
    print("\033[1;31m\nError:\033[0;m Carácter incorrecto, intente nuevamente cara de kuaker")