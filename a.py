#사용자로부터 정수형 변수 몸무게와 키를 입력받기
#입력 받는 과정에서 표시되는 메시지는 개발자가 임의로 정의할 수 있음
#몸무게 변수의 이름: myWeight, 키 변수의 이름: myHeight
#몸무게 변수는 kg단위로 입력받고, 키 변수는 m 단위로 입력받아야 함
#--> 키의 경우 m단위로 입력하려면 실수타입이어야 하므로 float 함수로 변환해야 함
myHeight=float(input("키를 m단위로 입력하세요 (예 175cm -> 1.75)"))
myWeight=int(input("몸무게를 kg단위로 입력하세요 (예 85"))

#입력받은 값을 출력하여 확인
print(myHeight)
print(myWeight)

#BMI산출 식을 적용하여 자신의 BMI수치를 출력
BMI=myWeight//myHeight**2
print(BMI)