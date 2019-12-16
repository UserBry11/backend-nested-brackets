#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Will read lines and determine if appropriate pairs are present and output
results to a new file.
"""
__author__ = "Bryan"

import sys


def main(args):
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as wf:
            f_lines = f.readlines()

            openers = ["(", "[", "{", "<", "(*"]
            closers = [")", "]", "}", ">", "*)"]

            def nested_funct(line):
                stack = []
                count = 0

                while line:
                    token = line[0]
                    if line.startswith('(*'):
                        token = '(*'
                    elif line.startswith('*)'):
                        token = '*)'
                    count += 1
                    line = line[len(token):]

                    if token in openers:
                        stack.append(token)
                    elif token in closers:
                        i = closers.index(token)
                        expected_opener = openers[i]

                        if not stack or stack.pop() != expected_opener:
                            return False, count
                if stack:
                    return False, count

                return True, 0

            for line in f_lines:
                result, index = nested_funct(line)
                result_str = "NO {}".format(index) if not result else "YES"
                wf.write("{}\n".format(result_str))


if __name__ == '__main__':
    main(sys.argv)
