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
        print("type", token_list[i].kind, "value ", token_list[i].value)


def tokenize(data):
    token_list = []

    keyword = ["var", "if"]
    operation = ["=", "+", "-", "*", "/"]
    arrow = "->"

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
    
    return token_list


# read from file
data = read_file("one.billo")
token_list = tokenize(data)

print_token(token_list)