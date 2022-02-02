import os
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
APPFILE = os.path.join(CURRENT_DIRECTORY, "galil.py")

ATTEMPT = 10
for i in range(0, ATTEMPT):
    os.system('python ' + APPFILE)
    print(str(ATTEMPT + 1))
