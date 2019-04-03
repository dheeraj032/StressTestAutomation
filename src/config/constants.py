BASE_URL = 'adb shell monkey -p '
# PACKAGE_NAME = 'tv.airtel.smartstick -c android.intent.category.HOME'
PARAMS = ' --ignore-crashes --ignore-native-crashes --ignore-timeouts '
# THROTTLE = 1000
# VERBOSE = 50


def constant_func(pname, th, vb):
    command = BASE_URL + pname + PARAMS + '-v --throttle ' + str(th) + ' ' + str(vb)
    return command


#'adb shell monkey -p tv.airtel.smartstick -c android.intent.category.HOME --ignore-crashes
# --ignore-native-crashes --ignore-timeouts -v --throttle 1000 50'