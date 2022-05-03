def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = 'x is same as y'
    else:
        result = 'x is greater than y'

    result = 'x is less than y' if x < y else 'x is greater than y'

    print(result)

    # match-case to compare multiple values
    value = 'three'
    match value:
        case 'one':
            result = 1
        case 'two':
            result = 2
        case 'three' | 'four':
            result = 'three or four'
        case _:
            result = -1
    print(result)
main()