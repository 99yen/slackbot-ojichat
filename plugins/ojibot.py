#coding: UTF-8

import subprocess
import re

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from slackbot_settings import OJICHAT_PATH, E_LEVEL, P_LEVEL

@default_reply()
def default_func(message):
    display_name = message.user["profile"]["display_name"]
    
    proc = subprocess.run([OJICHAT_PATH, "-e", E_LEVEL, "-p", P_LEVEL, display_name], stdout = subprocess.PIPE)
    ojisan_message = proc.stdout.decode("utf8")

    # アンダーバーがイタリック化の修飾になるのを防ぐために置換する
    # 'MODIFIER LETTER LOW MACRON' (U+02CD)
    ojisan_message = ojisan_message.replace('_', '\u02CD')
    
    #print(ojisan_message)
    message.reply(ojisan_message)
