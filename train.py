from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
import time
from pynput.keyboard import Key, Controller
import pyautogui as gui
a=str(input("Enter source station:"))
b=str(input("Enter destination:"))
c=str(input("Enter journey date:"))
d=str(input("Enter train number:"))
username=str(input("Enter your irctc account username:"))
password=str(input("Enter Password:"))
print("Please wait...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(5)
time.sleep(4)
try:
    origin = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="origin"]/span/input'))  # Update this if necessary
    )
    origin.send_keys(a)
    time.sleep(2)
    gui.press("enter")
    time.sleep(2)  
except TimeoutException:
    print("Network slow")
try:
    destination = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="destination"]/span/input'))  # Update this if necessary
    )
    destination.send_keys(b)
    time.sleep(2)
    gui.press("enter")
except TimeoutException :
    print("net slow")
gui.press("enter")
try:
    date = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="journeyDate"]/span/input'))  # Update this if necessary
    )
    time.sleep(5)
    date.click()
    time.sleep(2)
    gui.hotkey('ctrl','a')
    date.send_keys(c)
    time.sleep(2)
    gui.press("enter")
except TimeoutException:
    print("net slow")
gui.hotkey('ctrl','f')
gui.write(d)
gui.press("enter")
gui.press("esc")
gui.press("Tab")
gui.press("Tab")
gui.press("Enter")
time.sleep(2)
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("enter")
time.sleep(5)
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("Tab")
gui.press("enter")
time.sleep(5)
time.sleep(5)
gui.write(username)
time.sleep(3)
gui.press("Tab")
time.sleep(1.5)
gui.write(password)
time.sleep(2)
gui.press("Tab")
time.sleep(5)
keyboard = Controller()
gui.hotkey('alt','c')
time.sleep(5)
# Function to simulate holding spacebar and dragging a region
    #keyboard.press(Key.space)
    #print("Spacebar held down")

    # Step 2: Drag the mouse from start position to end position
start_x, start_y = 210, 600  # Starting coordinates for drag
end_x, end_y = 565, 700     # Ending coordinates for drag

    # Move to the starting position
gui.moveTo(start_x, start_y)

    # Click and hold to start dragging
gui.mouseDown(button='left')

    # Drag the mouse to the end position
gui.moveTo(end_x, end_y, duration=2)  # Dragging over 2 seconds

    # Release the mouse to drop
gui.mouseUp(button='left')
print("Dragging complete")
time.sleep(2)
gui.hotkey('ctrl','v')
time.sleep(2)
gui.press("enter")
time.sleep(3)
gui.write("jashwanth")
time.sleep(1)
gui.press("down")
time.sleep(1)
gui.press("enter")
try:
    change = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="2"]/div/div[2]/span'))  # Update this if necessary
    )
    change.click()
except TimeoutException:
    print("Network slow")
time.sleep(2)
gui.press("tab")
gui.press("tab")
time.sleep(1)
gui.press("enter")
time.sleep(15)
gui.press("down")
gui.press("down")
gui.press("down")
gui.press("down")
gui.press("down")
gui.press("down")
time.sleep(2)
keyboard = Controller()
gui.hotkey('alt','c')
time.sleep(5)
# Function to simulate holding spacebar and dragging a region
    #keyboard.press(Key.space)
    #print("Spacebar held down")

    # Step 2: Drag the mouse from start position to end position
start_x, start_y = 490, 847  # Starting coordinates for drag
end_x, end_y = 885, 906     # Ending coordinates for drag

    # Move to the starting position
gui.moveTo(start_x, start_y)

    # Click and hold to start dragging
gui.mouseDown(button='left')

    # Drag the mouse to the end position
gui.moveTo(end_x, end_y, duration=2)  # Dragging over 2 seconds

    # Release the mouse to drop
gui.mouseUp(button='left')
print("Dragging complete")
time.sleep(2)
try:
    box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="captcha"]'))  # Update this if necessary
    )
    box.click()
except TimeoutException:
    print("Network slow")
time.sleep(3)
gui.hotkey('ctrl','v')
time.sleep(2)
gui.press("enter")
try:
    go = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="review"]/div[1]/p-sidebar/div/div/div[2]/button'))  # Update this if necessary
    )
    go.click()
    time.sleep(2)
except TimeoutException:
    print("Network slow")
