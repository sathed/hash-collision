#!/usr/bin/python3
# from binascii import crc32
import crc16

val = input('Enter a value to hash: ')

if not val or val == '':
    val = 'supersecretpassword'

hashed = crc16.crc16xmodem(str.encode(val))

print(f'''
Attempting to locate a hash collision for the string: {val}
''')

input("Press any key to continue...")

i = 0

while (True):
    match = crc16.crc16xmodem(b'%s' % str(i).encode())
    if (match == hashed):
        print('''
============ Match Found =============
''')
        print('input(%s) -> %s' % (i, match))
        print(f'input({val}) -> %s' % hashed)
        exit()
    else:
        print('%s - No match (%s)' % (str(i), match))
        i += 1
