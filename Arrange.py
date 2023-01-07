import datetime
import logging
import shelve
import os
logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of arrange program')

#导入个人变量
PriName = os.environ['PRINAME']
password = os.environ['PASSWORD']
mail = os.environ['MAIL']
roster = os.environ['ROSTER']
mails = os.environ['MAILS']
logging.info('Recorded successfully')

#分割信息
nlists = roster.split(',')
mlists = mails.split(',')
roster_information = {}
n = 0
for member in nlists:
    roster_information[member] = mlists[n]
    n += 1
logging.info('Splited successfully')

#安排时间
delta = datetime.timedelta(days=3)
beginning_date = datetime.datetime(2023, 2, 13)
duty_roster = {}
for i in range(0, 1*len(nlists), len(nlists)):
    for person in nlists:
        time = beginning_date + delta*i
        i += 1
        duty_roster[time] = person
logging.info('Arranged successfully')

#保存二进制文件
shelfFile1 = shelve.open('roster_information')
shelfFile2 = shelve.open('duty_roster')
shelfFile1['roster_information'] = roster_information
shelfFile2['duty_roster'] = duty_roster
shelfFile1.close()
shelfFile2.close()
logging.info('Saved successfully')
