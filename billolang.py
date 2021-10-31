def read_file(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data


class token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


def print_token(token_list):
    for i in range(len(token_list)):
        print("token[kind = ", token_list[i].kind, "] [value = ", token_list[i].value, "]")

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

    # find what token is p2 recognise variable
        number_token = len(token_list)

    for i in range(number_token):
        if token_list[i].kind == "t_keyword" and token_list[i].value == "var":
            new_variable = token_list[i+1].value  # variable name

            # change all token after with type t_? with t_variable if is recognised t_variable = new_variable
            for y in range(i+1, number_token):
                if token_list[y].kind == "t_?" and token_list[y].value == new_variable:
                    token_list[y].kind = "t_variable"
    
    for tok in token_list:
        if tok.kind == "t_?":
            print("ERROR token without a kind with value ",tok.value)
            error = error + 1
    if error > 0:
        return -1
    else:
        return token_list

def traduce(token_list):

    token_line = []

    for tok in token_list:

        if tok.kind != "t_arrow":
            token_line.append(tok)

        else:
            #print_token(token_line)
            key_line = token_line[0] # key_line is keyword
            token_line.pop(0) #pop it form key_line
            if key_line.kind != "t_keyword" and key_line.kind != "t_operation":
                print("ERROR token with value ",key_line.value," after -> must be a keyword")
                return -1
            else:
                for ttok in token_line:
                    print(key_line.value, ttok.value)
            token_line = []

# read from file
name_file = "one.billo"
data = read_file(name_file)
if data != "": #if is not empty
    token_list = tokenize(data)
    print_token(token_list)

    if token_list != -1: #if tokenize() return no errors
        print("\n\n##############sasadsdas traduce\n\n")
        traduce(token_list)

    else:
        print("error EXIT")

else:
    print("file ", name_file, "empty EXIT")