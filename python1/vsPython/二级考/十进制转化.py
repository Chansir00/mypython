while 1:
    num = int(input('请输入数字：'))
    
    print('十进制转十六进制:','%d'%num,'--','%x'%num)
    print('十进制转八进制：','%d'%num,'--','%o'%num)
    print('十进制转二进制','%d'%num,'--',bin(num))
