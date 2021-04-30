
directions = {}

# O -> opcode
# 0 -> empty
# X -> opcode
# Z -> opcode
# Y -> opcode
JUMP_RULE = 'OOOOOOXXXXXXXXXX'

ALU_LEFT_RULE = 'OOOOXXXX0000YYYY'
ALU_RIGHT_RULE = 'OOOO0000XXXXYYYY'
ALU_BOTH_RULE = 'OOOOXXXXYYYYZZZZ'

IMM_RULE = 'OOOOXXXXXXXXYYYY'

NOOP_RULE = 'OOOOOO0000000000'

WORD_WRITE_RULE = 'OOOOYYYYXXXXXXXX'
WORD_READ_RULE = 'OOOOXXXXXXXXYYYY'

ADDR_WRITE_RULE = 'OOOOYYYYXXXX0000'
ADDR_READ_RULE = 'OOOO0000XXXXYYYY'

prep_rules = {
                                }

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
                'li': IMM_RULE,
                'lw': WORD_READ_RULE,
                'sw': WORD_WRITE_RULE,
                'la': ADDR_READ_RULE,
                'sa': ADDR_WRITE_RULE,
                'call': JUMP_RULE,
                'ret': NOOP_RULE,
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
                'li':'0001',
                'call':'010000',
                'ret':'010100',
                'lw':'0010',
                'sw':'0011',
                'la':'0110',
                'sa':'0111',
                'mov':'1000',
                'not':'1001',
                'add':'1010',
                'sub':'1011',
                'and':'1100',
                'or':'1101',
                'neg':'1110'
                }
