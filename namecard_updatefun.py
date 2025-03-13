

def card_update(card_list):
    
    email = input('수정할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(card_list)):
      if card_list[index][3] == email:
        check = 1
        while True:
          item = input('수정할 항목을 선택하세요(1.이름, 2.전화번호, 3.주소,  4.종료)')
          if item == '4':
            break
          item = int(item)
          if item in (1,2,3):         
            card_list[index][item-1] = input('수정할 값을 입력 >>> ')

    if check == 0:
      print('데이터가 없습니다.')    

    return card_list    