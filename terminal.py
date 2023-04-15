import sys
import os
import time
from datetime import datetime
import calendar


size = os.get_terminal_size()
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day = datetime.today().day
weekday = datetime.today().weekday()
year = datetime.today().year
month = datetime.today().month
smonth = months[month]
cdir = "C:/"
cdir_recover = ""
fix = ''


def cmd_clear():
    os.system('cls')
def help():
    with open('help.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
        print(contents.rstrip())
def cmd_exit():
    print('logout')
    time.sleep(1)
    print('[进程已完成]')
    time.sleep(1)
    sys.exit()
def cal():
    print(f'     {smonth} {year}')
    print(' S  M Tu  W Th  F  S')
    clndr = calendar.month(year, month)
    print(print(clndr[39: ]))
cmd_clear()
print('Last login: ' + weekdays[weekday] + ' ' + months[month] + ' ' + str(day) + ' ' + time.strftime('%H:%M:%S') + ' on console')
print('Welcome to Darwin！')
while True:
    os.system(f'title Terminal - bash - {size.columns}x{size.lines}')
    run = input('VMTD:~ VMTD$ ')
    if run.isspace() == False and run != '':            # 判断是否为空
        if run == 'clear':                              # clear
            cmd_clear()
        elif run == 'pwd':
            print(cdir)
        elif run[:2].lower() == 'cd':                   # cd
            cdir_recover = cdir
            if run[4:6] == ':/':
                cdir = run
            elif run[4:5] == ':':
                continue
            else:
                if run[3:] == '..' or run[3:] == '../':
                    print(cdir)
                    cdir = list(cdir)
                    if cdir[-1] != '/':
                        for i in range(len(cdir) - cdir[::-1].index('/') + 1):
                            cdir.pop()
                        cdir = ''.join(cdir)
                    else:
                        cdir.pop()
                        for i in range(len(cdir) - cdir[::-1].index('/') + 1):
                            cdir.pop()
                        cdir = ''.join(cdir)
                    for i in range(len(cdir) - 1):
                        fix = fix + cdir[i]
                    cdir = fix
                elif cdir[-1] == '/':
                    cdir = cdir + run[3:]
                else:
                    cdir = cdir + '/' + run[3:]
                if os.path.exists(cdir) == False:
                    print(cdir + ": no such directory")
                    cdir = cdir_recover
        elif run[:4].lower() == 'echo':                 # echo
            print(run[5 :])
        elif run == 'exit':
            cmd_exit()
        elif run == 'help':
            help()
        elif run == 'cal':
            cal()
        else:
            print(f'-bash: {run}: command not found')
