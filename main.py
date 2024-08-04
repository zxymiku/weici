import subprocess
import importlib
imoort time
import answershot
import sql
def run_main():
    subprocess.run(['python', 'Screenshot.py'])
    subject_value = answer.subject()
    subprocess.run(['python', 'sql.py', str(subject_value)])
    importlib.reload(answer)
    row_value = answer.row()
while True:
    run_main()
    time.sleep(1)