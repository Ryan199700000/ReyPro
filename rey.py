# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

ryan = LINETCR.LINE()
#ryan.login(qr=True)
ryan.login(token='ErZTJZ35hZxUib4y1c./xAA3piZkDNk7C2fd2YUQa.6VhsLGliwQ9vbCGIXOxkqYtJEbREyqaqksUeiy69Js4=')
ryan.loginResult()
print "ReyPro-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


helpMessage ="""╔═════════════════════╗
║   ™☆☞ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅ☜☆™
╠═══╣☞ʜ ᴇ ʟ ᴘ☜╠═════════╣
╠🌟『ᴏᴡɴᴇʀ』
╠🌟『ᴘᴀᴘ ᴏᴡɴᴇʀ』
╠🌟『sᴘᴇᴇᴅ』
╠🌟『sᴘᴇᴇᴅ ᴛᴇsᴛ』
╠🌟『sᴛᴀᴛᴜs』
╠═══╣☞ s ᴇ ʟ ғ☜╠═════════╣
╠✨『ʜɪ』
╠✨『ᴍᴇ』
╠✨『ᴍʏᴍɪᴅ』
╠✨『ᴍɪᴅ @』
╠✨『sᴇᴀʀᴄʜɪᴅ ɪᴅ ʟɪɴᴇ)』
╠✨『ᴄʜᴇᴄᴋᴅᴀᴛᴇᵈᵈ/ᵐᵐ/ʸʸ』
╠✨『ᴋᴀʟᴇɴᴅᴇʀ』
╠✨『sᴛᴇᴀʟ ᴄᴏɴᴛᴀᴄᴛ』
╠✨『ᴘᴘ @』
╠✨『ᴄᴏᴠᴇʀ @』
╠✨『ᴀᴜᴛᴏ ʟɪᴋᴇ』
╠✨『sᴄʙᴄᵗᵉˣᵗ』
╠✨『ᴄʙᴄᵗᵉˣᵗ』
╠✨『ɢʙᴄᵗᵉˣᵗ』
╠✨『ʙɪᴏ @』
╠✨『ɪɴғᴏ @』
╠✨『ɴᴀᴍᴇ @』
╠✨『ᴘʀᴏғɪʟᴇ @』
╠✨『ᴄᴏɴᴛᴀᴄᴛ @』
╠✨『ɢᴇᴛᴠɪᴅ @』
╠✨『ғʀɪᴇɴᴅʟɪsᴛ』
╠✨『ʀᴇᴘᴀᴅᴅ @』
╠✨『ʀᴇᴘᴅᴇʟ @』
╠✨『ᴍɪᴄʟɪsᴛ』
╠═══╣☞ʙ ᴏ ᴛ☜╠══════════╣
╠🚨『ᴀʙsᴇɴ』
╠🚨『ʀᴇsᴘᴏɴ』
╠🚨『ʀᴜɴᴛɪᴍᴇ』
╠🚨『ᴄᴏᴘʏ @』
╠🚨『ᴄᴏᴘʏᴄᴏɴᴛᴀᴄᴛ』
╠🚨『ᴍʏʙᴀᴄᴋᴜᴘ』
╠🚨『ᴍʏʙɪᴏᵗᵉˣᵗ』
╠🚨『ᴍʏɴᴀᴍᴇᵗᵉˣᵗ』
╠🚨『@ʙʏᴇ』
╠🚨『ʙᴏᴛᵒⁿ-ᵒᶠᶠ』
╠═══╣☞ ᴍ ᴇ ᴅ ɪ ᴀ ☜╠═══════╣
╠💻『ɢɪғᴛ』
╠💻『ɢɪғᴛʙʏᴄᴏɴᴛᴀᴄᴛ』
╠💻『ɢɪғ ɢᴏʀᴇ』
╠💻『ɢᴏᴏɢʟᴇ (ᴛᴇxᴛ)』
╠💻『ᴘʟᴀʏsᴛᴏʀᴇ ɴᴀᴍᴀᴀᴘᴘ』
╠💻『ғᴀɴᴄʏᴛᴇxᴛᵗᵉˣᵗ』
╠💻『ᴍᴜsɪᴋʲᵘᵈᵘˡ-ᵖᵉⁿʸᵃⁿʸⁱ』
╠💻『ʟɪʀɪᴋʲᵘᵈᵘˡ-ᵖᵉⁿʸᵃⁿʸⁱ』
╠💻『ᴍᴜsʀɪᴋʲᵘᵈᵘˡ-ᵖᵉⁿʸᵃⁿʸⁱ』
╠💻『ɪɢ ᴜʀsɴᴀᴍᴇɪɴsᴛᴀɢʀᴀᴍ』
╠💻『ᴄʜᴇᴄᴋɪɢ ᴜʀsɴᴀᴍᴇɪɢ』
╠💻『ᴀᴘᴀᴋᴀʜᵗᵉˣᵗ 』
╠💻『ᴋᴀᴘᴀɴᵗᵉˣᵗ 』
╠💻『ʜᴀʀɪᵗᵉˣᵗ 』
╠💻『ʙᴇʀᴀᴘᴀᵗᵉˣᵗ 』
╠💻『ʙᴇʀᴀᴘᴀᴋᴀʜᵗᵉˣᵗ』
╠💻『ʏᴏᴜᴛᴜʙᴇʲᵘᵈᵘˡ ᵛⁱᵈᵉᵒ』
╠💻『ʏᴏᴜᴛᴜʙᴇᴠɪᴅᴇᴏʲᵘᵈᵘˡ ᵛⁱᵈᵉᵒ』
╠💻『ʏᴏᴜᴛᴜʙᴇsᴇᴀʀᴄʜ:ʲᵘᵈᵘˡ ᵛⁱᵈᵉᵒ』
╠💻『ɪᴍᴀɢᴇ ɴᴀᴍᴀɢᴀᴍʙᴀʀ』
╠💻『sᴀʏᵗᵉˣᵗ』
╠💻『sᴀʏ-ᴇɴᵗᵉˣᵗ』
╠💻『sᴀʏ-ᴊᴘᵗᵉˣᵗ』
╠💻『ᴛʀ-ɪᴅᵗᵉˣᵗ ᴇɴ ᴋᴇ ɪᴅ』
╠💻『ᴛʀ-ᴇɴᵗᵉˣᵗ ɪᴅ ᴋᴇ ᴇɴ』
╠💻『ᴛʀ-ᴛʜᵗᵉˣᵗ ɪᴅ ᴋᴇ ᴛʜ』
╠💻『ɪᴅ@ᴇɴᵗᵉˣᵗ ɪᴅ ᴋᴇ ᴇɴ』
╠💻『ɪᴅ@ᴛʜᵗᵉˣᵗ ɪᴅ ᴋᴇ ᴛʜ』
╠💻『ᴇɴ@ɪᴅᵗᵉˣᵗ ᴇɴ ᴋᴇ ɪᴅ』
╠═══╣☞ ɢ ʀ ᴏ ᴜ ᴘ ☜╠═══════╣
╠🌀『ᴡᴇʟᴄᴏᴍᴇ』
╠🌀『sᴀʏ ᴡᴇʟᴄᴏᴍᴇ』
╠🌀『ɪɴᴠɪᴛᴇ ᴄʀᴇᴀᴛᴏʀ』
╠🌀『sᴇᴛᴠɪᴇᴡ/ᴄᴄᴛᴠ』
╠🌀『ᴠɪᴇᴡsᴇᴇɴ/ᴄɪᴅᴜᴋ』
╠🌀『ɢɴ: (ɴᴀᴍᴀɢʀᴏᴜᴘ)』
╠🌀『ᴛᴀɢ ᴀʟʟ/ᴄʀᴏᴏᴛ』
╠🌀『ʟᴜʀᴋᵒⁿ-ᵒᶠᶠ』
╠🌀『ʟᴜʀᴋᴇʀs』
╠🌀『ʀᴇᴄᴏᴠᴇʀ』
╠🌀『ᴄᴀɴᴄᴇʟ』
╠🌀『ᴄᴀɴᴄᴇʟ ᴀʟʟ』
╠🌀『ɢᴄʀᴇᴀᴛᴏʀ』
╠🌀『ɢɪɴғᴏ』
╠🌀『ɢᴜʀʟ』
╠🌀『ʟɪsᴛ ɢʀᴏᴜᴘ』
╠🌀『ᴘɪᴄᴛ ɢʀᴏᴜᴘ: ɴᴀᴍᴀɢʀᴏᴜᴘ』
╠🌀『sᴘᴀᴍ-5:ᵗᵉˣᵗ』
╠🌀『ɴsᴘᴀᴍ:ᵗᵉˣᵗ』
╠🌀『ɢʜᴏsᴛsᴘᴀᴍ:ᵗᵉˣᵗ』
╠🌀『ᴀᴅᴅ ᴀʟʟ』
╠🌀『ᴋɪᴄᴋ: ᴍɪᴅ』
╠🌀『ɪɴᴠɪᴛᴇ: ᴍɪᴅ』
╠🌀『ɪɴᴠɪᴛᴇ』
╠🌀『ᴍᴇᴍʟɪsᴛ』
╠🌀『ɢᴇᴛɢʀᴏᴜᴘ ɪᴍᴀɢᴇ』
╠🌀『ᴜʀʟɢʀᴏᴜᴘ ɪᴍᴀɢᴇ』
╠═══╣☞s ᴇ ᴛ ☜╠══════════╣
╠🔏『ɴᴏᴛɪғᵒⁿ-ᵒᶠᶠ』
╠🔏『ᴍɪᴍɪᴄᵒⁿ-ᵒᶠᶠ』
╠🔏『ᴜʀʟᵒⁿ-ᵒᶠᶠ』
╠🔏『ᴀʟᴡᴀʏsʀᴇᴀᴅᵒⁿ-ᵒᶠᶠ』
╠🔏『ʙᴜʀᴜ sɪᴅᴇʀᵇᵉʳᵇᵘʳᵘ ˢⁱᵈᵉʳ』
╠🔏『ʙs ᴏғғᵇᵉʳᵇᵘʳᵘ ˢⁱᵈᵉʳ ᵒᶠᶠ』
╠🔏『ᴘʀᴏᴛᴇᴄᴛᵒⁿ-ᵒᶠᶠ』
╠🔏『ʟᴇᴀᴠᴇᵒⁿ-ᵒᶠᶠ』
╠🔏『ɪɴᴠɪᴛᴇᴘʀᴏᵒⁿ-ᵒᶠᶠ』
╠🔏『ᴄᴀɴᴄᴇʟᴘʀᴏᵒⁿ-ᵒᶠᶠ』
╠🔏『ϙʀᵒⁿ-ᵒᶠᶠ』
╠🔏『ᴄᴏɴᴛᴀᴄᴛᵒⁿ-ᵒᶠᶠ』
╠🔏『sᴛɪᴄᴋᴇʀ ᴏɴ』
╠🔏『sɪᴍɪsɪᴍɪᵒⁿ-ᵒᶠᶠ』
╠═══╣☞ ᴄ ʀ ᴇ ᴀ ᴛ ᴏ ʀ ☜╠═════╣
╠🎬『ʙʟᴀɴᴋ』
╠🎬『ᴋɪᴄᴋᴀʟʟ/ᴄᴜss』
╠🎬『ʙᴄ:ᵗᵉˣᵗ』
╠🎬『ᴊᴏɪɴ ɢʀᴏᴜᴘ: (ɴᴀᴍᴀɢʀᴏᴜᴘ』
╠🎬『ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ: (ɴᴀᴍᴀɢʀᴏᴜᴘ』
╠🎬『ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ』
╠🎬『ᴛᴀɢᵒⁿ-ᵒᶠᶠ』
╠🎬『ʙᴏᴛ ʀᴇsᴛᴀʀᴛ/ʀᴇʙᴏᴏᴛ』
╠🎬『ᴛᴜʀɴ ᴏғғ』
╠═════════════════════╣
║♻ ᴄʀᴇᴀᴛɪɴɢ ʙʏ:®ʀ̸ʏ̸ᴀ̸̸ɴ̸  ʀ̸̸ᴀ̸s̸̸ʏ̸ɪ̸̸ᴅ̸ ♻
║    ®sᴜᴘᴘᴏʀᴛ ʙʏ :
║        s҈ ɪ҈ ʟ҈ ᴇ҈ ɴ҈ ᴛ҈  ҈ ᴋ҈ ɪ҈ ʟ҈ ʟ҈ ™҈ 『҈ s҈ ᴋ҈ 』҈
╚═════════════════════╝"""


ryanMessage ="""╔═════════════════════╗
║         ™☆☞ʀ̸ʏ̸ᴀ̸ɴ̸ ʀ̸ᴀ̸s̸ʏɪ̸ᴅ̸☜☆™
╠═════════════════════╣
╠🔒『ᴀʟʟᴘʀᴏᴛᴇᴄᴛᵒⁿ-ᵒᶠᶠ』
╠🔒『ʙᴀɴ』
╠🔒『ᴜɴʙᴀɴ』
╠🔒『ʙᴀɴ @』
╠🔒『ᴜɴʙᴀɴ @』
╠🔒『ʙᴀɴ ʟɪsᴛ』
╠🔒『ᴄʟᴇᴀʀ ʙᴀɴ』
╠🔒『ᴋɪʟʟ』
╠🔒『ᴋɪᴄᴋ @』
╠🔒『sᴇᴛ ᴍᴇᴍʙᴇʀ: ᴊᴜᴍʟᴀʜ』
╠🔒『ʙᴀɴ ɢʀᴏᴜᴘ: ɴᴀᴍᴀɢʀᴏᴜᴘ』
╠🔒『ᴅᴇʟ ʙᴀɴ: ɴᴀᴍᴀɢʀᴏᴜᴘ』
╠🔒『ʟɪsᴛ ʙᴀɴ』
╠🔒『ᴋɪʟʟ ʙᴀɴ』
╠🔒『ɢʟɪsᴛ』
╠🔒『ɢʟɪsᴛᴍɪᴅ』
╠🔒『ᴅᴇᴛᴀɪʟs ɢʀᴏᴜᴘ: ɢɪᴅ』
╠🔒『ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ: ɢɪᴅ』
╠🔒『ɪɴᴠɪᴛᴇᴍᴇᴛᴏ: ɢɪᴅ』
╠🔒『ᴀᴄᴄ ɪɴᴠɪᴛᴇ』
╠🔒『ʀᴇᴍᴏᴠᴇᴄʜᴀᴛ』
╠🔒『ϙʀᵒⁿ-ᵒᶠᶠ』
╠🔒『ᴀᴜᴛᴏᴋɪᴄᴋᵒⁿ-ᵒᶠᶠ』
╠🔒『ᴀᴜᴛᴏᴄᴀɴᴄᴇʟᵒⁿ-ᵒᶠᶠ』
╠🔒『ɪɴᴠɪᴛᴇᴘʀᴏᵒⁿ-ᵒᶠᶠ』
╠🔒『ᴊᴏɪɴᵒⁿ-ᵒᶠᶠ』
╠🔒『ᴊᴏɪɴᴄᴀɴᴄᴇʟᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴ1ᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴ2ᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴ3ᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴ4ᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴ5ᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴ6ᵒⁿ-ᵒᶠᶠ』
╠🔒『ʀᴇsᴘᴏɴᴋɪᴄᴋᵒⁿ-ᵒᶠᶠ』
╠═════════════════════╣
║♻ ᴄʀᴇᴀᴛɪɴɢ ʙʏ:®ʀ̸ʏ̸ᴀ̸̸ɴ̸  ʀ̸̸ᴀ̸s̸̸ʏ̸ɪ̸̸ᴅ̸ ♻
║®sᴜᴘᴘᴏʀᴛ ʙʏ :
║     s҈ ɪ҈ ʟ҈ ᴇ҈ ɴ҈ ᴛ҈  ҈ ᴋ҈ ɪ҈ ʟ҈ ʟ҈ ™҈ 『҈ s҈ ᴋ҈ 』҈ 
╚═════════════════════╝"""


KAC=[ryan]
mid = ryan.getProfile().mid
Bots=[mid]
Creator=["uf9769adcf23329d9caedcd850f6caea8"]
admin=["uf9769adcf23329d9caedcd850f6caea8","ue68f9047eead247fb9dcd452eb7649f9"]

contact = ryan.getProfile()
backup1 = ryan.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage
backup1.pictureStatus = contact.pictureStatus

responsename = ryan.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":True,
    "AutoJoinCancel":False,
    "memberscancel":1,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":True,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},
    'likeOn':{},
    'detectMention':False,
    'detectMention2':False,
    'detectMention3':False,
    'detectMention4':False,
    'detectMention5':False,
    'detectMention6':False,
    'kickMention':False,
    'sticker':False,
    'timeline':True,
    'autoAdd':True,
    "Timeline":True,
    "comment":"☆ᴀᴜᴛᴏ ʟɪᴋᴇ ©ʙʏ : ʀᴇ̶ʏ̶ᴘʀ̶ᴏ̶™\n╔═════════════════════\n╠♻sᴜᴘᴘᴏʀᴛ ʙʏ :\n╠☆☞ sɪʟᴇɴᴛ ᴋɪʟʟ™『sᴋ』\n╠☆☞ ɴᴊ ᴋɪʟʟᴇʀs™『ɴᴊᴋ』\n╠═════════════════════\n╠☆☞ ʜᴛᴛᴘ://ʟɪɴᴇ.ᴍᴇ/ᴛɪ/ᴘ/~s.ᴋ.9.7\n╚═════════════════════",
    "commentOn":True,
    "commentBlack":{},
    "message":"ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ (^_^)\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n╔══════════════════\n╠۩ᴄʀᴇᴀᴛᴏʀ ʙʏ : \n╠● ʀ̸ʏ̸ᴀ̸ɴ̸ ʀ̸ᴀ̸s̸ʏɪ̸ᴅ̸\n╠۩ʀᴇᴀʟ ᴀᴄᴄᴏᴜɴᴛ : \n╠● ʟɪɴᴇ.ᴍᴇ/ᴛɪ/ᴘ/~s.ᴋ.9.7\n╚══════════════════\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●",    
    "lang":"JP",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "protect":{},
    "cancelprotect":False,
    "Contact":False,
    "Sambutan":False,
    "inviteprotect":False,
    "alwaysRead":False,
    "Sider":{},
    "Simi":{},
#    "detectAll":True,
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ᴊᴀᴍ %02 ᴍᴇɴɪᴛ %02d ᴅᴇᴛɪᴋ' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       ryan.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              ryan.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                ryan.sendText(op.param1,str(wait["message"]))
                
      #  if op.type == 5:
         #   if wait["autoAdd"] == True:
             #   if (wait["message"] in [""," ","\n",None]):
              #      pass
               # else:
                #    ryan.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	
	    if op.type == 55:
                try:
                     if op.param1 in wait2['readPoint']:     
                         if op.param2 in wait2['readMember'][op.param1]:
                              pass
                         else:
                              wait2['readMember'][op.param1] += op.param2
                         wait2['ROM'][op.param1][op.param2] = op.param2
                         with open('sider.json', 'w') as fp:
                          json.dump(wait2, fp, sort_keys=True, indent=4)
                     else:
                         pass
                except:
                    pass
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ryan.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        ryan.sendText(op.param1, "ʜᴀɪɪ " + "☞ " + Name + " ☜" + "\nɴɢɪɴᴛɪᴘ ᴀᴊᴀ ɴɪɪʜ. . .\nᴄʜᴀᴛ ᴋᴇᴋ ɪᴅɪɪʜ (-__-)   ")
                                        time.sleep(0.0)
                                        summon(op.param1,[op.param2])
                                    else:
                                        ryan.sendText(op.param1, "ʜᴀɪɪ " + "☞ " + Name + " ☜" + "\nʙᴇᴛᴀʜ ʙᴀɴɢᴇᴛ ᴊᴀᴅɪ ᴘᴇɴᴏɴᴛᴏɴ. . .\nᴄʜᴀᴛ ɴᴀᴘᴀ (-__-)   ")
                                        time.sleep(0.0)
                                        summon(op.param1,[op.param2])
                                else:
                                    ryan.sendText(op.param1, "ʜᴀɪɪ " + "☞ " + Name + " ☜" + "\nɴɢᴀᴘᴀɪɴ ᴋᴀᴋ ɴɢɪɴᴛɪᴘ ᴀᴊᴀ???\nsɪɴɪ ɢᴀʙᴜɴɢ ᴄʜᴀᴛ...   ")
                                    time.sleep(0.0)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            if wait["LeaveRoom"] == True:
                ryan.leaveRoom(op.param1)

        if op.type == 21:
            ryan.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    ryan.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = ryan.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        ryan.acceptGroupInvitation(op.param1)
                        ryan.sendText(op.param1,"ᴍᴀᴀғ " + ryan.getContact(op.param2).displayName + "\nᴍᴇᴍʙᴇʀ ᴋᴜʀᴀɴɢ ᴅᴀʀɪ 30 ᴏʀᴀɴɢ\nᴜɴᴛᴜᴋ ɪɴғᴏ, sɪʟᴀʜᴋᴀɴ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴋᴀᴍɪ!")
                        ryan.leaveGroup(op.param1)                        
		    else:
                        ryan.acceptGroupInvitation(op.param1)
			ryan.sendText(op.param1,"☆『ᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ』☆\n☆『ɴᴇᴡʙɪᴇ ᴏᴍ, ᴊᴀɴɢᴀɴ ᴅɪʙᴜʟʟʏ』☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = ryan.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        ryan.rejectGroupInvitation(op.param1)
		    else:
                        ryan.acceptGroupInvitation(op.param1)
			ryan.sendText(op.param1,"☆『ᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ』☆\n☆『ɴᴇᴡʙɪᴇ ᴏᴍ, ᴊᴀɴɢᴀɴ ᴅɪʙᴜʟʟʏ』☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        ryan.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			ryan.cancelGroupInvitation(op.param1, [op.param3])
			ryan.sendText(op.param1, "ʙʟᴀᴄᴋʟɪsᴛ ᴅᴇᴛᴇᴄᴛᴇᴅ")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    ryan.cancelGroupInvitation(op.param1,[op.param3])
                    ryan.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass
                            
                elif wait["cancelprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    ryan.cancelGroupInvitation(op.param1,[op.param3])
                    ryan.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass
  
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               ryan.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    ryan.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        ryan.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ryan.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        ryan.kickoutFromGroup(op.param1,[op.param2])
			ryan.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    ryan.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ryan.kickoutFromGroup(op.param1,[op.param2])
			ryan.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                ryan.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ryan.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    ryan.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    ryan.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = ryan.getGroup(op.param1)
            contact = ryan.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            ryan.sendText(op.param1,"ʜᴀʟʟᴏ " + ryan.getContact(op.param2).displayName + "\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ☞ " + str(ginfo.name) + " ☜" + "\nʙᴜᴅᴀʏᴀᴋᴀɴ ᴄᴇᴋ ɴᴏᴛᴇ\nᴅᴀɴ sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ᴅɪsɪɴɪ ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ryan.sendMessage(c)  
            ryan.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "16457609",
                                    "STKPKGID": "8479",
                                    "STKVER": "3" }                
            ryan.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ryan.sendText(op.param1,"ɢᴏᴏᴅ ʙʏᴇ " + ryan.getContact(op.param2).displayName +  "\nsᴇᴇ ʏᴏᴜ ɴᴇxᴛ ᴛɪᴍᴇ . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "16457619",
                                    "STKPKGID": "8479",
                                    "STKVER": "3" }                
            ryan.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			ryan.kickoutFromGroup(op.param1,[op.param2])
			G = ryan.getGroup(op.param1)
			G.preventJoinByTicket = True
			ryan.updateGroup(G)
#			ryan.kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    ryan.kickoutFromGroup(op.param1,[op.param2])
			    G = ryan.getGroup(op.param1)
			    G.preventJoinByTicket = True
			    ryan.updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    ryan.sendText(op.param1,"ᴡᴇʟᴄᴏᴍᴇ. ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʙᴏᴛs. ɪ ᴄᴀɴ ᴋɪᴄᴋ ʏᴏᴜ!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ryan.kickoutFromGroup(op.param1,[op.param2])
		else:
		    ryan.sendText(op.param1,"")
	    else:
		ryan.sendText(op.param1,"")
            
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ryan.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ryan.sendText(msg.to,data['result']['response'].encode('utf-8'))
                                

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = ryan.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["ɴɢᴇᴛᴀɢ ʟᴀɢɪ ʏᴀᴡʟᴏʜ " + cName + "\n! sᴏʀʀʏ, ʙʏᴇᴇ!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  ryan.sendText(msg.to,ret_)
                                  ryan.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = ryan.getContact(msg.from_)
                     cName = contact.displayName 
                     balas = [".,,"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:  
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "Reiyan,'"}
                                  ryan.sendMessage(msg)   
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = ryan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["" + cName + " ɢᴏsᴀʜ ᴛᴀɢ-ᴛᴀɢ ᴊᴇᴍʙᴏᴛᴛ !!!","ɴɢɢᴀᴋ ᴜsᴀʜ ᴛᴀɢ-ᴛᴀɢ! ᴋᴀʟᴏ ᴘᴇɴᴛɪɴɢ ʟᴀɴɢsᴜɴɢ ᴘᴄ ᴀᴊᴀ","ʏᴀᴡʟᴏʜ,, ᴊᴏɴᴇs ᴋᴀʀᴀᴛᴀɴ " + cName + " ɴɢᴇᴛᴀɢ!!","ᴇʜ ᴊᴀᴍʙᴀɴ " + cName + " ᴊᴀɴɢᴀɴ ᴛᴜɢ-ᴛᴀɢ-ᴛᴜɢ-ᴛᴀɢ ᴍᴜʟᴜ!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ryan.sendText(msg.to,ret_)
                                  rnd = ["riyan nya lagi sibuk om, kalo penting, langsung pe em link tikel nya"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  ryan.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "28785553",
                                                       "STKPKGID": "1944857",
                                                       "STKVER": "1" }
                                  ryan.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = ryan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ᴏɴᴏ ᴏᴘᴏ " + cName + " ᴍʙᴏᴛ ɴɢᴇᴛᴀɢ-ᴛᴀɢ!"]
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ryan.sendText(msg.to,ret_)
                                  ryan.sendText(msg.to,balas1)
                                  ryan.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "2754644",
                                                       "STKPKGID": "1066653",
                                                       "STKVER": "1" }
                                  ryan.sendMessage(msg)                                
                                  break  
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention4"] == True:          
                    contact = ryan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ʏᴀᴡʟᴏʜ,, ᴊᴏɴᴇs ᴋᴀʀᴀᴛᴀɴ " + cName + " ɴɢᴇᴛᴀɢ!!","ᴇʜ ᴊᴀᴍʙᴀɴ " + cName + " ᴊᴀɴɢᴀɴ ᴛᴜɢ-ᴛᴀɢ-ᴛᴜɢ-ᴛᴀɢ ᴍᴜʟᴜ!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ryan.sendText(msg.to,ret_)
                                  rnd = ["Buset si joness ngetag mulu, kalo penting langsung pe em riyan nya aja","Ni orang kerjaan nya ngetag mulu, gift tikel aja enggak pernah, suwe lu jamban"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  ryan.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "5523409",
                                                       "STKPKGID": "1135371",
                                                       "STKVER": "1" }
                                  ryan.sendMessage(msg)                                
                                  break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention5"] == True:          
                    contact = ryan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["" + cName + ", ᴊᴀᴅɪʟᴀʜ ᴊᴏɴᴇs ᴀʟᴀᴍɪ ʏᴀɴɢ ɴɢɢᴀᴋ sᴜᴋᴀ ɴɢᴇᴛᴀɢ ᴏʀᴀɴɢ ɢᴀɴᴛᴇɴɢ"]
                    balas1 = "sᴇʟғɪᴇ ᴅᴜʟᴜ ʏᴀ ᴄᴇᴛ. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ryan.sendText(msg.to,ret_)
                                  ryan.sendText(msg.to,balas1)
                                  ryan.sendImageWithURL(msg.to,image)
                                  rnd = ["Yang Jomblo Bin Haji Joness Jangan Suka Ngetag Guwa"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  ryan.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "27695299",
                                                       "STKPKGID": "1900619",
                                                       "STKVER": "1" }
                                  ryan.sendMessage(msg)                                
                                  break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention6"] == True:          
                    contact = ryan.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ᴅɪɪʜʜʜ, " + cName + " ɴɢᴛᴀɢ ᴍᴜʟᴜ!!!","ɢᴏsᴀʜ ᴛᴀɢ-ᴛᴀɢ ᴊᴇᴍʙᴏᴛᴛ " + cName + "!!!","ᴇʜ ᴊᴀᴍʙᴀɴ " + cName + " ᴊᴀɴɢᴀɴ ᴛᴜɢ-ᴛᴀɢ-ᴛᴜɢ-ᴛᴀɢ ᴍᴜʟᴜ!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ryan.sendText(msg.to,ret_)
                                  rnd = ["Elu mandi dulu sana " + cName + ", Baru Nge Tag Guwa"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  ryan.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "28785545",
                                                       "STKPKGID": "1944857",
                                                       "STKVER": "1" }
                                  ryan.sendMessage(msg)                                
                                  break
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                ryan.sendText(msg.to,"ʙᴏᴛ sᴜᴅᴀʜ ᴏɴ ᴋᴇᴍʙᴀʟɪ.")

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 sᴛɪᴄᴋᴇʀ ᴄʜᴇᴄᴋ 』\nsᴛᴋɪᴅ : %s\nsᴛᴋᴘᴋɢɪᴅ : %s\nsᴛᴋᴠᴇʀ : %s\n『 ʟɪɴᴋ 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                ryan.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    ryan.sendChatChecked(msg.from_,msg.id)
                else:
                    ryan.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     ryan.like(url[25:58], url[66:], likeType=1005)
                     ryan.comment(url[25:58], url[66:], wait["comment"])
                     ryan.sendText(msg.to,"『sᴜᴄᴄᴇss ʟɪᴋᴇ』")                     
                     wait['likeOn'] = True


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            ryan.sendText(msg.to,"sᴜᴅᴀʜ")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            ryan.sendText(msg.to,"ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ")
		    else:
			ryan.sendText(msg.to,"ᴀᴅᴍɪɴ ᴅᴇᴛᴇᴄᴛᴇᴅ~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ryan.sendText(msg.to,"ᴛᴇʀʜᴀᴘᴜs")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        ryan.sendText(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋ ʟɪsᴛ")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     ryan.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = ryan.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = ryan.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         ryan.sendText(msg.to,"ɴᴀᴍᴀ:\n" + msg.contentMetadata["displayName"] + "\n\nᴍɪᴅ:\n" + msg.contentMetadata["mid"] + "\n\nsᴛᴀᴛᴜs:\n" + contact.statusMessage + "\n\nᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nᴘʜᴏᴛᴏ ᴄᴏᴠᴇʀ:\n" + str(cu))
                     else:
                         contact = ryan.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = ryan.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         ryan.sendText(msg.to,"ɴᴀᴍᴀ:\n" + msg.contentMetadata["displayName"] + "\n\nᴍɪᴅ:\n" + msg.contentMetadata["mid"] + "\n\nsᴛᴀᴛᴜs:\n" + contact.statusMessage + "\n\nᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nᴘʜᴏᴛᴏ ᴄᴏᴠᴇʀ:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ryan.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ryan.sendText(msg.to,"[ɢʀᴏᴜᴘ ɴᴀᴍᴇ]\n" + str(ginfo.name) + "\n\n[ɢɪᴅ]\n" + msg.to + "\n\n[ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ]\n" + gCreator + "\n\n[ᴘʀᴏғɪʟᴇ sᴛᴀᴛᴜs]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMᴇᴍʙᴇʀs:" + str(len(ginfo.members)) + "ᴍᴇᴍʙᴇʀs\nᴘᴇɴᴅɪɴɢ:" + sinvitee + "ᴘᴇᴏᴘʟᴇ\nᴜʀʟ:" + u + "ɪᴛ ɪs ɪɴsɪᴅᴇ")
                    else:
                        ryan.sendText(msg.to,"[ɢʀᴏᴜᴘ ɴᴀᴍᴇ]\n" + str(ginfo.name) + "\n[ɢɪᴅ]\n" + msg.to + "\n[ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ]\n" + gCreator + "\n[ᴘʀᴏғɪʟᴇ sᴛᴀᴛᴜs]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴄᴀɴ ɴᴏᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ")
                    else:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                ryan.sendText(msg.to,"●▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬●")
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uf9769adcf23329d9caedcd850f6caea8'}
                ryan.sendMessage(msg)
		ryan.sendText(msg.to,"●▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬●")
		ryan.sendText(msg.to,"I҈ t҈ u҈  M҈ a҈ j҈ i҈ k҈ a҈ n҈  K҈ a҈ m҈ i҈  (^_^)")
 
                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "ᴘᴏsᴛ ᴜʀʟ\n" + msg.contentMetadata["postEndUrl"]
                    ryan.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ryan.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ryan.findAndAddContactsByMid(target)
                                contact = ryan.getContact(target)
                                cu = ryan.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                ryan.sendText(msg.to,"ɴᴀᴍᴀ :\n" + contact.displayName + "\n\nᴍɪᴅ :\n" + msg.contentMetadata["mid"] + "\n\nʙɪᴏ :\n" + contact.statusMessage)
                                ryan.sendText(msg.to,"ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ " + contact.displayName)
                                ryan.sendImageWithURL(msg.to,image)
                                ryan.sendText(msg.to,"ᴄᴏᴠᴇʀ " + contact.displayName)
                                ryan.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ryan.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ryan.sendText(msg.to,"ɢ҈ ɪ҈ ғ҈ ᴛ҈  ҈ s҈ ᴜ҈ ᴅ҈ ᴀ҈ ʜ҈  ҈ ᴛ҈ ᴇ҈ ʀ҈ ᴋ҈ ɪ҈ ʀ҈ ɪ҈ ᴍ҈ !")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                ryan.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ryan.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        ryan.sendText(msg.to, "ɴᴏᴛ ғᴏᴜɴᴅ...")
                        pass
                    else:
                        for target in targets:
                            try:
                                ryan.CloneContactProfile(target)
                                ryan.sendText(msg.to, "ᴄᴏᴘɪᴇᴅ (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = ryan.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ryan.sendText(msg.to, _name + " ʙᴇʀᴀᴅᴀ ᴅɪɢʀᴜᴘ ɪɴɪ")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ryan.findAndAddContactsByMid(target)
                                 ryan.inviteIntoGroup(msg.to,[target])
                                 ryan.sendText(msg.to,"ɪɴᴠɪᴛᴇ " + _name)
                                 wait['invite'] = True
                                 break                              
                             except:             
                                      ryan.sendText(msg.to,"ʟɪᴍɪᴛ ɪɴᴠɪᴛᴇ")
                                      wait['invite'] = False
                                      break
                                  
 
         #   elif msg.text in ["Key creator","help creator","Help creator"]:
          #      ryan.sendText(msg.to,creatorMessage)

        #    elif msg.text in ["Key group","help group","Help group"]:
         #       ryan.sendText(msg.to,groupMessage)

            elif msg.text in ["Kasih help","help","Help"]:
                ryan.sendText(msg.to,helpMessage)
                ryan.sendText(msg.to,"〚ᴅ̰ɪ̰ʟ̰ᴀ̰ʀ̰ᴀ̰ɴ̰ɢ̰ ̰ᴛ̰ʏ̰ᴘ̰ᴏ̰ ̰ᴛ̰ᴀ̰ɴ̰ᴘ̰ᴀ̰ ̰ɪ̰ᴢ̰ɪ̰ɴ̰ ̰ᴅ̰ᴀ̰ʀ̰ɪ̰ ̰ᴏ̰ᴡ̰ɴ̰ᴇ̰ʀ̰〛")

            elif msg.text in ["Ryan key","Ryan help","ryan key"]:
                ryan.sendText(msg.to,ryanMessage)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uf9769adcf23329d9caedcd850f6caea8'}
                ryan.sendMessage(msg)

        #    elif msg.text in ["Key bot","help bot","Help bot"]:
         #       ryan.sendText(msg.to,botMessage)

         #   elif msg.text in ["Key set","help set","Help set"]:
             #   ryan.sendText(msg.to,setMessage)

        #    elif msg.text in ["Key media","help media","Help media"]:
         #       ryan.sendText(msg.to,mediaMessage)
                
         #   elif msg.text in ["Key admin","help admin","Help admin"]:
           #     ryan.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = ryan.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = ryan.getGroup(i).name
                        h += "🚩【%s】\n" % (gn)
		        jml += 1
                    ryan.sendText(msg.to,"=======[ʟɪsᴛ ɢʀᴏᴜᴘ]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = ryan.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = ryan.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    ryan.sendText(msg.to, "sᴜᴄᴄᴇss ʙᴀɴ ɢʀᴏᴜᴘ : "+grp)
			else:
			    pass
		else:
		    ryan.sendText(msg.to, "K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        ryan.sendText(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +ryan.getGroup(gid).name + "\n"
                        ryan.sendText(msg.to,"===[ʙᴀɴ ɢʀᴏᴜᴘ]===\n"+mc)
		else:
		    ryan.sendText(msg.to, "K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if ryan.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    ryan.sendText(msg.to, "sᴜᴄᴄᴇss ᴅᴇʟ ʙᴀɴ "+ng)
		        else:
			    pass
		else:
		    ryan.sendText(msg.to, "K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = ryan.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = ryan.getGroup(i).name
		            if h == ng:
		                ryan.inviteIntoGroup(i,[Creator])
			        ryan.sendText(msg.to,"sᴜᴄᴄᴇss ᴊᴏɪɴ ᴛᴏ ["+ h +"] ɢʀᴏᴜᴘ")
			    else:
			        pass
		    else:
		        ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
		except Exception as e:
		    ryan.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = ryan.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = ryan.getGroup(i).name
		        if h == ng:
			    ryan.sendText(i,"ʙᴏᴛ ᴅɪ ᴘᴀᴋsᴀ ᴋᴇʟᴜᴀʀ ᴏʟᴇʜ ᴏᴡɴᴇʀ!")
		            ryan.leaveGroup(i)
			    ryan.sendText(msg.to,"sᴜᴄᴄᴇss ʟᴇғᴛ ["+ h +"] ɢʀᴏᴜᴘ")
			else:
			    pass
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
 
	    elif "Leave all group" == msg.text:
		gid = ryan.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			ryan.sendText(i,"ʙᴏᴛ ᴅɪ ᴘᴀᴋsᴀ ᴋᴇʟᴜᴀʀ ᴏʟᴇʜ ᴏᴡɴᴇʀ!")
		        ryan.leaveGroup(i)
		    ryan.sendText(msg.to,"sᴜᴄᴄᴇss ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = ryan.getGroupIdsJoined()
                for i in gid:
                    h = ryan.getGroup(i).name
                    gna = ryan.getGroup(i)
                    if h == saya:
                        ryan.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
                    
            elif 'clear:inv' in msg.text.lower():
                if msg.toType == 2:
                    group = ryan.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ryan.cancelGroupInvitation(msg.to,[_mid])
                    else:
                        ryan.sendText(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴅɪɴɢ.")
                else:
                    ryan.sendText(msg.to,"ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪʟᴜᴀʀ ɢʀᴏᴜᴘ")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = ryan.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ryan.updateGroup(X)
                    ryan.sendText(msg.to,"ᴜʀʟ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
                else:
                    ryan.sendText(msg.to,"C҉ a҉ n҉  n҉ o҉ t҉  b҉ e҉  u҉ s҉ e҉ d҉  o҉ u҉ t҉ s҉ i҉ d҉ e҉  t҉ h҉ e҉  g҉ r҉ o҉ u҉ p҉ ")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = ryan.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ryan.updateGroup(X)
                    ryan.sendText(msg.to,"ᴜʀʟ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                else:
                    ryan.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
		    
            elif msg.text in ["Leave on","Autoleave on"]:
		if msg.from_ in admin:
                    wait["LeaveRoom"] = True
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Leave off","Autoleave off"]:
		if msg.from_ in admin:
                    wait["LeaveRoom"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")		    
		    
 
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ1 sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ1 sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
		
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ2 sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ2 sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
		
            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ3 sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    ryan.sendText(msg.to,"Aᴀᴜᴛᴏ ʀᴇsᴘᴏɴ3 sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
		
            elif msg.text in ["Respon4 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = True
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ4 sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Respon4 off"]:
		if msg.from_ in admin:
                    wait["detectMention4"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ4 sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
		
            elif msg.text in ["Respon5 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = True
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ5 sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Respon5 off"]:
		if msg.from_ in admin:
                    wait["detectMention5"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ5 sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
	
            elif msg.text in ["Respon6 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = True
                    wait["kickMention"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ6 sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Respon6 off"]:
		if msg.from_ in admin:
                    wait["detectMention6"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ6 sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
		
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
		
            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False  
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    ryan.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ sᴜᴅᴀʜ ᴏғғ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		print wait["AutoCancel"]
	     else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
		print wait["AutoCancel"]
	     else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                ryan.sendText(msg.to,"ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
		print wait["inviteprotect"]
	     else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                ryan.sendText(msg.to,"ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
		print wait["inviteprotect"]
	     else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")		    
		
		    
	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	ryan.sendText(msg.to,"ϙʀ ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
	     else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	ryan.sendText(msg.to,"ϙʀ ᴘʀᴏᴛᴇᴄᴛ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
	     else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
	     else:
	        ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
	     else:
	        ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["protect"] = True
                    wait["cancelprotect"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    ryan.sendText(msg.to,"sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["protect"] = False
                    wait["cancelprotect"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    ryan.sendText(msg.to,"sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ ᴛᴇʟᴀʜ ᴅɪ ɴᴏɴ-ᴀᴋᴛɪғᴋᴀɴ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                ryan.sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                ryan.sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                ryan.sendText(msg.to,"ᴀʟᴡᴀʏs ʀᴇᴀᴅ sᴜᴅᴀʜ ᴀᴋᴛɪғ")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                ryan.sendText(msg.to,"ᴀʟᴡᴀʏs ʀᴇᴀᴅ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")                


            elif msg.text in ["Notif on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"sᴀᴍʙᴜᴛᴀɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"sᴜᴅᴀʜ ᴏɴヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"sᴀᴍʙᴜᴛᴀɴ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"sᴜᴅᴀʜ ᴏғғ(p′︵‵。)")

            elif "Buru sider" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ryan.sendText(msg.to,"sɪᴀᴘ ʙᴇʀʙᴜʀᴜ sɪᴅᴇʀ")

            elif "BS off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    ryan.sendText(msg.to, "ʏᴀɴɢ sɪᴅᴇʀ ᴜᴅᴀʜ ᴘᴀᴅᴀ ᴋᴀʙᴜʀ(ᴏғғ)")
                else:
                    ryan.sendText(msg.to, "ʜᴇʜ ʙᴇʟᴏᴍ ᴅɪ sᴇᴛ")

            elif msg.text in ["Set"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠🔐sᴀᴍʙᴜᴛᴀɴ : 📱ᴏɴ\n"
		else:md+="╠🔐sᴀᴍʙᴜᴛᴀɴ : 📴ᴏғғ\n"
		if wait["likeOn"] == True: md+="╠🔐ᴀᴜᴛᴏ ʟɪᴋᴇ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʟɪᴋᴇ : 📴ᴏғғ\n"
		if wait["autoAdd"] == True: md+="╠🔐ᴀᴜᴛᴏ ᴀᴅᴅ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ᴀᴅᴅ : 📴ᴏғғ\n"
		if wait["LeaveRoom"] == True: md+="╠🔐ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ : 📴ᴏғғ\n"
		if wait["AutoJoin"] == True: md+="╠🔐ᴀᴜᴛᴏ ᴊᴏɪɴ : 📱ᴏɴ\n"
                else: md +="╠🔐ᴀᴜᴛᴏ ᴊᴏɪɴ : 📴ᴏғғ\n"
		if wait["AutoJoinCancel"] == True: md+="╠🔐ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ : 📱ᴏɴ\n"
                else: md +="╠🔐ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ : 📴ᴏғғ\n"                
		if wait["Contact"] == True: md+="╠🔐ɪɴғᴏ ᴄᴏɴᴛᴀᴄᴛ : 📱ᴏɴ\n"
		else: md+="╠🔐ɪɴғᴏ ᴄᴏɴᴛᴀᴄᴛ : 📴ᴏғғ\n"
                if wait["AutoCancel"] == True:md+="╠🔐ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ : 📱ᴏɴ\n"
                else: md+= "╠🔐ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ : 📴ᴏғғ\n"
                if wait["inviteprotect"] == True:md+="╠🔐ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ : 📱ᴏɴ\n"
                else: md+= "╠🔐ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ : 📴ᴏғғ\n"                
		if wait["Qr"] == True: md+="╠🔐ϙʀ ᴘʀᴏᴛᴇᴄᴛ : 📱ᴏɴ\n"
		else:md+="╠🔐ϙʀ ᴘʀᴏᴛᴇᴄᴛ : 📴ᴏғғ\n"
		if wait["AutoKick"] == True: md+="╠🔐ᴀᴜᴛᴏ ᴋɪᴄᴋ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ᴋɪᴄᴋ : 📴ᴏғғ\n"
		if wait["cancelprotect"] == True: md+="╠🔐ᴄᴀɴᴄᴇʟ ᴘʀᴏᴛᴇᴄᴛ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴄᴀɴᴄᴇʟ ᴘʀᴏᴛᴇᴄᴛ : 📴ᴏғғ\n"
		if wait["protect"] == True: md+="╠🔐ᴘʀᴏᴛᴇᴄᴛ ᴍᴏᴅᴇ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴘʀᴏᴛᴇᴄᴛ ᴍᴏᴅᴇ : 📴ᴏғғ\n"
		if wait["alwaysRead"] == True: md+="╠🔐ᴀʟᴡᴀʏs ʀᴇᴀᴅ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀʟᴡᴀʏs ʀᴇᴀᴅ: 📴ᴏғғ\n"
		if wait["detectMention"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ1 : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ1 : 📴ᴏғғ\n"		
		if wait["detectMention2"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ2 : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ2 : 📴ᴏғғ\n"	
		if wait["detectMention3"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ3 : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ3 : 📴ᴏғғ\n"	
		if wait["detectMention4"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ4 : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ4 : 📴ᴏғғ\n"		
		if wait["detectMention5"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ5 : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ5 : 📴ᴏғғ\n"		
		if wait["detectMention6"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ6 : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ6 : 📴ᴏғғ\n"		
		if wait["kickMention"] == True: md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ : 📴ᴏғғ\n"				
		if wait["Sider"] == True: md+="╠🔐ᴀᴜᴛᴏ sɪᴅᴇʀ : 📱ᴏɴ\n"
		else:md+="╠🔐ᴀᴜᴛᴏ sɪᴅᴇʀ: 📴ᴏғғ\n"	
		if wait["Simi"] == True: md+="╠🔐sɪᴍɪsɪᴍɪ : 📱ᴏɴ\n"
		else:md+="╠🔐sɪᴍɪsɪᴍɪ: 📴ᴏғғ\n"		
                ryan.sendText(msg.to,"╔════════════════════╗\n""║  ☆☞R҈ e҈ y҈ P҈ r҈ o҈  S҈ e҈ t҈ t҈ i҈ n҈ g҈ ☜☆\n""╠════════════════════╣\n"+md+"╠════════════════════╣\n║̶ᴘ̶̶ʀ̶̶ᴏ̶̶ᴛ̶̶ᴇ̶̶ᴄ̶̶ᴛ̶̶ ̶̶ᵇ̶̶ᵒ̶̶ᵗ̶̶ ̶̶ᴛ̶̶ʀ̶̶ᴏ̶̶ᴏ̶̶ᴘ̶̶s̶̶ ̶̶ᶠ̶̶ʳ̶̶ᵒ̶̶ᵐ̶̶ ̶̶s̶̶ɪ̶̶ʟ̶̶ᴇ̶̶ɴ̶̶ᴛ̶̶ ̶̶ᵏ̶̶ⁱ̶̶ˡ̶̶ˡ̶\n╚════════════════════╝")
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uf9769adcf23329d9caedcd850f6caea8'}
                ryan.sendMessage(msg)
                rnd = ["Di Atas Adalah Setting Untuk Mengatur Bot Anda, Silahkan Aktifkan Settingan Yang Sesuai Dengan Kebutuhan Anda"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")

            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ryan.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + " ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ryan.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ryan.sendText(msg.to,_name + "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢɪғᴛ")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    ryan.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5523427',
                                    'STKPKGID': '1135371',
                                    'STKVER': '1'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)
                
            elif msg.text.lower() in ["owh","walaahh","bahhh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '27695299',
                                    'STKPKGID': '1900619',
                                    'STKVER': '1'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '20470227',
                                    'STKPKGID': '1604391',
                                    'STKVER': '1'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5523426',
                                    'STKPKGID': '1135371',
                                    'STKVER': '1'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = ryan.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 ryan.sendMessage(cnt)
                 
            elif "anu" == msg.text.lower():
                 group = ryan.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 ryan.sendMessage(cnt)                 


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                ryan.sendText(msg.to, "☆ᴄʜᴇᴄᴋᴘᴏɪɴᴛ ᴄʜᴇᴄᴋᴇᴅ☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = ryan.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════\n║       ☆☞ ʟɪsᴛ ᴠɪᴇᴡᴇʀs ☜☆\n╠═════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════"
                        ryan.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        ryan.sendText(msg.to, "☆ᴀᴜᴛᴏ ᴄʜᴇᴄᴋᴘᴏɪɴᴛ☆")                        
                    else:
                        ryan.sendText(msg.to, "☆ʙᴇʟᴜᴍ ᴀᴅᴀ ᴠɪᴇᴡᴇʀs☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ryan.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    ryan.sendText(msg.to, "ᴊᴜᴍʟᴀʜ ᴍɪɴɪᴍᴀʟ ᴍᴇᴍʙᴇʀ ᴛᴇʟᴀʜ ᴅɪ sᴇᴛ : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = ryan.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    ryan.findAndAddContactsByMids(mi_d)
		    ryan.sendText(msg.to,"sᴜᴄᴄᴇss ᴀᴅᴅ ᴀʟʟ")


            elif msg.text in ["Invite on"]:
                wait["invite"] = True
                ryan.sendText(msg.to,"ɪɴᴠɪᴛᴇ ʙʏ ᴄᴏɴᴛᴀᴄᴛ sᴇᴛ ᴛᴏ ᴏɴ")
                
            elif msg.text in ["Invite off"]:
                wait["invite"] = False
                ryan.sendText(msg.to,"ɪɴᴠɪᴛᴇ ʙʏ ᴄᴏɴᴛᴀᴄᴛ ᴀʟʀᴇᴀᴅʏ ᴏғғ")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                ryan.sendText(msg.to,"『ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅɪᴀᴋᴛɪғᴋᴀɴ』")
                
                
            elif msg.text in ["Like off"]:
                wait["likeOn"] = False
                ryan.sendText(msg.to,"『ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅɪɴᴏɴ-ᴀᴋᴛɪғᴋᴀɴ』")


            elif msg.text in ["'Steal contact"]:
                wait["steal"] = True
                ryan.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                ryan.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                ryan.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                ryan.sendText(msg.to,"sᴛɪᴄᴋᴇʀ ɪᴅ ᴅᴇᴛᴇᴄᴛ ᴀʟʀᴇᴀᴅʏ ᴏɴ.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                ryan.sendText(msg.to,"ʙᴏᴛ sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ.")  

	    elif "Recover" in msg.text:
		thisgroup = ryan.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		ryan.createGroup("ʀᴇᴄᴏᴠᴇʀ", mi_d)
		ryan.sendText(msg.to,"sᴜᴄᴄᴇss ʀᴇᴄᴏᴠᴇʀ")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = ryan.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    ryan.updateGroup(X)
                else:
                    ryan.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    ryan.kickoutFromGroup(msg.to,[midd])
		else:
		    ryan.sendText(msg.to,"ᴀᴅᴍɪɴ ᴅᴇᴛᴇᴄᴛᴇᴅ")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                ryan.findAndAddContactsByMid(midd)
                ryan.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "uf9769adcf23329d9caedcd850f6caea8"
                ryan.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = ryan.getGroup(msg.to)
                ryan.sendText(msg.to,"sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                ryan.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = ryan.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			ryan.sendText(i,"=======[ʙʀᴏᴀᴅᴄᴀsᴛ]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~s.k.9.7")
		    ryan.sendText(msg.to,"sᴜᴄᴄᴇss ʙᴄ ʙᴏsϙ")
		else:
		    ryan.sendText(msg.to,"K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")

            elif msg.text in ["Cancel"]:
                gid = ryan.getGroupIdsInvited()
                for i in gid:
                    ryan.rejectGroupInvitation(i)
                ryan.sendText(msg.to,"ᴀʟʟ ɪɴᴠɪᴛᴀᴛɪᴏɴs ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇғᴜsᴇᴅ")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = ryan.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ryan.updateGroup(x)
                    gurl = ryan.reissueGroupTicket(msg.to)
                    ryan.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ")
                    else:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")


            elif msg.text in ["timeline"]:
		try:
                    url = ryan.activity(limit=5)
		    ryan.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    ryan.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		ryan.sendText(msg.to,"ʜᴀᴅɪʀ!!!")


            elif msg.text.lower() in ["respon"]:
                ryan.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		ryan.sendText(msg.to, "ᴘʀᴏɢʀᴇss...")
                ryan.sendText(msg.to, "%ssᴇᴄᴏɴᴅs" % (elapsed_time))
                
            elif msg.text in ["Xp","Speed test"]:
                start = time.time()
                ryan.sendText(msg.to, "ᴡᴀɪᴛɪɴɢ...")
                elapsed_time = time.time() - start
                ryan.sendText(msg.to, "%sᴅᴇᴛɪᴋ" % (elapsed_time))                
                
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ryan.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    ryan.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ryan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ryan.sendText(msg.to,"sᴜᴄᴄᴇs ʙᴏsϙ")
                                except:
                                    ryan.sendText(msg.to,"Error")
			    else:
				ryan.sendText(msg.to,"ᴀᴅᴍɪɴ ᴅᴇᴛᴇᴄᴛᴇᴅ~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    ryan.sendText(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ryan.getContact(mi_d).displayName + "\n"
                    ryan.sendText(msg.to,"===[ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ryan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ryan.sendText(msg.to,"sᴜᴄᴄᴇs ʙᴏsϙ")
                            except:
                                ryan.sendText(msg.to,"sᴜᴄᴄᴇs ʙᴏsϙ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    ryan.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉ᴜɴʙᴀɴɴᴇᴅ ᴀʟʟ sᴜᴄᴄᴇss❉ ┐") 

            elif msg.text.lower() == 'cancelpro on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴄᴀɴᴄᴇʟ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ🔓✍")
                    else:
                        ryan.sendText(msg.to,"ʜᴀʟ ɪɴɪ sᴜᴅᴀʜ ᴛᴇʀʙᴜᴋᴀ ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ✍")
                    else:
                        ryan.sendText(msg.to,"ɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴏɴ ô€¨")
                        
            elif msg.text.lower() == 'cancelpro off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴄᴀɴᴄᴇʟ ᴘʀᴏᴛᴇᴄᴛ ᴏғғ🔓✍")
                    else:
                        ryan.sendText(msg.to,"ʜᴀʟ ɪɴɪ sᴜᴅᴀʜ ᴛᴇʀʙᴜᴋᴀ ô€¨👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ✍")
                    else:
                        ryan.sendText(msg.to,"ɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴏғғ ô€¨")
                        
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ🔓✍")
                    else:
                        ryan.sendText(msg.to,"ʜᴀʟ ɪɴɪ sᴜᴅᴀʜ ᴛᴇʀʙᴜᴋᴀ 🔓✍")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ🔓✍")
                    else:
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ🔓✍")
                        
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏғғ🔓✍")
                    else:
                        ryan.sendText(msg.to,"ʜᴀʟ ɪɴɪ sᴜᴅᴀʜ ᴛᴇʀʙᴜᴋᴀ 🔓✍")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏғғ🔓✍")
                    else:
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏғғ🔓✍")
 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ryan.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ryan.sendText(msg.to,"ᴛʜᴇʀᴇ ᴡᴀs ɴᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                            return
                        for jj in matched_list:
                            ryan.kickoutFromGroup(msg.to,[jj])
                        ryan.sendText(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ ᴇᴍᴀɴɢ ᴘᴀɴᴛᴀs ᴛᴜᴋ ᴅɪ ᴜsɪʀ")
		else:
		    ryan.sendText(msg.to, "K҈ h҈ u҈ s҈ u҈ s҈  R҈ y҈ a҈ n҈ ")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = ryan.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ryan.sendText(msg.to,"ғᴜᴄᴋ ʏᴏᴜ")
                            return
                        for jj in matched_list:
                            try:
                                ryan.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
                                
 
            elif "Ratain" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Ratain","")
                        gs = ryan.getGroup(msg.to)
                        ryan.sendText(msg.to,"ᴍɪsɪ~ᴍɪsɪ")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        ryan.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        ryan.sendText(msg.to,str(e))
			    ryan.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    ryan.sendText(msg.to, "ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛᴇᴅ...")
		    restart_program()
		    print "@Restart"
		else:
		    ryan.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Blank' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Reiyan,'"}
                ryan.sendMessage(msg)

 
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ryan.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ryan.sendText(msg.to, "ɴᴏᴛ ғᴏᴜɴᴅ...")
                   else:
                       for target in targets:
                            try:
                               ryan.CloneContactProfile(target)
                               ryan.sendText(msg.to, "ᴄᴏᴘɪᴇᴅ (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    ryan.updateDisplayPicture(backup1.pictureStatus)
                    ryan.updateProfile(backup1)
                    ryan.sendText(msg.to, "ᴅᴏɴᴇ (^_^)")
                except Exception as e:
                    ryan.sendText(msg.to, str(e))

 
	    elif "musik " in msg.text:
					songname = msg.text.replace("musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						ryan.sendText(msg.to, "ᴛɪᴛʟᴇ : " + song[0] + "\nʟᴇɴɢᴛʜ : " + song[1] + "\nʟɪɴᴋ ᴅᴏᴡɴʟᴏᴀᴅ : " + song[4])
						ryan.sendText(msg.to, "ʟᴀɢᴜ " + song[0] + "\nsᴇᴅᴀɴɢ ᴅɪ ᴘʀᴏssᴇs... ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ ^_^ ")
						ryan.sendAudioWithURL(msg.to,abc)
						ryan.sendText(msg.to, "sᴇʟᴀᴍᴀᴛ ᴍᴇɴᴅᴇɴɢᴀʀᴋᴀɴ ʟᴀɢᴜ " + song[0])
	
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ryan.sendText(msg.to, hasil)
                except Exception as wak:
                        ryan.sendText(msg.to, str(wak))
                        
	    elif "musrik " in msg.text:
					songname = msg.text.replace("musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						ryan.sendText(msg.to, "ʟᴀɢᴜ " + song[0] + "\nsᴇᴅᴀɴɢ ᴅɪ ᴘʀᴏssᴇs... ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ ^_^ ")
						ryan.sendAudioWithURL(msg.to,abc)
						ryan.sendText(msg.to, "ᴛɪᴛʟᴇ : " + song[0] + "\nʟᴇɴɢᴛʜ : " + song[1] + "\nʟɪɴᴋ ᴅᴏᴡɴʟᴏᴀᴅ : " + song[4] +"\n\n" + hasil)
						ryan.sendText(msg.to, "sᴇʟᴀᴍᴀᴛ ᴍᴇɴᴅᴇɴɢᴀʀᴋᴀɴ ʟᴀɢᴜ " + song[0])
             
            
            
            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    ryan.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ryan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                h = ryan.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                ryan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                ryan.sendText(msg.to,"ᴜᴘʟᴏᴀᴅ ɪᴍᴀɢᴇ ғᴀɪʟᴇᴅ.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ryan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                h = ryan.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                ryan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                ryan.sendText(msg.to,"ᴜᴘʟᴏᴀᴅ ɪᴍᴀɢᴇ ғᴀɪʟᴇᴅ.")
                                
            elif "Changepict" in msg.text:
                if msg.from_ in admin:
                    path = "ryan.jpg"
                    ryan.sendText(msg.to,"ᴜᴘᴅᴀᴛᴇ ᴘᴘ :")
                    ryan.sendImage(msg.to,path)
                    ryan.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ryan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                h = ryan.getContact(target)
                                ryan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                ryan.sendText(msg.to,"ᴜᴘʟᴏᴀᴅ ɪᴍᴀɢᴇ ғᴀɪʟᴇᴅ.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ryan.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ryan.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                h = ryan.getContact(target)
                                ryan.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                ryan.sendText(msg.to,"ᴜᴘʟᴏᴀᴅ ɪᴍᴀɢᴇ ғᴀɪʟᴇᴅ.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0homsmjSOgMEJOFByXm4dPFXJRPi85OjYKNiV6LTgTbndqcXZHIHArcD4cbHc3dHZEeiZ4LT8dbnU2"]
                                pilih = random.choice(link)
                                ryan.sendImageWithURL(msg.to,pilih)

 
            elif "Nspam: " in msg.text:
                  bctxt = msg.text.replace("Nspam: ", "")
                  t = 15
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 50
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam1: " in msg.text:
                  bctxt = msg.text.replace("Spam1: ", "")
                  t = 100
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam2: " in msg.text:
                  bctxt = msg.text.replace("Spam2: ", "")
                  t = 200
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam3: " in msg.text:
                  bctxt = msg.text.replace("Spam3: ", "")
                  t = 300
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam4: " in msg.text:
                  bctxt = msg.text.replace("Spam4: ", "")
                  t = 400
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam5: " in msg.text:
                  bctxt = msg.text.replace("Spam5: ", "")
                  t = 500
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "GhostSpam: " in msg.text:
                  bctxt = msg.text.replace("GhostSpam: ", "")
                  t = 1000
                  while(t):
                    ryan.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = ryan.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      ryan.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = ryan.getAllContactIds()
                  for manusia in orang:
                    ryan.sendText(manusia, (broadcasttxt))

 
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========ɪɴsᴛᴀɢʀᴀᴍ ɪɴғᴏ ========\n"
                    details = "\n========ɪɴsᴛᴀɢʀᴀᴍ ɪɴғᴏ ========"
                    ryan.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ryan.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	ryan.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                ryan.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                ryan.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ryan.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    ryan.sendText(msg.to,"ᴄᴏᴜʟᴅ ɴᴏᴛ ғɪɴᴅ ɪᴛ")
                    
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ryan.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        ryan.sendText(msg.to, "ᴄᴏᴜʟᴅ ɴᴏᴛ ғɪɴᴅ ɪᴛ")                    

 
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = ryan.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")
                
            elif "lurk on" == msg.text.lower():
               if msg.from_ in admin:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         ryan.sendText(msg.to,"ʟᴜʀᴋɪɴɢ ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     ryan.sendText(msg.to, "sᴇᴛ ᴛʜᴇ ʟᴀsᴛsᴇᴇɴs' ᴘᴏɪɴᴛ (｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2


            elif "lurk off" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to not in wait2['readPoint']:
                    ryan.sendText(msg.to,"ʟᴜʀᴋɪɴɢ ᴀʟʀᴇᴀᴅʏ ᴏғғ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    ryan.sendText(msg.to, "ᴅᴇʟᴇᴛᴇ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ:\n" + datetime.now().strftime('%H:%M:%S'))



                    
            elif "lurkers" == msg.text.lower():
            	if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             ryan.sendText(msg.to, "ʟᴜʀᴋᴇʀs:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = ryan.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+ "@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          ryan.sendMessage(msg)
                          ryan.sendText(msg.to, "ᴊɪᴋᴀ sᴜᴅᴀʜ ʟɪʜᴀᴛ sɪᴅᴇʀ ᴘʟᴇᴀsᴇ\nᴛᴜʟɪs ʟᴜʀᴋ ᴏɴ ʟᴀɢɪ ᴋᴀᴋ  (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        ryan.sendText(msg.to, "ʟᴜʀᴋɪɴɢ ʜᴀs ɴᴏᴛ ʙᴇᴇɴ sᴇᴛ (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))    


            elif msg.text.lower() in ["Sayang","sayank","yang","yank"]:
                    beb = "Pala lue peank Jamban 😜 " +ryan.getContact(msg.from_).displayName + " 😒"
                    ryan.sendText(msg.to,beb)        

            elif msg.text.lower() == 'autoadd on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
                    else:
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴀᴋᴛɪғ")
                    else:
                        ryan.sendText(msg.to,"Auto Add Sudah Aktif")
            elif msg.text.lower() == 'autoadd off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴏғғ")
                    else:
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴏғғ")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴏғғ")
                    else:
                        ryan.sendText(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ sᴜᴅᴀʜ ᴏғғ")
		

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = ryan.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                ryan.sendMessage(msg)
		ryan.sendText(msg.to,"ɪᴛᴜ ʏᴀɴɢ ʙᴜᴀᴛ ɢʀᴜᴘ ɪɴɪ")


            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                ryan.sendText(msg.to,"sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ...")
                ryan.sendText(msg.to,"ᴛɪᴛʟᴇ : "+tob+"\nsᴏᴜʀᴄᴇ : ɢᴏᴏɢʟᴇ ᴘʟᴀʏ\nʟɪɴᴋ : https://play.google.com/store/search?q=" + tob)
                ryan.sendText(msg.to,"ᴛᴜʜ ʟɪɴᴋɴʏᴀ ᴋᴀᴋ (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = ryan.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ryan.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = ryan.getProfile()
                        profile.statusMessage = string
                        ryan.updateProfile(profile)
                        ryan.sendText(msg.to,"ᴅᴏɴᴇ")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ryan.getProfile()
                        profile.displayName = string
                        ryan.updateProfile(profile)
                        ryan.sendText(msg.to,"ᴅᴏɴᴇ")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "ɴᴀᴍᴇ : " +ryan.getContact(msg.from_).displayName + "\nᴍɪᴅ : " +msg.from_
                ryan.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ryan.sendMessage(msg)

            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")
                
            elif "dimana " in msg.text:
                apk = msg.text.replace("dimana ","")
                rnd = ["Di Jonggol","Di Anu","Di Dasar Samudra","Di Perempatan"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")
                
            elif "dimanakah " in msg.text:
                apk = msg.text.replace("dimanakah ","")
                rnd = ["Di Jonggol","Di Anu","Di Dasar Samudra","Di Perempatan"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")   


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ryan.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                ryan.sendText(msg.to," sɪᴍɪsɪᴍɪ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                ryan.sendText(msg.to,"sɪᴍɪsɪᴍɪ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ryan.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        ryan.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                ryan.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                ryan.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                ryan.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ryan.sendText(msg.to,"----ᴅᴀʀɪ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + kata + "\n\n----ᴋᴇ ɪɴɢɢʀɪs----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ryan.sendText(msg.to,"----ᴅᴀʀɪ ɪɴɢɢʀɪs----\n" + "" + kata + "\n\n----ᴋᴇ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ryan.sendText(msg.to,"----ᴅᴀʀɪ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + kata + "\n\n----ᴋᴇ ᴛʜᴀɪʟᴀɴᴅ----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ryan.sendText(msg.to,"----ᴅᴀʀɪ ᴛʜᴀɪʟᴀɴᴅ----\n" + "" + kata + "\n\n----ᴋᴇ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = ryan.getAllContactIds()
                kontak = ryan.getContacts(contactlist)
                num=1
                msgs="═════════ʟɪsᴛ ғʀɪᴇɴᴅ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════ʟɪsᴛ ғʀɪᴇɴᴅ═════════\n\nᴛᴏᴛᴀʟ ғʀɪᴇɴᴅ : %i" % len(kontak)
                ryan.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = ryan.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════ʟɪsᴛ ᴍᴇᴍʙᴇʀ═════════"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════ʟɪsᴛ ᴍᴇᴍʙᴇʀ═════════\n\nᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs : %i" % len(group)
                ryan.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = ryan.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ryan.sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ɴᴏᴛ ғᴏᴜɴᴅ")
                else:
                    for target in targets:
                        try:
                            contact = ryan.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ryan.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = ryan.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ryan.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = ryan.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ryan.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ryan.getContact(key1)
                cu = ryan.channel.getCover(key1)
                try:
                    ryan.sendText(msg.to, "===[ᴅɪsᴘʟᴀʏɴᴀᴍᴇ]===\n" + contact.displayName)
                except:
                    ryan.sendText(msg.to, "===[ᴅɪsᴘʟᴀʏɴᴀᴍᴇ]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ryan.getContact(key1)
                cu = ryan.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ryan.sendText(msg.to,"ɴᴀᴍᴀ :\n" + contact.displayName + "\n\nʙɪᴏ :\n" + contact.statusMessage)
                    ryan.sendText(msg.to,"ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ " + contact.displayName)
                    ryan.sendImageWithURL(msg.to,image)
                    ryan.sendText(msg.to,"Cover " + contact.displayName)
                    ryan.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = ryan.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                ryan.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ryan.getContact(key1)
                cu = ryan.channel.getCover(key1)
                try:
                    ryan.sendText(msg.to,"ɴᴀᴍᴀ :\n" + contact.displayName + "\n\nᴍɪᴅ :\n" + contact.mid + "\n\nʙɪᴏ :\n" + contact.statusMessage + "msg.from_n\nᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nʜᴇᴀᴅᴇʀ :\n" + str(cu))
                except:
                    ryan.sendText(msg.to,"ɴᴀᴍᴀ :\n" + contact.displayName + "\n\nᴍɪᴅ :\n" + contact.mid + "\n\nʙɪᴏ :\n" + contact.statusMessage + "\n\nᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ :\n" + str(cu))


            elif "Bio " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ryan.getContact(key1)
                cu = ryan.channel.getCover(key1)
                try:
                    ryan.sendText(msg.to, "===[sᴛᴀᴛᴜsᴍᴇssᴀɢᴇ]===\n" + contact.statusMessage)
                except:
                    ryan.sendText(msg.to, "===[sᴛᴀᴛᴜsᴍᴇssᴀɢᴇ]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "ʙᴏᴛ sᴜᴅᴀʜ ʙᴇʀᴊᴀʟᴀɴ sᴇʟᴀᴍᴀ :\n"+waktu(eltime)
                ryan.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                ryan.sendText(msg.to,"========== ɪ ɴ ғ ᴏ ʀ ᴍ ᴀ s ɪ ==========\n"+"Date Of ʙɪʀᴛʜ : "+lahir+"\nᴀɢᴇ : "+usia+"\nᴜʟᴛᴀʜ : "+ultah+"\nᴢᴏᴅɪᴀᴋ : "+zodiak+"\n========== ɪ ɴ ғ ᴏ ʀ ᴍ ᴀ s ɪ ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["sᴜɴᴅᴀʏ", "ᴍᴏɴᴅᴀʏ", "ᴛᴜᴇsᴅᴀʏ", "ᴡᴇᴅɴᴇsᴅᴀʏ", "ᴛʜᴜʀsᴅᴀʏ","ғʀɪᴅᴀʏ", "sᴀᴛᴜʀᴅᴀʏ"]
                hari = ["ᴍɪɴɢɢᴜ", "sᴇɴɪɴ", "sᴇʟᴀsᴀ", "ʀᴀʙᴜ", "ᴋᴀᴍɪs", "ᴊᴜᴍᴀᴛ", "sᴀʙᴛᴜ"]
                bulan = ["ᴊᴀɴᴜᴀʀɪ", "ғᴇʙʀᴜᴀʀɪ", "ᴍᴀʀᴇᴛ", "ᴀᴘʀɪʟ", "ᴍᴇɪ", "ᴊᴜɴɪ", "ᴊᴜʟɪ", "ᴀɢᴜsᴛᴜs", "sᴇᴘᴛᴇᴍʙᴇʀ", "ᴏᴋᴛᴏʙᴇʀ", "ɴᴏᴠᴇᴍʙᴇʀ", "ᴅᴇsᴇᴍʙᴇʀ"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nᴊᴀᴍ : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ryan.sendText(msg.to, rst)                
                 
                
            elif "SearchID " in msg.text:
                userid = msg.text.replace("SearchID ","")
                contact = ryan.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ryan.sendMessage(msg)
                
            elif "Searchid " in msg.text:
                userid = msg.text.replace("Searchid ","")
                contact = ryan.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ryan.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ryan.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        ryan.sendText(msg.to,"ᴅᴏɴᴇ")
                    except Exception as error:
                        print error
                        ryan.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto ","")
                    if gid == "":
                        ryan.sendText(msg.to,"ɪɴᴠᴀʟɪᴅ ɢʀᴏᴜᴘ ɪᴅ")
                    else:
                        try:
                            ryan.findAndAddContactsByMid(msg.from_)
                            ryan.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ryan.sendText(msg.to,"ᴍᴜɴɢᴋɪɴ sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅɪ ᴅᴀʟᴀᴀᴍ ɢʀᴜᴘ ɪᴛᴜ")


            elif msg.text in ["Glist"]:
                ryan.sendText(msg.to, "ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ. . .")                    
                gid = ryan.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (ryan.getGroup(i).name +" ~> ["+str(len(ryan.getGroup(i).members))+"]")
                ryan.sendText(msg.to,"╔══════════════════════\n║          ☆☞ ʟɪsᴛ ɢʀᴏᴜᴘs☜☆\n╠══════════════════════\n" + h + "╠══════════════════════" + "\n║ ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs =" +" ["+str(len(gid))+"]\n╚══════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = ryan.getGroupIdsJoined()
                kontak = ryan.getGroups(gruplist)
                num=1
                msgs="═════════ʟɪsᴛ ɢʀᴜᴘᴍɪᴅ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════ʟɪsᴛ ɢʀᴜᴘᴍɪᴅ═════════\n\nTotal Grup : %i" % len(kontak)
                ryan.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    ryan.sendText(msg.to,"sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ...")
                    ryan.sendText(msg.to, "https://www.google.com/" + b)
                    ryan.sendText(msg.to,"ɪᴛᴜ ᴅɪᴀ ʟɪɴᴋɴʏᴀ. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        ryan.sendText(msg.to,"ɢʀᴜᴘ ɪᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                    else:
                        try:
                            groups = ryan.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+ɢʀᴏᴜᴘɪᴅ : " + gid + "\n -+ᴍᴇᴍʙᴇʀs : " + members + "\n -+ᴍᴇᴍʙᴇʀsᴘᴇɴᴅɪɴɢ : " + pendings + "\n -+ᴄʀᴇᴀᴛᴏʀ : " + groups.creator.displayName + "\n -+ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            ryan.sendText(msg.to,h)
                        except Exception as error:
                            ryan.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = ryan.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                ryan.rejectGroupInvitation(i)
                            except:
                                ryan.sendText(msg.to,"ᴇʀʀᴏʀ!")
                                break
                        else:
                            break
                    if gid is not None:
                        ryan.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        ryan.sendText(msg.to,"ɢʀᴜᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = ryan.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = ryan.getGroup(i)
                            _list += gids.name
                            ryan.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        ryan.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴛᴇʀɪᴍᴀ sᴇᴍᴜᴀ ᴜɴᴅᴀɴɢᴀɴ ᴅᴀʀɪ ɢʀᴜᴘ :\n" + _list)
                    else:
                        ryan.sendText(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ ɢʀᴜᴘ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ sᴀᴀᴛ ɪɴɪ")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                ryan.sendGifWithURL(msg.to,gore)
                

                
            elif ("Repadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        ryan.sendText(msg.to,"ᴛᴀʀɢᴇᴛ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!")
                        break
                    except:
                        ryan.sendText(msg.to,"ғᴀɪʟ !")
                        break
                    
            elif ("Repdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        ryan.sendText(msg.to,"ᴛᴀʀɢᴇᴛ ᴅɪʜᴀᴘᴜsᴋᴀɴ!")
                        break
                    except:
                        ryan.sendText(msg.to,"ғᴀɪʟ !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            ryan.sendText(msg.to,"ɴᴏᴛʜɪɴɢ")
                        else:
                            mc = "ᴛᴀʀɢᴇᴛ ᴍɪᴍɪᴄ ᴜsᴇʀ:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+ryan.getContact(mi_d).displayName + "\n"
                            ryan.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                ryan.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                ryan.sendText(msg.to,"ᴍɪᴍɪᴄ ᴄʜᴀɴɢᴇ ᴛᴏ ᴛᴀʀɢᴇᴛ")
                            else:
                                ryan.sendText(msg.to,"ɪ ᴅᴏɴᴛ ᴋɴᴏᴡ")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        ryan.sendText(msg.to,"ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ ᴏɴ")
                    else:
                        ryan.sendText(msg.to,"sᴜᴅᴀʜ ᴏɴ")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        ryan.sendText(msg.to,"ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ ᴏғғ")
                    else:
                        ryan.sendText(msg.to,"sᴜᴅᴀʜ ᴏғғ")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = ryan.fetchOps(ryan.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ryan.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ryan.Poll.rev = max(ryan.Poll.rev, Op.revision)
            bot(Op)
