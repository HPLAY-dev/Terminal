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
    if run != '':
        if run == 'clear':
            cmd_clear()
        if run[: 4] == 'echo':
            print(run[5 :])
        elif run == 'exit':
            cmd_exit()
        elif run == 'help':
            help()
        elif run == 'cal':
            cal()
        else:
            print(f'-bash: {run}: command not found')