def alu(a, b, op):
    """
    4-bit ALU with overflow and carry detection.
    a, b: integers (0–15)
    op: 0 for ADD, 1 for SUB
    Returns: (result, carry, overflow)
    """
    a &= 0xF
    b &= 0xF

    if op == 0:  # ADD
        result = a + b
        carry = result > 0xF
    else:        # SUB
        b = (~b + 1) & 0xF  # 2's complement
        result = a + b
        carry = a < b

    result &= 0xF

    # Overflow detection (signed 4-bit)
    sign_a = (a >> 3) & 1
    sign_b = ((b >> 3) & 1) if op == 0 else ((~b >> 3) & 1)
    sign_res = (result >> 3) & 1
    overflow = (sign_a == sign_b) and (sign_res != sign_a)

    return result, int(carry), int(overflow)

# Sample tests
if __name__ == "__main__":
    tests = [
        (0b0111, 0b0001, 0),  # 7 + 1
        (0b1111, 0b0001, 0),  # 15 + 1
        (0b0111, 0b1000, 1),  # 7 - 8
        (0b1000, 0b1000, 0),  # -8 + -8
        (0b0110, 0b0010, 1),  # 6 - 2
        (0b0001, 0b0010, 1),  # 1 - 2
    ]
    for a, b, op in tests:
        r, c, o = alu(a, b, op)
        print(f"A={a:04b}, B={b:04b}, Op={'ADD' if op==0 else 'SUB'} → Result={r:04b}, Carry={c}, Overflow={o}")