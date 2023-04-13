# string operations
def my_str():
    s = "Hey varun how are you"
    s1 = "Have lunch @ 12PM"
    task = s + " " + s1
    print(task)


# list operations
def my_list():
    names = ['Varun', 'Ram', 'Dileep']
    age = [26, 25, 35]
    names.extend(age)
    print(names)
    details = list(zip(names, age))
    print(details)
    del names[0:1]
    print(names)


def my_list1():
    fname = ['Sai kruthik reddy','ADARSH','ANIKETH REDDY','Sarat Chandra Kumar','Able','Sumanth Reddy','pavani','Surya chand','Sai Kumar Reddy','deepika reddy','Haritha','Ram Madhav','dileep kumar','Varun Kumar','Jeevan kumar']
    lname = ['Paduru', 'VULLI','KAKULAVARAM','Cheendripu','Thankachan','Vootukuri','katkuri','Jasthi','Yenumula','uppula','Peddi','Mudumby','Bathina','Nainamoina','koppineni']
    name = []

    for i in range(len(fname)):
        name.append([fname[i], lname[i]])
    print(name)
    name += [['sidharth', 'malhotra'], ['sidharth', 'shetty'], ['Abhai', 'rag']]
    name.sort()
    print(name)

    name.remove(['sidharth', 'shetty'])
    print(name)


def my_string(string):
    duplicates = []
    seen_chars = set()
    for char in string:
        if char != ' ' and char in seen_chars and char not in duplicates:
            duplicates.append(char)
        else:
            seen_chars.add(char)
    return duplicates

print(my_string("This is a program experiment for fun in python"))




# my_str()
# my_list()
# my_list1()
my_string()
