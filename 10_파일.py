#f = open("새파일.txt", "a")
#result  = f.write("문서에 저장되는 내용\n")
#print(result)
#print(len("문서에 저장되는 내용"))
#f.close()

f = open('새파일.txt')

# for line in f.readlines(): #[리스트 > ' ',' ', ...]  
   # print(line)

#print(f.readline())
#while True:
#    line = f.readline()
#   print(line)
#    if not line: 
#        break

print(f.read())

f.close