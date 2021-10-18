#pragma once
#include <stddef.h>
#include <stdbool.h>

#define INITIAL_CAPACITY 4

typedef struct ht_cell
{
    size_t key;
    int value;
    bool empty;
} ht_cell;

typedef struct ht
{
    ht_cell* cell;
    size_t capacity;
    size_t length;
} ht;

ht* ht_create(ht* table);

void ht_destroy(ht* table);

int ht_get(ht* table, size_t key);

void ht_resize(ht *table, size_t new_capacity);

void ht_set_table(ht_cell *cell, size_t key, int value, size_t capacity);

void ht_set(ht* table, size_t key, int value);

void ht_delate(ht* table, size_t key);

void ht_show(ht *table);