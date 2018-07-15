'''
Version one
'''
length = int(sys.stdin.readline())
array_input = sys.stdin.readline()
array_input = [int(n) for n in array_input.split()]
array_input = sorted(array_input)

result = array_input[1] - array_input[0]
for index in range(1, len(array_input) - 1, 1):
    temp = array_input[index + 1] - array_input[index]
    if temp < result:
        result = temp

sys.stdout.write(result)


'''
Version two
'''
length = int(input())
array_input = list(map(int, input().split(' ')))

array_input = sorted(array_input)

result = array_input[1] - array_input[0]
for index in range(1, len(array_input) - 1, 1):
    temp = array_input[index + 1] - array_input[index]
    if temp < result:
        result = temp

print(result)
