def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
def f3(a, b, c=3, *d):
    int(c)
    print('a=',a,'b=',b,'c=',c,'d=',d)
def f4(a, b, c=None, *d):
    if c is None:
        c=[1,2,3]
    print('a=',a,'b=',b,'c=',c,'d=',d)
def f5(*a,**b):
    print('a=',a,'b=',b)
