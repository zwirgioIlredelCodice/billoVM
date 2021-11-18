#include <stdio.h>
#include <stdlib.h>
#include "billoVM.h"
#include "ht.h"

void debug_billoVM(billoVM *vm)
{

    printf("accumulator= %d\n", vm->accumulator);
    /*
    printf("memory= ");
    for (size_t i = 0; i < vm->memory.capacity; i++)
    {
        if (vm->memory.cell[i].empty)
        {
            printf("empty ");
        }
        
        printf("%d ", vm->memory.cell[i].value);
    }
    printf("\n");
    */
}

void init_billoVM(billoVM *vm)
{
    vm->accumulator = 0;
    vm->program_counter = 0;
    vm->call_stack_pointer = 0;

    ht_create(&vm->memory);

    for (size_t i = 0; i < CALL_STACK_SIZE; i++)
    {
        vm->call_stack[i] = 0;
    }
}

void delate_billoVM(billoVM *vm)
{
    ht_destroy(&vm->memory);
}

void run(billoVM *vm, code program[])
{
    int opcode, operand, value;

    while (1)
    {
        opcode = program[vm->program_counter].opcode;
        operand = program[vm->program_counter].operand;

        switch (opcode)
        {
        case LOAD_C:
            vm->accumulator = operand;
            (vm->program_counter)++;
            break;
        
        case ADDITION_C:
            vm->accumulator += operand;
            (vm->program_counter)++;
            break;
        
        case SUBTRACTION_C:
            vm->accumulator -= operand;
            (vm->program_counter)++;
            break;
        
        case MULTIPLICATION_C:
            vm->accumulator *= operand;
            (vm->program_counter)++;
            break;

        case DIVISION_C:
            vm->accumulator /= operand;
            (vm->program_counter)++;
            break;

        case AND_C:
            vm->accumulator &= operand;
            (vm->program_counter)++;
            break;

        case OR_C:
            vm->accumulator |= operand;
            (vm->program_counter)++;
            break;

        case XOR_C:
            vm->accumulator ^= operand;
            (vm->program_counter)++;
            break;

        case NOT_C:
            vm->accumulator = ~vm->accumulator;
            (vm->program_counter)++;
            break;

        case ADDITION:
            value = ht_get(&vm->memory, operand);
            vm->accumulator += value;
            (vm->program_counter)++;
            break;

        case SUBTRACTION:
            value = ht_get(&vm->memory, operand);
            vm->accumulator -= value;
            (vm->program_counter)++;
            break;

        case DIVISION:
            value = ht_get(&vm->memory, operand);
            vm->accumulator /= value;
            (vm->program_counter)++;
            break;

        case AND:
            value = ht_get(&vm->memory, operand);
            vm->accumulator &= value;
            (vm->program_counter)++;
            break;

        case OR:
            value = ht_get(&vm->memory, operand);
            vm->accumulator |= value;
            (vm->program_counter)++;
            break;

        case XOR:
            value = ht_get(&vm->memory, operand);
            vm->accumulator ^= value;
            (vm->program_counter)++;
            break;

        case NOT:
            vm->accumulator = ~vm->accumulator;
            (vm->program_counter)++;
            break;
        
        case LOAD_MEMORY:
            value = ht_get(&vm->memory, operand);
            vm->accumulator = value;
            (vm->program_counter)++;
            break;
        
        case STORE_MEMORY:
            ht_set(&vm->memory, operand, vm->accumulator);
            (vm->program_counter)++;
            break;
        
        case DELATE_MEMORY:
            ht_delate(&vm->memory, operand);
            (vm->program_counter)++;
            break;
        
        case JUMP:
            vm->program_counter = operand;
            (vm->program_counter)++;
            break;
        
        case JUMP_CONDITIONAL:
            if (vm->accumulator == 0) {
                vm->program_counter = operand;
                (vm->program_counter)++;
            }
            else
                (vm->program_counter)++;
            break;
        
        case CALL_FUNCTION:
            break;
        
        case RETURN_FUNCTION:
            break;
        
        case PRINT_ACCUMULATOR:
            printf("%c",vm->accumulator); //temp
            (vm->program_counter)++;
            break;
        
        case PRINT_MEMORY:
            value = ht_get(&vm->memory, operand);
            printf("%d\n",value); //temp
            (vm->program_counter)++;
            break;
        
        case HALT:
            return;
        }
        
        //debug_billoVM(vm);
    }
}