import itertools


input_number = input()
for i in range(len(input_number)):
    for j in itertools.combinations(input_number, len(input_number)-i):
        new_number = int(''.join(j))
        if new_number%3==0:
            exit(print(i))

print(-1)
