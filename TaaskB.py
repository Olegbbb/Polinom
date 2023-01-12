from random import randint
data_first = open('first.txt', 'r', encoding = 'UTF-8')
data_second = open('second.txt', 'r', encoding = 'UTF-8')
equation1 = ' '.join(data_first.readlines())
equation2 = ' '.join(data_second.readlines())
print(equation1)
print(equation2)


 
def ReplacePolinomInDict(equation):
    equation = equation.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -').split()
    new_list = []
    for _ in equation:
        if 'x' not in _:
            new_list.append((_ + ' 0').split())
        elif _.endswith('x') : 
            if _ == 'x':
                new_list.append(['1','1'])
            elif _ == '-x': 
                new_list.append(['-1','1'])
        elif _.startswith('x'): 
            new_list.append(('1' + _).split('x**'))
        elif _.startswith('-x'): 
            new_list.append(_.replace('-', '-1').split('x**'))
        else: new_list.append(_.split('x**'))
    result_dict = {}
    for _ in new_list:
        result_dict[int(_[1])] = int(_[0])
    return result_dict


def SumDicts (dict1, dict2):
    a = [dict1,dict2]
    resultdict = {}                                            #  результирующий словарь

    for dictionary in a:                                     # пробегаем по списку словарей
        for key in dictionary:                               # пробегаем по ключам словаря
            try:
                resultdict[key] += dictionary[key]            # складываем значения
            except KeyError:                                    # если ключа еще нет - создаем
                resultdict[key] = dictionary[key]  
    return resultdict 

print(ReplacePolinomInDict(equation1))
print(ReplacePolinomInDict(equation2))
print(SumDicts(ReplacePolinomInDict(equation1),ReplacePolinomInDict(equation2)))








