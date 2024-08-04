import subprocess
import importlib
import answershot
import sql
subprocess.run(['python', 'shoot.py'])
subject_value = answer.subject()
subprocess.run(['python', 'sql.py', str(subject_value)])
importlib.reload(answer)
row_value = answer.row()
