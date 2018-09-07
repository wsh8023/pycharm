import sys
def function():
    print('继续请按C！退出请按Q')
    inorout = input()
    if inorout == 'C' or inorout == 'c':
        symmetricsString()
    elif inorout == 'Q' or inorout == 'q':
        sys.exit()
def symmetricsString():
    input_str = input('请输入一个字符串：')

    tangentPoint = len(input_str) // 2

    left = input_str[:tangentPoint]
    if tangentPoint % 2 == 0:
        right = input_str[:tangentPoint:-1]
    else:
        right = input_str[:tangentPoint-1:-1]

    if left == right:
        print('你输入的是对成字符串！')
        function()
    else:
        print('No')
        function()

symmetricsString()    