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

void ht_set(ht *table, size_t key, int value)
{
    size_t hash_num = hash(key, table->capacity);
    size_t index = hash_num;

    while (!table->cell[index].empty)
    {
        if (key == table->cell[index].key)
        {
            // Found key (it already exists), update value.
            table->cell[index].value = value;
        }
        // Key wasn't in this slot, move to next (linear probing).
        index++;
        if (index >= table->capacity)
        {
            // At end of entries array, wrap around.
            index = 0;
        }
    }

    // Didn't find key, allocate+copy if needed, then insert it.
    table->cell[index].empty = false;
    table->cell[index].key = key;
    table->cell[index].value = value;
}

void ht_delate(ht *table, size_t key)
{
    size_t hash_num = hash(key, table->capacity);
    size_t index = hash_num;

    while (!table->cell[index].empty)
    {
        if (key == table->cell[index].key)
        {
            // Found key, delate value.
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

int main()
{
    ht table;
    ht_create(&table);
    ht_set(&table,2,55);
    int viva = ht_get(&table, 2);
    printf("%d", viva);
    ht_destroy(&table);
}