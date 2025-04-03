import uiautomator2 as u2
import time
import re
import sqlite3

def answer1(question):
    try:
        conn = sqlite3.connect("./omg/weici.db")
        cursor = conn.cursor()
        cursor.execute("SELECT answer FROM fb_word_test WHERE subject = ? AND answer != ?", (question, question))
        results = cursor.fetchall() 
        conn.close()
        if not results:
            print("notfond")
            return None
        for result in results:
            answer = result[0]
            tryanswer = answer[3:] if len(answer) > 3 else answer
            if not tryanswer:
                continue
            try:
                element = d(text=str(tryanswer))
                if element.exists():
                    print({tryanswer})
                    element.click()
                    time.sleep(0.5) 
                    break
            except Exception as e:
                print(f"wrong{str(e)}")
                continue
    except Exception as sqle:
        print(f"wrong{str(sqle)}")
        return None

def chuli1(lastque):
    elements = d.xpath('//*[@resource-id="com.android.weici.senior.student:id/question"]').all()
    question = None
    for element in elements:
        current_text = element.text
        if current_text != lastque:
            question = current_text
            answer1(question)
            break 
    if question:
        answer1(question)

def chuli2(lastque):
    elements = d.xpath('//*[@resource-id="com.android.weici.senior.student:id/english"]').all()
    question = None
    for element in elements:
        current_text = element.text
        if current_text != lastque:
            question = current_text
            answer1(question)
            break 
    if question:
        answer1(question)

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

def main():
    global d
    d = u2.connect("127.0.0.1:16384")  
    print(d.info)
    weici="com.android.weici.senior.student"
    d.app_start(weici)
    while True:
        if d(text="立即查看").exists:
            d(text="立即查看").click()
        if d(text="提交").exists(timeout=0):
            d(text="提交").click()
        elif d(resourceId="com.android.weici.senior.student:id/review_btn1").exists(timeout=0):
            d(resourceId="com.android.weici.senior.student:id/review_btn1").click()
        elif d(text="继续订正").exists(timeout=0):
            d(text="继续订正").click()
        
        elements = d(resourceId="com.android.weici.senior.student:id/all_count")
        for element in elements:
            text = element.get_text()
            numbers = re.findall(r'\d+', text)
            if len(numbers) == 2:
                if numbers[0] != numbers[1]:
                    time.sleep(0.5)
                    element.click()
        
        if d(text="未提交").exists:
            d(text="未提交").click()

        if d(resourceId="com.android.weici.senior.student:id/ui_item_text",text="练习").exists:
            d(resourceId="com.android.weici.senior.student:id/ui_item_text").click()


        if d(resourceId="com.android.weici.senior.student:id/english").count == 1 and not d(resourceId="com.android.weici.senior.student:id/question").exists:
            time.sleep(0.5)
            question = d(resourceId="com.android.weici.senior.student:id/english").get_text()
            lastque = question
            answer1(lastque)
            st = 2

        if d(resourceId="com.android.weici.senior.student:id/question").count == 1 and not d(resourceId="com.android.weici.senior.student:id/english").exists:
            time.sleep(0.5)
            question = d(resourceId="com.android.weici.senior.student:id/question").get_text()
            lastque = question
            answer1(lastque)
            st = 1

        if d(resourceId="com.android.weici.senior.student:id/english").count == 2:
            chuli2(lastque)
            st = 2

        if d(resourceId="com.android.weici.senior.student:id/question").count == 2:
            chuli1(lastque)
            st = 1
        if d(resourceId="com.android.weici.senior.student:id/part_word").exists:
            part()
        if d(resourceId="com.android.weici.senior.student:id/english").exists and d(resourceId="com.android.weici.senior.student:id/question").exists:
            if st == 1:
                time.sleep(0.5)
                question = d(resourceId="com.android.weici.senior.student:id/english").get_text()
                answer1(question)
                lastque = question
                st = 2
            elif st == 2:
                time.sleep(0.5)
                question = d(resourceId="com.android.weici.senior.student:id/question").get_text()
                lastque = question
                answer1(question)
                st = 1        
        time.sleep(1)
if __name__ == "__main__":
    main()