from Check_adb import *
from Call_Monkey import *
import sys
import threading
from src.config.constants import *


class Runnable:

    def __init__(self, pname, th, vb):
        print "Inside Runnable"
        self.pname = pname
        self.th = th
        self.vb = vb
        if GetData().get_devices():
            print GetData().get_devices()
            print 'Clearning old logs'
            GetData().clear_logcat()

        else:
            print('No device conencted')
            sys.exit()

    def main(self):
        print constant_func(self.pname, self.th, self.vb)
        monkeyobj = MonkeyClass(self.pname, self.th, self.vb)

        # Define your jobs
        t1 = threading.Thread(target=monkeyobj.proc_monkey)
        t2 = threading.Thread(target=monkeyobj.proc_logcat)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()
        t2.join()

        print("Both threads exited, exiting.")


PACKAGE_NAME = 'tv.airtel.smartstick -c android.intent.category.HOME'
#PACKAGE_NAME = 'com.android.deskclock'
THROTTLE = 500
VERBOSE = 50
print Runnable(PACKAGE_NAME, THROTTLE, VERBOSE).main()

# print Runnable(COMMAND).main()
