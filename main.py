from concurrent.futures import ThreadPoolExecutor
from requests import Session
import os 
from threading import Semaphore
import datetime
import time

class FavsBot:
    def __init__(self):
        self.semaphore = Semaphore(150)
        self.session = Session()
        self.get = self.session.get
        self.susu = 0
        self.success = 0
        self.dateiname = "sessions.txt"
        
        with open(self.dateiname, 'r') as datei:
            for zeile in datei:
                self.susu += 1
        
        os.system("title Amgxp's Favs Bot ")
        self.videoid = input("[?] VideoID: ")
        print("\n")

    def digg(self, sessionid):
        saved = False 
        
        for _ in range(5):
            try:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                url = "https://api31-normal-useast2a.tiktokv.com/aweme/v1/aweme/collect/?aweme_id={}&action=1&channel=beta&aid=1233&app_name=musical_ly&version_code=300015&device_platform=android&device_type=unknown&os_version=9".format(self.videoid)
                
                headers = {
                    'cookie'     : f'sessionid={sessionid}',
                    'user-agent' : 'com.zhiliaoapp.musically/2023000150 (Linux; U; Android 9; en; unknown; Build/PI;tt-ok/3.12.13.1)',
                    'x-argus'    : '6/4Ixi5HhJlI9uQQ53v6tfgstiGWncc8cXAdJv3B4bYHhdfaOHbsTjhflGqNLOvkrjwx4dOgB7WkmBgfbzEpRJuTuOXbV/E3mpp5q50CGlxsj36HnopveP4HytXQz78l17XI4HmrtzIvynNT2+F3UfiFJxUbtAJoGtvqeGQeb7kg6V1O1dfCFI4jNJwmEso5zOH5F5keoBwvUiZhcf8FZOWNWuPKYgR26vVOlu90fxczeGnP6bvr2+gzuCbrNZ4rR+LQ7E0gEx2q9Uw6ev3nZyP8XaVmXRtqmCO4/nWqxiWtPZDxmbDAoRITB0/rt05MJ75eaYNwBzQ3SYboFk/f/RyJmKRb7q/eUAp25f1cD93N4S+RlYTBFzlbZlUodgdQDbDEhl8EK46mDJ4qJmwpd6dZo2hlTnuoxvnlJRgzZydJrvXNBsXpv3+cY6X80HExvOlOvcZQ9ZuuqKY9J6bk7M2o3Jvxr+ZuvJkIqHUwF3LmSGhG2CJuOlcDwoTlcb5KLN/7JL4Wi8nvvE7HsMt+Zd5MqsC12QYI9gHwqghu0U6W4A=='
                }

                if b'"saved"' in self.get(url, headers=headers).content:
                    if saved:
                        continue
                    print(f'[?] [{current_time}] Saved: +++ ({self.videoid})', flush=True)
                    saved = True 
                    self.success += 1
                    break
                else: 
                    continue
            except Exception as e:
                continue

    def process_session(self, sessionid):
        self.semaphore.acquire()
        os.system(f"title Amgxp's Favs Bot  Sent: [{self.success}] From: [{self.susu}] SessionID: [{sessionid}]")
        self.digg(sessionid)
        self.semaphore.release()

    def run(self):
        with open("sessions.txt", "r") as file:
            with ThreadPoolExecutor(max_workers=150) as executor:
                for line in file.read().splitlines():
                    executor.submit(self.process_session, line)

bot = FavsBot()
bot.run()
