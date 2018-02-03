###################################
# File Name : daemon_thread_join.py
###################################
#!/usr/bin/python3

import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")

def daemon():
    logging.debug("start")
    time.sleep(5)
    logging.debug("Exit")


def non_daemon():
    logging.debug("start")
    time.sleep(5)
    logging.debug("Exit")


t = threading.Thread(name="daemon", target=daemon)
t.setDaemon(True)

t.start()
t.join()
