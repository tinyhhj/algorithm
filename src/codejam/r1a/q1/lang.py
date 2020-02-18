# type
# scalar type int, float , None , bool
def showType(t):
    print(t,type(t))

showType(-1)
showType(123)
showType(123.123)
showType('str')
showType("str")
showType([1,2,3,"str"])
showType((1,2,3,"str"))
showType({"k":"v"})
showType(True)

# input
# all input is string
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)
_ = input()
showType(_)

# immutable
# int , float, string, tuple
a = 1
b = a
b += 3
showType(a)
showType(b)

a = 123.123
b = a
b += 321.321
showType(a)
showType(b)

a = 'str'
b = a
b += 'str'
showType(a)
showType(b)

a = (1,2,3)
b = a
b += (4,)
showType(a)
showType(b)

# mutable
# list, dict, set
a = [1,2,3]
b = a
b.append(4)
showType(a)
showType(b)

a = {1:1,2:2}
b = a
b.setdefault(3,3)
showType(a)
showType(b)

a = {1,2,3}
b = a
b.add(4)
showType(a)
showType(b)

# dict
a = {1:1,123.123:2}
showType(a)

# set
a = {1,2,3}
showType(a)

# list
a = [1,2,3]
a.append(4)
showType(a)

