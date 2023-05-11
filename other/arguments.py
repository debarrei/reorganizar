m = [9, 15, 24]

def modify(k):
    print("m = ", m)
    print("k = ", k)
    k.append(39)
    print("m = ", m)
    print("k = ", k)

modify(m)

f = [14, 23, 37]

def replace(g):
    print("g = ", g)
    print("f = ", f)
    g = [17, 28, 45]
    print("g = ", g)
    print("f = ", f)


replace(f)

def replace_contents(g):
    print("g = ", g)
    print("f = ", f)
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g = ", g)
    print("f = ", f)

f = [14, 23, 37]
replace_contents(f)