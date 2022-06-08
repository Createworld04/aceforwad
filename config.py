#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5062996213:AAEXV4jWvivu-zqPfv8eBuPc1vLwhEFSoVE")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "18516364"))
    API_HASH = os.environ.get("API_HASH", "2e90970ea9e3ad55a3d7566754274fae")
    AUTH_USERS = os.environ.get("OWNER","5193769090")

