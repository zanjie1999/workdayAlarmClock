# 工作日闹钟


Python 2.7


设置一个计划任务到点执行此程序,程序会自动判断今天是不是工作日(需要联网),工作日就按设定闹钟类型执行,不是工作日就退出


## 设置


Server酱 的url换成你自己的


三种闹钟类型(type)
1. 执行shell
2. 执行shell来播放路径的下的指定音乐文件
3. 执行shell随机播放路径目录下的mp3


使用类型2时的音乐文件名(musicFile)


存放音乐的文件夹路径(path)


播放器的shell执行路径(shell)


### 例子


Linux:


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


Windows:


    ## 设置闹钟类型
    # 1:执行shell
    # 2:执行shell来播放路径的下的指定音乐文件
    # 3:执行shell随机播放路径目录下的mp3
    type = 3

    # 路径
    path = u'D:/资料/音乐'

    # 音乐文件
    musicFile = u''

    # 执行shell
    shell = u''
