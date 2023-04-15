import os

try:
    from selenium import webdriver
    from random import randint
    from time import sleep
    import webbrowser
    import threading
    from colorama import Fore, Style
    import io
    import json
    import requests
except Exception as e:
    os.system(f'mode 110,30')
    os.system('cls'); os.system("title [Terrific's ViewBot - Not Connected]")
    print(f" [ERROR] Coulnt import library's, installing librarys")
    reqpath = input(f" [>] Input The path of the folder this file is in: ")
    reqpath.replace('\\', '/')
    try:
        os.system(f'cd {reqpath}')
        os.system('python -m pip install -r requirements.txt')
    except Exception as e:
        print(" [ERROR] {e}")
    print(" Press Enter to exit")
    input(); exit()

os.system(f'mode 110,30')
os.system('cls'); os.system("title [Terrific's ViewBot - Connected]")
    
err = f"[{Fore.RED}-{Style.RESET_ALL}]"
out = f"[{Fore.GREEN}:{Style.RESET_ALL}]"
inp = f"[{Fore.MAGENTA}>{Style.RESET_ALL}]"
log = f"[{Fore.CYAN}={Style.RESET_ALL}]"
cr = f"[{Fore.GREEN}c{Style.RESET_ALL}/{Fore.RED}r{Style.RESET_ALL}]"
finish = f"press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit"

def get_config():
    global PATH
    path = input(f" {inp} Config file path without config.json: ")

    path = path + "/config.json"
    if not os.path.exists(path):
        with io.open(path, "w") as f:
            data = {
                    "executable_path": str(input(f" {inp} Full chromedriver path without .exe: "))
            }
            json.dump(data, f, indent=4)
            f.close
            print(f" {log} Generated config.json file")
    else:
        try:
            f = io.open(path, 'r')
            config = json.load(f)
            PATH = config.get('executable_path')
            f.close()
        except Exception as e:
            print(f" {err} {e}\n {finish}")
            input(); exit()
        pass
    pass

# Channel ViewBot
class Bot():
    global randomdel
    randomdel = int(randint(0, 60))

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=PATH)

    def __home(self):
        self.browser.get(channel)
        sleep(2)
        
    def __videoPage(self):
        self.__home()
        try:
            accept = self.browser.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form')
            accept.click()
            sleep(2)
        except:
            pass
        sleep(2)
        videoElm = self.browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]')
        videoElm.click()
        sleep(2)
    
    def __videoID(self, elementNumber):
        self.ids = self.browser.find_elements_by_id('thumbnail')
        return self.ids[elementNumber]

    def watchVideo(self, videoNumber, watchTime):
        self.videoNumber = videoNumber
        self.watchTime = watchTime

        self.__videoPage()
        self.__videoID(self.videoNumber)

        thumbnailElm = self.__videoID(self.videoNumber)
        thumbnailElm.click()
        print(f" {log} Watchtime: {watchTime}(sec) + {randomdel+(watchTime/2)}(sec)")
        sleep(int(watchTime + round(randomdel+(watchTime/2))))
    
    def stop(self):
        self.browser.close()
        print(f" {out} Finished, {finish}")
        input(); exit()

# ViewBot's
def viewbotv1():
    global randomdel
    randomdel = int(randint(0, 60))

    if str(d).lower() == "c":
        duration = input(f" {inp} Enter Duration (min): ")

    delay = input(f" {inp} Input a delay to open Tabs: ")
    def view():
        if str(d).lower() == "c":
            webbrowser.open(url)
            print(f" {log} Delay: {duration}(sec) + {randomdel+(duration/2)}(sec)")
            sleep(round(int(duration))*60 + round(randomdel+(duration/2)))
        elif str(d).lower() == "r":
            webbrowser.open(url)
            sleep(round(int(randint(1, 5)*60)))
        exit()

    threads = []
    try:
        for i in range(int(sessions)):
            thread =threading.Thread(target=view)
            thread.daemon = True
            threads.append(thread)
            thread.start()
            sleep(int(delay+(delay/2)))
        print(f" {out} Finished, {finish}")
    except Exception as e:
        print(f" {err} {e}\n {finish}")
        input(); exit()

    try:
        for i in range(len(threads)):
            thread.join()
            print(f" {log} Delay: {delay}(sec) + {randomdel+(delay/2)}(sec)")
            sleep(int(delay) + round(randomdel+(delay/2)))
    except Exception as e:
        print(f" {err} {e}\n {finish}")
        input(); exit()


class viewbotv2():
    global randomdel
    randomdel = int(randint(0, 60))

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=PATH)

    def __video(self):
        self.browser.get(url)
        sleep(1)
        try:
            accept = self.browser.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string')
            accept.click()
            sleep(1)
        except:
            pass
        sleep(1)
        
    def watchVideo(self, watchTime):
        self.watchTime = watchTime

        for i in range(int(sessions)):
            self.__video()
            print(f" {log} Delay: {watchTime}(sec) + {randomdel+(watchTime/2)}(sec)")
            sleep(round(int(randomdel+(watchTime/2))))
    
    def stop(self):
        self.browser.close()
        print(f" {log} Finished, {finish}")
        input(); exit()

banner = f'''{Fore.RED}

    ██▒   █▓ ██▓▓█████  █     █░ ▄▄▄▄    ▒█████  ▄▄▄█████▓
    ▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
    ▓██  █▒░▒██▒▒███   ▒█░ █ ░█ ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
    ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
    ▒▀█░  ░██░░▒████▒░░██▒██▓ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
    ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒  ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
    ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░  ▒░▒   ░   ░ ▒ ▒░     ░    
        ░░   ▒ ░   ░     ░   ░   ░    ░ ░ ░ ░ ▒    ░      
        ░   ░     ░  ░    ░     ░          ░ ░           
        ░                             ░   {Style.RESET_ALL}'''
inputs = f'''
     This is no longer Maintained...
     Do NOT expect this to work properly...

    [x]=====================================================[x]
     ║  [1]   =  Watch Videos on a Channel (YouTube only)    ║
     ║  [2]   =  viewbot v.1                                 ║
     ║  [3]   =  viewbot v.2                                 ║
     ║  [4]   =  Credits                                     ║
     ║  [5/X] =  Exit                                        ║
    [x]=====================================================[x]'''

def screen():
    global url; global d; global sessions
    os.system(f'mode 110,30')
    os.system('cls'); os.system("title [Terrific's ViewBot - Connected]")
    print(banner)
    print(f"\n {inputs}\n")
    get_config()
    i1 = input(f"\n {inp} $ ")

    if str(i1) == "1":
        global channel
        os.system("title [Terrific's ViewBot - YouTube]")
        channel = input(f" {inp} Channel url: ")
        if channel.startswith("https://www.youtube.com/c/") == False and channel.startswith("https://www.youtube.com/channel/") == False:
            print(f" {err} Invalid Input, {finish}")
            input(); exit()

        videos = input(f" {inp} How much Videos: ")
        watchtime = input(f" {inp} Watch next video after (sec): ")
        myBot = Bot()
        print(f"\n {log} Started")

        for i in range(int(videos)):
            print(f" {log} Watching Video: {i}/{videos}")
            myBot.watchVideo(i, int(watchtime))
        myBot.stop()

    elif str(i1) == "2":
        url = input(f" {inp} Enter URL: ")
        d = input(f" {inp} You want a custom or random duration {cr}: ")
        sessions = input(f" {inp} How much view's you want to bot: ")

        if url.startswith("https://youtube.com/") or url.startswith("https://youtu.be/"):
            os.system("title [Terrific's ViewBot - YouTube]")
        elif url.startswith("https://www.tiktok.com") or url.startswith("www.tiktok.com") or url.startswith("https://tiktok.com"):
            os.system("title [Terrific's ViewBot - TikTok]")
        viewbotv1()

    elif str(i1) == "3":
        os.system("title [Terrific's ViewBot - YouTube]")

        url = input(f" {inp} Enter URL: ")
        duration = input(f" {inp} Enter Duration (min): ")
        sessions = input(f" {inp} How much view's you want to bot: ")

        if url.startswith("https://youtube.com/watch") == False and  url.startswith("https://www.youtube.com/watch") == False:
            print(f" {err} Invalid Input, {finish}")
            input(); exit()

        watchtime = input(f" {inp} Watch video again after (sec): ")
        myBot = viewbotv2()
        for i in range(int(sessions)):
            myBot.watchVideo(int(duration)*60)
            print(f"\n {log} Started")
            sleep(int(watchtime))
        myBot.stop()
        print(f" {log} Finished, {finish}")
        input(); exit()

    elif str(i1) == "4":
        os.system('cls')
        os.system('title [Terrific`s ViewBot - Credits]')
        print(banner)
        print(f'''
        [x]========[x]====================[x]
         ║ Made By  ║ TerrificTable, Dom   ║
        [x]========[x]====================[x]
        ''')
        input(f" {log} {finish}"); exit()

    elif str(i1) == "4" or str(i1).lower() == "x":
        exit()
    else: 
        print(f" {err} Invalid Input, {finish}")
        input(); exit()
screen()
