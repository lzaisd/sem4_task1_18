def read_from_file(file):
    data = []
    with open(file) as f:
        line = f.readline()
        data.extend([int(x) for x in line.split()])
    return data


def write_to_file(data, file):
    f = open(file, 'w')
    for k in range(len(data)):
        f.write(str(data[k]) + " ")


def get_sum(data):
    summa = 0
    for elem in data:
        summa += elem
    return summa


def check(data1, data2):
    return len(data1) < len(data2) or (len(data1) == len(data2) and get_sum(data1) < get_sum(data2))


arr = read_from_file('input.txt')

answer = []
temp = [arr[0]]

for i in range(1, len(arr)):
    if len(temp) == 0:
        temp.append(arr[i - 1])
    if arr[i] < arr[i - 1]:
        if check(answer, temp):
            answer = temp.copy()
            temp.clear()
        else:
            temp.clear()
    else:
        temp.append(arr[i])
        if i == len(arr) - 1 and check(answer, temp):
            answer = temp.copy()

write_to_file(answer, 'output.txt')
