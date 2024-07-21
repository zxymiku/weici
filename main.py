import subprocess
import time
scripts = ["screenshot.py", "subjiectre.py", "sql.py", "answershot.py"]

while True:
    for script in scripts:
        subprocess.run(["python", script])
        time.sleep(1)
