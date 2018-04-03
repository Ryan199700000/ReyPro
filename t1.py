# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

cl = LINETCR.LINE()
cl.login(token="Ermj3t0OyexaXqqYSKn8./xAA3piZkDNk7C2fd2YUQa.Pe/Es7dysXw4rw834bssI1kBVsZSv8C5LW4V/spgEJA=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ErTkcRRTacBpJqx2PDE1.41AePsIvs+AqJ/J+rIkvqq.Zr1WRkV3QD9km6JYV684/B2nDFDcnlpPGiJHXYvxi20=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="ErgDXLv0dO76Nupz1ex0.zey9kENsGNNTEEjm2CJZea.o29zasFR6hdCYQOwPP7qw1OKoH9PZKQ2ZZXJ3+jlGOQ=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Erhra5ZZMuIxZseYtEY7.A3htjkZb9sd+Tu69MaEHnW.jTPe5UqGd66s+ln+YwbOGApX6PEJXEUqSZZ/OOpPLJA=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EriZphnl0SwvXR9SYbQa./CsmtSUZXHMuj2E9gZB1IG.4Aw+uZqbv7XindK2hWbHPoGzfXPgwTFlNCOr4hFY09g=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="Er0aI9OJIo66idJSUl1c.acsM3ILuw//4x4z4wkYata.sf1ABptuqT/1xGgN7yHUHcZ4sK21YeUdjgGn1WLW4ug=") #Eq688BcWiFMvaATiKWW6./QTl046oneusnakwA1BlvG.aSNsh1ccJpuuc9wMCiOfNtel7PFvVuYHyhdR94Bn/QI=
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="ErU9efGnjlVJzucOCrNc.ah+Kr/GBFcC8ErxqiEFI+a.GZymPL7c/9GqPpClVZRhWTO5XoMrbxQlmy/XqNEBBAA=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="ErJoOUMoFVK6IdN8fLp9.3UzlgtAf2NrLcjwv6Ge9Iq.NfAmqSrleCl0VkVV9P6K9CPBlgcul1Xgy6I1D+dKVd8=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EreNoKVyTqhJSVqam6Rd.VeBUD0FZHgmujpoP2tnpJq.fwu17q8KKBJSR/dptuPMpWTcjIo4zWLILmd7U0RRy/U=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="ErjucvjadVf9tYu2rw72.r+UNzG/gL/WydGlXqDQvGG.nuFbU/RkTdSS1NDWxx91S11vHasMVOxLu+krUpN79CA=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="ErpkCFQcmRzqw58S1JQ8.PxrhHI3p4UUZTOVIf8TNEa.yUu1Vgk6maomXp7+Rd+tlXiDX0Ia+0D55AUjj9d8sAk=")
ki10.loginResult()

print u"Login Success CyberTK"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔══════════════════════
║   ™☆☞General Command☜☆™
╠═══☆☞H E L P☜☆═════════
╠🌟『Owner』
╠🌟『Pap owner』
╠🌟『Speed』
╠🌟『Rey sp』
╠🌟『Speed test』
╠🌟『Status』
╠═══☆☞S E L F☜☆═════════
╠✨『Hi』
╠✨『Me』
╠✨『Mymid』
╠✨『Mid @』
╠✨『SearchID ID LINE)』
╠✨『Checkdate DD/MM/YY』
╠✨『Kalender』
╠✨『Steal contact』
╠✨『Getpict @』
╠✨『Getcover @』
╠✨『Auto like』
╠✨『System』
╠✨『Kernel』
╠✨『Cpu』
╠✨『Bio @』
╠✨『Info @』
╠✨『Name @』
╠✨『Profile @』
╠✨『Contact @』
╠✨『Comment on/off』
╠✨『Friendlist』
╠✨『Kicker on/off』
╠✨『Repdel @』
╠✨『Miclist』
╠═══☆☞ B O T ☜☆═════════
╠🚨『Absen』
╠🚨『Respon』
╠🚨『Runtime』
╠🚨『copy @』
╠🚨『Copycontact』
╠🚨『Mybackup』
╠🚨『Mybio Text』
╠🚨『Myname Text』
╠🚨『@bye』
╠🚨『Bot on/off』
╠═══☆☞ M E D I A ☜☆═══════
╠💻『Gift』
╠💻『Giftbycontact』
╠💻『Gif gore』
╠💻『Google (Text)』
╠💻『Playstore NamaApp』
╠💻『Fancytext Text』
╠💻『musik Judul-Penyanyi』
╠💻『lirik Judul-Penyanyi』
╠💻『musrik Judul-Penyanyi』
╠💻『ig UrsnameInstagram』
╠💻『Checkig UrsnameIG』
╠💻『apakah Text 』
╠💻『kapan Text 』
╠💻『hari Text 』
╠💻『berapa Text 』
╠💻『berapakah Text』
╠💻『Youtube Judul Video』
╠💻『Youtubevideo Judul Video』
╠💻『Youtubesearch: Judul Video』
╠💻『Image NamaGambar』
╠💻『Say Text』
╠💻『Say-en Text』
╠💻『Say-jp Text』
╠💻『Tr-id Text En Ke ID』
╠💻『Tr-en Text ID Ke En』
╠💻『Tr-th Text ID Ke Th』
╠💻『Id@en Text ID Ke En』
╠💻『Id@th Text ID Ke TH』
╠💻『En@id Text En Ke ID』
╠═══☆☞ G R O U P ☜☆═══════
╠🌀『Welcome』
╠🌀『Say welcome』
╠🌀『Invite creator』
╠🌀『Setview/Cctv』
╠🌀『Viewseen/Ciduk』
╠🌀『Gn: (NamaGroup)』
╠🌀『Tag all/Croot』
╠🌀『lurk on/off』
╠🌀『lurkers』
╠🌀『Recover』
╠🌀『Cancel』
╠🌀『Cancelall』
╠🌀『Gcreator』
╠🌀『Ginfo』
╠🌀『Gurl』
╠🌀『List group』
╠🌀『Pict group: NamaGroup』
╠🌀『Spam-5: Text』
╠🌀『Nspam: Text』
╠🌀『GhostSpam: Text』
╠🌀『Add all』
╠🌀『Kick: Mid』
╠🌀『Invite: Mid』
╠🌀『Bot:inv』
╠🌀『Memlist』
╠🌀『Getgroup image』
╠🌀『Urlgroup Image』
╠═══☆☞S E T ☜☆══════════
╠🔏『Notif on/off』
╠🔏『Protect on/off』
╠🔏『Invitepro on/off』
╠🔏『Alwaysread on/off』
╠🔏『Sider on/off』
╠🔏『Auto like』
╠🔏『Invitepro on/off』
╠🔏『Auto add on/off』
╠🔏『Auto leave on/off』
╠🔏『Auto join on/off』
╠🔏『Join cancel on/off』
╠🔏『Auto kick on/off』
╠🔏『Kicker on/off』
╠🔏『Comment on/off』
╠🔏『Share on/off』
╠🔏『Contact on/off』
╠🔏『Sticker on』
╠🔏『Qrprotect on/off』
╠═══☆☞C R E A T O R ☜☆═════
╠🎬『Blank』
╠🎬『Kickall/1997』
╠🎬『Bc: Text』
╠🎬『Join group: (NamaGroup』
╠🎬『Leave group: (NamaGroup』
╠🎬『Leave all group』
╠🎬『Tag on/off』
╠🎬『Bot restart/Reboot』
╠🎬『Turn off』
╠══════════════════════
║♻ Creating by:®R̸y̸a̸̸n̸  R̸̸a̸s̸̸y̸i̸̸d̸ ♻
║®Support by :
║☆☞ Silent Kill™『SK』
║☆☞ Ninja Jawa Killer™『NJK』
╚══════════════════════"""


ryanMessage ="""╔══════════════════════
║          ™☆☞R̸y̸a̸n̸ R̸a̸s̸yi̸d̸☜☆™
╠══════════════════════
╠🔒『Allprotect on/off』
╠🔒『Ban』
╠🔒『Unban』
╠🔒『Ban @』
╠🔒『Unban @』
╠🔒『Ban list』
╠🔒『Invite』
╠🔒『Clear ban』
╠🔒『Kill』
╠🔒『Kick @』
╠🔒『Set member: Jumlah』
╠🔒『Ban group: NamaGroup』
╠🔒『Del ban: NamaGroup』
╠🔒『List ban』
╠🔒『Kill ban』
╠🔒『Com set: text』
╠🔒『Pesan add- text』
╠🔒『Message set: text』
╠🔒『Message set text』
╠🔒『Help set: text』
╠🔒『Glist』
╠🔒『Glistmid』
╠🔒『Details group: Gid』
╠🔒『Cancel invite: Gid』
╠🔒『InviteMeTo: Gid』
╠🔒『Acc invite』
╠🔒『Removechat』
╠🔒『Qr on/off』
╠🔒『Autokick on/off』
╠🔒『Autocancel on/off』
╠🔒『Invitepro on/off』
╠🔒『Join on/off』
╠🔒『Joincancel on/off』
╠🔒『Respon1 on/off』
╠🔒『Respon2 on/off』
╠🔒『Respon3 on/off』
╠🔒『Respon4 on/off』
╠🔒『Responkick on/off』
╠══════════════════════
║♻ Creating by:®R̸y̸a̸̸n̸  R̸̸a̸s̸̸y̸i̸̸d̸ ♻
║®Support by :
║☆☞ Silent Kill™『SK』
║☆☞ Ninja Jawa Killer™『NJK』
╚══════════════════════"""

helo=""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
Bots = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid]
admsa = 'uf9769adcf23329d9caedcd850f6caea8','u81acb7e1e964063dc3cfbec063d22bc6','uf48b6148d0bc3eed934ea0a9e68e816d'
admin = 'uf9769adcf23329d9caedcd850f6caea8'

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":10},
    'leaveRoom':True,
    'timeline':True,
    'pap':{},
    'likeOn':{},
    'invite':{},
    'winvite':{},
    'steal':{},
    'gift':{},
    'copy':{},
    'sticker':False,
    'detectMention':False,
    'detectMention2':False,
    'detectMention3':False,
    'detectMention4':True,
    'detectMention5':False,
    'detectMention6':False,
    'kickMention':False,
    'autoAdd':True,
    'message':"Thanks For Add Me\n┅͜͡૨γαղ‮┅͜͡\n\n♻Support By ~ ҳ̸Ҳ̸ҳ Сўв∝я тҝ ҳ̸Ҳ̸ҳ\n\n✯==== Creator ====✯\n\nhttp://line.me/ti/p/~s.k.9.7",
    "lang":"JP",
    "Timeline":True,
    "comment":"☆Auto Like ©By : R̶y̶an Pr̶o̶tect\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment1":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ1\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment2":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ2\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment3":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ3\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment4":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ4\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment5":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ5\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment6":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ6\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment7":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ7\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment8":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ8\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment9":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ9\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "comment10":"☆Auto Like ©By : Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ10\n╔═════════════════════\n╠♻Support by :\n╠☆☞ Silent Kill™『SK』\n╠☆☞ NJ Killer™『NJK』\n╠═════════════════════\n╠☆☞ http://line.me/ti/p/~s.k.9.7\n╚═════════════════════",
    "commentOn":True,
    "commentBlack":{},
    "Sambutan":False,
    "wblack":False,
    "dblack":False,
    "joinkick":{},
    "AutoJoinCancel":True,
    "AutoKick":{},
    "Members":{},
    "AutoKickon":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "alwaysRead":False,
    "Mimic":{},
    "Sider":{},
    "Simi":{},
    "linkprotect":False,
}
    
settings = {
    "simiSimi":{}
    }
mode='self'
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
mimic = {
    "copy":False,
    "botcopy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup1 = ki.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage
backup1.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup2 = ki2.getProfile()
backup2.displayName = contact.displayName
backup2.statusMessage = contact.statusMessage
backup2.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup3 = ki3.getProfile()
backup3.displayName = contact.displayName
backup3.statusMessage = contact.statusMessage
backup3.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup4 = ki4.getProfile()
backup4.displayName = contact.displayName
backup4.statusMessage = contact.statusMessage
backup4.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup5 = ki5.getProfile()
backup5.displayName = contact.displayName
backup5.statusMessage = contact.statusMessage
backup5.pictureStatus = contact.pictureStatus

contact = ki6.getProfile()
backup6 = ki6.getProfile()
backup6.displayName = contact.displayName
backup6.statusMessage = contact.statusMessage
backup6.pictureStatus = contact.pictureStatus

contact = ki7.getProfile()
backup7 = ki7.getProfile()
backup7.displayName = contact.displayName
backup7.statusMessage = contact.statusMessage
backup7.pictureStatus = contact.pictureStatus

contact = ki8.getProfile()
backup8 = ki8.getProfile()
backup8.displayName = contact.displayName
backup8.statusMessage = contact.statusMessage
backup8.pictureStatus = contact.pictureStatus

contact = ki9.getProfile()
backup9 = ki9.getProfile()
backup9.displayName = contact.displayName
backup9.statusMessage = contact.statusMessage
backup9.pictureStatus = contact.pictureStatus

contact = ki10.getProfile()
backup10 = ki10.getProfile()
backup10.displayName = contact.displayName
backup10.statusMessage = contact.statusMessage
backup10.pictureStatus = contact.pictureStatus

responsename1 = ki.getProfile().displayName
responsename2 = ki2.getProfile().displayName
responsename3 = ki3.getProfile().displayName
responsename4 = ki4.getProfile().displayName
responsename5 = ki5.getProfile().displayName
responsename6 = ki6.getProfile().displayName
responsename7 = ki7.getProfile().displayName
responsename8 = ki8.getProfile().displayName
responsename9 = ki9.getProfile().displayName
responsename10 = ki10.getProfile().displayName

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
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
                            Name = cl.getContact(op.param2).displayName
                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

    else:
        pass    	  
        
    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Maaf " + cl.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"☆『Assalamu'alaikum』☆\n☆『Newbie Om, Jangan Dibully』☆")


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            ki.rejectGroupInvitation(op.param1)
                            ki2.rejectGroupInvitation(op.param1)
                            ki3.rejectGroupInvitation(op.param1)
                            ki4.rejectGroupInvitation(op.param1)
                            ki4.rejectGroupInvitation(op.param1)
                            ki6.rejectGroupInvitation(op.param1)
                            ki7.rejectGroupInvitation(op.param1)
                            ki8.rejectGroupInvitation(op.param1)
                            ki9.rejectGroupInvitation(op.param1)
                            ki10.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            ki2.acceptGroupInvitation(op.param1)
                            ki3.acceptGroupInvitation(op.param1)
                            ki4.acceptGroupInvitation(op.param1)
                            ki5.acceptGroupInvitation(op.param1)
                            ki6.acceptGroupInvitation(op.param1)
                            ki7.acceptGroupInvitation(op.param1)
                            ki8.acceptGroupInvitation(op.param1)
                            ki9.acceptGroupInvitation(op.param1)
                            ki10.acceptGroupInvitation(op.param1)
                    else:  
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        ki2.acceptGroupInvitation(op.param1)
                        ki3.acceptGroupInvitation(op.param1)
                        ki4.acceptGroupInvitation(op.param1)
                        ki5.acceptGroupInvitation(op.param1)
                        ki6.acceptGroupInvitation(op.param1)
                        ki7.acceptGroupInvitation(op.param1)
                        ki8.acceptGroupInvitation(op.param1)
                        ki9.acceptGroupInvitation(op.param1)
                        ki10.acceptGroupInvitation(op.param1)
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     ki.like(url[25:58], url[66:], likeType=1002)
                     ki2.like(url[25:58], url[66:], likeType=1004)
                     ki3.like(url[25:58], url[66:], likeType=1003)
                     ki4.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment"])
                     ki.comment(url[25:58], url[66:], wait["comment"])
                     ki2.comment(url[25:58], url[66:], wait["comment"])
                     ki3.comment(url[25:58], url[66:], wait["comment"])
                     ki4.comment(url[25:58], url[66:], wait["comment"])
                     cl.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = True
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "uf9769adcf23329d9caedcd850f6caea8":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in admsa:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in admsa:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               ki.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    ki2.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in admsa:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        ki3.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ki4.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in admsa:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in admsa:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in admsa:
                      if op.param2 in Bots:
                        pass
                    try:
                        ki5.kickoutFromGroup(op.param1,[op.param2])
			ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    ki7.kickoutFromGroup(op.param1,[op.param2])
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

 
                if admsa in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki8.kickoutFromGroup(op.param1,[op.param2])
			ki9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                ki10.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    ki2.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1002)
                ki2.like(url[25:58], url[66:], likeType=1004)
                ki3.like(url[25:58], url[66:], likeType=1003)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1002)
                ki6.like(url[25:58], url[66:], likeType=1004)
                ki7.like(url[25:58], url[66:], likeType=1003)
                ki8.like(url[25:58], url[66:], likeType=1001)
                ki9.like(url[25:58], url[66:], likeType=1002)
                ki10.like(url[25:58], url[66:], likeType=1004)
                cl.comment(url[25:58], url[66:], wait["comment"])
                ki.comment(url[25:58], url[66:], wait["comment1"])
                ki2.comment(url[25:58], url[66:], wait["comment2"])
                ki3.comment(url[25:58], url[66:], wait["comment3"])
                ki4.comment(url[25:58], url[66:], wait["comment4"])
                ki5.comment(url[25:58], url[66:], wait["comment5"])
                ki6.comment(url[25:58], url[66:], wait["comment6"])
                ki7.comment(url[25:58], url[66:], wait["comment7"])
                ki8.comment(url[25:58], url[66:], wait["comment8"])
                ki9.comment(url[25:58], url[66:], wait["comment9"])
                ki10.comment(url[25:58], url[66:], wait["comment10"])
                cl.sendText(msg.to,"Like Success") 
                
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ki3.sendText(msg.to,text)             
                
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ki2.sendText(msg.to,data['result']['response'].encode('utf-8'))
                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Ngetag Lagi Yawloh " + cName + "\n! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  ki2.kickoutFromGroup(msg.to,[msg.from_])
                                  break            
                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:          
                    contact = ki.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Gosah TAG-TAG " + cName + " JEMBOTT!!!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja " + cName ,"Woii " + cName + " Jangan Ngetag, Riibut!","Yawloh,, Jones Karatan " + cName + " NgeTag!!","Ono Opo MBOTT" + cName + " NgeTag-Tag!!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ki.sendText(msg.to,ret_)
                                  rnd = ["Buset si joness ngetag mulu, kalo penting langsung pe em riyan nya aja","Ni orang kerjaan nya ngetag mulu, gift tikel aja enggak pernah, suwe lu jamban"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  ki.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "145",
                                                       "STKPKGID": "2",
                                                       "STKVER": "100" }
                                  ki.sendMessage(msg)                                
                                  break

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Gosah TAG-TAG " + cName + " JEMBOTT!!!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja " + cName ,"Woii " + cName + " Jangan Ngetag, Riibut!","Yawloh,, Jones Karatan " + cName + " NgeTag!!","Ono Opo MBOTT" + cName + " NgeTag-Tag!!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "2754644",
                                                       "STKPKGID": "1066653",
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                
                                  break
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["" + cName + ", Jadilah Jones Alami Yang Nggak Suka NgeTag Orang Ganteng"]
                    balas1 = "Selfie dulu ya Cet. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "5523427",
                                                       "STKPKGID": "1135371",
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                
                                  break  
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention4"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Gosah TAG-TAG " + cName + " JEMBOTT!!!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja " + cName ,"Woii " + cName + " Jangan Ngetag, Riibut!","Yawloh,, Jones Karatan " + cName + " NgeTag!!","Ono Opo MBOTT " + cName + " NgeTag-Tag!!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  rnd = ["Buset si joness ngetag mulu, kalo penting langsung pe em riyan nya aja","Ni orang kerjaan nya ngetag mulu, gift tikel aja enggak pernah, suwe lu jamban"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  cl.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "5523400",
                                                       "STKPKGID": "1135371",
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                
                                  break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention5"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["" + cName + ", Jadilah Jones Alami Yang Nggak Suka NgeTag Orang Ganteng"]
                    balas1 = "Selfie dulu ya Cet. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to,image)
                                  rnd = ["Yang Jomblo Bin Haji Joness Jangan Suka Ngetag Guwa"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  cl.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "28785553",
                                                       "STKPKGID": "1944857",
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                
                                  break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention6"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Dihh, " + cName + " Ngtag Mulu!!!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja " + cName ,"Iya-Iya Nanti Nah " + cName + " ,Tanggung Lagi Be'ol~_~!","Yawloh,, Jones Karatan " + cName + " NgeTag!!","Ono Opo MBOTT " + cName + " NgeTag-Tag!!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  rnd = ["Elu mandi dulu sana " + cName + ", Baru Nge Tag Guwa"]
                                  p = random.choice(rnd)
                                  lang = 'id'
                                  tts = gTTS(text=p, lang=lang)
                                  tts.save("hasil.mp3")
                                  cl.sendAudio(msg.to,"hasil.mp3")   
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "28785545",
                                                       "STKPKGID": "1944857",
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                
                                  break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki2.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                              targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     ki2.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     #wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         #wait["winvite"] = False
                                     except:
                                         ki.sendText(msg.to,"Negative, Error detected")
                                         #wait["winvite"] = False
                                         break
                                         
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ki.getGroup(msg.to)
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
                                ki.findAndAddContactsByMid(target)
                                contact = ki.getContact(target)
                                cu = ki.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                ki.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                ki.sendText(msg.to,"Profile Picture " + contact.displayName)
                                ki.sendImageWithURL(msg.to,image)
                                ki.sendText(msg.to,"Cover " + contact.displayName)
                                ki.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
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
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                ki.sendMessage(msg)
                                ki2.sendMessage(msg)
                                ki3.sendMessage(msg)
                                ki4.sendMessage(msg)
                                ki5.sendMessage(msg)
                                ki6.sendMessage(msg)
                                ki7.sendMessage(msg)
                                ki8.sendMessage(msg)
                                ki9.sendMessage(msg)
                                ki10.sendMessage(msg)
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
                    groups = cl.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.CloneContactProfile(target)
                                cl.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait[q] = False
                                     break
            if msg.contentType == 13:
                if wait["botcopy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ki.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                ki.CloneContactProfile(target)
                                ki2.CloneContactProfile(target)
                                ki3.CloneContactProfile(target)
                                ki4.CloneContactProfile(target)
                                ki5.CloneContactProfile(target)
                                ki6.CloneContactProfile(target)
                                ki7.CloneContactProfile(target)
                                ki8.CloneContactProfile(target)
                                ki9.CloneContactProfile(target)
                                ki10.CloneContactProfile(target)
                                ki10.sendText(msg.to, "Copied (^_^)")
                                wait["botcopy"] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait[q] = False
                                     break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["invite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                              targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["invite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["invite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["invite"] = False
                                         break
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                cl.sendText(msg.to, filler)
                #wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    ki.sendText(msg.to,msg.text)
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Kasih help","help","[∆√ cувєя тк™ √∆]"]:
            	if msg.from_ in admin:
                    cl.sendText(msg.to,helpMessage)
                    cl.sendText(msg.to,"『Dilarang Typo Tanpa Izin Dari Owner』")
                    
            elif msg.text in ["Ryan key","help","[∆√ cувєя тк™ √∆]"]:
            	if msg.from_ in admin:
                    cl.sendText(msg.to,ryanMessage)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': admsa}
                    cl.sendMessage(msg)
                    
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    ki.sendText(msg.to,"Auto Respon1 Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    ki.sendText(msg.to,"Auto Respon1 Sudah Off")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")	
		
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon2 Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")

            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    cl.sendText(msg.to,"Auto Respon2 Sudah Off")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")	
		
            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    cl.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")	
		
            elif msg.text in ["Respon4 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = True
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon4 Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")

            elif msg.text in ["Respon4 off"]:
		if msg.from_ in admin:
                    wait["detectMention4"] = False
                    cl.sendText(msg.to,"Auto Respon4 Sudah Off")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")	
		
            elif msg.text in ["Respon5 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = True
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon5 Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")

            elif msg.text in ["Respon5 off"]:
		if msg.from_ in admin:
                    wait["detectMention5"] = False
                    cl.sendText(msg.to,"Auto Respon5 Sudah Off")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")	
	
            elif msg.text in ["Respon6 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon6 Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")

            elif msg.text in ["Respon6 off"]:
		if msg.from_ in admin:
                    wait["detectMention6"] = False
                    cl.sendText(msg.to,"Auto Respon6 Sudah Off")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")	
		
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")
		
            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False  
                    cl.sendText(msg.to,"Auto Respon Kick Di Nonaktifkan")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")
		
            elif msg.text in ["AllRespon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = True
                    wait["detectMention3"] = True
                    wait["detectMention4"] = True
                    wait["kickMention"] = True
                    cl.sendText(msg.to,"Semua Auto Respon Sudah Aktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")
		
            elif msg.text in ["AllRespon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["detectMention4"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Semua Auto Respon Sudah Nonaktif")
		else:
		    ki.sendText(msg.to,"Khusus Ryan")
		
            elif msg.text in ["Bot:inv on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 ki.sendText(msg.to,"Bot Invite : Enable")
                 
            elif msg.text in ["Bot:inv off"]:
            	if msg.from_ in admin:
                 wait["winvite"] = False
                 ki.sendText(msg.to,"Bot Invite : Disable")
                 
            elif msg.text in ["K on","Contact on"]:
                wait["contact"] = True
                cl.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["contact"] = False
                cl.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                 
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                
                 
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Bots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13           
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                cl.sendMessage(msg) 
                time.sleep(0.0)
                msg.contentType = 13
            elif "MyBots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg) 
                msg.contentType = 13           
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg) 
                msg.contentType = 13
            elif "Rey1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Rey2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Rey3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Rey4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg) 
 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)                

            
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


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
                cl.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
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
                cl.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)   
            elif "musik " in msg.text:
					        songname = msg.text.replace("musik ","")
					        params = {"songname": songname}
					        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					        data = r.text
					        data = json.loads(data)
					        for song in data:
						        abc = song[3].replace('https://','http://')
						        ki.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						        ki2.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						        ki3.sendAudioWithURL(msg.to,abc)
						        ki4.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
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
                        ki.sendText(msg.to, hasil)
                except Exception as wak:
                        ki.sendText(msg.to, str(wak))
                        
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
						ki.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ki2.sendAudioWithURL(msg.to,abc)
						ki3.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						ki4.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
            elif "Fancytext " in msg.text:
                txt = msg.text.replace("Fancytext ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
               
            elif msg.text in ["Rey1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Rey2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)
                
            elif msg.text in ["Rey3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki3.sendMessage(msg)
                
            elif msg.text in ["Rey4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki4.sendMessage(msg)
              
            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                cl.sendText(msg.to,"『Auto Like DiAktifkan』")
                             
            elif msg.text in ["Like off"]:
                wait["likeOn"] = False
                cl.sendText(msg.to,"『Auto Like Di Nonaktifkan』")
                
            elif msg.text in ["Rey Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Davet yok😤")
                        else:
                            ki.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Tidak ada undangan")
                    else:
                        ki.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No is Invite✍😤")
                        else:
                            ki.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        ki.sendText(msg.to,"invitan tidak ada")
            elif "gurl" == msg.text:
                print cl.getGroup(msg.to)
                cl.sendMessage(msg)
            elif "rey gurl" == msg.text:
                print ki.getGroup(msg.to)
                ki.sendMessage(msg)
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"URL on ✍")
                        ki2.sendText(msg.to,"URL on ✍")
                        ki3.sendText(msg.to,"URL on ✍")
                        ki4.sendText(msg.to,"URL on ✍")
                        ki5.sendText(msg.to,"URL on ✍")
                        ki6.sendText(msg.to,"URL on ✍")
                        ki7.sendText(msg.to,"URL on ✍")
                        ki8.sendText(msg.to,"URL on ✍")
                        ki9.sendText(msg.to,"URL on ✍")
                        ki10.sendText(msg.to,"URL on ✍")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        ki.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    ki.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"URL Closed ✍")
                        ki2.sendText(msg.to,"URL Closed ✍")
                        ki3.sendText(msg.to,"URL Closed ✍")
                        ki4.sendText(msg.to,"URL Closed ✍")
                        ki5.sendText(msg.to,"URL Closed ✍")
                        ki6.sendText(msg.to,"URL Closed ✍")
                        ki7.sendText(msg.to,"URL Closed ✍")
                        ki8.sendText(msg.to,"URL Closed ✍")
                        ki9.sendText(msg.to,"URL Closed ✍")
                        ki10.sendText(msg.to,"URL Closed ✍")
                    else:
                        ki.sendText(msg.to,"URL Kapalí ✍")
                        ki2.sendText(msg.to,"URL Kapalí ✍")
                        ki3.sendText(msg.to,"URL Kapali ✍")
                        ki4.sendText(msg.to,"URL Kapali ✍")
                        ki5.sendText(msg.to,"URL Kapali ✍")
                        ki6.sendText(msg.to,"URL Kapali ✍")
                        ki7.sendText(msg.to,"URL Kapali ✍") 
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif "Ginfo" == msg.text:
                ginfo = ki.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                ki.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                ki.sendMessage(msg)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Rey1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Rey2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Rey3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Rey4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Rey5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Rey6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "Rey7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "Rey8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "Rey9 mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "Rey10 mid" == msg.text:
                ki10.sendText(msg.to,ki10mid)
            elif "all mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
            elif "Rey:" in msg.text:
                tl_text = msg.text.replace("Rey:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    ki2.updateProfile(profile)
                    ki3.updateProfile(profile)
                    ki4.updateProfile(profile)
                    ki5.updateProfile(profile)
                    ki6.updateProfile(profile)
                    ki7.updateProfile(profile)
                    ki8.updateProfile(profile)
                    ki9.updateProfile(profile)
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Done")
            elif "Mybio " in msg.text:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Done")
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
                    
            elif "Rey1 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey1 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Rey2 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey2 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki2.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki2.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki2.CloneContactProfile(target)
                               ki2.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Rey3 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey3 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki3.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki3.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki3.CloneContactProfile(target)
                               ki3.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e                                

            elif "Rey4 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey4 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki4.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki4.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki4.CloneContactProfile(target)
                               ki4.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Rey5 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey5 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki5.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki5.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki5.CloneContactProfile(target)
                               ki5.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Rey6 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey6 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki6.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki6.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki6.CloneContactProfile(target)
                               ki6.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Rey7 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey7 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki7.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki7.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki7.CloneContactProfile(target)
                               ki7.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e                                

            elif "Rey8 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey8 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki8.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki8.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki8.CloneContactProfile(target)
                               ki8.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Rey9 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey9 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki9.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki9.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki9.CloneContactProfile(target)
                               ki9.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e                                

            elif "Rey10 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Rey10 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki10.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki10.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki10.CloneContactProfile(target)
                               ki10.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Backup all"]:
                try:
                    ki.updateDisplayPicture(backup1.pictureStatus)
                    ki.updateProfile(backup1)

                    ki2.updateDisplayPicture(backup2.pictureStatus)
                    ki2.updateProfile(backup2)

                    ki3.updateDisplayPicture(backup3.pictureStatus)
                    ki3.updateProfile(backup3)

                    ki4.updateDisplayPicture(backup4.pictureStatus)
                    ki4.updateProfile(backup4)
                    
                    ki5.updateDisplayPicture(backup5.pictureStatus)
                    ki5.updateProfile(backup5)

                    ki6.updateDisplayPicture(backup6.pictureStatus)
                    ki6.updateProfile(backup6)

                    ki7.updateDisplayPicture(backup7.pictureStatus)
                    ki7.updateProfile(backup7)

                    ki8.updateDisplayPicture(backup8.pictureStatus)
                    ki8.updateProfile(backup8)
                    
                    ki9.updateDisplayPicture(backup9.pictureStatus)
                    ki9.updateProfile(backup9)

                    ki10.updateDisplayPicture(backup10.pictureStatus)
                    ki10.updateProfile(backup10)
                    cl.sendText(msg.to, "All Done (^_^)")
                except Exception as e:
                    cl.sendText(msg.to, str(e))

#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Cipok","Rey Tagall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-------------Fungsi Tag All Finish---------------#

#---------------------------------------------------------
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------                    
            elif "3name:" in msg.text:
                string = msg.text.replace("3name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4name:" in msg.text:
                string = msg.text.replace("4name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------                    
            elif "5name:" in msg.text:
                string = msg.text.replace("5name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6name:" in msg.text:
                string = msg.text.replace("6name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------                    
            elif "7name:" in msg.text:
                string = msg.text.replace("7name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "8name:" in msg.text:
                string = msg.text.replace("8name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------                    
            elif "9name:" in msg.text:
                string = msg.text.replace("9name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "10name:" in msg.text:
                string = msg.text.replace("10name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------                    
#--------------------------------------------------------
            elif "Allname:" in msg.text:
                string = msg.text.replace("Allname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki2.updateProfile(profile)
                    ki3.updateProfile(profile)
                    ki4.updateProfile(profile)
                    ki5.updateProfile(profile)
                    ki6.updateProfile(profile)
                    ki7.updateProfile(profile)
                    ki8.updateProfile(profile)
                    ki9.updateProfile(profile)
                    ki10.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + "")
#--------------------------------------------------------                    
            elif msg.text.lower() == 'responsename':
                ki.sendText(msg.to,responsename1)
                ki2.sendText(msg.to,responsename2)
                ki3.sendText(msg.to,responsename3)
                ki4.sendText(msg.to,responsename4)
                ki5.sendText(msg.to,responsename5)
                ki6.sendText(msg.to,responsename6)
                ki7.sendText(msg.to,responsename7)
                ki8.sendText(msg.to,responsename8)
                ki9.sendText(msg.to,responsename9)
                ki10.sendText(msg.to,responsename10)
                
#--------------------------------------------------------                
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                
            elif "Set member: " in msg.text:
		      if msg.from_ in admin:	 	        
		        jml = msg.text.replace("Set member: ","")
		        wait["Members"] = int(jml)
		        cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		
            elif ("Repadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        ki3.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
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
                        ki3.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            ki3.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            ki3.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                ki3.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                ki3.sendText(msg.to,"Mimic change to target")
                            else:
                                ki3.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                    	wait["Mimic"] = True
                        mimic["status"] = True
                        ki3.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                    	wait["Mimic"] = False
                        mimic["status"] = False
                        ki3.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")

	    elif "Add all" in msg.text:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")

            elif msg.text in ["Invite"]:
                wait["invite"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Spam"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Aku belum mandi")
                ki2.sendText(msg.to,"Tak tun tuang")
                ki3.sendText(msg.to,"Tak tun tuang")
                ki3.sendText(msg.to,"Tapi masih cantik juga")
                ki4.sendText(msg.to,"Tak tun tuang")
                ki5.sendText(msg.to,"Tak tun tuang")
                ki6.sendText(msg.to,"apalagi kalau sudah mandi")
                ki7.sendText(msg.to,"Tak tun tuang")
                ki8.sendText(msg.to,"Pasti cantik sekali")
                ki9.sendText(msg.to,"yiha")
                ki10.sendText(msg.to,"Kalau orang lain melihatku")
                ki.sendText(msg.to,"Tak tun tuang")
                ki2.sendText(msg.to,"Badak aku taba bana")
                ki3.sendText(msg.to,"Tak tun tuang")
                ki4.sendText(msg.to,"Tak tuntuang")
                ki5.sendText(msg.to,"Tapi kalau langsuang diidu")
                ki6.sendText(msg.to,"Tak tun tuang")
                ki7.sendText(msg.to,"Atagfirullah baunya")
                ki8.sendText(msg.to,"Males lanjutin ah")
                ki9.sendText(msg.to,"Sepi bat")
                ki10.sendText(msg.to,"Iya sepi udah udah")
                ki.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                ki2.sendText(msg.to,"Nah")
                ki3.sendText(msg.to,"Mending gua makan dulu")
                ki4.sendText(msg.to,"Siyap")
                ki5.sendText(msg.to,"Okeh")
                ki6.sendText(msg.to,"Katanya owner kita Jomblo ya")
                ki7.sendText(msg.to,"Iya emang")
                ki8.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                ki9.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Group image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ki.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ki.getContact(key1)
                cu = ki.channel.getCover(key1)
                try:
                    ki.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    ki.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ki.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    ki2.sendText(msg.to,"Profile Picture " + contact.displayName)
                    ki3.sendImageWithURL(msg.to,image)
                    ki4.sendText(msg.to,"Cover " + contact.displayName)
                    ki5.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                        
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
                ki.sendText(msg.to,van)
                ki2.sendText(msg.to,van)
                ki3.sendText(msg.to,van)
                ki4.sendText(msg.to,van)
                ki5.sendText(msg.to,van)
                ki6.sendText(msg.to,van)
                ki7.sendText(msg.to,van)
                ki8.sendText(msg.to,van)
                ki9.sendText(msg.to,van)
                ki10.sendText(msg.to,van)
                
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ki.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ki.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        ki2.removeAllMessages(op.param2)
                        ki3.removeAllMessages(op.param2)
                        ki4.removeAllMessages(op.param2)
                        ki5.removeAllMessages(op.param2)
                        ki6.removeAllMessages(op.param2)
                        ki7.removeAllMessages(op.param2)
                        ki8.removeAllMessages(op.param2)
                        ki9.removeAllMessages(op.param2)
                        ki10.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"Done")
                        ki2.sendText(msg.to,"Done")
                        ki3.sendText(msg.to,"Done")
                        ki4.sendText(msg.to,"Done")
                        ki5.sendText(msg.to,"Done")
                        ki6.sendText(msg.to,"Done")
                        ki7.sendText(msg.to,"Done")
                        ki8.sendText(msg.to,"Done")
                        ki9.sendText(msg.to,"Done")
                        ki10.sendText(msg.to,"All Messages From Owner To Bot Have Been Deleted Successfully")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")      
                
            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki2.sendAudio(msg.to,"hasil.mp3")   


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki3.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki4.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ki5.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                ki2.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                ki2.sendText(msg.to,"Simisimi Di Nonaktifkan")
                
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    ki.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                                        
            elif msg.text in ["Notif on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off(p′︵‵。)")
                        
            elif "Sider on" in msg.text:
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
                cl.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Heh Belom Di Set")      
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ki.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Protect on🔓✍")
                        ki2.sendText(msg.to,"Auto Protect on🔓✍")
                        ki3.sendText(msg.to,"Auto Protect on🔓✍")
                        ki4.sendText(msg.to,"Auto Protect on🔓✍")
                        ki5.sendText(msg.to,"Auto Protect on🔓✍")
                        ki6.sendText(msg.to,"Auto Protect on🔓✍")
                        ki7.sendText(msg.to,"Auto Protect on🔓✍")
                        ki8.sendText(msg.to,"Auto Protect on🔓✍")
                        ki9.sendText(msg.to,"Auto Protect on🔓✍")
                        ki10.sendText(msg.to,"Auto Protect on🔓✍")
                    else:
                        ki.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Protect on🔓✍")
                        ki2.sendText(msg.to,"Auto Protect on🔓✍")
                        ki3.sendText(msg.to,"Auto Protect on🔓✍")
                        ki4.sendText(msg.to,"Auto Protect on🔓✍")
                        ki5.sendText(msg.to,"Auto Protect on🔓✍")
                        ki6.sendText(msg.to,"Auto Protect on🔓✍")
                        ki7.sendText(msg.to,"Auto Protect on🔓✍")
                        ki8.sendText(msg.to,"Auto Protect on🔓✍")
                        ki9.sendText(msg.to,"Auto Protect on🔓✍")
                        ki10.sendText(msg.to,"Auto Protect on🔓✍")
                    else:
                        ki.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Qr code On✍")
                    else:
                        ki2.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Already on✍")
                    else:
                        ki2.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'invitepro on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Invite protect On✍")
                    else:
                        ki.sendText(msg.to,"Hal ini sudah terbuka ô€¨����👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Already on✍")
                    else:
                        ki.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Cancel Protect on✍ 􀜁􀇔􏿿👈")
                    else:
                        ki2.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Already on✍")
                    else:
                        ki2.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Login on✍")
                    else:
                        ki.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Already on✍")
                    else:
                        ki.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'kicker on':
                if wait["joinkick"] == True:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Kicker Auto set On✍")
                    else:
                        ki2.sendText(msg.to,"Kicker Auto set On✍")
                else:
                    wait["joinkick"] = True
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Kicker Auto set On✍")
                    else:
                        ki2.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'kicker off':
                if wait["joinkick"] == False:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Kicker Auto set Off✍")
                    else:
                        ki2.sendText(msg.to,"Kicker Auto set Off✍")
                else:
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Kicker Auto set Off✍")
                    else:
                        ki2.sendText(msg.to,"It is already Off ô€¨")
            elif msg.text.lower() == 'autokick on':
                if wait["AutoKick"] == True:
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Auto Kick set On✍")
                    else:
                        ki3.sendText(msg.to,"Auto Kick set On✍")
                else:
                    wait["AutoKick"] = True
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Auto Kick set On✍")
                    else:
                        ki3.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'autokick off':
                if wait["AutoKick"] == False:
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Auto Kick set Off✍")
                    else:
                        ki3.sendText(msg.to,"Auto Kick set Off✍")
                else:
                    wait["AutoKick"] = False
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Auto Kick set Off✍")
                    else:
                        ki3.sendText(msg.to,"It is already Off ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = ki.getBlockedContactIds()
                ki.sendText(msg.to, "Please wait ✍")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Allprotect on","Mode on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"All Protect on🔓✍")
                        ki2.sendText(msg.to,"All Protect on🔓✍")
                        ki3.sendText(msg.to,"All Protect on🔓✍")
                        ki4.sendText(msg.to,"All Protect on🔓✍")
                        ki5.sendText(msg.to,"All Protect on🔓✍")
                        ki6.sendText(msg.to,"All Protect on🔓✍")
                        ki7.sendText(msg.to,"All Protect on🔓✍")
                        ki8.sendText(msg.to,"All Protect on🔓✍")
                        ki9.sendText(msg.to,"All Protect on🔓✍")
                        ki10.sendText(msg.to,"All Protect on🔓✍")
                    else:
                        ki.sendText(msg.to,"")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Invite Protect set On✍")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Cancel Protect set On✍")
                    else:
                        ki2.sendText(msg.to,"Cancel Protect set On✍")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Cancel Protect set On✍")      
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Protect set On✍")
                    else:
                        ki3.sendText(msg.to,"Protect set On✍")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Protect set On✍")
                    else:
                        ki3.sendText(msg.to,"Protect set on✍")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        ki4.sendText(msg.to,"Link Protect set On✍")
                    else:
                        ki4.sendText(msg.to,"Link Protect set On✍")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        ki4.sendText(msg.to,"Link Protect set On✍")
                    else:
                        ki4.sendText(msg.to,"Link Protect set On✍")
                if wait["joinkick"] == True:
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Kicker Protect set On✍")
                    else:
                        ki5.sendText(msg.to,"Kicker Protect set On✍")
                else:
                    wait["joinkick"] = True
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Kicker Protect set On✍")
                    else:
                        ki5.sendText(msg.to,"Kicker Protect set On✍")
                if wait["AutoKick"] == True:
                    if wait["lang"] == "JP":
                        ki6.sendText(msg.to,"Auto Kick set On✍")
                    else:
                        ki6.sendText(msg.to,"Auto Kick set On✍")
                else:
                    wait["AutoKick"] = True
                    if wait["lang"] == "JP":
                        ki6.sendText(msg.to,"Auto Kick set On✍")
                    else:
                        ki6.sendText(msg.to,"Auto Kick set On✍")
            elif msg.text in ["Allprotect off","Mode off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"All Protect off🔓✍")
                        ki2.sendText(msg.to,"All Protect off🔓✍")
                        ki3.sendText(msg.to,"All Protect off🔓✍")
                        ki4.sendText(msg.to,"All Protect off🔓✍")
                        ki5.sendText(msg.to,"All Protect off🔓✍")
                        ki6.sendText(msg.to,"All Protect off🔓✍")
                        ki7.sendText(msg.to,"All Protect off🔓✍")
                        ki8.sendText(msg.to,"All Protect off🔓✍")
                        ki9.sendText(msg.to,"All Protect off🔓✍")
                        ki10.sendText(msg.to,"All Protect off🔓✍")
                    else:
                        ki.sendText(msg.to,"")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Invite Protect set Off✍")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Cancel Protect set Off✍")
                    else:
                        ki2.sendText(msg.to,"Cancel Protect set Off✍")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Cancel Protect set Off✍")      
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Protect set Off✍")
                    else:
                        ki3.sendText(msg.to,"Protect set Off✍")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ki3.sendText(msg.to,"Protect set Off✍")
                    else:
                        ki3.sendText(msg.to,"Protect set Off✍")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        ki4.sendText(msg.to,"Link Protect set Off✍")
                    else:
                        ki4.sendText(msg.to,"Link Protect set Off✍")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        ki4.sendText(msg.to,"Link Protect set Off✍")
                    else:
                        ki4.sendText(msg.to,"Link Protect set Off✍")
                if wait["joinkick"] == False:
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Kicker Protect set Off✍")
                    else:
                        ki5.sendText(msg.to,"Kicker Protect set Off✍")
                else:
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Kicker Protect set Off✍")
                    else:
                        ki5.sendText(msg.to,"Kicker Protect set Off✍")
                if wait["AutoKick"] == False:
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Auto Kick set Off✍")
                    else:
                        ki5.sendText(msg.to,"Auto Kick set Off✍")
                else:
                    wait["AutoKick"] = False
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Auto Kick set Off✍")
                    else:
                        ki5.sendText(msg.to,"Auto Kick set Off✍")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Join set Off✍")
                    else:
                        ki.sendText(msg.to,"Auto Join set Off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Join set Off✍")
                    else:
                        ki.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text.lower() == 'kicker off':
                if wait["joinkick"] == False:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Kicker Auto set Off✍")
                    else:
                        ki2.sendText(msg.to,"Kicker Auto set Off✍")
                else:
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Kicker Auto set Off✍")
                    else:
                        ki.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Protect off🔓✍")
                        ki2.sendText(msg.to,"Auto Protect off🔓✍")
                        ki3.sendText(msg.to,"Auto Protect off🔓✍")
                        ki4.sendText(msg.to,"Auto Protect off🔓✍")
                        ki5.sendText(msg.to,"Auto Protect off🔓✍")
                        ki6.sendText(msg.to,"Auto Protect off🔓✍")
                        ki7.sendText(msg.to,"Auto Protect off🔓✍")
                        ki8.sendText(msg.to,"Auto Protect off🔓✍")
                        ki9.sendText(msg.to,"Auto Protect off🔓✍")
                        ki10.sendText(msg.to,"Auto Protect off🔓✍")
                    else:
                        ki.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Protect off🔓✍")
                        ki2.sendText(msg.to,"Auto Protect off🔓✍")
                        ki3.sendText(msg.to,"Auto Protect off🔓✍")
                        ki4.sendText(msg.to,"Auto Protect off🔓✍")
                        ki5.sendText(msg.to,"Auto Protect off🔓✍")
                        ki6.sendText(msg.to,"Auto Protect off🔓✍")
                        ki7.sendText(msg.to,"Auto Protect off🔓✍")
                        ki8.sendText(msg.to,"Auto Protect off🔓✍")
                        ki9.sendText(msg.to,"Auto Protect off🔓✍")
                        ki10.sendText(msg.to,"Auto Protect off🔓✍")
                    else:
                        ki.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Qr protect off✍")
                    else:
                        ki.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Qr protect off✍")
                    else:
                        ki.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Invitepro off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Invite Protect Off🛡")
                    else:
                        ki.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Invite Protect Off🛡")
                    else:
                        ki.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Cancel Protect Off📌")
                    else:
                        ki.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Cancel Protect off✍")
                    else:
                        ki.sendText(msg.to,"It is already open ô€œ👈")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                          ki.sendText(msg.to,"ItuItu Off")
                        else:
                            ki.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Auto leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Leave on🛡")
                    else:
                        ki.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Leave On ✍")
                    else:
                        ki.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Auto leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave off🛡")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Leave Off ✍")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Joincancel on","Joincancel:on"]:
                if wait["AutoJoinCancel"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Join Cancel set on✍")
                    else:
                        ki.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Join Cancel set On✍")
                    else:
                        ki.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Joincancel off","Joincancel:off"]:
                if wait["AutoJoinCancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Cancel set Off✍")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["AutoJoinCancel"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Auto Join Cancel set Off ✍")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Share on ✍ 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ready On👈")
                    else:
                        cl.sendText(msg.to,"Ready On👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Share off ✍ 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ready Off👈")
                    else:
                        cl.sendText(msg.to,"Ready Off👈")
            elif msg.text in ["Set"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠🔐Sambutan : 📱On\n"
		else:md+="╠🔐Sambutan : 📴Off\n"
		if wait["likeOn"] == True: md+="╠🔐Auto Like : 📱On\n"
		else:md+="╠🔐Auto Like : 📴Off\n"
		if wait["timeline"] == True: md+="╠🔐Share : 📱On\n"
		else:md+="╠🔐Share : 📴Off\n"
		if wait["autoAdd"] == True: md+="╠🔐Auto Add : 📱On\n"
		else:md+="╠🔐Auto Add : 📴Off\n"
		if wait["autoJoin"] == True: md+="╠🔐Auto Join : 📱On\n"
                else: md +="╠🔐Auto Join : 📴Off\n"
                if wait["leaveRoom"] == True: md+="╠🔐Auto Leave : 📱On\n"
		else:md+="╠🔐Auto Leave : 📴Off\n"		
		if wait["AutoJoinCancel"] == True: md+="╠🔐Auto Join Cancel : 📱On\n"
                else: md +="╠🔐Auto Join Cancel : 📴Off\n"                
		if wait["contact"] == True: md+="╠🔐Info Contact : 📱On\n"
		else: md+="╠🔐Info Contact : 📴Off\n"
                if wait["cancelprotect"] == True:md+="╠🔐Auto Cancel : 📱On\n"
                else: md+= "╠🔐Auto Cancel : 📴Off\n"
                if wait["inviteprotect"] == True:md+="╠??Invite Protect : 📱On\n"
                else: md+= "╠🔐Invite Protect : 📴Off\n"                
		if wait["protect"] == True: md+="╠🔐Protect Mode : 📱On\n"
		else:md+="╠🔐Protect Mode : 📴Off\n"
		if wait["linkprotect"] == True: md+="╠🔐Link Protect : 📱On\n"
		else:md+="╠🔐Link Protect : 📴Off\n"			
		if wait["AutoKick"] == True: md+="╠🔐Auto Kick : 📱On\n"
		else:md+="╠🔐Auto Kick : 📴Off\n"
		if wait["joinkick"] == True: md+="╠🔐Kick Joiners : 📱On\n"
		else:md+="╠🔐Kick Joiners : 📴Off\n"		
		if wait["alwaysRead"] == True: md+="╠🔐Always Read : 📱On\n"
		else:md+="╠🔐Always Read: 📴Off\n"
		if wait["detectMention"] == True: md+="╠🔐Auto Respon1 : 📱On\n"
		else:md+="╠🔐Auto Respon1 : 📴Off\n"	
		if wait["detectMention2"] == True: md+="╠🔐Auto Respon2 : 📱On\n"
		else:md+="╠🔐Auto Respon2 : 📴Off\n"		
		if wait["detectMention3"] == True: md+="╠🔐Auto Respon3 : 📱On\n"
		else:md+="╠🔐Auto Respon3 : 📴Off\n"		
		if wait["detectMention4"] == True: md+="╠🔐Auto Respon4 : 📱On\n"
		else:md+="╠🔐Auto Respon4 : 📴Off\n"		
		if wait["detectMention5"] == True: md+="╠🔐Auto Respon5 : 📱On\n"
		else:md+="╠🔐Auto Respon5 : 📴Off\n"		
		if wait["detectMention6"] == True: md+="╠🔐Auto Respon6 : 📱On\n"
		else:md+="╠🔐Auto Respon6 : 📴Off\n"		
		if wait["kickMention"] == True: md+="╠🔐Auto Respon Kick : 📱On\n"
		else:md+="╠🔐Auto Respon Kick : 📴Off\n"		
		if wait["commentOn"] == True: md+="╠🔐Auto Comment : 📱On\n"
		else:md+="╠🔐Auto Comment Kick : 📴Off\n"		
		if wait["sticker"] == True: md+="╠🔐Detect Sticker : 📱On\n"
		else:md+="╠🔐Detect Sticker : 📴Off\n"		
		if wait["Sider"] == True: md+="╠🔐Detect Sider : 📱On\n"
		else:md+="╠🔐Detect Sider : 📴Off\n"		
		if wait["Mimic"] == True: md+="╠🔐Mimic Mode : 📱On\n"
		else:md+="╠🔐Mimic Mode : 📴Off\n"
		if wait["Simi"] == True: md+="╠🔐Simisimi : 📱On\n"
		else:md+="╠🔐Simisimi: 📴Off\n"		
                cl.sendText(msg.to,"╔════════════════════\n""║    ☆☞ Re̶y̶Pr̶o̶  Setting ☜☆\n""╠════════════════════\n"+md+"╚════════════════════")
                eltime = time.time() - mulai
                van = "Runtime :" +waktu(eltime)+"\nVersi Bot :2.6.4-ŠĒ『Python 2.7』"
                cl.sendText(msg.to,van)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                ki.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
                ki2.sendMessage(msg)
                ki2.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group  ")
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been refused")
                else:
                    ki.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")	
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                ki.sendText(msg.to,h)
            elif 'Blank' in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Reiyan,'"}
                ki3.sendMessage(msg)
            elif msg.text in ["Out"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    ki10.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki.sendText(msg.to,"Declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Auto add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                ki.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                ki2.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    ki.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Come off")
                    else:
                        ki.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Off👈")
                    else:
                        ki.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can't be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif "Rey gurl" in msg.text:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"URL on ✍")
                else:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        ki2.sendText(msg.to,"Can not be used for groups other than ô€œ")

            elif "Rey curl" in msg.text:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    ki.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"URL Closed ✍")
                else:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        ki2.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = True
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.0)
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
                                    ki3.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)

            elif msg.text == "Sider":
                    cl.sendText(msg.to, "hmm..")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text == "Read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "== Bakekok Sider == %s\nthat's it\n\nPeople who have ignored reads\n%skampret lo sider. ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")						

#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Add Staff @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove Staff @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "=>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
#-----------------------------------------------------------

            elif ("Vk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Contact " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
#----------------------------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "Cek pm @" in msg.text:
                _name = msg.text.replace("Cek pm @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(msg.to, "Done")
                       ki2.sendText(msg.to, "Done")
                       ki3.sendText(msg.to, "Done")
                       ki4.sendText(msg.to, "Done")
                       ki5.sendText(msg.to, "Done")
                       ki6.sendText(msg.to, "Done")
                       ki7.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "Hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki6.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki7.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki.sendText(msg.to, "Done")
                       ki2.sendText(msg.to, "Done")
                       ki3.sendText(msg.to, "Done")
                       ki4.sendText(msg.to, "Done")
                       ki5.sendText(msg.to, "Done")
                       ki6.sendText(msg.to, "Done")
                       ki7.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------)
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Bosque")
                   except:
                      pass
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    kk.sendText(msg.to,"Error")
#-----------------------------------------------------------

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
                                    

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Bot restart","Reboot"]:
		    if msg.from_ in admsa:
		        cl.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki2.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki3.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki4.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki5.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki6.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki7.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki8.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki9.sendText(msg.to,"🔄ʀᴇsᴛᴀʀᴛɪɴɢ...")
		        ki10.sendText(msg.to,"🔄sᴜᴄᴄᴇss ᴛᴏ ʀᴇsᴇᴛ ᴛʜᴇ ᴘʀᴏɢʀᴀᴍ☑")
		        restart_program()
		        print "@Restart"
		    else:
		        ki.sendText(msg.to, "No Access")
		
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                cl.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Allcopy"]:
                wait["botcopy"] = True
                ki.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["'Steal contact"]:
                wait["steal"] = True
                ki.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                cl.sendText(msg.to,"Send Contact") 
                    
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                cl.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Sticker off"]:
                wait["sticker"] = False
                cl.sendText(msg.to,"Sticker ID Detect Already Off.")  
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup1.pictureStatus)
                    ki.updateProfile(backup1)
                    ki2.updateDisplayPicture(backup2.pictureStatus)
                    ki2.updateProfile(backup2)
                    ki3.updateDisplayPicture(backup3.pictureStatus)
                    ki3.updateProfile(backup3)
                    ki4.updateDisplayPicture(backup4.pictureStatus)
                    ki4.updateProfile(backup4)
                    ki5.updateDisplayPicture(backup5.pictureStatus)
                    ki5.updateProfile(backup5)
                    ki6.updateDisplayPicture(backup6.pictureStatus)
                    ki6.updateProfile(backup6)
                    ki7.updateDisplayPicture(backup7.pictureStatus)
                    ki7.updateProfile(backup7)
                    ki8.updateDisplayPicture(backup8.pictureStatus)
                    ki8.updateProfile(backup8)
                    ki9.updateDisplayPicture(backup9.pictureStatus)
                    ki9.updateProfile(backup9)
                    ki10.updateDisplayPicture(backup10.pictureStatus)
                    ki10.updateProfile(backup10)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------<------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif msg.text in ["Rey Sp","Speed Bot","speed"]:
                start = time.time()
                ki.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki10.sendText(msg.to, "%sseconds" % (elapsed_time))

#-----------------------------------------------------------
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                cl.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"

#-------------------------------------------------------------------

#------------------------------------------------------------------	
            elif "Getcover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "Getpict @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"		
 #------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "➡" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak ada")
                        return
                    for jj in matched_list:
                        try:
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "1997" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("1997","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    ki.sendText(msg.to,"Test anu")
                    ki2.sendText(msg.to,"Misi-Misi")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
    
            elif msg.text in ["Mangat","B"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == ["reypro"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket) 
                        time.sleep(0.0)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["ReyPro"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket) 
                        time.sleep(0.0)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)                    
                        time.sleep(0.0)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)

            elif msg.text.lower() == 'rey invitebot':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    
            elif msg.text.lower() in ["pap owner","pap ryan"]:
                                link = ["http://dl.profile.line-cdn.net/0hsaE-74FqLE54VACDRjRTGUQRIiMPeioGAGVrLlpcIisHM2gaRjFrfVUGIioANj4RQDM0Lw8EJi5c"]
                                pilih = random.choice(link)
                                ki.sendImageWithURL(msg.to,pilih)
                                
            elif msg.text.lower() in ["pap anu","pap ryan"]:
                                link = ["http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=u6eea92950c109508a43dd97f9f3b8b54&oid=76642d6b2fb679fadf93730441d58f44"]
                                pilih = random.choice(link)
                                ki.sendImageWithURL(msg.to,pilih)
                                
            elif msg.text.lower() in ["pap anu2","pap ryan"]:
                                link = ["http://dl.profile.line-cdn.net/0hWoBP1xnKCEB_KSSNrS53F0NsBi0IBw4IB0gTcgohVXhWGB0WQkdDJ1N5U3IHTEcQFEcQJAkgBXRX"]
                                pilih = random.choice(link)
                                ki.sendImageWithURL(msg.to,pilih)
                                
            elif msg.text.lower() in ["pap admin","pap raisa"]:
                                link = ["http://dl.profile.line-cdn.net/0hd00mj6gAOx8NFBfScO5ESDFRNXJ6Oj1XdXB8Ky9GYn0jcH1PNXtze38cYXhzJS8dZXJxLngdYSsn"]
                                pilih = random.choice(link)
                                ki.sendImageWithURL(msg.to,pilih)
                                
            elif "Nspam: " in msg.text:
                  bctxt = msg.text.replace("Nspam: ", "")
                  t = 15
                  while(t):
                    ki.sendText(msg.to, (bctxt))
                    t-=1
 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 50
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam1: " in msg.text:
                  bctxt = msg.text.replace("Spam1: ", "")
                  t = 100
                  while(t):
                    ki.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam2: " in msg.text:
                  bctxt = msg.text.replace("Spam2: ", "")
                  t = 200
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam3: " in msg.text:
                  bctxt = msg.text.replace("Spam3: ", "")
                  t = 300
                  while(t):
                    ki2.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam4: " in msg.text:
                  bctxt = msg.text.replace("Spam4: ", "")
                  t = 400
                  while(t):
                    ki3.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "Spam5: " in msg.text:
                  bctxt = msg.text.replace("Spam5: ", "")
                  t = 500
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif "GhostSpam: " in msg.text:
                  bctxt = msg.text.replace("GhostSpam: ", "")
                  t = 1000
                  while(t):
                    ki5.sendText(msg.to, (bctxt))
                    t-=1
#-----------------------------------------------
            elif "Rey1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Rey2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Rey3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Rey4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Rey5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Rey6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "Rey7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)         
#-----------------------------------------------
            elif msg.text in ["ReyOut"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki.sendText(msg.to,"Good bye  "  +  str(ginfo.name)  + "\nBot dipaksa keluar Oleh Owner")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)         
                        ki10.leaveGroup(msg.to)           
                    except:
                        pass
#-----------------------------------------------
            elif "Rey1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------                   
            elif "Rey8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------                   
            elif "Rey9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------                      
            elif "Rey10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Rey Key" in msg.text:
                ki.sendText(msg.to,"""      􀜁􀇔􏿿􀜁􀇔􏿿 CYBER Rey BOT [Rey] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Rey1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n??􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Rey1 Gift]\n􀜁􀇔􏿿[Rey1 bye]\n\n   
  
        
  
Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ
""")
                ki2.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿  􀜁􀇔􏿿􀜁􀇔􏿿 CYBER Rey BOT [Rey] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Rey1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Rey1 Gift]\n􀜁􀇔􏿿[Rey1 bye]\n\n   
        
  
Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ
""")
                ki3.sendText(msg.to,"""     􀜁􀇔􏿿 􀜁􀇔􏿿􀜁􀇔􏿿 CYBER Rey BOT [Rey] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Rey1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Rey1 Gift]\n􀜁􀇔􏿿[Rey1 bye]\n\n   
        
  
Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ
""")
                ki4.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿  􀜁􀇔??􀜁􀇔􏿿 CYBER Rey BOT [Rey] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Rey1 in]\n􀜁??􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Rey1 Gift]\n􀜁􀇔??[Rey1 bye]\n\n        
        
  
Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ
""")
                ki5.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔??  􀜁􀇔􏿿􀜁􀇔􏿿 CYBER Rey BOT [Rey] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Rey1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n??􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔??[Respons]\n􀜁􀇔􏿿[Rey1 Gift]\n􀜁􀇔??[Rey1 bye]\n\n   
        
  
Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ
""")
                ki6.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿  􀜁􀇔􏿿􀜁􀇔􏿿 CYBER Rey BOT [Rey] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Rey1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Rey1 Gift]\n􀜁􀇔􏿿[Rey1 bye]\n\n   
        g
  
Re̶y̶Pr̶o̶ᵃˢⁱˢᵗ
""")
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Hosgeldiniz" + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.admin.displayName )
            elif "Rey Say " in msg.text:
				bctxt = msg.text.replace("Rey Say ","")
				ki2.sendText(msg.to,(bctxt))
            elif "BotBc: " in msg.text:
		        bc = msg.text.replace("BotBc: ","")
		        gid = ki.getGroupIdsJoined()
		        if msg.from_ in admsa:
		            for i in gid:
			        ki.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~s.k.9.7")
		            ki.sendText(msg.to,"Success BC BosQ")
		        else:
		            ki.sendText(msg.to,"Khusus Ryan")
            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = cl.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      cl.sendText(manusia, (bctxt))
                      t-=1
            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = cl.getAllContactIds()
                  for manusia in orang:
                    cl.sendText(manusia, (broadcasttxt))
            elif msg.text in ["Cancel"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")
            elif "say" in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				k8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki11.sendText(msg.to,(bctxt))
				ki12.sendText(msg.to,(bctxt))
				ki13.sendText(msg.to,(bctxt))
				ki14.sendText(msg.to,(bctxt))
				ki15.sendText(msg.to,(bctxt))
				ki16.sendText(msg.to,(bctxt))
				ki17.sendText(msg.to,(bctxt))
				ki18.sendText(msg.to,(bctxt))
				ki19.sendText(msg.to,(bctxt))
				ki20.sendText(msg.to,(bctxt))
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki7.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki8.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki9.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki10.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki11.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki12.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki13.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki14.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki15.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki16.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki17.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki18.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki19.sendText(msg.to,"Ping 􀜁􀇔??")
                ki20.sendText(msg.to,"Ping 􀜁􀇔􏿿")
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        
                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                 
                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
            except:
                pass
                
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
            
            
        if op.type == 17:
          if wait["joinkick"] == True:
            if op.param2 in admin:
              if op.param2 in Bots:
                return
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            print "MEMBER JOIN KICK TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            cl.sendText(op.param1,"Good Bye " + cl.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP"
              
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
