"""write your code in following methods"""
file_path = './tasks.txt'

todo_list = []


def writetotext():
    with open(file_path, 'a+') as f:
        for i in todo_list:
            f.write(i)
    f.close()


def processinput(origin_cnd):
    if len(origin_cnd) > 10:
        key = origin_cnd[6]
        item = origin_cnd[9:].split('"')
        while ' ' in item:
            item.remove(' ')
        while '' in item:
            item.remove('')
        return key, item
    else:
        key = origin_cnd[6:]
        return key


def add(item):
    for i in item:
        temp = "todo:" + i + "\n"
        todo_list.append(temp)
    writetotext()


def delete(item):
    for i in item:
        temp = "todo:" + i + "\n"
        todo_list.remove(temp)
    writetotext()


def complete(item):
    for i in item:
        temp = "todo:" + i + "\n"
        for j in range(len(todo_list)):
            if todo_list[j] == temp:
                todo_list[j] = "completed:" + i + "\n"
    writetotext()


def status(item):
    for i in todo_list:
        if i[0:4] == str(item):
            print(i, end='')
        else:
            if i[0:9] == str(item):
                print(i, end='')


def all():
    for i in todo_list:
        print(i, end='')


def to_do():
    cnd = input()
    key, staff = processinput(cnd)
    while key != 'quit':
        if key == 'a':
            add(staff)
        if key == 'd':
            delete(staff)
        if key == 'c':
            complete(staff)
        if key == 'f':
            status(staff)
        if key == 'all':
            all()

        cnd = input()
        key, staff = processinput(cnd)
    return
# key,item = processinput('todo -a "complete homework" "do handwriting" "go shopping" "read books" "visit grandparents" "participate the interview"')
# print(key,item)
# add(item)
# all()
# complete(['go shopping'])
# status('todo')