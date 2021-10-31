def read_file(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data


class token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


def print_token(token_list_line):
    line_n = 0
    for line_tok in token_list_line:
        print("line ", line_n)
        for tok in line_tok:
            print("\ttoken[kind = ", tok.kind, ", variable = ", tok.value,"]")
        line_n = line_n + 1

keyword = ["var", "if"]
operation = ["=", "+", "-", "*", "/"]
arrow = "->"

def tokenize(data):

    error = 0

    token_list = []

    # split string into token when "\n" " " "\t"
    token_value = data.split()

    # set class token value
    for tok in token_value:
        token_list.append(token("", tok))


    # find what token is p1
    for i in token_list:

        if i.value.isdigit():
            i.kind = "t_number"

        elif i.value in keyword:
            i.kind = "t_keyword"

        elif i.value == arrow:
            i.kind = "t_arrow"

        elif i.value in operation:
            i.kind = "t_operation"

        else:
            i.kind = "t_?"

    # p2 make list line

    token_list_line = []
    token_line = []

    for tok in token_list:

        if tok.kind != "t_arrow":
            token_line.append(tok)

        else:
            token_list_line.append(token_line)
            token_line = []
    
    return token_list_line

def traduce(token_list_line):
    for line_tok in token_list_line:
        keyword_startline = line_tok[0].value
        for tok in line_tok[1:]:
            print(keyword_startline, tok.value)

# read from file
name_file = "one.billo"
data = read_file(name_file)
if data != "": #if is not empty
    token_list_line = tokenize(data)
    print_token(token_list_line)

    if token_list_line != -1: #if tokenize() return no errors
        print("\nTRADUCE\n")
        traduce(token_list_line)

    else:
        print("error EXIT")

else:
    print("file ", name_file, "empty EXIT")