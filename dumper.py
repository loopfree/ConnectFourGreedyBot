from src.algorithm import *
from src.constant import Path
from src.utility import dump

def dumper(path_b1, path_b2, path_pvb):
    model1 = Bot13519144()
    model2 = Bot13520131()
    dump(model1, Path.BVB_P1.format(path_b1))
    dump(model2, Path.BVB_P2.format(path_b2))
    dump(model1, Path.PVB.format(path_pvb))

if __name__ == '__main__':
    bot1_filename = 'Bot1.pkl' 
    bot2_filename = 'Bot13520131.pkl'
    pvp_bot_filename = 'random-1.pkl'
    dumper(bot1_filename, bot2_filename, pvp_bot_filename)
