with open ("demo.py",'r') as fl:                                              #1
    with open("demo_new.py",'w') as f:                                        #2
        s = 0                                                                 #3
        for line in fl:                                                       #4
            s += 1                                                            #5
            line = line.rstrip('\n')                                          #6
            f.write(line)                                                     #7
            f.write('#{}'.format(s).rjust(80-len(line)))                      #8
            f.write('\n')                                                     #9
