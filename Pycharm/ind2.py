#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def del_number(type='even'):
    def helper(lst):
        if type == 'even':
            lst = [i for i in lst if i % 2 != 0]
        else:
            lst = [i for i in lst if i % 2 == 0]
        return lst

    return helper


if __name__ == '__main__':
    print(del_number(input('Введите even/odd: '))(map(int, input('Введите список целых чисел: ').split(', '))))
