def seven_segment_display_alternative(number):
    segments = {
        0: ['1', '1', '1', '1', '1', '1', '0'],
        1: ['0', '1', '1', '0', '0', '0', '0'],
        2: ['1', '1', '1', '0', '0', '1', '1'],
        3: ['1', '1', '0', '1', '0', '1', '1'],
        4: ['0', '1', '1', '0', '1', '0', '1'],
        5: ['1', '0', '1', '1', '0', '1', '1'],
        6: ['1', '0', '1', '1', '1', '1', '1'],
        7: ['1', '1', '1', '0', '0', '0', '0'],
    }

    return segments.get(number, ['0', '0', '0', '0', '0', '0', '0'])

def decimal_to_binary_truth_table(number):
    binary_truth_table = format(number, '03b')
    return list(map(int, binary_truth_table))

def print_truth_table(decimal_input): 
    binary_output = decimal_to_binary_truth_table(decimal_input)
    seven_segment_output_alternative = seven_segment_display_alternative(decimal_input)

    print("-------------------------------------")
    print("| Decimal |  Binary | Seven Segment |")
    print("-------------------------------------")
    print(f"|    {decimal_input}    |   {''.join(map(str, binary_output))}   | {' '.join(seven_segment_output_alternative)} |")
    print("-------------------------------------")

if __name__ == "__main__":
    input_decimal = int(input("Masukkan angka desimal: "))

    if 0 <= input_decimal <= 7:
        print_truth_table(input_decimal)
    else:
        print("Input tidak valid. Harap masukkan angka antara 0 dan 7.")
def seven_segment_display(number):
    segments = {
        0: [' _ ', '| |', '|_|'],
        1: ['   ', '  |', '  |'],
        2: [' _ ', ' |', '| '],
        3: [' _ ', ' _|', ' _|'],
        4: ['   ', '|_|', '  |'],
        5: [' _ ', '|_ ', ' _|'],
        6: [' _ ', '|_ ', '|_|'],
        7: [' _ ', '  |', '  |'],
    }

    return segments.get(number, ['   ', '   ', '   '])
if 0 <= input_decimal <= 7:
    segments = seven_segment_display(input_decimal)
    print("Seven Segment Display:")
    for segment in segments:
        print(segment)
else:
    print("Input tidak valid. Harap masukkan angka antara 0 dan 7.")
