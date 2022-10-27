import sys, os

prev = sys.stdout
f = open('zen.txt', 'w')
sys.stdout = f
import this
f.close()

sys.stdout = prev
print('Done')

with open("zen.txt") as file:
    while True:
        try:
            print(next(file), end='')
        except StopIteration:
            print('End of file')
            break

