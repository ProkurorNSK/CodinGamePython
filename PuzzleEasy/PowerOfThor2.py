a, b, x, y = [int(i) for i in input().split()]
c = ["S", "", "N"]
d = ["E", "", "W"]
while 1:e = 1 if (a < x)else-1 if (x < a)else 0;f = 1 if (b < y)else-1 if (y < b)else 0;x -= e;y -= f;print(c[f + 1] + d[e + 1])