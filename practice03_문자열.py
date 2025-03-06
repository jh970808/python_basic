text01 = "문자열"
print(text01)
text02 = '문자열'
print(text02)
text03 = "sunny's cloth"
print(text03)
text04 = '"sunny" is'
print(text04)
text05 = """첫번째 줄
두번째 줄"""
print(text05)
text06 = '첫 줄 \n두 줄'
print(text06)
print(text01 + text03)
# 문자 + 숫자 안됨!
print(text01 * 2)
# 문자 * 숫자는 문자 반복
print(len(text01))

a = "Life is too short, You need Python"
print(a[-3])
print(a[19:22])

# b = "pithon"
#  b[1] = "y"
# print(b)

data01 = "I eat %d apples %s"
print(data01 % (3,"ggg"))

num01 = 1
txt01 = "I eat {:0.2f} apples {}"
print(txt01.format(3, text03))

txt01 = "I eat {:,.2f} apples {}"
print(txt01.format(3000, text03))

name = "강주현"
age = 24
txt03 = f'나의 이름은 {name}이며 {age}살 입니다'
print(txt03)