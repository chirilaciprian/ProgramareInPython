def merge_files(files_list,order):
    data = []
    for i in files_list:
        file = open(i,'r')
        data.append(file.read())
    result = open('result.txt','w')
    for i in order:
        result.write(data[i])
    print("Files merged into result.txt")
            
            