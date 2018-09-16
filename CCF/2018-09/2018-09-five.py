# -*- coding:utf-8 -*-


orl_input = list(map(int, input().split(' ')))
m, l, r = orl_input[0], orl_input[1], orl_input[2]
k = list(map(int, input().split(' ')))

an = [1 for l in range(r+1)]

def calc_a_n(n):
    global k
    global m
    global an
    
    if n == 0:
        return 1
    else:
        temp = 0
        for index in range(0, min(m, n)):
            temp += k[index] * an[n-index-1]
        return temp % 998244353

for index in range(len(an)):
    an[index] = calc_a_n(index)

an = an[l:]
for index in an:
    print(index)



"""
case one:
3 3 6
2 0 4

12
32
80
208
"""

"""
case two:
2 1 11
1 1

1
2
3
5
8
13
21
34
55
89
144
"""

"""
case three:
10 10 20
532737790 634932889 335818534 101179174 977780682 695192541 779962395 295668292 157661238 325351676

119744921
651421717
601080475
163399777
291546699
108479226
406175654
344671679
459752012
489415425
349454810
"""
