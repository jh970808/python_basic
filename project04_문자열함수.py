# 이메일 주소 입력 입력시 ***@**.**
# 입력 받아서 아이디 출력
# 1 input을 활용하여 이메일 적게 유도
# input("이메일을 입력하세요 >> ")
# a = 인풋으로 받은 값
# a에서 아이디 부분을 알 수 있는 @의 위치를 index, find로 찾는다
# a.find("@") 값의 왼쪽부분까지 프린트(어떻게?)
# 또는 split을 사용하여 아이디 부분과 홈페이지 부분을 나눈다.
# a.split("@")를 한다면 값이 [아이디 부분, 홈페이지 부분]으로 나올 것이다.
# print(a.split("@")의 아이디 부분(첫번째 부분))을 가져온다
# split을 통해 나눈 앞부분을 어떻게 가져올까

# a = input("이메일을 입력하시오 >>")
# print(a.split("@")[0])

# 이메일 주소는 최소 5글자 이상이어야 한다.
# 최대 20글자까지 가능
# 반드시 글자 중간에 @가 포함되어야 한다.
# input()을 이용하여 입력을 받는다.
# 받은 값은 email 이름의 변수에 저장
#  email에 저장되어 있는 값에서 index를 이용하여 @를 위치를 확인
# 찾은 위치값은 index라는 이름으로 저장한다.
# print를 이용해서 email의 값에서 처음부터 index의 저장되어 있는 값까지 슬라이싱 한다.
# 슬라이싱 한 값을 data 변수에 저장
# data변수에 있는 값을 print 함수를 이용해서 출력한다.

# email = input("이메일 주소를 입력하시오 >>")
# print('값은 5~20',len(email))
# print('값은 1이 나와야 된다',email.count("@"))
# index = email.index("@")
# data = email[:index]
# print(data)


# 주민등록번호를 입력받아서 다음을 출력
# 성별을 출력 
# 생년월일(00년 0월 0일생)
# 뒷자리 숫자의 첫글자는 그대로 나머지는 *로 변경
# 입력시 글자 앞, 뒤로 공백이 포함될 수 있습니다.(공백에 대한 처리)
# 자릿수 및 성별 코드 오류값 없도록록

# 주현 주민등록번호
=input("주민등록번호 13자리를 입력해주세요. (-포함하여 주세요)")
raw_id = input.strip()
# yymmdd = raw_id.split("-", [0])
# sex_num = raw_id.split("-", [1])
# modify_sex_num = sex_num[0]+"*"*6
# yy = yymmdd[:2]
# mm = yymmdd[2:4]
# dd = yymmdd[4:6]
# sex_num_cal = int(sex_num[0])%2
# sex_value = str(sex_num_cal)
# sex = sex_value.replace("0", "여자")
# sex = sex_value.replace("1", "남자")
# print(yy,"년", mm,"월", dd,"일", yymmdd + "-" + modify_sex_num )