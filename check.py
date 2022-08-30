import os
def ck(game):
    if os.path.exists(game.__class__.path + str(game.num) + ' ' + game.file_name):
        print("Game already downloaded")
        return True