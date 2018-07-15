# sys_in = list(map(int, input().split()))
# n, k = sys_in[0], sys_in[1]
n, k = 10, 3


def check_number(num, flag):
    if num % flag == 0:
        return 0
    elif num % 10 == flag:
        return 0
    else:
        return 1


count = 0
user_id = [index for index in range(1, n + 1, 1)]
seat = [index for index in range(1, n + 1, 1)]

while len(user_id) > 1:
    print(user_id)
    print(seat)

    seat_len = len(seat)
    count += seat_len
    # index = []
    for n in range(seat_len, 0, -1):
        if check_number(seat[n], k) == 0:
            # index.append(n)
            del user_id[n]
            del seat[n]

    # print(count)
    length = len(seat)
    seat = [index for index in range(count + 1, count + length + 1, 1)]


print(user_id[0])




sys_in = list(map(int, input().split()))
n, k = sys_in[0], sys_in[1]
# n, k = 5, 2


def check_number(num, flag):
    if (num % flag == 0) or (num % 10 == flag):
        return 0
    return 1


count = 0
user_id = [index for index in range(1, n + 1, 1)]
seat = [index for index in range(1, n + 1, 1)]

while len(user_id) > 1:
    # print(user_id)
    # print(seat)
    count += len(seat)
    for n in seat:
        if check_number(n, k) == 0:
            user_id.remove(user_id[seat.index(n)])
            seat.remove(n)
        else:
            continue

    # print(count)
    length = len(seat)
    seat = [index for index in range(count + 1, count + length + 1, 1)]


print(user_id[0])



'''
Version three
'''

sys_in = list(map(int, input().split()))
n, k = sys_in[0], sys_in[1]
# n, k = 7, 3


def check_number(num, flag):
    if num % flag == 0:
        return 0
    elif num % 10 == flag:
        return 0
    else:
        return 1


count = 0
user_id = [index for index in range(1, n + 1, 1)]
seat = [index for index in range(1, n + 1, 1)]

while len(user_id) > 1:
    # print(user_id)
    # print(seat)

    seat_len = len(seat)
    count += seat_len

    user_temp = []
    seat_temp = []
    for n in range(0, seat_len, 1):
        if check_number(seat[n], k) == 1:
            user_temp.append(user_id[n])
            seat_temp.append(seat[n])

    user_id = user_temp[:]
    seat = seat_temp[:]

    length = len(seat)
    seat = [index for index in range(count + 1, count + length + 1, 1)]


print(user_id[0])
