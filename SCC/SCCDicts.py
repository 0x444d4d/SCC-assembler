
directions = {}

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
