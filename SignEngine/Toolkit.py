import smtplib,sys
from email.mime.text import MIMEText

log = open('toolkit.log','w+')


def notificationByMail(text):
    mailto_list=["xiewei.fire@gmail.com"]
    mail_host="smtp.gmail.com"
    mail_user="***"
    mail_pass="***"

    me='xiewei.fire@gmail.com'
    msg = MIMEText("This is an auto-generated Email",_charset='gbk')
    msg['Subject'] = text
    msg['From'] = 'MyBudgetVM'
    msg['To'] = ";".join(mailto_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, mailto_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print >>log,str(e)
        return False


if __name__ == '__main__':
    print 'this is main'
