with open ("demo.py",'r') as fl:
    with open("demo_new.py",'w') as f:
        s = 0
        for line in fl:
            s += 1
            line = line.rstrip('\n')
            f.write(line)
            f.write('#{}'.format(s).rjust(80-len(line)))
            f.write('\n')