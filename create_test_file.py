instr_file = 'TYAH16.txt'
test_file = open('test_file.txt',"w+")
test_file2 = open('test_file2.txt',"w+")
with open(instr_file) as f:
        counter = 0
        lines = f.readlines()
        for i in lines:
            counter += 1
            if counter == 1:
                test_file.write(i)
                test_file2.write(i)
            elif counter <=5001:
                test_file.write(i)
            elif counter <=10001:
                test_file.write(i)
                test_file2.write(i)
            elif counter <=15001:
                test_file2.write(i)
test_file.close()

# with open('test_file.txt') as f:
#     lines = f.readlines()
#     for i in lines:
#         print(i)



