from ascii_to_dict import get_ascii_to_dict
import textwrap

def unpacker(text: str) -> str:
    index = bits_to_int(text[:5])
    code_to_char, char_to_code = get_ascii_to_dict()
    text = text[5:]
    nums: list = textwrap.wrap(text,index)
    table_index: int = 257
    working_str: str = ""
    temp_str: str = ""
    ans: str = ""
    for num in range(len(nums)):
        current_char: str = ""
        if len(temp_str) == 0 :
            code = bits_to_int(nums[num])
            current_char = chr(code)
        else:
            current_char = temp_str[0]
            temp_str = temp_str[1:]
        if code in code_to_char:
            ans += code_to_char[code]
        if len(code_to_char[code]) > 1:
           current_char = code_to_char[code][0]
           temp_str = code_to_char[code][1:]
        augmented_str: str = working_str + current_char
        if augmented_str in char_to_code:
            working_str=augmented_str
        else:
            print(augmented_str)
            code_to_char[table_index] = augmented_str
            char_to_code[augmented_str] = table_index
            table_index += 1
            working_str = current_char
    return ans


def bits_to_int(num: str) -> int:
    ans: int = 0
    num = num[::-1]
    power: int = 0
    for bit in num:
        ans += int(bit) * (2**power)
        power += 1
    return ans


if __name__ == "__main__":
    print(unpacker("01001001100010001100001001101110100000010001100001"))
