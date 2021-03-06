import csv
import re

from SCCDicts import *

def writeList2File(fileName, list, append=0):
    mode = ('w', 'a')[append]
    with open(fileName, mode) as file:
        for item in list:
            print(item)
            file.write(f'{item}\n')

def isRegister(operand):
    return registers[operand]

def isImm(operand):
    
    if int(operand) > 128:
        raise Exception(f'Operand too large. Must be under 8 bits. Received {operand}')

    operand = format(int(operand), '08b')
    return operand 

def isOther(operand):
    if operand in directions:
        return directions[operand]
    else:
        raise Exception(f'Operand not recognized. Received {operand}')

def opType(operand):
    regexps = [r'(?:R(?:1[0-5]|[1-9])|zero)', r'[0-9]+', r'[:a-zA-Z0-9]']
    functions = [isRegister, isImm, isOther] # This is a function list
    index = -1
    for regex in regexps:
        index += 1
        if re.match(regex, operand):
            # Now a function is applied to the item to turn it into binary code
            return functions[index](operand)

    raise Exception(f'Operand {operand} is not valid')

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
