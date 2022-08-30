import os
import time
def waitdl(game):
    while True:
            if os.path.exists(game.__class__.path + game.file_name):
                old_name = game.__class__.path + game.file_name
                new_name = game.__class__.path + str(game.num) + ' ' + game.file_name
                os.rename(old_name,new_name)
                print('Download Finished!')
                break
            else:
                print('downloading')
                time.sleep(10)