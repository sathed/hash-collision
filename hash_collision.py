#!/usr/bin/python3
# from binascii import crc32
import crc16
import zlib

val = input('Enter a value to hash: ')
type = int(input('Use CRC16 or CRC32 (16 or 32): '))

if type != 16 and type != 32:
    print('Invalid value. Must use enter either 16 or 32.')
    exit(1)
elif type == 32:
    print("*** WARNING: This may consume a LOT of system resources before a match is found! ***")
    input("Press any key to continue. Ctrl + C to exit.")

if not val or val == '':
    val = 'supersecretpassword'

hashed16 = crc16.crc16xmodem(str.encode(val))
hashed32 = zlib.crc32(b'%s' % val.encode())

print(f'''
Attempting to locate a hash collision for the string: {val}

crc16 - {hashed16}
crc32 - {hashed32}
''')

input("Press any key to continue...")

i = 0

if type == 16:
    while (True):
        match = crc16.crc16xmodem(b'%s' % str(i).encode())
        if (match == hashed16):
            print('''
    ============ Match Found =============
    ''')
            print('input(%s) -> %s' % (i, match))
            print(f'input({val}) -> %s' % hashed16)
            exit()
        else:
            print('%s - No match (%s)' % (str(i), match))
            i += 1
elif type == 32:
    while (True):
        match = zlib.crc32(b'%s' % str(i).encode())
        if (match == hashed32):
            print('''
    ============ Match Found =============
    ''')
            print('input(%s) -> %s' % (i, match))
            print(f'input({val}) -> %s' % hashed32)
            exit()
        else:
            print('%s - No match (%s)' % (str(i), match))
            i += 1
