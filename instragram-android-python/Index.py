from ppadb.client import Client as AdbClient
from ppadb.device import Device
import cv2
import numpy as np
from numpy import random
import time
print('start!!')

KEY_ENTER = 66
KEY_BACK = 4
KEY_HOME = 3
KEY_POWER = 26
KEY_VOLUME_UP = 24
KEY_VOLUME_DOWN = 25

SCREEN_WIDTH = 1080
TAIL_WIDTH = 350
KEYBOARD_ENDTER_POSITION = '987 2070'
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


#전체화면 capture
def capture():
    img_byte = device.screencap()
    img = cv2.imdecode(np.frombuffer(img_byte,np.uint8), flags=-1)
    img = img[:,:,:3]
    return img

# ★ search함수
def search(img,name,threshold=0.8):
    '''
    img = 현재화면 캡처
    name = 비교할 이미지 (미리 저장해놓은 file)
    threshold = 일치율 지정 ( 기본 0.8 )
    '''
    templ = cv2.imread('./templates/' + name + '.png', cv2.IMREAD_COLOR)
    # img = cv2.resize(img,dsize=None,fx=0.4,fy=0.4)
    # templ = cv2.resize(templ,dsize=None,fx=0.4,fy=0.4)
    res = cv2.matchTemplate(img,templ,cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    ziloc = list(zip(*loc[::-1]))
    return ziloc

# ★ picture click
def picture_click(img,name):
    '''
    현재화면(img) 과 template(name) 비교해서,
    일치하는 이미지 있으면 클릭한다.
    '''
    ziloc = search(img,name)
    basic_template = cv2.imread('./templates/' + name + '.png', cv2.IMREAD_COLOR)
    h, w = basic_template.shape[:-1]
    x1 = ziloc[0][0]
    y1 = ziloc[0][1]
    random_click_picture(x1, y1, w, h)
    print(f'click {name}')

# 저장해논 사진 범위 내로 임의 클릭/ picture_click 함수와 사용
def random_click_picture(x1,y1,w,h):
    new_x = random.randint(x1,x1+int(w))
    new_y = random.randint(y1,y1+int(h))
    delay = random.randint(50,111)
    device.input_swipe(new_x,new_y,new_x,new_y,delay)



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

    firstSearchPosition = '384 435'
    filterButtonPosition = '996 609'
    recentPopularPosts = '1011 2118'
    device.shell(f'input tap {searchTabPosition}')
    time.sleep(0.5)
    device.shell(f'input tap {searchInputPosition}')
    time.sleep(0.5)
    device.shell(f'input text {keyword}')
    time.sleep(0.5)
    device.shell(f'input tap {KEYBOARD_ENDTER_POSITION}')
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
    screen = capture()
    heart = len(search(screen, 'heart'))
    comment = len(search(screen, 'comment'))
    # following = len(search(screen, 'following'))
    if (heart > 0):
        picture_click(screen, 'heart')
    # if (following > 0):
    #     picture_click(screen, 'following')

    time.sleep(1)
    print(f'heart: {heart}')
    if (heart > 0 and comment > 0):
        keyword = 'wkfksek'
        picture_click(screen, 'comment')
        time.sleep(1)
        device.shell(f'input text {keyword}')
        time.sleep(1)
        device.shell(f'input tap {KEYBOARD_ENDTER_POSITION}')
        time.sleep(0.5)
        device.shell(f'input keyevent {KEY_BACK}')
        time.sleep(0.5)
        device.shell(f'input keyevent {KEY_BACK}')
        time.sleep(0.5)
        device.shell(f'input tap 219 297')
        # todo..
        time.sleep(1)
        device.shell(f'input keyevent {KEY_BACK}')
    time.sleep(3)



def step_process(device: Device):
    xPosition = 0
    tailSize = int(SCREEN_WIDTH / TAIL_WIDTH)
    print(f'tailSize: {tailSize}')
    for i in range(1, tailSize + 1):
        xPosition = SCREEN_WIDTH - (TAIL_WIDTH * i + 1) + (TAIL_WIDTH / 2);
        print(f'xPosition: {xPosition}')
        device.shell(f'input tap {xPosition} 752')
        time.sleep(1)
        process(device)
        time.sleep(1)
        device.shell(f'input keyevent {KEY_BACK}')
        time.sleep(1)
        # device.input_swipe(570,2040, 570,1750 , 100)


if __name__ == '__main__':
    device, client = adb_connect()

    # device.shell(f'input tap {554.0} 752')
    # device.shell(f'input tap {904.0} 752')
        # time.sleep(2)
    # device.shell(f'input tap {904.0} 752')
    # screen = capture()
    # print(len(search(screen, 'heart')))
    # nextPage(device,5)
    # device.input_swipe(570,2040, 570, 1750, 100)
    # screen_capture(device)
    # step_process(device)
    # device.shell(f'input keyevent {KEY_BACK}')
    # device.input_keyevent()
    # device.input_press()
    # device.input_press()
    #
    # step_process(device)
    for i in range(0, 1):
        step_search(device)
        time.sleep(2)
        nextPage(device,3)
        time.sleep(1)
        step_process(device)
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
