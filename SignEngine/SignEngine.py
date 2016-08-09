import subprocess,sys
import Toolkit
import datetime

log = open('SignEngine.log','a+')

def signAll():
    for username,password in users.items():
        for i in range(5):
            status = sign(username,password)
            if status:
                print >>log,username + 'sign successfully'
                break
        else:
            print >>log, 'Error sign with '+username + '||' + str(datetime.datetime.now())
            Toolkit.notificationByMail('Error sign with '+username)
            return False

    print >>log, 'Successfully sign.' + '||' + str(datetime.datetime.now())
    Toolkit.notificationByMail('Successfully sign.')

    return True


def sign(username,password):

    cmd = 'xvfb-run python SignTemplate.py ' + username + ' ' + password
    process = subprocess.Popen(
        cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    status = False
    while True:
        out = process.stdout.readline()
        if out == '' and process.poll() != None:
            'sign break'
            break
        if out != '':
            if out.find('OK')>-1:
                print 'find ok'
                status = True
                break
    return status




if __name__ == "__main__":
    signAll()
    print 'main'
