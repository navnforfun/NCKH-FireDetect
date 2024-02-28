def infinite_sequence():
    num = 0
    while True:
        print(num)
        yield num
        num += 1
# for i in infinite_sequence():
#     print('----')
gen = infinite_sequence()
next(gen)
next(gen)
next(gen)