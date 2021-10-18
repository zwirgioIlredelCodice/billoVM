#include <stdio.h>
#include <stdlib.h>
#include "ht.h"

ht *ht_create(ht *table)
{
    table->capacity = INITIAL_CAPACITY;
    table->length = 0;
    table->cell = malloc(sizeof(ht_cell) * INITIAL_CAPACITY);
    for (size_t i = 0; i < INITIAL_CAPACITY; i++)
    {
        table->cell[i].empty = true;
    }
}

void ht_destroy(ht *table)
{
    free(table->cell);
}

size_t hash(size_t key, size_t capacity)
{
    return key % capacity;
}

int ht_get(ht *table, size_t key)
{
    size_t hash_num = hash(key, table->capacity);
    size_t index = hash_num;

    while (!table->cell[index].empty)
    {
        if (key == table->cell[index].key)
        {
            // Found key, return value.
            return table->cell[index].value;
        }
        // Key wasn't in this slot, move to next (linear probing).
        index++;
        if (index >= table->capacity)
        {
            // At end of entries array, wrap around.
            index = 0;
        }
    }
    return 0;
}

void ht_resize(ht *table, size_t new_capacity)
{
    ht_cell *new_cell = malloc(sizeof(ht_cell) * new_capacity);

    for (size_t i = 0; i < new_capacity; i++)
    {
        new_cell[i].empty = true;
    }
    for (size_t i = 0; i < table->capacity; i++)
    {
        ht_cell cell = table->cell[i];
    
        if (!cell.empty)
        {
            ht_set_table(new_cell, cell.key, cell.value, new_capacity);
        }
    }
    // Free old entries array and update this table's details.
    free(table->cell);
    table->cell = new_cell;
    table->capacity = new_capacity;
}

void ht_set_table(ht_cell *cell, size_t key, int value, size_t capacity)
{
    size_t hash_num = hash(key, capacity);
    size_t index = hash_num;

    while (!cell[index].empty)
    {
        if (key == cell[index].key)
        {
            // Found key (it already exists), update value.
            cell[index].value = value;
        }
        // Key wasn't in this slot, move to next (linear probing).
        index++;
        if (index >= capacity)
        {
            // At end of entries array, wrap around.
            index = 0;
        }
    }

    // Didn't find key, allocate+copy if needed, then insert it.
    cell[index].empty = false;
    cell[index].key = key;
    cell[index].value = value;
}

void ht_set(ht *table, size_t key, int value)
{
    // If length will exceed 3/4 of current capacity, expand it.
    if (table->length >= (table->capacity / 4) * 3)
    {
        ht_resize(table, (table->capacity / 4) * 3);
    }

    ht_set_table(table->cell, key, value, table->capacity);
    table->length++;
}

void ht_delate(ht *table, size_t key)
{
    // If length is less than 1/2 of current capacity, reduce it.
    if (table->length <= table->capacity / 2)
    {
        ht_resize(table, table->capacity / 2);
    }

    size_t hash_num = hash(key, table->capacity);
    size_t index = hash_num;

    while (!table->cell[index].empty)
    {
        if (key == table->cell[index].key)
        {
            // Found key, delate value.
            table->length--;
            table->cell[index].value = 0;
            table->cell[index].empty = true;
        }
        // Key wasn't in this slot, move to next (linear probing).
        index++;
        if (index >= table->capacity)
        {
            // At end of entries array, wrap around.
            index = 0;
        }
    }
}

void ht_show(ht *table)
{
    printf("elements=%d\n", table->length);
    for (size_t i = 0; i < table->capacity; i++)
    {
        if (table->cell[i].empty)
        {
            printf("empty\n");
        }
        else
        {
            printf("slot %d key=%d value=%d\n", i, table->cell[i].key, table->cell[i].value);
        }
    }
    printf("\n");
}

int main()
{
    ht table;
    ht_create(&table);
    ht_set(&table, 2, 54);
    ht_set(&table, 3, 53);
    ht_set(&table, 4, 52);
    ht_show(&table);
    ht_set(&table, 5, 51);
    ht_show(&table);
    ht_destroy(&table);
}