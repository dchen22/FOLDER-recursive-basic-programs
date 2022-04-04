def parenthesis_parser(func):
    count = 0
    while count < len(func):
        if func[count] == "(":
            newfunc = parenthesis_parser(func[1 + count:])
            print(func[1 + count:1 + count + newfunc])
            count = count + newfunc + 1
        elif func[count] == ")":
            return count
        count = count + 1

parenthesis_parser("(x + 1) * (x(x + 3) x + 5 + (()x + 5))")