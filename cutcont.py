#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
这个脚本是在一个内容过剩中，抽取自己想要的一段信息，是基于python2.X的
例子： python cutcont.py -i 1 -f data.txt -o email.txt -s ,
i是内容开始的索引
f:是那份内容过剩文件
o:是抽取信息后写到的文件
s:是以什么为分界点来截取，例子的是逗号（,）

i f o s 这四个参数必须齐
'''
import sys


# deal with parameters
def formatArgv():
    argvs = len(sys.argv)
    if argvs < 9:
        if argvs == 2:
            if sys.argv[1] =='-h' or sys.argv[1] == '-H':
                printHelp()
        print "[Error] parameter number error"
        printHelp()

    for a in range(1,argvs):
        if sys.argv[a].startswith('-'):
            option = sys.argv[a][1:]
            if option == 'f':
                filename = sys.argv[a+1]
            if option == 'i':
                contentIndex = sys.argv[a+1]
            if option == 's':
                splitStr = sys.argv[a+1]
            if option == 'o':
                outputfile = sys.argv[a+1]
            if option == 'h' or option == 'H':
                printHelp()
            try:
                if not sys.argv[a+2].startswith('-'):
                    print '[Error] parameter type error'
                    printHelp()
            except IndexError:
               pass
        else:
            pass
    return filename, contentIndex, splitStr, outputfile


# get target what we want. For example: email
def getTarget(filename, splitStr, contentIndex, outputfile):
    contentIndex = int(contentIndex)
    record = 0
    with open(filename) as f:
        for content in f.readlines():
            target = content.split(splitStr)[contentIndex].strip()
            with open(outputfile,'a') as e:
                e.write(target+ '\n')
            record += 1
    print 'Cut content successfully! record: '+ str(record)

def printHelp():
    print 'Example: python cutcont.py -i [0] -s [,] -f [data.txt] -o [email.txt]'
    print '-h       print help'
    print '-i       content index'
    print '-o       outputfile'
    print '-f       origin file'
    print '-s       divide str'
    sys.exit()

# main program
def main():
    (filename, contentIndex, splitStr,outputfile) = formatArgv()
    getTarget(filename, splitStr, contentIndex,outputfile)


if __name__ == '__main__':
    main()
    
