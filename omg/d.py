import time
from time import sleep
import subprocess
import uiautomator2 as u2
import psutil
import os
import re
import sqlite3

WEICI_PACKAGE_NAME = "com.android.weici.senior.student"

def get_by_id(rid):
    return d(resourceId=rid)

def danyuan():
     if d(resourceId="com.android.weici.senior.student:id/all_count").wait(timeout=0):
            element_text = d(resourceId="com.android.weici.senior.student:id/all_count").get_text()
            numbers = re.findall(r'\d+', element_text)
            a = int(numbers[0]) if len(numbers) > 0 else None
            b = int(numbers[1]) if len(numbers) > 1 else None
            if a == b:
                elements = d(resourceId="com.android.weici.senior.student:id/all_count")
                for element in elements:
                    element_text = element.get_text()
                    numbers = re.findall(r'\d+', element_text)
                    a = int(numbers[0]) if len(numbers) > 0 else None
                    b = int(numbers[1]) if len(numbers) > 1 else None
                else:
                    elements = d(resourceId="com.android.weici.senior.student:id/all_count")
                    for element in elements:
                        element_text = element.get_text()
                        numbers = re.findall(r'\d+', element_text)
                        a = int(numbers[0]) if len(numbers) > 0 else None
                        b = int(numbers[1]) if len(numbers) > 1 else None
                        if a != b:
                            element.click()


def wait_and_get(rid):
    print("waiting", rid)
    get_by_id(rid).wait()
    return get_by_id(rid)

class Progress:
    current: int
    total: int

    def __init__(self, source) -> None:
        a = str(source).split("/")
        self.current = int(a[0])
        self.total = int(a[1])

    def is_done(self) -> bool:
        return self.current >= self.total

def tianci_answer():
    question1=question+"_"
    question2="_"+question
    conn = sqlite3.connect('./weici/weici.db')
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT DISTINCT answer 
            FROM fb_word_test 
            WHERE subject = ?
        """, (question1,))
        results = cursor.fetchall()
        print(results)
        if not results:
            cursor.execute("""
            SELECT DISTINCT answer 
            FROM fb_word_test 
            WHERE subject = ?
        """, (question2,))
            results = cursor.fetchall()
        if results:
            for result in results:
                answer = str(result).strip("(),'")
                answer = answer.replace(",", "")
                answer = answer.replace(question, "")
            if d(textContains=answer).wait(timeout=0):
                d(textContains=answer).click(timeout=0)
    except sqlite3.Error as e:
        print(f"数据库操作出错: {e}")
    finally:
        cursor.close()
        conn.close()



def process_answers():
    conn = sqlite3.connect('./weici/weici.db')
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT DISTINCT answer 
            FROM fb_word_test 
            WHERE subject = ?
        """, (question,))

        results = cursor.fetchall()

        if not results:
            print('未找到subject为'+question+'的记录')
            return
        processed_answers = []
        for idx, (answer,) in enumerate(results, 1):
            if not isinstance(answer, str):
                continue
            original = answer
            if not answer:
                processed = "[空值]"
            else:
                if len(answer) >= 1 and answer[0] in {'A', 'B', 'C'}:
                    processed = answer[3:] if len(answer) >=3 else "[字符串过短]"
                    print(processed)
                    if d(textContains=processed).wait(timeout=0):
                        d(textContains=processed).click(timeout=0)
                else:
                    processed = answer
                    print(processed)
                    if d(text=processed).wait(timeout=0):
                        d(textContains=processed).click(timeout=0)
                processed_answers.append( (original, processed) )
        return processed_answers

    except sqlite3.Error as e:
        print(f"数据库操作出错: {e}")
    finally:
        cursor.close()
        conn.close()

def click_practice_button():
            button = d(resourceId="com.android.weici.senior.student:id/ui_item_img")
            if button.exists:
                button.click()

def activity():
    
    WEICI_PACKAGE_NAME = "com.android.weici.senior.student"
    if d.app_wait(WEICI_PACKAGE_NAME, front=True, timeout=5):
        pass
    else:
        d.app_start(WEICI_PACKAGE_NAME)
        sleep(3)


def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

if is_process_running("MuMuPlayer.exe"):
    d = u2.connect("127.0.0.1:16384")
    print(d.info)
    activity()

else:
    subprocess.Popen("D:\\Program Files\\Netease\MuMu Player 12\\shell\\MuMuPlayer.exe")
    sleep(15)
    d = u2.connect("127.0.0.1:16384")
    print(d.info)
    activity()


def works():
    while True:
        item_layout_element = d(text="未提交")
        global question
        if d(resourceId="com.android.weici.senior.student:id/ui").exists:
            click_practice_button()
            sleep(0.5)

        if d(resourceId="com.android.weici.senior.student:id/ui_item_img").exists:
            all_count_element = d(resourceId="com.android.weici.senior.student:id/ui_item_img")
            all_count_element.click()
            sleep(0.5)

        danyuan()

        if d(text="未提交").exists:
            item_layout_element = d(text="未提交")
            day_text = item_layout_element.get_text()
            sleep(0.5)
            print("状态", day_text)
    
        if item_layout_element.exists:
            item_layout_element.click()    
            sleep(0.5)
    
        sleep(0.5)
        tianci_element = d(resourceId="com.android.weici.senior.student:id/part_word")
        if tianci_element.exists:
            tianci_text = tianci_element.get_text()
            print(type(tianci_text))
            question = str(tianci_text)
            print("Question3:", question)
            tianci_answer()

        english_element = d(resourceId="com.android.weici.senior.student:id/english")
        if english_element.exists:
            english_text = english_element.get_text()
            print(type(english_text))
            question = str(english_text)
            print("Question2:", question)
            process_answers()
        
        sleep(2)
        question_element = d(resourceId="com.android.weici.senior.student:id/question")
        if question_element.exists:
            question_text = question_element.get_text()
            print(type(question_text))
            question = str(question_text)
            print("Question1:", question)
            process_answers()

        if d(text="提交").exists(timeout=0):
            d(text="提交").click()
        elif d(resourceId="com.android.weici.senior.student:id/review_btn1").exists(timeout=0):
            d(resourceId="com.android.weici.senior.student:id/review_btn1").click()
        elif d(text="继续订正").exists(timeout=0):
            d(text="继续订正").click()
        sleep(0.5)

works()