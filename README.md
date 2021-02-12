# 6502 CPU emulator written in python
![6502](https://camo.githubusercontent.com/3f3e4877bd335a5003269398b0fa3fe0c71900e69b08f3f93513a663b0ff30ce/68747470733a2f2f7261772e6769746875622e636f6d2f626c69747a636f64652f6e65736b656c6c2f6d61737465722f363530322e706e67)
## Little side project to train my python skills.
## Emulator is coded according to [this](http://www.obelisk.me.uk/6502/) page
### Implemented instructions: 30 / 56

### Arithmetic: 0 / 5
- ~~ADC~~, ~~CMP~~, ~~CPX~~, ~~CPY~~, ~~SBC~~, 

### Branches: 0 / 8
- ~~BCC~~, ~~BCS~~, ~~BEQ~~, ~~BMI~~, ~~BNE~~, ~~BPL~~, ~~BVC~~, ~~BVS~~

### Increments & Decrements: 6 / 6
- [DEC](http://www.obelisk.me.uk/6502/reference.html#DEC 'DEC - Decrement Memory'),
  [DEX](http://www.obelisk.me.uk/6502/reference.html#DEX 'DEX - Decrement X Register'),
  [DEY](http://www.obelisk.me.uk/6502/reference.html#DEY 'DEY - Decrement Y Register'),
  [INC](http://www.obelisk.me.uk/6502/reference.html#INC 'INC - Increment Memory'),
  [INX](http://www.obelisk.me.uk/6502/reference.html#INX 'INX - Increment X Register'),
  [INY](http://www.obelisk.me.uk/6502/reference.html#INY 'INY - Increment Y Register')

### Jumps & Calls: 1 / 3
- ~~JMP~~,
  [JSR](http://www.obelisk.me.uk/6502/reference.html#JSR 'JSR - Jump to Subroutine')
  ~~RTS~~

### Load/Store Operations: 6 / 6
- [LDA](http://www.obelisk.me.uk/6502/reference.html#LDA 'LDA - Load Accumulator'),
  [LDX](http://www.obelisk.me.uk/6502/reference.html#LDX 'LDX - Load X Register'),
  [LDY](http://www.obelisk.me.uk/6502/reference.html#LDY 'LDY - Load Y Register'),
  [STA](http://www.obelisk.me.uk/6502/reference.html#STA 'STA - Store Accumulator'),
  [STX](http://www.obelisk.me.uk/6502/reference.html#STX 'STX - Store X Register'),
  [STY](http://www.obelisk.me.uk/6502/reference.html#STY 'STY - Store Y Register')

### Logical: 4 / 4
- [AND](http://www.obelisk.me.uk/6502/reference.html#AND 'AND - Logical AND'),
  [BIT](http://www.obelisk.me.uk/6502/reference.html#BIT 'BIT - Bit Test'),
  [EOR](http://www.obelisk.me.uk/6502/reference.html#EOR 'EOR - Exclusive OR'),
  [ORA](http://www.obelisk.me.uk/6502/reference.html#ORA 'ORA - Logical Inclusive OR')

### Register Transfers: 4 / 4
- [TAX](http://www.obelisk.me.uk/6502/reference.html#TAX 'TAX - Transfer Accumulator to X'),
  [TAY](http://www.obelisk.me.uk/6502/reference.html#TAY 'TAY - Transfer Accumulator to Y'),
  [TXA](http://www.obelisk.me.uk/6502/reference.html#TXA 'TXA - Transfer X to Accumulator'),
  [TYA](http://www.obelisk.me.uk/6502/reference.html#TYA 'TYA - Transfer Y to Accumulator')

### Shifts: 2 / 4
- [ASL](http://www.obelisk.me.uk/6502/reference.html#ASL 'ASL - Arithmetic Shift Left'),
  [LSR](http://www.obelisk.me.uk/6502/reference.html#LSR 'LSR - Logical Shift Right'),
  ~~ROL~~,
  ~~ROR~~

### Stack Operations: 6 / 6
- [TSX](http://www.obelisk.me.uk/6502/reference.html#TSX 'TSX - Transfer Stack Pointer to X'),
  [TXS](http://www.obelisk.me.uk/6502/reference.html#TXS 'TXS - Transfer X to Stack Pointer'),
  [PHA](http://www.obelisk.me.uk/6502/reference.html#PHA 'PHA - Push Accumulator'),
  [PHP](http://www.obelisk.me.uk/6502/reference.html#PHP 'PHP - Push Processor Status'),
  [PLA](http://www.obelisk.me.uk/6502/reference.html#PLA 'PLA - Pull Accumulator'),
  [PLP](http://www.obelisk.me.uk/6502/reference.html#PLP 'PLP - Pull Processor Status')

### Status Flag Changes: 0 / 7
- ~~CLC~~, ~~CLD~~, ~~CLI~~, ~~CLV~~, ~~SEC~~, ~~SED~~, ~~SEI~~

### System Functions: 1 / 3
- ~~BRK~~,
  [NOP](http://www.obelisk.me.uk/6502/reference.html#NOP 'NOP - No Operation'),
  ~~RTI~~