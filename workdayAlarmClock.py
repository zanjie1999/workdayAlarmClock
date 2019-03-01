# -*- coding: UTF-8 -*-

# 工作日闹钟
# 版本: 3.0

import random
import os
import json
import urllib2
import urllib
import time
import platform
import sys

reload(sys)
if platform.system() == u'Windows':
    sys.setdefaultencoding('gbk')
else:
    sys.setdefaultencoding('utf-8')


# 设置闹钟类型
# 1:执行shell
# 2:执行shell来播放路径的下的指定音乐文件
# 3:执行shell随机播放路径目录下的mp3
type = 3

# 随机抽取的数量
size = 2

# 路径
path = u'/home/sparkle/Music/'

# 音乐文件
musicFile = u''

# 执行shell
shell = u'/usr/bin/vlc --play-and-exit'


# 获取今日类型
def getDayType():
    url = 'http://api.goseek.cn/Tools/holiday?date=' + \
        time.strftime("%Y%m%d", time.localtime())
    try:
        data = json.load(urllib2.urlopen(url))
        return data['data']
    except BaseException:
        print('api ERROR')
        return 0


# 随机获取目录下的mp3
def getFile(p):
    dirL = []
    for name in os.listdir(p):
        if name.endswith(u'.mp3') or name.endswith(u'.MP3') or name.endswith(u'.flac') or name.endswith(u'.FLAC'):
            dirL.append(name)

    # dirL = os.listdir(p)
    # return dirL[random.randint(1, len(dirL)) - 1]
    if len(dirL) <= size:
        return dirL
    else:
        j = ''
        # 看看文件是否存在，有就读出来
        if os.path.exists(path + "workdayAlarmClock.json"):
            db = open(path + "workdayAlarmClock.json", 'r')
            j = db.read().strip()
            db.close()

        if j == '':
            print("db empty")
            j = '[]'
        if not (j.startswith('[') and j.endswith(']')):
            print("db error")
            j = '[]'
        played = json.loads(j)
        if len(played) > 0:
            if len(dirL) >= len(played) + size:
                # 筛选掉曾经放过的
                dirL = list(set(dirL).difference(set(played)))
            else:
                # 数量不够了重置曾经播放过的
                played = []

        # 随机抽取
        randomFile = random.sample(dirL, size)
        played += randomFile
        # 保存
        db = open(path + "workdayAlarmClock.json", 'w')
        db.write(json.dumps(played, ensure_ascii=False))
        db.close()

        return randomFile


# Server酱
def serverChan(p):
    url = u'https://sc.ftqq.com/'
    urllib2.urlopen(url, data=urllib.urlencode({
        'text': '工作日闹钟' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'desp': p
    }))


# 执行命令
def runShell(c):
    if path != u'':
        os.chdir(path)

    cmd = ""
    for i in c:
        #        if platform.system() == u'Windows':
        cmd += shell + u' "' + i.replace('"', '\"') + u'"; '
#        else:
#            cmd += shell + u" '" + i.replace("'","\'") + u"'; "

    print(cmd)
    os.system(cmd)

    serverChan('\n\n'.join(c))


# 判断是否工作日
dayType = getDayType()
if dayType == 0:
    if type == 1:
        runShell(u'')
    if type == 2:
        runShell(musicFile)
    if type == 3:
        runShell(getFile(path))

if dayType == 1:
    print('Weekend')
if dayType == 2:
    print('Holiday')
