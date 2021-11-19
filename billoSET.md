# billo's instruction set


## single registre machine
```
|======================|
| accumulator          |
|======================|
| program counter      |
|======================|
| function             |
| call stack           |
| [[] [] []]           |
|======================|
| memory               |
|(hash table)          |
| [[key=1, value = 2]  |
|  [empty = true]      |
|  [key=3, value = 7]  |
| ]                    |
|                      |
|======================|

code =  |=========================|
        | OPCODE |    OPERAND     |
        | 8bit   |    16bit       |
        |=========================|
```


OPCODE_C for constant

OPCODE                  | DESCRIPTION                                           | EXAMPLE
------------------------| ------------------------------------------------------| ---------------------
LOAD_C                  | **accumulator** = *OPERAND*                           | LOAD_C **1**
ADDITION_C              | **accumulator** + *OPERAND*                           | ADDITION_C **2**
SUBTRACTION_C           | **accumulator** - *OPERAND*                           | SUBTRACTION_C **3**
MULTIPLICATION_C        | **accumulator** * *OPERAND*                           | MULTIPLICATION_C **3**
DIVISION_C              | **accumulator** / *OPERAND*                           | DIVISION_C **4**
AND_C                   | **accumulator** and *OPERAND*                         | AND_C **1**
OR_C                    |  **accumulator** or *OPERAND*                         | OR_C **0**
XOR_C                   | **accumulator** xor *OPERAND*                         | XOR_C **1**
NOT_C                   | **accumulator** not *OPERAND*                         | NOT_C **0**
ADDITION                | **accumulator** + memory[ *OPERAND* ]                 | ADDITION **324**
SUBTRACTION             | **accumulator** - memory[ *OPERAND* ]                 | SUBTRACTION **324**
MULTIPLICATION          | **accumulator** * memory[ *OPERAND* ]                 | MULTIPLICATION **673**
DIVISION                | **accumulator** - memory[ *OPERAND* ]                 | DIVISION **324**
AND                     | **accumulator** and memory[ *OPERAND* ]               | AND **324**
OR                      | **accumulator** or memory[ *OPERAND* ]                | OR **324**
XOR                     | **accumulator** xor memory[ *OPERAND* ]               | XOR **324**
NOT                     | **accumulator** not memory[ *OPERAND* ]               | NOT **324**
LOAD_MEMORY             | **accumulator** = memory[ *OPERAND* ]                 | LOAD_MEMORY **1**
STORE_MEMORY            | memory[ *OPERAND* ] = **accumulator**                 | STORE_MEMORY **1**
DELATE_MEMORY           | memory[ *OPERAND* ].empty = true                      | DELATE_MEMORY **1**
JUMP                    | program counter = *OPERAND*                           | JUMP **34**
JUMP_CONDITIONAL        | if **accumulator** = 0 program counter = *OPERAND*    | JUMP_CONDITIONAL **34**
CALL_FUNCTION           |                                                       | 
RETURN_FUNCTION         |                                                       | 
PRINT_ACCUMULATOR       | print out **accumulator**                             | PRINT
PRINT_MEMORY            | print out memory[ *OPERAND* ]                         | PRINT 34
HALT                    | terminate pogram                                      | HALT **1**