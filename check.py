no = '2'
# nec()
# with open(r"home/vimal/Documents/task/fellowship-python/python/task.txt", "r+") as f:
#     lines = f.readlines()
#     f.seek(0)
lines="2 vimal \n 1 vimkl"
for i in lines:
    line=i.strip('\n')
    l_tmp=line.split('_')
    print(l_tmp)
    # if l_tmp[0]!=no:
        # f.write(i)
        # print(line)