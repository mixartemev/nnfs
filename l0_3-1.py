import numpy as np


def act(x):
    return 0 if x < 0.5 else 1


def go(h, r, a):
    x = np.array([h, r, a])
    w1 = [0.45, -0.5, 0.55]

    out = np.dot(w1, x)  # scalar vector product
    print("3 input neurons sum: "+str(out))

    y = act(out)
    print("result: "+str(y))

    return y


house = 0
rock = 0
attr = 1

res = go(house, rock, attr)

if res == 1:
    print("Come in tiger")
elif res == 0:
    print("Get out from here looser")
