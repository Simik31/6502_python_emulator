# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 30/01/2021, 22:07  #
# ######################################

from CPU import CPU
from Memory import Memory


class Debug:
    """
    CPU and Memory Debugging class
    """

    def __init__(self, cpu: CPU):
        self.CPU = cpu
        self.MEM = cpu.get_memory()

    def cpu(self) -> None:
        """
        Prints CPU Registers and Flags
        """

        buffer = "Current instruction: " + self.CPU.current_instruction.get_hex_value() + "\n\n    "
        header = line_pc = line_sp = line_a = line_x = line_y = line_f = spacer = ""

        pc = self.CPU.get_PC()
        sp = self.CPU.get_SP()
        a = self.CPU.get_register_A()
        x = self.CPU.get_register_X()
        y = self.CPU.get_register_Y()
        f = self.CPU.get_register_F()

        for i in range(16):
            spacer += " "
            header += "{:1s} ".format(hex(i)[2:])
            line_pc += "{:1d} ".format(pc.get_bit(i))
            if i < 8:
                line_sp += "{:1d} ".format(sp.get_bit(i))
                line_a += "{:1d} ".format(a.get_bit(i))
                line_x += "{:1d} ".format(x.get_bit(i))
                line_y += "{:1d} ".format(y.get_bit(i))
                line_f += "{:1d} ".format(f.get_bit(i))

        buffer += header
        buffer += "\tDEC\t\tHEX\nPC: "
        buffer += line_pc
        buffer += "\t{:<5d}\t{:<6s}\nSP: ".format(pc.get_value(), pc.get_hex_value())
        buffer += spacer + line_sp
        buffer += "\t{:<5d}\t{:<6s}\n A: ".format(sp.get_value(), sp.get_hex_value(6))
        buffer += spacer + line_a
        buffer += "\t{:<5d}\t{:<6s}\n X: ".format(a.get_value(), a.get_hex_value(6))
        buffer += spacer + line_x
        buffer += "\t{:<5d}\t{:<6s}\n Y: ".format(x.get_value(), x.get_hex_value(6))
        buffer += spacer + line_y
        buffer += "\t{:<5d}\t{:<6s}\n F: ".format(y.get_value(), y.get_hex_value(6))
        buffer += spacer + line_f
        buffer += "\t{:<5d}\t{:<6s}\nFlags:".format(f.get_value(), f.get_hex_value(6))
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(7), "CARRY")
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(6), "ZERO")
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(4), "IRQ DISABLE")
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(3), "DECIMAL MODE")
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(2), "BREAK COMMAND")
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(1), "OVERFLOW")
        buffer += "\n{} {}".format(self.CPU.get_register_F().get_bit(0), "NEGATIVE")

        print(buffer)

    def mem(self, cols: int = 16) -> None:
        """
        Prints Memory
        """

        previous_row = ""
        same_rows_counter = 0

        buffer = "\n"
        hex_header = ""
        chr_header = ""
        dec_header = ""

        for i in range(cols):
            hex_header += " {:<2s}".format(hex(i)[2:])
            chr_header += " {:<1s}".format(hex(i)[2:])
            dec_header += " {:<3s}".format(hex(i)[2:])

        buffer += "             {}\t{}\t{}\n".format(hex_header, chr_header, dec_header)

        for r in range(self.MEM.size // cols):
            row = ""
            cha = ""
            dec = ""
            for c in range(cols):
                value = self.MEM.get_byte(r * cols + c)
                row += " {:<2s}".format(value.get_hex_value()[2:])
                cha += " {:<1s}".format((chr(value.get_value()) if value.get_value() != 0 else " "))
                dec += " {:<3d}".format(value.get_value())

            if row == previous_row:
                if same_rows_counter == 0:
                    same_rows_counter += 1
                    buffer += ".... - .... |" + " .." * cols + "\t" + " ." * cols + "\t" + " ..." * cols + "\n"
            else:
                s = Memory(16, hex(r * cols))
                e = Memory(16, hex((r + 1) * cols - 1))
                buffer += "{} - {} |{}\t{}\t{}\n".format(s.get_hex_value()[2:], e.get_hex_value()[2:], row, cha, dec)

                previous_row = row
                same_rows_counter = 0

        print(buffer)
