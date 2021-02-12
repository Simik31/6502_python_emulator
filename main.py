# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 31/01/2021, 13:51  #
# ######################################

from CPU import CPU
from Debug import Debug
from file_manager import load_memory_from_file, save_memory_into_file
from Instructions import *

import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
    pass
    #cpu = CPU()
    #cycles = load_memory_from_file(cpu, "test.mem")

    #cpu.reset()

    #debug = Debug(cpu)

    #cpu.execute(cycles)

    #debug.cpu()
    #debug.mem()

    #save_memory_into_file(cpu, 'dump.mem')

if __name__ == '__main__':
    main()
