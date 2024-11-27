#!/usr/bin/env python3


def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]


print(return_evens([0, 1, 3, 5, 7, 8, 9]))
pass


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]


print(make_exclamation)
pass
