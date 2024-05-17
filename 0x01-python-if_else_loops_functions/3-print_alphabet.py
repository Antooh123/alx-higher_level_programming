#!/usr/bin/python3
for i in range(ord('a'), ord("z")+1):
    if chr(i) not in ['q', 'e']:
<<<<<<< HEAD
        print("{0}" .format(chr(i)), end='')!= 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
=======
        print("{0}" .format(chr(i)), end='')
>>>>>>> 36a3c72003a9a6ab3dc666f6890350cabc013183
