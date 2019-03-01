print('---------------------------file------------------------------')
def openfile(filetxtaa):
    f = open(filetxtaa)
    f_new = []
    for e_line in f:
        f_new.append(e_line.strip())
    print(f_new)

    employee = []
    boss = []
    num = 1

    for e_line in f_new:
        if e_line[:3] != '===' :
            (role,str_spoken) = e_line.split(':',1)
            if role == '吕秀才':
                employee.append(str_spoken)
            elif role == '老板娘':
                boss.append(str_spoken)
            elif role == '盗神':
                employee.append(str_spoken)
            else :
                boss.append(str_spoken)
        else:
            employee_num_txt = 'employee_' + str(num) + '.txt'
            boss_num_txt = 'boss_' + str(num) + '.txt'

            employee_file = open(employee_num_txt,'w')
            boss_file = open(boss_num_txt,'w')

            employee_file.writelines(employee)
            boss_file.writelines(boss)

            employee_file.close()
            boss_file.close()

            employee = []
            boss = []
            num += 1
    f.close()

openfile("test.txt")



