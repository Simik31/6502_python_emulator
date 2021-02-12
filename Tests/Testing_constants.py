# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 31/01/2021, 02:37  #
# ######################################

from typing import Union
from CPU import CPU
from Debug import Debug
from Memory import Byte, Word

Expected_no_flag_byte = Byte(0x31)
Expected_zero_flag_byte = Byte(0x00)
Expected_negative_flag_byte = Byte(0xff)

flag_names = [
	"NEGATIVE FLAG",
	"OVERFLOW FLAG",
	"",
	"BREAK_COMMAND FLAG",
	"DECIMAL MODE FLAG",
	"IRQ DISABLE FLAG",
	"ZERO FLAG",
	"CARRY FLAG"
]


def T_Reset_cpu() -> CPU:
	cpu = CPU()
	cpu.write_word(0xfffc, 0x0200)
	cpu.reset()
	return cpu


def execute_and_assert(cpu: CPU, cycles: int, e_reg: str, e_val: str, flags: Union[Byte, None], name: str, mode: Union[int, str]) -> [str]:
	cpu.execute(cycles)

	if e_reg == "A":
		if e_val != cpu.get_register_A().get_hex_value():
			return [e_val, cpu.get_register_A().get_hex_value(), f"{name}, Register A value incorrect"]
	elif e_reg == "X":
		if e_val != cpu.get_register_X().get_hex_value():
			return [e_val, cpu.get_register_X().get_hex_value(), f"{name}, Register X value incorrect"]
	elif e_reg == "Y":
		if e_val != cpu.get_register_Y().get_hex_value():
			return [e_val, cpu.get_register_Y().get_hex_value(), f"{name}, Register Y value incorrect"]
	elif e_reg == "PC":
		if e_val != cpu.get_PC().get_hex_value():
			return [e_val, cpu.get_PC().get_hex_value(), f"{name}, PC address incorrect"]
	elif e_reg.startswith("0x"):
		cpu.cycles += 1
		address = Word(int(e_reg, 16))
		if e_val != cpu.read_byte(address).get_hex_value():
			return [e_val, cpu.read_byte(address).get_hex_value(),
			        f"{name}, Memory[{address.get_hex_value()}] value incorrect"]

	if 0 != cpu.cycles:
		return ["0", str(cpu.cycles), f"{name}, CPU Cycles incorrect"]

	if flags is not None:
		for i in range(8):
			if (mode == 0 and i == 6) or\
					(mode == -1 and i == 0) or\
					(mode == 'c' and i == 7) or\
					(mode == 'c+0' and (i == 7 or i == 6)) or\
					(mode == 'c-1' and (i == 7 or i == 0)):
				if 1 != cpu.get_register_F().get_bit(i):
					return ["1", str(cpu.get_register_F().get_bit(i)), f"{name}, {flag_names[i]} incorrect"]

			else:
				if flags.get_bit(i) != cpu.get_register_F().get_bit(i):
					return [str(flags.get_bit(i)), str(cpu.get_register_F().get_bit(i)),
					        f"{name}, {flag_names[i]} incorrect"]

	# all ok
	return ["", "", ""]
