import asyncio
import json,re,sys,os
from time import sleep
import requests
from telethon import TelegramClient, sync, events

api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

ltc = '@litcoinautotopup_bot'

def tunggu(x):
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;30m[\033[1;33m!\033[1;30m] \033[1;33mClaim lagi setelah \033[1;33m{:2d} detik".format(remaining))
       sys.stdout.flush()
       sleep(1)
       sys.stdout.write("\r                                                 \r")

async def main():
    if len(sys.argv) < 2:
        print('Usage: python start.py phone_number')
        print('-> Input number in international format (example: +639162995600)\n')
        e = input('Press any key to exit...')
        exit(1)

    phone_number = sys.argv[1]
    
    os.system('clear')
    print("\033[1;35meeeee  eeeee e    e eeee eeeee       e  eeeee ")
    print("\033[1;35m8   8  8   8 8    8 8    '   8       8  8   8 ")
    print("\033[1;35m8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 ")
    print("\033[1;35m88   8 88  8   88   88   88          88 88  8 ")
    print("\033[1;35m88   8 88  8   88   88ee 88ee8       88 88ee8 ")
    print("\033[1;35m                               eeeee          ")
    print("\033[0;36m=============================================")
    print(f"\033[1;32m • anthesphong1998@gmail.com ({phone_number})")
    print("\033[0;36m=============================================\n\n")
    if not os.path.exists("session"):
        os.mkdir("session")
   
    client = TelegramClient('session/' + phone_number, api_id, api_hash)
    await client.start(phone_number)
    me = await client.get_me()
    
    print (f"\033[1;35mScript ini untuk nuyul \033[1;36m{ltc}\n\033[1;35mWelcome to bot \033[1;36m- {me.first_name}\n")

    i = 1
    while i <= 10000:
        await client.send_message(ltc, '🧀Bonus🧀')
        print('\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32m0.00000005 Has been added to your balance ')
        tunggu(int(60))
        
    i += 1
    await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
