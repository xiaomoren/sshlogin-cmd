#!/usr/bin/env
#coding=utf-8
__author__ = 'LIDA'

import paramiko
import optparse
import threading

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=2)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            #屏幕输出
            for o in out: #是否存在输出
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()

    except :
        print '%s\tError\n'%(ip)

'''
if __name__=='__main__':
    cmd = ['cat /etc/passwd']
    username = "root"
    passwd = "toor"    #密码
    threads = []   #多线程
    print "Begin......"
    ip = '10.10.10.95'
    ssh2(ip,username,passwd,cmd)
'''
def main():
    parser = optparse.OptionParser('usage%prog'+\
                                   '-i <target ip> -u <user> -p <passwd>' )
    parser.add_option('-i',dest='ip',type='string',help='specify ipaddress')
    parser.add_option('-u',dest='username',type='string',help='specify username')
    parser.add_option('-p', dest='passwd', type='string', help='specify passwd')
    (options,args)=parser.parse_args()
   # m = ['cat /etc/passwd']
    ip = options.ip
    username = options.username
    passwd = options.passwd
    if ip==None or username ==None or passwd == None:
        print parser.usage
    else:
        m=input()
        ssh2(ip, username, passwd, m)

if __name__=="__main__":
    main()
