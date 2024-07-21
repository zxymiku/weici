import sqlite3
from subjectre import subject

conn = sqlite3.connect('weici_ext400.db')

try:
    cursor = conn.cursor()
    cursor.execute('SELECT answer FROM fb_word_test WHERE subject = ?', (subject,))
    row = cursor.fetchone()

finally:
    conn.close()
