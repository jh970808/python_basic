# 주석
# 과일을 받아서 박스에 담고 싶다.
# 박스에 담겨지는 과일의 갯수는 과일마다 다르다.
# 과일의 갯수를 받고, 박스에 몇개 담겨지는지도 입력을 받고
# 박스에 담아서 몇박스 몇개인지 알려주는 프로그램을 작성
# 변수가 필요 : 과일의 갯수, 박스당 몇개 담겨지는지
# 데이터가 변동 > 입력을 받아야함 = input
# 값 데이터 타입 = 문자 > 우리는 숫자가 필요 > 변환 = int or float
# 결과값 출력 = print 

count = input('과일의 갯수를 입력하시오 >>>', )
count = int(count)
print(type(count))
print('입력받은 값의 데이터 타입은 >', type(count))
box_count = int(input('박스당 몇개 담을 것인가 >>'))
print(type(box_count))
print(count//box_count,"박스",count % box_count, "개")