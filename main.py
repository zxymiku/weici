import subprocess
import importlib
import time
import subject
import answershot
import sql

def run_main():
    subprocess.run(['python', 'Screenshot.py'])

   subprocess:run(['python','subject.py'])
    subject_value = subject.subject()
    subprocess.run(['python', 'sql.py', str(subject_value)])
    importlib.reload(answer)
    row_value = answer.row()
while True:
    run_main()
    time.sleep(1)