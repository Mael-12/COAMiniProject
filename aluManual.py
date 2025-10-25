def alu(a, b, op):
    a &= 0xF
    b &= 0xF

    if op == 0:  # ADD
        result = a + b
        carry = result > 0xF
    else:        # SUB
        b = (~b + 1) & 0xF
        result = a + b
        carry = a < b

    result &= 0xF

    sign_a = (a >> 3) & 1
    sign_b = ((b >> 3) & 1) if op == 0 else ((~b >> 3) & 1)
    sign_res = (result >> 3) & 1
    overflow = (sign_a == sign_b) and (sign_res != sign_a)

    return result, int(carry), int(overflow)

if __name__ == "__main__":
    print("Enter 4-bit values (0–15) for A and B")
    try:
        a = int(input("A: "))
        b = int(input("B: "))
        op = int(input("Operation (0 = ADD, 1 = SUB): "))
        if a < 0 or a > 15 or b < 0 or b > 15 or op not in [0, 1]:
            raise ValueError("Invalid input range.")
        result, carry, overflow = alu(a, b, op)
        print(f"\nResult: {result:04b} ({result})")
        print(f"Carry: {carry}")
        print(f"Overflow: {overflow}")
    except ValueError as e:
        print("Error:", e)