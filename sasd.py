# 도서관 = [{도서명, 저자, 수량, 빌려간 수},{},{}] # 디스플레이_대출
# 디스플레이_반납
# 디스플레이_검색

display = '''
--------------------------------------------------------------
1. 추가 2. 검색 3. 대출 4. 반납 5. 목록, 6.종료
--------------------------------------------------------------
메뉴 번호를 선택해주세요 >>> '''

# 빈 리스트 선언 (도서 목록)
books = [{"title": "소유냐 존재냐", "author": "에리히 프롬", "quantity": 12, "borrowed" : 1},
         {"title": "천사와 악마", "author": "댄 브라운", "quantity": 43, "borrowed": 4}]

print(" 도서관 관리 시스템")
print("명령어: 추가, 검색, 대출, 반납, 목록, 종료")

while True:
    menu = input(display).strip()

    # 1. 도서 추가
    if menu == '1':
        print("\n")
        
        title = input(" 책 제목: ").strip()
        author = input(" 저자: ").strip()
        quantity = int(input(" 수량: ").strip())
        # borrowed = 초기값 = 0이라 안넣어도 될려나?x / 아니면 키값 정의해주고 밸류 =0 해줘야하나?
                
        found = False  # 우선적으로 책 검색 # false값 설정의 이유유
        for book in books:
            if book["title"] == title:
                book["quantity"] += quantity
                print(f" '{title}'의 수량이 {quantity}권 추가되었습니다. (총 {book['quantity']}권)")
                found = True
                break

        if not found:
            books.append({"title": title, "author": author, "quantity": quantity, "borrowed": 0})
            print(f" 새로운 도서 '{title}'이(가) 추가되었습니다. ({quantity}권)")

    # 2. 도서 검색
    elif menu == '2':
        keyword = input(" 검색어 (제목 또는 저자): ").strip()
        results = [b for b in books if keyword in b["title"] or keyword in b["author"]] #b["title"]

        if results:
            print("검색 결과:")
            for book in results:
                available = book["quantity"] - book["borrowed"]
                print(f" 제목: {book['title']}, 저자: {book['author']}, 남은 수량: {available}")
        else:
            print(" 검색 결과가 없습니다.")

    # 3. 도서 대출
    elif menu == '3':
        title = input(" 대출할 책 제목: ").strip()
        for book in books:
            if book["title"] == title:
                available = book["quantity"] - book["borrowed"]
                if available > 0:
                    book["borrowed"] += 1
                    print(f" '{title}'을(를) 대출했습니다. 남은 수량: {available - 1}")
                else:
                    print(f" '{title}'은(는) 현재 모두 대출 중입니다.")
                break
        else:
            print(" 해당 도서는 도서관에 없습니다.")

    # 4. 도서 반납
    elif menu == "4":
        title = input(" 반납할 책 제목: ").strip()
        for book in books:
            if book["title"] == title and book["borrowed"] > 0:
                book["borrowed"] -= 1
                print(f" '{title}'을(를) 반납했습니다. 현재 남은 대출 가능 수량: {book['quantity'] - book['borrowed']}")
                break
        else:
            print(" 반납할 수 없는 도서입니다.")

    # 5. 전체 도서 목록 출력
    elif menu == "5": 
        print("\n")
        if books:
            
            print("현재 도서 목록")
            print("-"*30)
            for book in books:
                available = book["quantity"] - book["borrowed"]
        
                print(f" 제목: {book['title']}")
                print(f" 저자: {book['author']}") 
                print(f" 수량: {available}")
                print("-"*30)
        else:
            print(" 도서관에 책이 없습니다.")

    # 6. 종료
    elif menu == "6":
        print(" 도서관 시스템을 종료합니다.")
        break

    # 7. 잘못된 명령어 처리
    else:
        print(" 올바른 명령어를 입력하세요. (추가, 검색, 대출, 반납, 목록, 종료)")
