import string

def day16():
    def swappos(l, a, b):
        temp = (l[a],l[b])
        l.pop(a)
        l.insert(a, temp[1])
        l.pop(b)
        l.insert(b, temp[0])
        return l


    def swapval(l, a, b):



    def apply(l, func):
        switch = {
            's': lambda x: l[len(l)-int(func[1:]):] + l[:len(l)-int(func[1:])],
            'x': lambda x: swappos(l, int(func[1:].split('/')[0]), int(func[1:].split('/')[1]))
        }
        return switch.get(func[0])(l)

    f = open('day16input.txt')
    data = f.readline().split(',')
    f.close()

    #TESTING
    data = ['s1','x3/4','pe/b']
    line = list(string.ascii_lowercase[:5])
    for d in data:
        print line
        line = apply(line, d)

day16()