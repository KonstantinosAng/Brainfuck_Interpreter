#!/usr/bin/python
"""
Author: Konstantinos Angelopoulos
Date: 04/02/2020
All rights reserved.
Feel free to use and modify and if you like it give it a star.
"""


class Brainfuck:

    def __init__(self, code=None):
        if code is None:
            import sys
            if len(sys.argv) == 2:
                file = sys.argv[1]
                if file[-3:] == '.bf':
                    with open(file, 'r') as f:
                        self._code = f.read()
                else:
                    raise Exception('[ARGUMENT ERROR] Not a brainf*ck file. File must end with .bf')
            else:
                raise Exception("Usage: python {} filename".format(sys.argv[0]))
        else:
            if isinstance(code, str):
                self._code = code
            else:
                raise Exception('[ARGUMENT ERROR] Code is not type string: {}'.format(code))
        self._buffer = [0]
        self._pointer = 0
        self._loop_map = []

    def syntax(self):
        brackets = 0
        for c in self._code:
            if c == '[' or c == ']':
                brackets += 1
            if c not in ['+', '-', '<', '>', '.', ',', '[', ']']:
                raise Exception('[Syntax Error] Unexpected character: {}'.format(c))
        if brackets % 2 != 0:
            raise Exception("[Syntax Error] Loop Brackets miss match!")

    def loop_mapping(self):
        loops = []
        for i, c in enumerate(self._code):
            if c == '[':
                loops.append(i)
            if c == ']':
                self._loop_map.append([loops[-1], i])
                del loops[-1]

    def evaluate(self):
        import sys
        self.syntax()
        self.loop_mapping()
        i = 0
        while i < len(self._code):
            c = self._code[i]
            if c == '+':
                if self._buffer[self._pointer] < 255:
                    self._buffer[self._pointer] += 1
                else:
                    self._buffer[self._pointer] = 0
            if c == '-':
                if self._buffer[self._pointer] > 0:
                    self._buffer[self._pointer] -= 1
                else:
                    self._buffer[self._pointer] = 255
            if c == '>':
                if len(self._buffer) <= 2 ** 16:
                    self._buffer.append(0)
                    self._pointer += 1
                else:
                    self._pointer = 0
            if c == '<':
                if self._pointer == 0:
                    self._pointer = len(self._buffer) - 1
                else:
                    self._pointer -= 1
            if c == '[':
                if self._buffer[self._pointer] == 0:
                    for s, e in self._loop_map:
                        if s == i:
                            i = e
                            break
            if c == ']':
                if self._buffer[self._pointer] != 0:
                    for s, e in self._loop_map:
                        if e == i:
                            i = s
                            break
            if c == '.':
                sys.stdout.write(chr(self._buffer[self._pointer]))
            if c == ',':
                user_input = input("Enter Value: ")
                if len(user_input) == 1:
                    self._buffer[self._pointer] = ord(user_input)
                else:
                    raise Exception("[INPUT ERROR] Only one byte is allowed: {}".format(user_input))
            i += 1


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--mode', action='store', default='run', type='string', dest='mode', help='Run Hello world')
    (options, args) = parser.parse_args()

    if options.mode == 'test':
        interpreter = Brainfuck(code='+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.')
        interpreter.evaluate()
    else:
        interpreter = Brainfuck()
        interpreter.evaluate()
