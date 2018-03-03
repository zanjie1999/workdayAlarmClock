# -*- coding: UTF-8 -*-

# 工作日闹钟
# 版本: 1.8

import platform
import sys

reload(sys)
if platform.system() == u'Windows':
    sys.setdefaultencoding('gbk')
else:
    sys.setdefaultencoding('utf-8')

import time
import urllib
import urllib2
import json
import os
import random

## 设置闹钟类型
# 1:执行shell
# 2:执行shell来播放路径的下的指定音乐文件
# 3:执行shell随机播放路径目录下的mp3
type = 3

# 路径
path = u'/home/pi/Music/'

# 音乐文件
musicFile = u''

# 执行shell
shell = u'export DISPLAY=:0.0 && lxterminal -t 闹钟 -e /usr/bin/play'

# 获取今日类型
def getDayType():
    return 0
    url = 'http://api.goseek.cn/Tools/holiday?date=' + time.strftime("%Y%m%d", time.localtime())
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
        if name.endswith(u'.mp3'):
            dirL.append(name)

    return dirL[random.randint(1, len(dirL)) - 1]


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
    
    if platform.system() == u'Windows':
        cmd = shell + u' \"' + c + u'\"'
    else:
        cmd = shell + u' \'' + c + u'\''
    
    try:
        print(cmd)
    except:
        print(u'')
    
    os.system(cmd)
    
    serverChan(c)


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
