def read_all():
    file = open('text.txt')
    all_lines = file.read()
    print(all_lines)
    file.close()
    
def list_file():
    file = open('text.txt')
    num_list = file.readlines()
    print(num_list)
    num = (num_list[0])
    print("The first line says:", num)
    file.close()
    
def read_linebyline():
    file = open('text.txt')
    for lines in open('text.txt'):
        line = file.readline()
        print(line)
    file.close()
        
read_all()
list_file()
read_linebyline()
