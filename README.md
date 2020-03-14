# Brainfuck_Interpreter

A simple Python Interpreter for the [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) Esoteric Language.

## Requirements

Download and Install [Python](https://www.python.org).
Tested for Python 2.7.X and Python 3.8.0

## Instructions

Usage:

    **Windows**:

        - For Testing Hello_World:
        
	        python brainfuck.py --m=test

        - For passing a file:
           
	     python brainfuck.py filename

	- Importing the class:

		from brainfuck import Brainfuck
		interpreter = Brainfuck(code='+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.')
		interpreter.evaluate()
		
		or 
		
		from brainfuck import Brainfuck
		interpreter = Brainfuck(code='')
		with open(filename, 'r') as f:
			code = f.read()
		interpreter._code = code
		interpreter.evaluate()

        ! Filename must always be *.bf

    **Linux**:

        Execute Command:
                
		chmod +x brainfuck.py

        - For Testing Hello_World:
                
		./brainfuck.py --m=test

        - For passing a file:
                
		./brainfuck.py filename

	- Importing the class:
		
		from brainfuck import Brainfuck
		interpreter = Brainfuck(code='+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.')
		interpreter.evaluate()
		
		or
		
		from brainfuck import Brainfuck
		interpreter = Brainfuck(code='')
		with open(filename, 'r') as f:
			code = f.read()
		interpreter._code = code
		interpreter.evaluate()
	
	! Filename must always be *.bf
