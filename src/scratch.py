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
            list2.append(item)

        return random.sample(list2,urlnum)


def get_url_safari(fn, urlnum):
    urllst = get_rand_urls(fn,urlnum)

    for url in urllst:
        print 'Accessing: {}'.format(url)
        print '='*int(len(url))
        print get_timestamp()
        webbrowser.get('safari').open_new_tab(url)
    close_app('Safari')





get_url_safari('data/validUrls.txt',100)
