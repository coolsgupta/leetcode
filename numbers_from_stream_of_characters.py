nums = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

nums_char = {num: dict.fromkeys(name, 0) for num, name in nums.items()}
for num, name in nums.items():
    for ch in name:
        nums_char[num][ch] += 1

# input_str = 'veiifogvweesotwnetnvfeheiot'
input_str = 'xtneiootnrnoeneeeeuoeoheetehounzoiuetrhfefeezuivirfwieotgoottf'
char_map = {}
output = []
for ch in input_str:
    if ch not in char_map:
        char_map[ch] = 0
    char_map[ch] += 1

    for num in nums_char:
        for n_ch in nums_char[num]:
            if nums_char[num][n_ch] > char_map.get(n_ch, 0):
                break
        else:
            output.append(num)
            for n_ch in nums_char[num]:
                char_map[n_ch] -= nums_char[num][n_ch]

print(''.join(map(str, sorted(output))))

