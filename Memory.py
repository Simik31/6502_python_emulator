# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 01/02/2021, 23:39  #
# ######################################

from typing import Union
import numpy as np

from instance import test_instance


class Memory:

    def __init__(self, size: int, value: Union[int, str, list, "Memory"] = None, d_type: type = int) -> None:
        self.size = size
        self._data: list[int]

        if d_type == Byte:
            self._data: list[Byte] = [Byte(0x0) for _ in range(self.size)]
        else:
            self._data: list[int] = [0 for _ in range(self.size)]

        if value is not None:
            self.set(value)

    def __getitem__(self, item: int) -> Union[int, "Byte"]:
        return self._data[item]

    def __setitem__(self, key: int, value: Union[int, "Byte"]) -> None:
        self._data[key] = value

    def __add__(self, other: Union[int, "Memory"]) -> "Memory":
        test_instance(self.__add__, other, (int, Memory))

        if issubclass(type(other), Memory):
            other = other.get_value()

        return Memory(self.size, hex(self.get_value() + other))

    def __sub__(self, other: Union[int, "Memory"]) -> "Memory":
        test_instance(self.__add__, other, (int, Memory))

        if issubclass(type(other), Memory):
            other = other.get_value()

        he = hex(self.get_value() - other)

        if int(he, 16) < 0xff:
            he = 0x100 + int(he, 16)

        return Memory(self.size, he)

    def __and__(self, other: Union[int, "Memory"]) -> "Memory":
        test_instance(self.__and__, other, (int, Memory))

        if issubclass(type(other), Memory):
            other = other.get_value()

        return Memory(self.size, hex(self.get_value() & other))

    def __or__(self, other: Union[int, "Memory"]) -> "Memory":
        test_instance(self.__or__, other, (int, Memory))

        if issubclass(type(other), Memory):
            other = other.get_value()

        return Memory(self.size, hex(self.get_value() | other))

    def __xor__(self, other: Union[int, "Memory"]) -> "Memory":
        test_instance(self.__and__, other, (int, Memory))

        if issubclass(type(other), Memory):
            other = other.get_value()

        return Memory(self.size, hex(self.get_value() ^ other))

    def __lshift__(self, other: int) -> "Memory":
        test_instance(self.__lshift__, other, (int,))

        return Memory(self.size, self.get_value() << other)

    def __rshift__(self, other: int) -> "Memory":
        test_instance(self.__rshift__, other, (int,))

        return Memory(self.size, self.get_value() >> other)

    def set(self, value: Union[int, str, "Memory", list]) -> None:
        test_instance(self.set, value, (int, str, Memory, list))

        if isinstance(value, int):
            if str(value)[0] == "-":
                value = 0x80 | int(str(value)[1:])

            value = [int(i) for i in bin(value)[2:]]

        elif isinstance(value, str):
            value = [int(i) for i in bin(int(value, 16))[2:]]

        elif issubclass(type(value), Memory):
            value = [value.get_bit(i) for i in range(value.size)]

        while len(value) < self.size:
            value.insert(0, 0)

        self._data = value[-self.size:]

    def set_bit(self, offset: int, value: int) -> None:
        test_instance(self.set_mask, offset, (int,))
        test_instance(self.set_mask, value, (int,), parameter_offset=2)

        self._data[offset] = value

    def set_byte(self, offset: Union[int, "Memory"], value: "Byte", protected=False) -> None:
        test_instance(self.get_bit, offset, (int, Memory))
        test_instance(self.set_mask, value, (Byte,), parameter_offset=2)

        if issubclass(type(offset), Memory):
            offset = offset.get_value()

        if offset in range(0x0100, 0x0200) and not protected:
            raise PermissionError("ILLEGAL MEMORY ACCESS ON ADDRESS %#06x" % offset)

        self[offset] = value

    def set_mask(self, value: int, mask: int) -> None:
        test_instance(self.set_mask, value, (int,))
        test_instance(self.set_mask, mask, (int,), parameter_offset=2)

        for i in range(self.size):
            if pow(2, i) == mask:
                self.set_bit(self.size - 1 - i, value)

    def get_value(self) -> int:
        return int(np.sum([self.get_bit(self.size - 1 - i) * (2 ** i) for i in range(self.size)]))

    def get_hex_value(self, length = None) -> str:
        return "{0:#0{1}x}".format(self.get_value(), length if length is not None else self.size // 4 + 2)

    def get_bit(self, offset: int) -> int:
        test_instance(self.get_bit, offset, (int,))

        return self._data[offset]

    def get_byte(self, offset: Union[int, "Memory"]) -> "Byte":
        test_instance(self.get_bit, offset, (int, Memory))

        if issubclass(type(offset), Memory):
            offset = offset.get_value()

        return self[offset]

    def copy(self):
        return Memory(self.size, self.get_value())


class Byte(Memory):
    def __init__(self, value: Union[int, str, Memory, list] = None, d_type: type = int):
        super().__init__(8, value, d_type)

    def __add__(self, other: Union[int, "Memory"]) -> "Byte":
        return Byte(super().__add__(other))

    def __sub__(self, other: Union[int, "Memory"]) -> "Byte":
        return Byte(super().__sub__(other))

    def __and__(self, other: Union[int, "Memory"]) -> "Byte":
        return Byte(super().__and__(other))

    def __or__(self, other: Union[int, "Memory"]) -> "Byte":
        return Byte(super().__or__(other))

    def __xor__(self, other: Union[int, "Memory"]) -> "Byte":
        return Byte(super().__xor__(other))

    def __lshift__(self, other: int) -> "Byte":
        return Byte(super().__lshift__(other))

    def __rshift__(self, other: int) -> "Byte":
        return Byte(super().__rshift__(other))

    def copy(self) -> "Byte":
        return Byte(self.get_value())


class Word(Memory):

    def __init__(self, value: Union[int, str, Memory, list] = None, d_type: type = int):
        super().__init__(16, value, d_type)

    def __add__(self, other: Union[int, "Memory"]) -> "Word":
        return Word(super().__add__(other))

    def __sub__(self, other: Union[int, "Memory"]) -> "Word":
        return Word(super().__sub__(other))

    def __and__(self, other: Union[int, "Memory"]) -> "Word":
        return Word(super().__and__(other))

    def __or__(self, other: Union[int, "Memory"]) -> "Word":
        return Word(super().__or__(other))

    def __xor__(self, other: Union[int, "Memory"]) -> "Word":
        return Word(super().__xor__(other))

    def __lshift__(self, other: int) -> "Word":
        return Word(super().__lshift__(other))

    def __rshift__(self, other: int) -> "Word":
        return Word(super().__rshift__(other))

    def get_least_significant_byte(self) -> Byte:
        return Byte(self._data[-8:]).copy()

    def get_least_significant_byte_hex(self) -> str:
        return self.get_least_significant_byte().get_hex_value()

    def get_least_significant_byte_value(self) -> int:
        return self.get_least_significant_byte().get_value()

    def get_most_significant_byte(self) -> Byte:
        return Byte(self._data[:8]).copy()

    def get_most_significant_byte_hex(self) -> str:
        return self.get_most_significant_byte().get_hex_value()

    def get_most_significant_byte_value(self) -> int:
        return self.get_most_significant_byte().get_value()

    def copy(self) -> "Word":
        return Word(self.get_value())
