instr_file = 'TYAH16.txt'
test_file = open('test_file.txt',"w+")
with open(instr_file) as f:
        counter = 0
        lines = f.readlines()
        for i in lines:
            counter += 1
            test_file.write(i)
            if counter >100:
                break
test_file.close()

with open('test_file.txt') as f:
    lines = f.readlines()
    for i in lines:
        print(i)



