#!/usr/bin/python

import subprocess
import time
import datetime
from pexpect import *
import sys
import random

VALOPER = sys.argv[1]
WALLET = sys.argv[2]
PASSWORD = sys.argv[3]


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def get_balance():
    data = subprocess.check_output(f"seid q bank balances {WALLET}", shell=True, encoding='cp437')
    return data.split('\n')[1]\
        .replace('"', '')\
        .replace('-', '')\
        .replace(':', '')\
        .replace('amount', '').strip()


def delegate():
    cmd = f"seid tx staking delegate {VALOPER} 500000usei --from {WALLET} --fees 2000usei -y"
    child = spawn(cmd, timeout=5, encoding='utf-8')
    child.expect('(?i)pass')
    child.sendline(PASSWORD)
    print(child.after)
    child.interact()


def claim_commision():
    cmd = f"seid tx distribution withdraw-rewards {VALOPER} --from {WALLET} --fees 2000usei -y"
    child = spawn(cmd, timeout=5, encoding='utf-8')
    child.expect('(?i)pass')
    child.sendline(PASSWORD)
    print(child.after)
    child.interact()


def claim_reward():
    cmd = f"seid tx distribution withdraw-all-rewards --from {WALLET} --fees 2000usei -y"
    child = spawn(cmd, timeout=5, encoding='utf-8')
    child.expect('(?i)pass')
    child.sendline(PASSWORD)
    print(child.after)
    child.interact()


print("Telegram: https://t.me/icodragon")
print("Discord: icodragon [NODERS]#4560")
while True:
    print(datetime.datetime.now(), '🔴 --> Send request get commision.')
    claim_commision()
    time.sleep(random.randint(60, 70))
    print(datetime.datetime.now(), '🔴 --> Send request get reward.')
    claim_reward()
    time.sleep(random.randint(60, 70))
    balance = get_balance()
    if check_int(balance):
        if int(balance) >= 510000:
            print(datetime.datetime.now(), '🟢 --> Send request delegate.')
            delegate()
            time.sleep(random.randint(60, 70))
        else:
            print(510000 - int(balance), 'tokens left till delegate.')
