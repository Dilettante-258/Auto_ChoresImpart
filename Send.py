import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import logging
from Arrange import PriName,mail,password
logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of send program')

#时间获取部分
week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
today = datetime.datetime.now()
weekday = "今天是第%d周的%s。\n" % (int(today.strftime("%U")), week[int(today.strftime("%w"))])
ntime = today.strftime('%Y.%b.%d %a.\n%p  %H:%M:%S')
beginning_date = datetime.datetime(2023, 2, 13, 7, 30, 0)
logging.debug('Got Time')


# 发送内容设定
def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def configure(name, email):
    text = "亲爱的%s同学：\n你好！\n很高兴在这里写信给你。我是你的寝室室友。\n%s我想通过这封信提醒你，今天是你负责打扫寝室公共区域卫生的日子。为了保证我们寝室的整洁卫生，请你尽快完成这项任务。\n你需要简单地清理一下走廊过道，冲刷一下卫生间，并更换纸篓内的垃圾袋。\n如果你有任何困难，请随时告诉我，我们可以一起完成这项任务。希望你能按时完成这项任务。\n祝你生活愉快！\n%s\n%s\n\n此邮件由程序自动发布。" % (name, weekday, PriName, ntime)
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = format_addr('%s<%s>' % (PriName, mail))
    message['To'] = format_addr('%s<%s>' % (name, email))
    subject = '寝室卫生安排通知'
    message['Subject'] = Header(subject, 'utf-8')
    return message
    logging.debug('Confugured Successfully.')
def FirstConfigure(name, email):
    text = "亲爱的%s同学：\n你好！\n这是一封测试邮件。\n%s示例文字示例文字示例文字示例文字示例文字\n祝你生活愉快！\n%s\n%s\n\n此邮件由程序自动发布。" % (name, weekday, PriName, ntime)
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = format_addr('%s<%s>' % (PriName, mail))
    message['To'] = format_addr('%s<%s>' % (name, email))
    subject = '这是第一封测试邮件'
    message['Subject'] = Header(subject, 'utf-8')
    return message
    logging.debug('Confugured First letter Successfully.')

#发送部分
def sendmail(name, email):
    smtpObj = smtplib.SMTP('smtp.qq.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail, password)
    logging.debug('Sending email to %s...' % email)
    sendmail_status = smtpObj.sendmail(mail, email, configure(name, email).as_string())
    if sendmail_status != {}:
        logging.debug('There was a problem sending email to %s: %s' % (email, sendmail_status))
    time.sleep(3.0)
    smtpObj.quit()
    logging.info('Sending succeeded.')

def sendfirstmail(name, email):
    smtpObj = smtplib.SMTP('smtp.qq.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail, password)
    sendmail_status = smtpObj.sendmail(mail, email, FirstConfigure(name, email).as_string())
    if sendmail_status != {}:
        logging.debug('There was a problem sending email to %s: %s' % (email, sendmail_status))
    time.sleep(5.0)
    smtpObj.quit()
    logging.info('First sending succeeded.')