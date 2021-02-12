# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 31/01/2021, 00:56  #
# ######################################

from CPU import CPU
from Memory import Byte, Word


def load_memory_from_file(cpu: CPU, filename: str) -> int:
	"""
	Loads instruction and data from given file

	:return: required cycles (sum of all instruction cycles)
	"""

	ins_cyc = dict()
	ret = 0

	with open('instructions_cycles.txt') as inst:
		for line in inst.readlines():
			ins, cyc = line.split(" ")
			ins_cyc.update({ins.lower(): int(cyc)})

	with open(filename) as f:
		for line in f.readlines():
			address, data, t, _ = line.split(", ")
			cpu.write_byte(int(address, 16), Byte(int(data, 16)))
			if t == "i":
				ret += ins_cyc.get(data.lower(), 0)

	return ret


def save_memory_into_file(cpu: CPU, filename: str) -> None:
	mem = cpu.get_memory()
	with open(filename, 'w') as f:
		for address in range(mem.size):
			data = mem.get_byte(address).get_hex_value()
			if data != Byte().get_hex_value():
				f.write(Word(address).get_hex_value() + ", " + data + '\n')
