#!/usr/bin/env python3
# if not working chmod +x billolang.py

import sys

#           DECLARING TERMINAL
#           COLOR 
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

#           DECLARING INSTRUCTION SET 
#           CONSTANT
LOAD_C                  = 0
ADDITION_C              = 1
SUBTRACTION_C           = 2
MULTIPLICATION_C        = 3
DIVISION_C              = 4
AND_C                   = 5
OR_C                    = 6
XOR_C                   = 7
NOT_C                   = 8
ADDITION                = 9
SUBTRACTION             = 10
DIVISION                = 11
AND                     = 12
OR                      = 13
XOR                     = 14
NOT                     = 15
LOAD_MEMORY             = 16
STORE_MEMORY            = 17
DELATE_MEMORY           = 18
JUMP                    = 19
JUMP_CONDITIONAL        = 20
CALL_FUNCTION           = 21
RETURN_FUNCTION         = 22
PRINT_ACCUMULATOR       = 23
PRINT_MEMORY            = 24
HALT                    = 25

#           DECLARING TOKEN 
#           TYPES
keyword = ["var", "if"]
operation = ["+", "-", "*", "/", "and", "or", "xor", "not"]
arrow = "->"

#           DECLARING CLASSES
#
class token:
    def __init__(self, kind, value):
        self.kind = kind                # kind is es keyword, operation ..
        self.value = value              # value is the token value es token("operation", "+")

class control_flow:
    def __init__(self, kind, position):
        self.kind = kind                # kind is es if, do, while
        self.position = position        # position is the position of the token 

class Instruction:                      # opcode and operand can be strings
    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand
        self.point_control_flow = []    # is an array of control flow block open (o@..) and closed (c@..) es ["o@32", "c@11"]

class instruction_n:                    #step after Instruction -> opcode and operand can be only numbers
    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand

#           DECLARING
#           FUNCTIONS

# given a file path es "folder/myfile.txt"
# return content  
def read_file(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

def print_byte_file(file, bytecode):
    f = open(file, "wb")
    f.write(bytecode)
    f.close()


# given a list of token, print them
# 
def print_token(token_list_line):
    line_n = 0
    for line_tok in token_list_line:
        print("line ", line_n)
        for tok in line_tok:
            print("\ttoken[kind = ", tok.kind, ", variable = ", tok.value,"]")
        line_n = line_n + 1

def print_instruction(instruction):
    for istr in instruction:
        print(istr.opcode, istr.operand)
        for pcf in istr.point_control_flow:
            if pcf.startswith("c@"):
                print("\tclose block",pcf[2:])
            elif pcf.startswith("o@"):
                print("\topen block",pcf[2:])
            else:
                print("WARNING strange point_control_flow definition", pcf)
def tokenize(data):

    # split string into token when "\n" " " "\t"
    token_value = data.split()

    token_list = []
    kind  = ""
    
    for value in token_value:
        if value.isdigit():
            kind = "t_number"

        elif value in keyword:
            kind = "t_keyword"

        elif value == arrow:
            kind = "t_arrow"

        elif value in operation:
            kind = "t_operation"

        else:
            kind = "t_?"
        
        token_list.append(token(kind, value)) #add new token to token_list[]
        
    # p2 make list line

    token_list_line = []
    token_line = []

    for tok in token_list:

        if tok.kind != "t_arrow": # when -> end line
            token_line.append(tok)

        else:
            token_list_line.append(token_line)
            token_line = []
    
    return token_list_line

def instruction_str_to_n(program):
    program_n = []
    opcode = 0
    operand = 0

    for i in range(len(program)):

        # like switch case for all of opcodes
        # translate opcode name(string) to a opcode value(number)
        if program[i].opcode == "LOAD_C":
            opcode = LOAD_C
        elif program[i].opcode == "ADDITION_C":
            opcode = ADDITION_C
        elif program[i].opcode == "SUBTRACTION_C":
            opcode = SUBTRACTION_C 
        elif program[i].opcode == "MULTIPLICATION_C":
            opcode = MULTIPLICATION_C         
        elif program[i].opcode == "DIVISION_C":
            opcode = DIVISION_C      
        elif program[i].opcode == "AND_C":
            opcode = AND_C           
        elif program[i].opcode == "OR_C":
            opcode = OR_C            
        elif program[i].opcode == "XOR_C":
            opcode = XOR_C           
        elif program[i].opcode == "NOT_C":
            opcode = NOT_C           
        elif program[i].opcode == "ADDITION":
            opcode = ADDITION        
        elif program[i].opcode == "SUBTRACTION":
            opcode = SUBTRACTION     
        elif program[i].opcode == "DIVISION":
            opcode = DIVISION        
        elif program[i].opcode == "AND":
            opcode = AND             
        elif program[i].opcode == "OR":
            opcode = OR              
        elif program[i].opcode == "XOR":
            opcode = XOR             
        elif program[i].opcode == "NOT":
            opcode = NOT             
        elif program[i].opcode == "LOAD_MEMORY":
            opcode = LOAD_MEMORY     
        elif program[i].opcode == "STORE_MEMORY":
            opcode = STORE_MEMORY    
        elif program[i].opcode == "DELATE_MEMORY":
            opcode = DELATE_MEMORY   
        elif program[i].opcode == "JUMP":
            opcode = JUMP            
        elif program[i].opcode == "JUMP_CONDITIONAL":
            opcode = JUMP_CONDITIONAL
        elif program[i].opcode == "CALL_FUNCTION":
            opcode = CALL_FUNCTION   
        elif program[i].opcode == "RETURN_FUNCTION":
            opcode = RETURN_FUNCTION  
        elif program[i].opcode == "PRINT_ACCUMULATOR":
            opcode = PRINT_ACCUMULATOR
        elif program[i].opcode == "PRINT_MEMORY":
            opcode = PRINT_MEMORY
        else:
            print("not found opcode",program[i].opcode)
            exit(1)
        
        # check operand validity and set value for jumps 
        if program[i].operand.startswith("o@") or program[i].operand.startswith("c@"):
            for ii in range(len(program)):
                if program[i].operand in program[ii].point_control_flow:
                    operand = ii
        else:
            operand = int(program[i].operand)
        
        program_n.append(instruction_n(opcode, operand))

    program_n.append(instruction_n(HALT, 0))
    return program_n

# given array of line of token
#
def traduce(token_list_line):

    control_flow_stack = [] #stack containing if, for, while statement open
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

                instruction_n += 1

        elif keyword_startline == "if":

            control_flow_stack.append(control_flow("if", instruction_n))
            program[-1].point_control_flow.append("o@"+str(control_flow_stack[-1].position))

        elif keyword_startline == "while":

            control_flow_stack.append(control_flow("while", instruction_n))
            program[-1].point_control_flow.append("o@"+str(control_flow_stack[-1].position))

        elif keyword_startline == "do":

            opcode = "JUMP_CONDITIONAL"
            operand = "c@"+str(control_flow_stack[-1].position) # is not right todo: after make code all instruction change @.. value with right ones
            program.append(Instruction(opcode, operand))
            instruction_n += 1
        
        elif keyword_startline == "else":
            control_flow_stack.append(control_flow("if", instruction_n))
            
            opcode = "JUMP"
            operand = "c@"+str(control_flow_stack[-1].position)
    
            program.append(Instruction(opcode, operand))
            instruction_n += 1

            program[-1].point_control_flow.append("c@"+str(control_flow_stack[-2].position))
            program[-1].point_control_flow.append("o@"+str(control_flow_stack[-1].position))

            control_flow_stack.pop(-2)

        elif keyword_startline == "end":

                if control_flow_stack[-1].kind == "while":
                    opcode = "JUMP"
                    operand = "o@"+str(control_flow_stack[-1].position)
                    program.append(Instruction(opcode, operand))
                    instruction_n += 1
                    program[-1].point_control_flow.append("c@"+str(control_flow_stack[-1].position))

                    control_flow_stack.pop()

                else:
                    program[-1].point_control_flow.append("c@"+str(control_flow_stack[-1].position))
                    control_flow_stack.pop() #problem when if close not close his own if block ------------------to fix
                    #print(sas.kind)

        #base case
        else:
            opcode = "LOAD_C"
            for tok in line_tok:
                program.append(Instruction(opcode, tok.value))
                instruction_n += 1
    return program
        

def to_bytecode(code):
    size_int = 4 # 4 byte make a c int
    size_char = 1 # 1 byte make a c char
    bytecode = b''
    for instruction in code:
        b_opcode = instruction.opcode.to_bytes(size_char, byteorder='big', signed=False) #https://docs.python.org/3/library/stdtypes.html#int.to_bytes
        b_operand = instruction.operand.to_bytes(size_int, byteorder='big', signed=True)
        bytecode += b_opcode
        bytecode += b_operand
    return bytecode

if __name__ == "__main__":
    cli_arguments = sys.argv[1:] # the first argument is the mane of the script so delate it
    if len(cli_arguments) > 0:
        file_in = cli_arguments[0]
        file_out = cli_arguments[1]
        data = read_file(file_in)
        token_list_line = tokenize(data)
        instruction = traduce(token_list_line)
        instruction_n = instruction_str_to_n(instruction)
        bytecode = to_bytecode(instruction_n)
        print_byte_file(file_out, bytecode)
        if cli_arguments[2] == "debug":
            print_token(token_list_line)
            print_instruction(instruction)
            print(bytecode)
    else:
        print("file name argument is missing -> EXIT")