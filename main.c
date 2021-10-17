#include <stdio.h>
#include "billoVM.h"

int main()
{
    code program[] =
        {
            {LOAD_CONSTANT, 5},
            {STORE_MEMORY, 0},
            {CALL_FUNCTION, 4},
            {HALT, 0},
            {ADDITION, 0},
            {PRINT, 0},
            {RETURN_FUNCTION, 0}};

    billoVM vm;
    init_billoVM(&vm);

    run(&vm, program);

    delate_billoVM(&vm);
}