RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def read_file(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

class token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

class control_flow:
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number


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

    control_flow_stack = [] #stack containing if, for, while statment open
    control_flow_number = 0
 
    for line_tok in token_list_line:

        keyword_startline = line_tok[0].value

        if keyword_startline == "if":

            control_flow_number = control_flow_number + 1

            control_flow_stack.append(control_flow("if", control_flow_number))
            print(RED,"\t=OPEN= statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)

        elif keyword_startline == "while":

            control_flow_number = control_flow_number + 1

            control_flow_stack.append(control_flow("while", control_flow_number))
            print(RED,"\t=OPEN= statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)

        elif keyword_startline == "do":
            print(GREEN,"\tif register is false jump *CLOSE* statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)
    
        elif keyword_startline == "end":

                if control_flow_stack[-1].kind == "while":
                     print(GREEN,"\tjump *OPEN* statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)
                     print(RED,"\t=CLOSE= statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)
                     control_flow_stack.pop()
                
                elif len(line_tok) > 1 and line_tok[1].value == "else":

                    control_flow_temp = control_flow_stack.pop()
                    control_flow_number = control_flow_number + 1

                    control_flow_stack.append(control_flow("else", control_flow_number))
                    print(GREEN,"\tjump *CLOSE* statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)
                    print(RED,"\t=CLOSE= statment",control_flow_temp.number, "type",control_flow_temp.kind ,RESET)
                    print(RED,"\t=OPEN= statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)
                    
                else:
                    print(RED,"\t=CLOSE= statment",control_flow_stack[-1].number, "type",control_flow_stack[-1].kind ,RESET)
                    control_flow_stack.pop()

        #base case
        else:
            for tok in line_tok[1:]:
                print(keyword_startline, tok.value)

class Instruction:
    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand
        pass

def to_bytecode(code):
    size_int = 2 # 2 byte make a c int
    size_char = 1 # 1 byte make a c char
    bytecode = b''
    for instruction in code:
        b_opcode = instruction.opcode.to_bytes(size_char, byteorder='big') #https://docs.python.org/3/library/stdtypes.html#int.to_bytes
        b_operand = instruction.operand.to_bytes(size_int, byteorder='big', signed=True)
        bytecode += b_opcode
        bytecode += b_operand
    print(bytecode)

    f = open("out.bbillo", "wb")
    f.write(bytecode)
    f.close()

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

program = [Instruction(2, 234),Instruction(2, 234),Instruction(2, 234)]
to_bytecode(program)

if a < 43:
    print("sas ciao sono c")
