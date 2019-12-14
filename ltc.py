from telethon import TelegramClient, sync, events, errors
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json,re,sys,os
try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("\033[1;30m# \033[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4")
   sys.exit()

c = requests.Session()

banner = """                                              
eeeee  eeeee e    e eeee eeeee       e  eeeee 
8   8  8   8 8    8 8    "   8       8  8   8 
8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 
88   8 88  8   88   88   88          88 88  8 
88   8 88  8   88   88ee 88ee8       88 88ee8 
                               eeeee"""""
                               
if not os.path.exists("session"):
    os.makedirs("session")
   
if len(sys.argv)<2:
   print ("\n\n\n\033[1;32mUsage : python main.py +62")
   sys.exit(1)

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;30m[\033[1;32m+\033[1;30m]\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)
       
ua={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
api_id = 800812
api_hash = "db55ad67a98df35667ca788b97f771f5"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
  client.send_code_request(phone_number)
  me = client.sign_in(phone_number, input("\n\n\n\n033[1;33mEnter Your Verification Code : "))
myself = client.get_me()
os.system('clear')
print("\033[1;35m",banner)
print("\033[1;36m=============================================")
sys.stdout.write(f"\033[1;32m ~ anthesphong1998@gmail.com ({phone_number})\n")
print("\033[1;36m=============================================\n\n")
print (f"\033[1;35mTHIS SCRIPT IS NOT FOR SALE \033[1;36m- {myself.first_name}\n")
try:
 channel_entity=client.get_entity("@Litecoin_click_bot")
 channel_username="@Litecoin_click_bot"
 
 for i in range(5000000):
  sys.stdout.write("\r")
  sys.stdout.write("                                                              ")
  sys.stdout.write("\r")
  sys.stdout.write("\033[1;30m[\033[1;33m!\033[1;30m] \033[1;33mMencoba Mengambil URL")
  sys.stdout.flush()
  client.send_message(entity=channel_entity,message="ðŸ–¥ Visit sites")
  sleep(2)
  posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
  if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
     print ("\n\033[1;30m[\033[1;31mx\033[1;30m] \033[1;31mIklan sudah habis, Coba lagi besok\033[1;32m")
     client.send_message(entity=channel_entity,message="ðŸ’° Balance")
     sleep(1)
     posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
     messag = posts.messages[0].message
     print ("\033[1;30m[\033[1;32m+\033[1;30m]\033[1;32m",messag,channel_username)
     sys.exit()
     
  else:
    try:
     url = posts.messages[0].reply_markup.rows[0].buttons[0].url
     sys.stdout.write("\r")
     sys.stdout.write("\033[1;30m[\033[1;33m!\033[1;30m] \033[1;33mVisit "+url)
     sys.stdout.flush()
     id = posts.messages[0].id
     r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
     soup = BeautifulSoup(r.content,"html.parser")
     if soup.find("div",class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
        sleep(2)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           tunggu(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write("\r\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32m"+messageres+"\n")
        else:
           pass
     elif soup.find('div', id="headbar") is not None:
        for dat in soup.find_all('div',class_="container-fluid"):
            code = dat.get('data-code')
            timer = dat.get('data-timer')
            tokena = dat.get('data-token')
            tunggu(int(timer))
            r = c.post("https://dogeclick.com/reward",data={"code":code,"token":tokena}, headers=ua, timeout=15, allow_redirects=True)
            js = json.loads(r.text)
            sys.stdout.write("\r\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32mYou earned "+js['reward']+" LTC for visiting a site!\n")
     else:
        sys.stdout.write("\r")
        sys.stdout.write("                                                                ")
        sys.stdout.write("\r")
        sys.stdout.write("\033[1;30m[\033[1;31mx\033[1;30m] \033[1;31mCaptcha Detected")
        sys.stdout.flush()
        sleep(2)
        client(GetBotCallbackAnswerRequest(
        channel_username,
        id,
        data=posts.messages[0].reply_markup.rows[1].buttons[1].data
        ))
        sys.stdout.write("\r\033[1;30m[\033[1;31mx\033[1;30m] \033[1;31mSkip Captcha...!       \n")
        sleep(2)
    except:
        sleep(3)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           tunggu(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write("\r\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32m"+messageres+"\n")
        else:
           pass

finally:
   client.disconnect()