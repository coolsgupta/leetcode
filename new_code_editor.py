from copy import deepcopy
def newTextEditor(operations):
    result = ""
    clipboard = ""
    del_temp = [deepcopy(result)]

    for op in operations:
        if "UNDO" in op:
            if del_temp:
                result = del_temp.pop()

            else:
                result = ""

        if "INSERT" in op:
            del_temp.append(deepcopy(result))
            result += op[7:]
        elif "DELETE" in op:
            del_temp.append(deepcopy(result))
            result = result[:-1]
        elif "COPY" in op:
            clipboard = result[int(op[5:]):]

        elif "PASTE" in op:
            del_temp.append(deepcopy(result))
            result += clipboard

    return result

operations = [
    "INSERT Da",
    "COPY 0",
    "UNDO",
    "PASTE",
    "PASTE",
    "COPY 2",
    "PASTE",
    "PASTE",
    "DELETE",
    "INSERT aaam"
]

res = newTextEditor(operations)
print(res)