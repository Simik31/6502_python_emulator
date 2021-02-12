# ##############################
#  Copyright (c) 2021          #
#                              #
#  Author: Martin Šimara       #
#  Last modified on 12.2.2021  #
# ##############################

from typing import Union
from instance import test_instance
from Memory import Memory, Byte, Word
import Instructions

"""
Memory map:
    Zero page:          0x0000 - 0x00ff
    Stack:              0x0100 - 0x01ff
    Unreserved:         0x0200 - 0xfff9
    NMI address:        0xfffa - 0xfffb
    reset address:      0xfffc - 0xfffd
    IRQ/BRK address:    0xfffe - 0xffff
"""


class CPU:
    def __init__(self) -> None:

        self._memory = Memory(65536, d_type=Byte)

        self._PC = Word()

        self._SP = Byte()
        self._A = Byte()
        self._X = Byte()
        self._Y = Byte()
        self._F = Byte()

        self.CARRY_FLAG = 0b00000001
        self.ZERO_FLAG = 0b00000010
        self.IRQ_DISABLE_FLAG = 0b00000100
        self.DECIMAL_MODE_FLAG = 0b00001000
        self.BREAK_COMMAND_FLAG = 0b00010000
        self.OVERFLOW_FLAG = 0b01000000
        self.NEGATIVE_FLAG = 0b10000000

        self.cycles = -1
        self.instruction = None

    def reset(self) -> None:
        # nmi_address = self.read_word(Word(0xfffa))
        reset_address = self.read_word(Word(0xfffc))
        # irq_brk_address = self.read_word(Word(0xfffe))

        self.set_PC(reset_address)

        self.set_SP(0x0)
        self.set_register_A(0x0)
        self.set_register_X(0x0)
        self.set_register_Y(0x0)
        self.set_register_F(0x0)

    def execute(self, cycles: int) -> None:
        test_instance(self.execute, cycles, (int,))

        self.cycles = cycles
        while self.cycles > 0:
            self.instruction = Instructions.selector(self.fetch_byte())
            if self.instruction is not None:
                self.instruction(self)

        if self.cycles < 0:
            self.cycles = 0

    def set_PC(self, value: Union[int, str, Byte, Word, Memory, list]) -> None:
        test_instance(self.set_PC, value, (int, str, Byte, Word, Memory, list))

        self._PC.set(value)

    def get_PC(self) -> Word:
        return self._PC.copy()

    def set_SP(self, value: Union[int, str, Byte, Word, Memory, list]) -> None:
        test_instance(self.set_SP, value, (int, str, Byte, Word, Memory, list))

        self._SP.set(value)

    def get_SP(self) -> Byte:
        return self._SP.copy()

    def set_register_A(self, value: Union[int, Byte, Word, Memory]) -> None:
        test_instance(self.set_register_A, value, (int, Byte, Word, Memory))

        self._A.set(value)

    def get_register_A(self) -> Byte:
        return self._A.copy()

    def set_register_X(self, value: Union[int, Byte, Word, Memory]) -> None:
        test_instance(self.set_register_X, value, (int, Byte, Word, Memory))

        self._X.set(value)

    def get_register_X(self) -> Byte:
        return self._X.copy()

    def set_register_Y(self, value: Union[int, Byte, Word, Memory]) -> None:
        test_instance(self.set_register_Y, value, (int, Byte, Word, Memory))

        self._Y.set(value)

    def get_register_Y(self) -> Byte:
        return self._Y.copy()

    def set_register_F(self, value: Union[int, Byte, Word, Memory]) -> None:
        test_instance(self.set_register_F, value, (int, Byte, Word, Memory))

        self._F.set(value)

    def set_mask_register_F(self, value: Union[int, Byte, Word, Memory], mask: int) -> None:
        test_instance(self.set_mask_register_F, value, (int, Byte, Word, Memory))
        test_instance(self.set_mask_register_F, mask, (int,), parameter_offset=2)

        self._F.set_mask(value, mask)

    def get_register_F(self) -> Byte:
        return self._F.copy()

    def fetch_byte(self) -> Byte:
        data = self.read_byte(self.get_PC())
        self._PC += 1
        return data

    def fetch_word(self) -> Word:
        byte = self._memory.get_byte(self._PC.get_value())
        data = Word(byte)
        self._PC += 1

        byte = self._memory.get_byte(self._PC.get_value())
        data |= Word(byte.get_value() << 8)
        self._PC += 1

        self.cycles -= 2

        return data

    def read_byte(self, address: Union[Byte, Word, Memory]) -> Byte:
        test_instance(self.read_byte, address, (Byte, Word, Memory))

        self.cycles -= 1
        return Byte(self._memory.get_byte(address.get_value()))

    def read_word(self, address: Union[Byte, Word, Memory]) -> Word:
        test_instance(self.read_word, address, (Byte, Word, Memory))

        address = address.get_value()
        lsb = self._memory.get_byte(address)
        self.cycles -= 2

        return Word(self._memory.get_byte(address + 1)) << 8 | lsb

    def write_byte(self, address: Union[int, Byte, Word, Memory], value: Union[int, Byte, Word, Memory]) -> None:
        test_instance(self.write_byte, address, (int, Byte, Word, Memory))
        test_instance(self.write_byte, value, (int, Byte, Word, Memory))

        if isinstance(address, Memory):
            address = address.get_value()

        if isinstance(value, int):
            value = Byte(value)

        self._memory.set_byte(address, value)
        self.cycles -= 1

    def write_word(self, offset: int, value: Union[int, Word]) -> None:
        test_instance(self.write_word, offset, (int,))
        test_instance(self.write_word, value, (int, Memory))

        if isinstance(value, int):
            value = Word(value)

        self._memory.set_byte(offset, value.get_least_significant_byte())
        offset += 1
        self._memory.set_byte(offset, value.get_most_significant_byte())

    def write_to_stack(self, value: Byte) -> None:
        self._memory.set_byte(self.get_SP(), value, protected = True)
        self.set_SP(self.get_SP() + 1)

    def read_from_stack(self) -> Byte:
        self.set_SP(self.get_SP() - 1)
        return self._memory.get_byte(self.get_SP())

    def get_memory(self) -> Memory:
        return self._memory
