from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
from pynput.mouse import Button, Controller
#	For creation of the Headless Webdriver
def setUp():
    opts = Options()
    #opts.set_headless()
    #assert opts.headless
    unpacked_extension_path = '/home/harshv47/SIH_20/SIH-20-qual'
    mouse_vis_extension_path = '/home/harshv47/SIH_20/Mouse-vis'
    opts.add_argument("window-size=1400,600")
    opts.add_argument('--load-extension={}'.format(unpacked_extension_path))
    opts.add_argument('--load-extension={}'.format(mouse_vis_extension_path))
    driver = webdriver.Chrome('/home/harshv47/SIH_20/BotTest/chromedriver', options=opts)
    driver.set_window_size(1920, 1080)
    #ChromeOptions options = new ChromeOptions();
    return driver

def closeDown(driver):
    driver.close()



if __name__ == "__main__":
    driver = setUp()
    times = 500
    driver.get("https://lipsum.com/")
    arr = np.load("mouse_data.npy")[2] * 600
    print(arr.astype(int).shape)
    action =  ActionChains(driver)
    startElement = driver.find_element_by_id('Outer')
    # First, go to your start point or Element:
    action.move_to_element(startElement)
    action.perform()
    mouse = Controller()
    #mouse.position = (500, 500)
    for i in range(arr.shape[0]):
        first = arr[i][0]
        sec = arr[i][1]
        mouse.position = (first, sec)
        time.sleep(0.3)
        #action.move_by_offset(first,sec)
        #action.perform()
    #while time :
    print("success")
    time.sleep(50)
    closeDown(driver)