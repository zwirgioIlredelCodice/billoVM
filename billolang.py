
#delcaring things

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

LOAD_C                  = 0
ADDITION_C              = 1
SUBTRACTION_C           = 2
DIVISION_C              = 3
AND_C                   = 4
OR_C                    = 5
XOR_C                   = 6
NOT_C                   = 7
ADDITION                = 8
SUBTRACTION             = 9
DIVISION                = 10
AND                     = 11
OR                      = 12
XOR                     = 13
NOT                     = 14
LOAD_MEMORY             = 15
STORE_MEMORY            = 16
DELATE_MEMORY           = 17
JUMP                    = 18
JUMP_CONDITIONAL        = 19
CALL_FUNCTION           = 20
RETURN_FUNCTION         = 21
PRINT_ACCUMULATOR       = 22
PRINT_MEMORY            = 23

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
    def __init__(self, kind, position):
        self.kind = kind
        self.position = position

class Instruction:
    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand
        self.open_here_control_flow = []
        self.closed_here_control_flow = []


def print_token(token_list_line):
    line_n = 0
    for line_tok in token_list_line:
        print("line ", line_n)
        for tok in line_tok:
            print("\ttoken[kind = ", tok.kind, ", variable = ", tok.value,"]")
        line_n = line_n + 1

keyword = ["var", "if"]
operation = ["+", "-", "*", "/", "and", "or", "xor", "not"]
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
    opcode = ""
    program = []
    instruction_n = 0
 
    for line_tok in token_list_line:

        keyword_startline = line_tok[0].value
        opcode = ""

        if keyword_startline in operation:
            if keyword_startline == "+":
                opcode = "ADDITION_C"
            elif keyword_startline == "-":
                opcode = "SUBTRACTION_C"
            elif keyword_startline == "/":
                opcode = "DIVISION_C"
            elif keyword_startline == "*":
                opcode = "MULTIPLICATION_C"
            elif keyword_startline == "and":
                opcode = "AND_C"
            elif keyword_startline == "or":
                opcode = "OR_C"
            elif keyword_startline == "xor":
                opcode = "XOR_C"
            elif keyword_startline == "not":
                opcode = "NOT_C"
            for tok in line_tok[1:]:
                program.append(Instruction(opcode, tok.value))
                print(instruction_n, opcode, tok.value)

                instruction_n += 1

        elif keyword_startline == "if":

            control_flow_stack.append(control_flow("if", instruction_n))
            print(RED,"\t=OPEN= statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
            program[-1].open_here_control_flow.append("o@"+str(control_flow_stack[-1].position))

        elif keyword_startline == "while":

            control_flow_stack.append(control_flow("while", instruction_n))
            print(RED,"\t=OPEN= statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
            program[-1].open_here_control_flow.append("o@"+str(control_flow_stack[-1].position))

        elif keyword_startline == "do":
            print(GREEN,"\tif register is false jump *CLOSE* statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)

            opcode = "JUMP_CONDITIONAL"
            operand = "c@"+str(control_flow_stack[-1].position) # is not right todo: after make code all instruction chage @.. value with right ones
            print(GREEN,instruction_n, opcode, operand, RESET)
            program.append(Instruction(opcode, operand))
            instruction_n += 1
    
        elif keyword_startline == "end":

                if control_flow_stack[-1].kind == "while":
                    print(GREEN,"\tjump *OPEN* statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
                    opcode = "JUMP"
                    operand = "o@"+str(control_flow_stack[-1].position)
                    print(GREEN,instruction_n, opcode, operand, RESET)
                    program.append(Instruction(opcode, operand))
                    instruction_n += 1
                    print(RED,"\t=CLOSE= statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
                    program[-1].closed_here_control_flow.append("c@"+str(control_flow_stack[-1].position))

                    control_flow_stack.pop()
                
                elif len(line_tok) > 1 and line_tok[1].value == "else":

                    control_flow_temp = control_flow_stack.pop()

                    control_flow_stack.append(control_flow("else", instruction_n))
                    print(GREEN,"\tjump *CLOSE* statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
                    opcode = "JUMP"
                    operand = "c@"+str(control_flow_stack[-1].position)
                    print(GREEN,instruction_n, opcode, operand, RESET)
                    program.append(Instruction(opcode, operand))
                    instruction_n += 1
                    print(RED,"\t=CLOSE= statment",control_flow_temp.position, "type",control_flow_temp.kind ,RESET)
                    program[-1].closed_here_control_flow.append("c@"+str(control_flow_stack[-1].position))
                    print(RED,"\t=OPEN= statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
                    program[-1].open_here_control_flow.append("o@"+str(control_flow_stack[-1].position))
                    
                else:
                    print(RED,"\t=CLOSE= statment",control_flow_stack[-1].position, "type",control_flow_stack[-1].kind ,RESET)
                    program[-1].closed_here_control_flow.append("c@"+str(control_flow_stack[-1].position))
                    control_flow_stack.pop()

        #base case
        else:
            opcode = "LOAD_C"
            for tok in line_tok:
                program.append(Instruction(opcode, tok.value))
                print(instruction_n, opcode, tok.value)
                instruction_n += 1
    
    i = 0
    for instruction in program:
        print(i, instruction.opcode, instruction.operand, 
            instruction.open_here_control_flow,
            instruction.closed_here_control_flow)
        i += 1

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

#program = [Instruction(2, 234),Instruction(2, 234),Instruction(2, 234)]
#to_bytecode(program)