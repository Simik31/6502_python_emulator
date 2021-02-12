# 6502 CPU emulator written in python
## Little side project to train my python skills.
## Emulator is coded according to [this](http://www.obelisk.me.uk/6502/) page
### Implemented instructions: 30 / 56

### Load/Store Operations: 6 / 6
- [LDA](http://www.obelisk.me.uk/6502/reference.html#LDA),
  [LDX](http://www.obelisk.me.uk/6502/reference.html#LDX),
  [LDY](http://www.obelisk.me.uk/6502/reference.html#LDY),
  [STA](http://www.obelisk.me.uk/6502/reference.html#STA),
  [STX](http://www.obelisk.me.uk/6502/reference.html#STX),
  [STY](http://www.obelisk.me.uk/6502/reference.html#STY)

### Register Transfers: 4 / 4
- [TAX](http://www.obelisk.me.uk/6502/reference.html#TAX),
  [TAY](http://www.obelisk.me.uk/6502/reference.html#TAY),
  [TXA](http://www.obelisk.me.uk/6502/reference.html#TXA),
  [TYA](http://www.obelisk.me.uk/6502/reference.html#TYA)

### Stack Operations: 6 / 6
- [TSX](http://www.obelisk.me.uk/6502/reference.html#TSX),
  [TXS](http://www.obelisk.me.uk/6502/reference.html#TXS),
  [PHA](http://www.obelisk.me.uk/6502/reference.html#PHA),
  [PHP](http://www.obelisk.me.uk/6502/reference.html#PHP),
  [PLA](http://www.obelisk.me.uk/6502/reference.html#PLA),
  [PLP](http://www.obelisk.me.uk/6502/reference.html#PLP)

### Logical: 4 / 4
- [AND](http://www.obelisk.me.uk/6502/reference.html#AND),
  [BIT](http://www.obelisk.me.uk/6502/reference.html#BIT),
  [EOR](http://www.obelisk.me.uk/6502/reference.html#EOR),
  [ORA](http://www.obelisk.me.uk/6502/reference.html#ORA)

### Arithmetic: 0 / 5
- ~~ADC~~, ~~CMP~~, ~~CPX~~, ~~CPY~~, ~~SBC~~, 

### Increments & Decrements: 6 / 6
- [DEC](http://www.obelisk.me.uk/6502/reference.html#DEC),
  [DEX](http://www.obelisk.me.uk/6502/reference.html#DEX),
  [DEY](http://www.obelisk.me.uk/6502/reference.html#DEY),
  [INC](http://www.obelisk.me.uk/6502/reference.html#INC),
  [INX](http://www.obelisk.me.uk/6502/reference.html#INX),
  [INY](http://www.obelisk.me.uk/6502/reference.html#INY)

### Shifts: 2 / 4
- [ASL](http://www.obelisk.me.uk/6502/reference.html#ASL),
  [LSR](http://www.obelisk.me.uk/6502/reference.html#LSR),
  ~~ROL~~,
  ~~ROR~~

### Jumps & Calls: 1 / 3
- ~~JMP~~,
  [JSR](http://www.obelisk.me.uk/6502/reference.html#JSR)
  ~~RTS~~

### Branches: 0 / 8
- ~~BCC~~, ~~BCS~~, ~~BEQ~~, ~~BMI~~, ~~BNE~~, ~~BPL~~, ~~BVC~~, ~~BVS~~

### Status Flag Changes: 0 / 7
- ~~CLC~~, ~~CLD~~, ~~CLI~~, ~~CLV~~, ~~SEC~~, ~~SED~~, ~~SEI~~

### System Functions: 1 / 3
- ~~BRK~~,
  [NOP](http://www.obelisk.me.uk/6502/reference.html#NOP),
  ~~RTI~~
