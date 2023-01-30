def label(func):
    def wrapper(name):
        print(name, end = ' : ')
        func(name)
    return wrapper

def label2(func):
    def wrapper(name):
        print('자기소개 끝!')
    return wrapper



@label
def prof(name):
    # name : 반갑네 {name} 교수라네
    print(f'반갑네 {name} 교수라네.')
    print('과제 했나?')

@label
@label2
def student(name):
    print(f'안녕하세요, {name} 입니다')



prof_name = 'vik'
print(label(prof)(prof_name))
print(prof(prof_name))
# prof(prof_name)

stu_name = '이소정'
print(label(student)(stu_name))
# label(stu_name, student)
# prof(stu_name)

