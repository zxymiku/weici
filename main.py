import datetime
import time
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
time.sleep(500)
driver = webdriver.Edge()
driver.get("http://localhost:22367/")
time.sleep(2)
src_btn = driver.find_element(By.XPATH, "//button[normalize-space()='src']")
src_btn.click()
time.sleep(2)
start_btn = driver.find_element(By.XPATH, "//button[normalize-space()='启动']")
start_btn.click()

now = datetime.datetime.now()
weekday = now.weekday()

if weekday in [0, 2, 4, 5]:
    shutdown_hour, shutdown_minute = 8, 0
elif weekday in [1, 3]:
    shutdown_hour, shutdown_minute = 12, 10
elif weekday == 6:
    shutdown_hour, shutdown_minute = 13, 0
shutdown_time = now.replace(hour=shutdown_hour, minute=shutdown_minute, second=0, microsecond=0)

if now < shutdown_time:
    wait_seconds = (shutdown_time - now).total_seconds()
    time.sleep(wait_seconds) 
    os.system("shutdown -s -f -t 0")




