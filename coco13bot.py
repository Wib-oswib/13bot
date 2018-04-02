# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("Line帳號","Line密碼")
kicker01 = LINE("Line帳號","Line密碼")
kicker02 = LINE("Line帳號","Line密碼")
kicker03 = LINE("Line帳號","Line密碼")
kicker04 = LINE("Line帳號","Line密碼")
kicker05 = LINE("Line帳號","Line密碼")
kicker06 = LINE("Line帳號","Line密碼")
kicker07 = LINE("Line帳號","Line密碼")
kicker08 = LINE("Line帳號","Line密碼")
kicker09 = LINE("Line帳號","Line密碼")
kicker10 = LINE("Line帳號","Line密碼")
kicker11 = LINE("Line帳號","Line密碼")
kicker12 = LINE("Line帳號","Line密碼")
print ("======登入成功=====")
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
clMID = cl.profile.mid
kicker01MID = kicker01.profile.mid
kicker02MID = kicker02.profile.mid
kicker03MID = kicker03.profile.mid
kicker04MID = kicker04.profile.mid
kicker05MID = kicker05.profile.mid
kicker06MID = kicker06.profile.mid
kicker07MID = kicker07.profile.mid
kicker08MID = kicker08.profile.mid
kicker09MID = kicker09.profile.mid
kicker10MID = kicker10.profile.mid
kicker11MID = kicker10.profile.mid
kicker12MID = kicker10.profile.mid
KAC = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11,kicker12]
admin = ['u28d781fa3ba9783fd5144390352b0c24',clMID,kicker10MID,kicker01MID,kicker02MID,kicker03MID,kicker04MID,kicker05MID,kicker06,kicker07MID,kicker08MID,kicker09MID,kicker10MID,kicker11MID,kicker12MID]
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """
╔═══════════
♥ ✿ 修羅特製指令表 ✿ ♥
════✪〘 查看指令表 〙✪════
↪ 「Help」查看全部指令
↪ 「HelpBot」查看機器指令
════✪〘 狀態 〙✪═══════
↪ 「Rebot」重新啟動機器
↪ 「Runtime」查看機器運行時間
↪ 「Speed」查看機器速度
↪ 「Set」查看設定
↪ 「About」查看自己的狀態
↪ 「K1-K12 About」查看機器的狀態
════✪〘 設定 〙✪═══════
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Read On/Off」自動已讀 打開/關閉
↪ 「Inviteprotect On/Off」邀請保護 打開/關閉
↪ 「Qr On/Off」保護 打開/關閉
↪ 「Protect On/Off」保護 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
════✪〘 踢人 〙✪═══════
↪ 「Kickall」翻群
↪ 「Speed/Test」測速
↪ 「Alljoin/Bot bye」機器進群/退群
↪ 「Gcancel/Cancel」取消群組/成員邀請
↪ 「Unban/Ban @」標注解除/加入黑單
↪ 「Clear Ban」清除全部黑單
↪ 「banlist」查看黑單
↪ 「Kill Ban」踢出黑單
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessage
def helpmessagebot():
    helpMessageBot ="""
╔══〘 設定 〙✪═══════
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Read On/Off」自動已讀 打開/關閉
↪ 「Inviteprotect On/Off」邀請保護 打開/關閉
↪ 「Qr On/Off」保護 打開/關閉
↪ 「Protect On/Off」保護 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessageBot
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(param2)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                kicker01.findAndAddContactsByMid(op.param1)
                kicker02.findAndAddContactsByMid(op.param1)
                kicker03.findAndAddContactsByMid(op.param1)
                kicker04.findAndAddContactsByMid(op.param1)
                kicker05.findAndAddContactsByMid(op.param1)
                kicker06.findAndAddContactsByMid(op.param1)
                kicker07.findAndAddContactsByMid(op.param1)
                kicker08.findAndAddContactsByMid(op.param1)
                kicker09.findAndAddContactsByMid(op.param1)
                kicker10.findAndAddContactsByMid(op.param1)
                kicker11.findAndAddContactsByMid(op.param1)
                kicker12.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker01.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker02.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker03.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker04.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker05.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker06.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker07.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker08.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker09.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker10.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker11.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker12.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            print ("[11]有人打開群組網址 群組名稱: " + str(group.name) + "\n" + op.param1 + "\n名字: " + contact.displayName)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    range.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param3)
                    range.choice(KAC).sendMessage(op.param1, "禁止邀請")
                    range.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        print ("進入群組: " + str(group.name))
                        cl.acceptGroupInvitation(op.param1)
                        if settings["kickerjoin"] == True:
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(op.param1)
                            kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if  msg.text.lower() == '/ti/g/':
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = trev.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                        kicker01.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker02.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker03.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker04.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker05.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker06.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker07.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker08.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker09.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker10.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker11.acceptGroupInvitationByTicket(group.id, ticket_id)
                        kicker12.acceptGroupInvitationByTicket(group.id, ticket_id)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][op.param2] = True
            else:
                pass
            if clMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker01MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker02.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker02.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker02.updateGroup(G)
                    invsend = 0
                    Ti = kicker02.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker02MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker03.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker03.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker03.updateGroup(G)
                    invsend = 0
                    Ti = kicker03.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker03MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker04.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker04.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker04.updateGroup(G)
                    invsend = 0
                    Ti = kicker04.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker04MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker05.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker05.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker05.updateGroup(G)
                    invsend = 0
                    Ti = kicker05.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker05MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker06.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker06.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker06.updateGroup(G)
                    invsend = 0
                    Ti = kicker06.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker06MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker07.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker07.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker07.updateGroup(G)
                    invsend = 0
                    Ti = kicker07.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker07MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker08.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker08.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker08.updateGroup(G)
                    invsend = 0
                    Ti = kicker08.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker08MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker09.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker09.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker09.updateGroup(G)
                    invsend = 0
                    Ti = kicker09.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker09MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kicker11.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker10.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker10.updateGroup(G)
                    invsend = 0
                    Ti = kicker10.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker10MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker11.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kicker12.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker11.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker11.updateGroup(G)
                    invsend = 0
                    Ti = kicker11.reissueGroupTicket(op.param1)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker11MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker12.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker12.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker12.updateGroup(G)
                    invsend = 0
                    Ti = kicker12.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker12MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            range.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker04.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker05.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker06.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker07.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker08.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker09.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker10.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker11.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker12.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
                kicker01.leaveRoom(op.param1)
                kicker02.leaveRoom(op.param1)
                kicker03.leaveRoom(op.param1)
                kicker04.leaveRoom(op.param1)
                kicker05.leaveRoom(op.param1)
                kicker06.leaveRoom(op.param1)
                kicker07.leaveRoom(op.param1)
                kicker08.leaveRoom(op.param1)
                kicker09.leaveRoom(op.param1)
                kicker10.leaveRoom(op.param1)
                kicker11.leaveRoom(op.param1)
                kicker12.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[顯示名稱]:\n" + msg.contentMetadata["顯示名稱"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[顯示名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "文章網址\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to, "u28d781fa3ba9783fd5144390352b0c24")
                elif text.lower() == 'helpbot':
                    helpMessageBot = helpMessageBot()
                    cl.sendMessage(to, str(helpMessageBot))
                elif 'alljoin' in text.lower():
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            kicker04.acceptGroupInvitationByTicket(to, Ti)
                            kicker05.acceptGroupInvitationByTicket(to, Ti)
                            kicker06.acceptGroupInvitationByTicket(to, Ti)
                            kicker07.acceptGroupInvitationByTicket(to, Ti)
                            kicker08.acceptGroupInvitationByTicket(to, Ti)
                            kicker09.acceptGroupInvitationByTicket(to, Ti)
                            kicker10.acceptGroupInvitationByTicket(to, Ti)
                            kicker11.acceptGroupInvitationByTicket(to, Ti)
                            kicker12.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            kicker04.acceptGroupInvitationByTicket(to, Ti)
                            kicker05.acceptGroupInvitationByTicket(to, Ti)
                            kicker06.acceptGroupInvitationByTicket(to, Ti)
                            kicker07.acceptGroupInvitationByTicket(to, Ti)
                            kicker08.acceptGroupInvitationByTicket(to, Ti)
                            kicker09.acceptGroupInvitationByTicket(to, Ti)
                            kicker10.acceptGroupInvitationByTicket(to, Ti)
                            kicker11.acceptGroupInvitationByTicket(to, Ti)
                            kicker12.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'bot bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            kicker01.leaveGroup(to)
                            kicker02.leaveGroup(to)
                            kicker03.leaveGroup(to)
                            kicker04.leaveGroup(to)
                            kicker05.leaveGroup(to)
                            kicker06.leaveGroup(to)
                            kicker07.leaveGroup(to)
                            kicker08.leaveGroup(to)
                            kicker09.leaveGroup(to)
                            kicker10.leaveGroup(to)
                            kicker11.leaveGroup(to)
                            kicker12.leaveGroup(to)
                        except:
                            pass
                elif text.lower() == 'test':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=5000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                    kicker01.sendMessage(to, 'ok')
                    kicker02.sendMessage(to, 'ok')
                    kicker03.sendMessage(to, 'ok')
                    kicker04.sendMessage(to, 'ok')
                    kicker05.sendMessage(to, 'ok')
                    kicker06.sendMessage(to, 'ok')
                    kicker07.sendMessage(to, 'ok')
                    kicker08.sendMessage(to, 'ok')
                    kicker09.sendMessage(to, 'ok')
                    kicker10.sendMessage(to, 'ok')
                    kicker11.sendMessage(to, 'ok')
                    kicker12.sendMessage(to, 'ok')
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部群組邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "已加入黑名單")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "已解除黑名單")
                                except:
                                    pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        cl.sendMessage(to, "以下是黑名單")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "->" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        klist = [kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11,kicker12]
                        kickers = random.choice(klist)
                        for jj in matched_list:
                            kickers.kickoutFromGroup(to, [jj])
                        cl.sendMessage(to, "黑名單以踢除")
                elif msg.text in ["全群掃黑"]:
                    gid = cl.getGroupIdsJoined()
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "掃黑結束")
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "SR修羅帝国--邪席£聯合拜访")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            klist=[cl,kicker01,kicker02,kicker03,kicker04,kicker05,kicker06,kicker07,kicker08,kicker09,kicker10,kicker11,kicker12]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "邀機 " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    num = 1
                    rand = 'SR修羅帝国--邪席£聯合拜访'
                    for var in range(0,num):
                        for target in targets:
                            cl.findAndAddContactsByMid(target)
                            kicker01.findAndAddContactsByMid(target)
                            kicker02.findAndAddContactsByMid(target)
                            kicker03.findAndAddContactsByMid(target)
                            kicker04.findAndAddContactsByMid(target)
                            kicker05.findAndAddContactsByMid(target)
                            kicker06.findAndAddContactsByMid(target)
                            kicker07.findAndAddContactsByMid(target)
                            kicker08.findAndAddContactsByMid(target)
                            kicker09.findAndAddContactsByMid(target)
                            kicker10.findAndAddContactsByMid(target)
                            kicker11.findAndAddContactsByMid(target)
                            kicker12.findAndAddContactsByMid(target)
                            cl.createGroup(rand, [target])
                            kicker01.createGroup(rand, [target])
                            kicker02.createGroup(rand, [target])
                            kicker03.createGroup(rand, [target])
                            kicker04.createGroup(rand, [target])
                            kicker05.createGroup(rand, [target])
                            kicker06.createGroup(rand, [target])
                            kicker07.createGroup(rand, [target])
                            kicker08.createGroup(rand, [target])
                            kicker09.createGroup(rand, [target])
                            kicker10.createGroup(rand, [target])
                            kicker11.createGroup(rand, [target])
                            kicker12.createGroup(rand, [target])
                    cl.sendMessage(to, 'ok')
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "設置已讀點")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "||已讀順序||%s\n\n||已讀的人||\n\n%s\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入SR設置已讀點")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=50000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'k1 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker01.getContact(owner)
                        contact = kicker01.getContact(clMID)
                        grouplist = kicker01.getGroupIdsJoined()
                        contactlist = kicker01.getAllContactIds()
                        blockedlist = kicker01.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker01.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker01.sendMessage(msg.to, str(e))
                elif text.lower() == 'k2 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker02.getContact(owner)
                        contact = kicker02.getContact(clMID)
                        grouplist = kicker02.getGroupIdsJoined()
                        contactlist = kicker02.getAllContactIds()
                        blockedlist = kicker02.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker02.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker02.sendMessage(msg.to, str(e))
                elif text.lower() == 'k3 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker03.getContact(owner)
                        contact = kicker03.getContact(clMID)
                        grouplist = kicker03.getGroupIdsJoined()
                        contactlist = kicker03.getAllContactIds()
                        blockedlist = kicker03.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker03.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker03.sendMessage(msg.to, str(e))
                elif text.lower() == 'k4 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker04.getContact(owner)
                        contact = kicker04.getContact(clMID)
                        grouplist = kicker04.getGroupIdsJoined()
                        contactlist = kicker04.getAllContactIds()
                        blockedlist = kicker04.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker04.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker04.sendMessage(msg.to, str(e))
                elif text.lower() == 'k5 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker05.getContact(owner)
                        contact = kicker05.getContact(clMID)
                        grouplist = kicker05.getGroupIdsJoined()
                        contactlist = kicker05.getAllContactIds()
                        blockedlist = kicker05.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker05.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker05.sendMessage(msg.to, str(e))
                elif text.lower() == 'k6 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker06.getContact(owner)
                        contact = kicker06.getContact(clMID)
                        grouplist = kicker06.getGroupIdsJoined()
                        contactlist = kicker06.getAllContactIds()
                        blockedlist = kicker06.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker06.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker06.sendMessage(msg.to, str(e))
                elif text.lower() == 'k7 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker07.getContact(owner)
                        contact = kicker07.getContact(clMID)
                        grouplist = kicker07.getGroupIdsJoined()
                        contactlist = kicker07.getAllContactIds()
                        blockedlist = kicker07.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker07.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker07.sendMessage(msg.to, str(e))
                elif text.lower() == 'k8 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker08.getContact(owner)
                        contact = kicker08.getContact(clMID)
                        grouplist = kicker08.getGroupIdsJoined()
                        contactlist = kicker08.getAllContactIds()
                        blockedlist = kicker08.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker08.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker08.sendMessage(msg.to, str(e))
                elif text.lower() == 'k9 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker09.getContact(owner)
                        contact = kicker09.getContact(clMID)
                        grouplist = kicker09.getGroupIdsJoined()
                        contactlist = kicker09.getAllContactIds()
                        blockedlist = kicker09.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker09.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker09.sendMessage(msg.to, str(e))
                elif text.lower() == 'k10 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker10.getContact(owner)
                        contact = kicker10.getContact(clMID)
                        grouplist = kicker10.getGroupIdsJoined()
                        contactlist = kicker10.getAllContactIds()
                        blockedlist = kicker10.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker10.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker10.sendMessage(msg.to, str(e))
                elif text.lower() == 'k11 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker11.getContact(owner)
                        contact = kicker11.getContact(clMID)
                        grouplist = kicker11.getGroupIdsJoined()
                        contactlist = kicker11.getAllContactIds()
                        blockedlist = kicker11.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker11.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker11.sendMessage(msg.to, str(e))
                elif text.lower() == 'k12 about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = kicker12.getContact(owner)
                        contact = kicker12.getContact(clMID)
                        grouplist = kicker12.getGroupIdsJoined()
                        contactlist = kicker12.getAllContactIds()
                        blockedlist = kicker12.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 修羅特製13聯機"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        kicker12.sendMessage(to, str(ret_))
                    except Exception as e:
                        kicker12.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 設定 ]"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 自動離開副本 ✅"
                        else: ret_ += "\n╠ 自動離開副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 ✅"
                        else: ret_ += "\n╠ 自動已讀 ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ 群組邀請保護 ✅"
                        else: ret_ += "\n╠ 群組邀請保護 ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠ 群組網址保護 ✅"
                        else: ret_ += "\n╠ 群組網址保護 ❌"
                        if settings["protect"] == True: ret_ += "\n╠ 群組保護 ✅"
                        else: ret_ += "\n╠ 群組保護 ❌"
                        if settings["contact"] == True: ret_ += "\n╠ 詳細資料 ✅"
                        else: ret_ += "\n╠ 詳細資料 ❌"
                        if settings["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✅"
                        else: ret_ += "\n╠ 查詢收回關閉 ❌"
                        ret_ += "\n╚══[ 設定 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開啟")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關閉")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開啟")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關閉")
                elif text.lower() == 'protect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開啟")
                elif text.lower() == 'protect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關閉")
                    cl.sendMessage(to, "Kick:1")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉")
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
            try:
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"%s\n[收回了]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[•]" + Name
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
