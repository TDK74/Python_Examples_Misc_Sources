''' content of infile.py '''
import sys
import fileinput


with fileinput.input(files = ('sample.txt')) as f:
    for line in f:
        print(line)

with open('sample.txt', 'r') as f:
    readme = f.read()
    print(readme)

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")

# source: https://www.geeksforgeeks.org/take-input-from-stdin-in-python/
