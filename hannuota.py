def hannuo(n, a, b, c):
    '''
    n: 代表几个盘子
    a: 代表第一个塔
    b: 代表第二个塔
    c:  代表第三个塔
    '''
    if n == 1:
        print(a, '-->', c)
        return None
    if n == 2:
        print(a, '-->', b)
        print(a, "-->", c)
        print(b, '-->', c)
        return None
    #把n-1个盘子，从a塔借助于c他，挪到b塔上去
    hannuo(n-1,a, c, b)
    hannuo(n-1,b,a,c)

hannuo(n=4,a='A', b='B', c='C')