import os
import re
from pyrogram.errors import exceptions
import pickle

def get_banned_users() -> list:
    f = open("data", "rb")
    r = []
    try:
        up = pickle.load(f)
        if "banned_users" in up:
            r = up["banned_users"]
        else:
            r = []
    except:
        pass
    f.close()
    return r
