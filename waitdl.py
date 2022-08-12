import os
import time
def waitdl(name, DIR):
    while True:
            if os.path.exists(DIR + name):
                print('Download Finished!')
                break
            else:
                print('downloading')
                time.sleep(10)