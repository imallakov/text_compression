from ascii_to_dict import get_ascii_to_dict


def archiver(text: str) -> str:
    if len(text) < 3:
        return text
    code_to_char, char_to_code = get_ascii_to_dict()
    pos: int = 0
    working_str: str = ""
    table_index: int = 256
    max_index = 16  # in power of 2, e.g. 2**max_index = 2**16 = 65536, we allow to store 65536 tables in dictionary
    current_index = 9  # also in power of 2, e.g. 2**current_index = 2**9 = 512
    bits: list = []
    for pos in range(len(text)):
        current_char: str = text[pos]
        augmented_work_str: str = working_str + current_char
        if not (augmented_work_str in char_to_code):
            if current_index < max_index:
                char_to_code[augmented_work_str] = table_index
                code_to_char[table_index] = augmented_work_str
                table_index += 1
                if table_index == 2**current_index:
                    current_index += 1
            bits.append(int_to_bits(char_to_code[augmented_work_str[:-1]]))
            working_str = current_char
        else:
            working_str = augmented_work_str
    bits.append(int_to_bits(char_to_code[working_str]))
    return get_one_str(bits, current_index)


def get_one_str(bits: list, index: int) -> str:
    ans: str = ""
    if index < 16:
        ans += "0"
    ans += int_to_bits(index)
    for bit in bits:
        for _ in range(index - len(bit)):
            ans += "0"
        ans += str(bit)
    return ans


def int_to_bits(num: int) -> str:
    byte: str = ""
    while num > 0:
        rem = num % 2
        byte += str(rem)
        num //= 2
    byte = byte[::-1]
    return byte


if __name__ == "__main__":
    print(archiver("banana"))
