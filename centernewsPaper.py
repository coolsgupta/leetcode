def centerNewsPaperText(paragraphs, width):
    res = ['*'*(width+2)]
    for x in paragraphs:
        i = 0
        while i<len(x):
            line = x[i]
            i += 1
            while i<len(x) and len(line) + len(x[i]) + 1 <= width:
                line += ' ' + x[i]
                i += 1

            spaces = (width - len(line))
            l_spaces = spaces//2
            line = '*' + ' '*(l_spaces) + line + ' '*(spaces - l_spaces) + '*'
            res.append(line)

    res.append('*' * (width + 2))
    return res

if __name__ == '__main__':
    case = [['hello', 'world'], ['how', 'areYou', 'doing'], ['please look', 'and align', 'to center']]
    width = 16
    res = centerNewsPaperText(case, width)
    print(res)