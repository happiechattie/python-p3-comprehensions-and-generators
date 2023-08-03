#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [item for item in num_list if item % 2 == False]
    return new_list

def make_exclamation(sentence_list):
    new_list = [item + "!" for item in sentence_list if True]
    return new_list