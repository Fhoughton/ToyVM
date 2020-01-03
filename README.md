# ToyVM
A small toy VM and assembler written in python as a learning exercise. Has 3 registers, with storage, maths and printing. Writes the binary as a string rather than direct set of bits for better readability and due to python limitations.
- [X] 2 bit instruction set
- [X] Three registers
- [X] Supports direct and immediate addressing
- [X] Addition and multiplication
- [X] Assembler, turns asm into binary to be executed by the VM

## Instruction set
STR, stores a value into a register
```
STR R0 #1 ;STORE 1 IN REGISTER 0
```
ADD, adds a value to another value and stores the result in a selected register
```
ADD R2 R0 R1 ;ADD THE VALUES IN REGISTER 0 AND 1 TOGETHER AND STORE IN REGISTER 2
```
MUL, multiplies a value by another value and stores the result in a selected register
```
MUL R2 R2 #2 ;DOUBLE THE VALUE IN REGISTER 2
```
OUT, prints the value from a register out to the console
```
OUT R2 ;OUTPUT THE VALUE IN REGISTER 2
```

## Usage

To assemble the sample asm file run:
```python ToyAssembler.py foo.asm```

To execute the assembled program run:
```python ToyVM.py foo.s```
