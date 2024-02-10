from ppadb.client import Client
from ppadb.device import Device
import time;
print('start!!')

KEY_ENTER = 66
KEY_BACK = 4
KEY_HOME = 3
KEY_POWER = 26
KEY_VOLUME_UP = 24
KEY_VOLUME_DOWN = 25
def adb_connect():
    client = Client(host="127.0.0.1", port=5037)
    find_devices = client.devices()
    if len(find_devices) == 0:
        print('No device connected')
        print('Please connect your device and try again')
        quit()

    device = find_devices[0]
    print(f"Device connected: {device}")
    return device, client



def screen_capture(device: Device):
    now = time.localtime()
    scan_name = "scan_%s-%s_%s:%s" %(now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    device.shell(f'screencap -p /sdcard/Download/scan_{scan_name}.png')
    print('Saved screenshot!')
    # result = device.screencap()
    # with open('screen.png', 'wb') as file:
    #     file.write(result)
    #

def step_search(device: Device, keyword: str = '자란다'):
    searchTabPosition = '318 2148'
    searchInputPosition = '431 140'
    keyboardEndterPosition = '987 2070'
    firstSearchPosition = '384 435'
    filterButtonPosition = '996 609'
    recentPopularPosts = '1011 2118'
    device.shell(f'input tap {searchTabPosition}')
    time.sleep(2)
    device.shell(f'input tap {searchInputPosition}')
    time.sleep(1)
    device.shell(f'input text \\#wkfksek')
    time.sleep(1)
    device.shell(f'input tap {keyboardEndterPosition}')
    time.sleep(1)
    device.shell(f'input tap {firstSearchPosition}')
    time.sleep(1)
    device.shell(f'input tap {filterButtonPosition}')
    time.sleep(1)
    device.shell(f'input tap {recentPopularPosts}')
    time.sleep(1)

def step_search(device: Device, keyword: str = '자란다'):
    searchTabPosition = '318 2148'
    searchInputPosition = '431 140'
    keyboardEndterPosition = '987 2070'
    firstSearchPosition = '384 435'
    filterButtonPosition = '996 609'
    recentPopularPosts = '1011 2118'
    device.shell(f'input tap {searchTabPosition}')
    time.sleep(2)
    device.shell(f'input tap {searchInputPosition}')
    time.sleep(1)
    device.shell(f'input text \\#wkfksek')
    time.sleep(1)
    device.shell(f'input tap {keyboardEndterPosition}')
    time.sleep(1)
    device.shell(f'input tap {firstSearchPosition}')
    time.sleep(1)
    device.shell(f'input tap {filterButtonPosition}')
    time.sleep(1)
    device.shell(f'input tap {recentPopularPosts}')
    time.sleep(1)



if __name__ == '__main__':
    device, client = adb_connect()

    for i in range(0, 1):
        step_search(device)
        time.sleep(2)
    # pst_full_chrgr = '851 355'
    # pst_member = '285 363'
    # pst_terminate_chrgr = '843 474'
    # pst_terminate_chck = '701 395'

    # pst_skip_card_tag = '895 476'
    # device.shell('input keyevent 25')
    # device.shell('input touchscreen swipe 500 1000 500 500')
    # time.sleep(2)
    # device.shell('input keyevent 26')
