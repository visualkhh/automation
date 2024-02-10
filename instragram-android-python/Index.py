from ppadb.client import Client as AdbClient
from ppadb.device import Device
import time;
print('start!!')

KEY_ENTER = 66
KEY_BACK = 4
KEY_HOME = 3
KEY_POWER = 26
KEY_VOLUME_UP = 24
KEY_VOLUME_DOWN = 25

SCREEN_WIDTH = 1080
TAIL_WIDTH = 350
def adb_connect():
    client = AdbClient(host="127.0.0.1", port=5037)
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
    img_byte = device.screencap()
    with open(f'scan_{scan_name}.png', 'wb') as file:
        file.write(img_byte)
    print('Saved screenshot!')

    # device.shell(f'screencap -p /sdcard/Download/scan_{scan_name}.png')
    # device.shell(f'screencap -p /Users/hyunhakim/source/visualkhh/automation/instragram-android-python/scan_{scan_name}.png')
    # print('Saved screenshot!')
    # result = device.screencap()
    # with open('screen.png', 'wb') as file:
    #     file.write(result)
    #

def step_search(device: Device, keyword: str = '\\#wkfksek'):
    searchTabPosition = '318 2148'
    searchInputPosition = '431 140'
    keyboardEndterPosition = '987 2070'
    firstSearchPosition = '384 435'
    filterButtonPosition = '996 609'
    recentPopularPosts = '1011 2118'
    device.shell(f'input tap {searchTabPosition}')
    time.sleep(0.5)
    device.shell(f'input tap {searchInputPosition}')
    time.sleep(0.5)
    device.shell(f'input text {keyword}')
    time.sleep(0.5)
    device.shell(f'input tap {keyboardEndterPosition}')
    time.sleep(0.5)
    device.shell(f'input tap {firstSearchPosition}')
    time.sleep(0.5)
    device.shell(f'input tap {filterButtonPosition}')
    time.sleep(0.5)
    device.shell(f'input tap {recentPopularPosts}')

def nextPage(device: Device, page: int = 3 ):
   for i in range(0, page):
       device.input_swipe(570,2040, 570, 0, 100)
       time.sleep(3)
   device.input_swipe(570,2040, 570, 0, 100)

def process(device: Device):
    device.shell(f'input tap 531 903')
    time.sleep(0.1)
    device.shell(f'input tap 531 903')
    time.sleep(0.1)
    device.shell(f'input tap 855 279')
    time.sleep(0.5)
    device.shell(f'input tap 219 297')
    time.sleep(1)
    device.shell(f'input keyevent {KEY_BACK}')



def step_process(device: Device):
    xPosition = 0
    tailSize = int(SCREEN_WIDTH / TAIL_WIDTH)
    print(f'tailSize: {tailSize}')
    for i in range(1, tailSize + 1):
        xPosition = SCREEN_WIDTH - (TAIL_WIDTH * i + 1) + (TAIL_WIDTH / 2);
        print(f'xPosition: {xPosition}')
        device.shell(f'input tap {xPosition} 852')
        time.sleep(1)
        process(device)
        time.sleep(1)
        device.shell(f'input keyevent {KEY_BACK}')
        time.sleep(1)
        # device.input_swipe(570,2040, 570,1750 , 100)


if __name__ == '__main__':
    device, client = adb_connect()

    # nextPage(device,5)
    # device.input_swipe(570,2040, 570, 1750, 100)
    screen_capture(device);
    # device.shell(f'input keyevent {KEY_BACK}')
    # device.input_keyevent()
    # device.input_press()
    # device.input_press()
    for i in range(0, 1):
        # step_search(device)
        # time.sleep(2)
        # nextPage(device,3)
        step_process(device)
    #     time.sleep(2)
    # pst_full_chrgr = '851 355'
    # pst_member = '285 363'
    # pst_terminate_chrgr = '843 474'
    # pst_terminate_chck = '701 395'

    # pst_skip_card_tag = '895 476'
    # device.shell('input keyevent 25')
    # device.shell('input touchscreen swipe 500 1000 500 500')
    # time.sleep(2)
    # device.shell('input keyevent 26')
