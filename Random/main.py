#Luke Murdock, Random Tests
import datetime as dt
print(dt.datetime.now())


def y(x):
    return x+x
def funcmanipulate(func=lambda x: x+x, v=0):
    func(v)
funcmanipulate(5)

print(y(2))