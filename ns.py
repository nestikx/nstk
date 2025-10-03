import threading
import requests
import time

def timer():
    while True:
        time.sleep(300)
        requests.get(url = "https://nstk.onrender.com")

thread = threading.Thread(target = timer)
thread.start()