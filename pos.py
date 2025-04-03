import uiautomator2 as u2
import sqlite3
import re
import time

d = u2.connect("127.0.0.1:16384")
d.app_start("com.android.weici.senior.student")
english = "com.android.weici.senior.student:id/english"
que = "com.android.weici.senior.student:id/question"

def part():
    word_element = d.xpath('//*[@resource-id="com.android.weici.senior.student:id/part_word"]').get()
    if not word_element:
        raise Exception("Word element not found")

    word_info = word_element.info
    word_bounds = word_info['bounds'] 
    word_left = word_bounds['left']
    word_right = word_bounds['right']
    word_text = word_element.text

    line_elements = d.xpath('//*[@resource-id="com.android.weici.senior.student:id/line"]').all()
    if len(line_elements) == 1:
        line_info = line_elements[0].info
        line_bounds = line_info['bounds']
        line_left = line_bounds['left']
        line_right = line_bounds['right']
        
        if line_left > word_right:
            word_text += '"'
        elif line_right < word_left:
            word_text = f'"{word_text}'
    elif len(line_elements) == 2:
        word_text = f'_{word_text}_'

    conn = sqlite3.connect('weici.db')
    cursor = conn.cursor()
    cursor.execute('SELECT answer FROM fb_word_test WHERE subject = ?', (word_text,))
    rows = cursor.fetchall()

    for row in rows:
        answer = row[0]
        if answer.count(',') == 1:
            iniword = word_text.replace('_', '')
            processed = answer.replace(iniword, '').replace(',', '').strip()
            if d.xpath(f'//*[@text="{processed}"]').exists:
                d(text=processed).click()
                break
        elif answer.count(',') == 2:
            parts = answer.split(',')
            for text in parts:
                if text.strip():
                    d(text=text.strip()).click()
            break

    conn.close()

def answer(question):
    conn = sqlite3.connect('weici.db')
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM fb_word_test WHERE subject = ?", (question,))
    results = cursor.fetchall()
    for result in results:
        answer = result[0]
        if answer != question:
            tryanswer = answer[3:]
            element = d(text=str(tryanswer))
            if element.exists():
                print({tryanswer})
                element.click()
                break
            else:
                continue
    conn.close()

def main():
    while True:
        if d(text="立即查看").exists:
            d(text="立即查看").click()
        if d(text="提交").exists(timeout=0):
            d(text="提交").click()
        elif d(resourceId="com.android.weici.senior.student:id/review_btn1").exists(timeout=0):
            d(resourceId="com.android.weici.senior.student:id/review_btn1").click()
        elif d(text="继续订正").exists(timeout=0):
            d(text="继续订正").click()
        if d(text="未提交").exists:
            d(text="未提交").click()
        if d(text="练习").exists:
            d(text="练习").click()
        if d(resourceId="com.android.weici.senior.student:id/all_count").exists:
            numebr = d(resourceId="com.android.weici.senior.student:id/all_count").get_text()
            numbers = re.findall(r'\d+', numebr)
            if len(numbers) == 2:
                if numbers[0] != numbers[1]:
                    d(resourceId="com.android.weici.senior.student:id/all_count").click()
        
        if d(resourceId="com.android.weici.senior.student:id/english").count == 1 and not d(resourceId="com.android.weici.senior.student:id/question").exists and not d(resourceId="com.android.weici.senior.student:id/part_word").exists:
            question = d(resourceId="com.android.weici.senior.student:id/english").get_text()
            lastquestion = question
            st = 1
            answer(question)
            time.sleep(0.5)

        if d(resourceId="com.android.weici.senior.student:id/question").count == 1 and not d(resourceId="com.android.weici.senior.student:id/english").exists and not d(resourceId="com.android.weici.senior.student:id/part_word").exists:
            question = d(resourceId="com.android.weici.senior.student:id/question").get_text()
            lastquestion = question
            st = 2
            answer(question)
            time.sleep(1)
        if d(resourceId = english).exists and d(resourceId = que).exists:
            if st == 1:
                question = d(resourceId = que).get_text()
                lastquestion = question
                st = 2
                answer(question)
                time.sleep(1)
            elif st == 2:
                question = d(resourceId = english).get_text()
                lastquestion = question
                st = 1
                answer(question)
                time.sleep(1)

        if d(resourceId = english).count == 2:
            elements = d(resourceId=english)
            for element in elements:
                current_text = element.get_text()
                if current_text != lastquestion:
                    question = current_text
                    lastquestion = question
                    st = 1
                    answer(question)
                    time.sleep(1)
                    break
        if d(resourceId = que).count == 2:
            elements = d(resourceId=que)
            for element in elements:
                current_text = element.get_text()
                if current_text != lastquestion:
                    question = current_text
                    lastquestion = question
                    st = 2
                    answer(question)
                    time.sleep(1)
                    break
        if d(resourceId="com.android.weici.senior.student:id/part_word").exists:
            time.sleep(1)
            part()

        time.sleep(1)
        if d(text="已提交").exists and not d(text="未提交").exists:
            d.press("back")
            
main()