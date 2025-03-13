 
def card_del(card_list)
    email = input('삭제할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(card_list)):
      if card_list[index][3] == email:
        check = 1
        print('삭제 >>> ', card_list.pop(index))
        break
    if check == 0:
      print('데이터가 없습니다.')
 
    return card_list
