import uiautomator2 as u2
import sqlite3

# 连接设备
d = u2.connect('127.0.0.1:16384')

part_word_element = d(resourceId='com.android.weici.senior.student:id/part_word')
question_element = d(resourceId='com.android.weici.senior.student:id/part_word').get_text()
if part_word_element.exists:
    part_word_left = part_word_element.info['bounds']['left']
else:
    exit()
line_elements = d(resourceId='com.android.weici.senior.student:id/line')
if line_elements.exists:
    line_left_values = []
    for element in line_elements:
        line_left_values.append(element.info['bounds']['left'])
    for left_value in line_left_values:
        if left_value < part_word_left:
            question_element="_"+question_element
        elif left_value > part_word_left:
            question_element=question_element+"_"
conn = sqlite3.connect('./omg/weici.db')
cursor = conn.cursor()
cursor.execute("SELECT answer FROM fb_word_test WHERE subject = ?", (question_element,))
results = cursor.fetchall()
for result in results:
    answer = result[0]
    print(answer)