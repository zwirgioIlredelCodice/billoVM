def read_file(file):
    f  = open(file, "r")
    data = f.read()
    f.close()
    return data

keyword = ["function", "return", "print"]
newline = ["->", "-->"]
operation = ["=", "+", "-", "*", "/"]
block_open = "("
block_close = ")"

data = read_file("one.billo")
data_splitted = data.split()

data_token_type = []
for token in data_splitted:
    if token in keyword:
        data_token_type.append("t_keyword")
    elif token in newline:
        data_token_type.append("t_newline")
    elif token in operation:
        data_token_type.append("t_operation")
    elif token == block_open:
        data_token_type.append("t_block_open")
    elif token == block_close:
        data_token_type.append("t_block_close")
    else:
        data_token_type.append("t_?")

print(data)
for i in range(len(data_splitted)):
    print("token= ", data_splitted[i], "type= ",data_token_type[i])
