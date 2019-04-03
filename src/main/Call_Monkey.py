import os, sys
import subprocess
from src.config.constants import *
import datetime


class MonkeyClass:

    def __init__(self, pname, th, vb):
        self.pname = pname
        self.th = th
        self.vb = vb
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        self.reports_path = os.path.join(path, 'Reports')

    def proc_monkey(self):
        print datetime.datetime.now()
        c = constant_func(self.pname, self.th, self.vb)
        proc_monkey = os.system(c + ' > ' + self.reports_path + '/Event_logs.txt')

        print proc_monkey

    def proc_logcat(self):
        print datetime.datetime.now()
        proc_logcat = subprocess.Popen(['adb', 'logcat', '-v', 'time'], stdout=subprocess.PIPE)
        flogs = open(self.reports_path + '/Error_log.txt', 'w')
        for line in proc_logcat.stdout:
            if 'Monkey finished' in line:
                print 'Dlogs : Monkey finished'
                sys.exit()
            else:
                if 'Monkey' in line:
                    flogs.write('Dlogs: ' + line)

        else:
            flogs.close()
