import webbrowser
import random
import time
import subprocess, signal
import os


def close_app(appName):
    p = subprocess.Popen(['ps','-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
        if appName in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


def get_timestamp():
    now = time.strftime("%c")
    return now

def get_rand_urls(fn,urlnum):
    with open(fn, "r") as f:
        list2 = []
        for item in f:
            list2.append(item.rstrip('\n'))

        return random.sample(list2,urlnum)


def get_url_safari(fn, urlnum):
    urllst = get_rand_urls(fn,urlnum)
    print urllst
    for url in urllst:
        time.sleep(random.randint(1, 8))
        webbrowser.get('safari').open_new(url)
        time.sleep(10)
        with open('interactions.log','a+') as logfile:
            logfile.write('{}, {}\n'.format(url, get_timestamp()))

    close_app('Safari')




for x in range(10):
    time.sleep(5)
    get_url_safari('data/validUrls.txt',1)
