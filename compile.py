#!/usr/bin/env python3

import csv
import sys
import tempfile
import re

JUMP_RULE = 'OOOOOOXXXXXXXXXX'
ALU_LEFT_RULE = 'OOOOXXXX0000YYYY'
ALU_RIGHT_RULE = 'OOOO0000XXXXYYYY'
ALU_BOTH_RULE = 'OOOOXXXXYYYYZZZZ'
IMM_RULE = 'OOOOXXXXXXXXYYYY'
NOOP_RULE = 'OOOOOO0000000000'
PORT_READ_RULE = 'OOOOOOXX0000YYYY'
PORT_WRITE_RULE = 'OOOOOOXXYYYYZZZZ'

registers = {   'zero':'0000',
                'R1': '0001',
                'R2': '0010',
                'R3': '0011',
                'R4': '0100',
                'R5': '0101',
                'R6': '0110',
                'R7': '0111',
                'R8': '1000',
                'R9': '1001',
                'R10': '1010',
                'R11': '1011',
                'R12': '1100',
                'R13': '1101',
                'R14': '1110',
                'R15': '1111'
                }

rules = {       'noop': NOOP_RULE,
                'jump': JUMP_RULE,
                'jz': JUMP_RULE,
                'jnz': JUMP_RULE,
                'limm': IMM_RULE,
                'jal': JUMP_RULE,
                'ret': NOOP_RULE,
                'read': PORT_READ_RULE,
                'write': PORT_WRITE_RULE,
                'mov': ALU_LEFT_RULE,
                'not': ALU_LEFT_RULE,
                'add': ALU_BOTH_RULE,
                'sub': ALU_BOTH_RULE,
                'and': ALU_BOTH_RULE,
                'or': ALU_BOTH_RULE,
                'neg': ALU_LEFT_RULE
                }

opcodeDict = {  'noop':'000000',
                'jump':"000001",
                'jz':'000010',
                'jnz':'000011',
                'limm':'0001',
                'jal':'001000',
                'ret':'001001',
                'read':'001010',
                'write':'001011',
                'mov':'1000',
                'not':'1001',
                'add':'1010',
                'sub':'1011',
                'and':'1100',
                'or':'1101',
                'neg':'1110'
                }

directions = {}

def isRegister(operand):
    return registers[operand]

def isImm(operand):
    
    if int(operand) > 128:
        raise Exception(f'Operand too large. Must be under 8 bits')

    operand = format(int(operand), '08b')
    return operand 

def isOther(operand):
    if operand in directions:
        return directions[operand]
    else:
        raise Exception(f'Operand not recognized')
    

def opType(operand):
    regexps = [r'(?:R(?:1[0-5]|[1-9])|zero)', r'[0-9]+', r'[:a-zA-Z0-9]']
    functions = [isRegister, isImm, isOther]
    index = -1
    for regex in regexps:
        index += 1
        if re.match(regex, operand):
            return functions[index](operand) 

    raise Exception(f'operand ', operand, f' is not valid')

def operateFile(file, func):
    result = func(file)
    file.seek(0)
    return result

def translate(file):
    #Transform assembly instructions into machine code.
        
    result = []
    for line in file:
        operation = ''
        opcode = ''

        line = line.strip('\n')
        items = line.split(' ')
        items = list(filter(None, items))

        if items[0] in opcodeDict:
            operation = rules[items[0]]
            opcode = opcodeDict[items[0]]
            operation = re.sub(r'O+', opcode, operation)

            items.remove(items[0])

            s = 'X'
            for item in items:
                operand = opType(item)
                operation = re.sub(s+'+', operand, operation)
                s = chr((ord(s) + 1))

            result.append(str(operation))
        elif items[0][0] == ':':
            continue
        else:
            raise Exception(f'ERROR: {line[0]} in not a valid opcode')
    return result
        
def resolveDirections(file):
    
    instructionDir = 0
    for line in file:
        line = line.strip('\n')
        match = re.search(r'^:([a-zA-Z0-9]*)', line)
        if match:
            directions[match.group(1)] = format(instructionDir, '010b')
        else:
            instructionDir += 1
    

def read_file(path):
    file = tempfile.TemporaryFile()
    strip_input(file, path)
    return read_mem_file(file)


def strip_input(out_file, csvFile):
    #with open(path, 'r') as csvFile:
    lines = csvFile.read().splitlines()
    for line in lines:
        if re.match(r'^#', line): #If line is a comment ignore it
            continue
        elif re.search(r'#', line): #Strip comment ater instruction
            index = re.search(r'#', line).start()
            out_file.write(line[0:index]+'\n')
        else: #Add instruction to virtual file
            out_file.write(line+'\n')
    #Make file ready to be read again
    out_file.seek(0)


def read_mem_file( input_file ):
    #assembly_code will contain the lines of assembly code to translate
    with open(input_file, 'r') as infile:
        return_code = []
        assembly_code = csv.DictReader(infile, delimiter = ' ',
                                       fieldnames = ["opcode", "op1", "op2"],
                                       restval = None,
                                       quoting = csv.QUOTE_NONE)
        for instruction in assembly_code:
            opc, op1, op2 = instruction["opcode"], instruction["op1"], instruction["op2"]
            return_code.append({"opcode":opc, "op1":op1, "op2":op2})
    return return_code

#def strip_comments():


def main(argv):
    #Create virtual file
    virtual_file = tempfile.SpooledTemporaryFile(mode = "w+", encoding = "utf-8", dir = "/tmp/")

    #Open input file
    input_file = open( "test_strip.csv", 'r' )

    #Strip file
    strip_input(virtual_file, input_file)

    operateFile(virtual_file, resolveDirections)
    instructions = operateFile(virtual_file, translate)
    input_file.close()


    with open('a.out', 'w') as file:
        for instruction in instructions:
            file.write(f'{instruction}\n')

    



if __name__ == "__main__":
    main(sys.argv)
