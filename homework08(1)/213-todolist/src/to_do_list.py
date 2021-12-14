"""write your code in following methods"""
file_path = './tasks.txt'

def writetotext(todo_list):
    with open(file_path, 'a+') as f:
        for i in todo_list:
            f.write(i+'\n')


def processinput(origin_cnd):
    if len(origin_cnd) > 10:
        key = origin_cnd[6]
        item = origin_cnd[9:].split('"')
        if ' ' in item:
            while ' ' in item:
                item.remove(' ')
        if '' in item:
            while '' in item:
                item.remove('')
        return key, item
    else:
        key = origin_cnd[6:]
        return key,[]


def add(item,todo_list):
    for i in item:
        temp = "todo:" + i
        todo_list.append(temp)


def delete(item,todo_list):
    for i in item:
        temp = "todo:" + i
        if temp in todo_list:
            todo_list.remove(temp)


def complete(item,todo_list):
    for i in item:
        temp = "todo:" + i
        for j in range(len(todo_list)):
            if todo_list[j] == temp:
                todo_list[j] = "completed:" + i


def status(item,todo_list):
    for i in todo_list:
        if i[0:4] == str(item):
            print(i, end='')
        else:
            if i[0:9] == str(item):
                print(i)


def all(todo_list):
    for i in todo_list:
        print(i)


def to_do():
    with open(file_path,'a+') as f:
        todo_list = f.readlines
        cnd = input()
        key, staff = processinput(cnd)
        while key != 'quit':
            if key == 'a':
                add(list(staff),list(todo_list))
            if key == 'd':
                delete(staff,list(todo_list))
            if key == 'c':
                complete(staff,list(todo_list))
            if key == 'f':
                status(staff,list(todo_list))
            if key == 'all':
                all(list(todo_list))

            cnd = input()
            staff.clear()
            key, staff = processinput(cnd)
        writetotext(list(todo_list))
    return
