# ALU with Overflow and Carry Detection

## 🧠 Overview
This project implements a 4-bit Arithmetic Logic Unit (ALU) in Python that supports:
- Addition and subtraction
- Unsigned carry detection
- Signed overflow detection

## ⚙️ Features
- 4-bit inputs (`A`, `B`)
- Operation selector (`Op = 0` for ADD, `1` for SUB)
- Outputs: `Result`, `Carry`, `Overflow`

## 🧪 How It Works
- **Carry** is set if there's a carry out of the MSB (for unsigned addition).
- **Overflow** is set if signed addition/subtraction exceeds representable range:
  - Adding two positives yields a negative
  - Adding two negatives yields a positive

## 🚀 Usage
Run the script:
```bash
python alu.py