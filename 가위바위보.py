import random

#가위바위보
choose = [ "가위" , "바위" , "보" ]
choose2 = random.choice(choose)

#낸거 확인
while True:
    ask = input("안내면 진다 가위바위보:")
    if ask in choose:
        break
    print("")
    print("가위 바위 보중 하나로 입력하세요.")

#결과창
print("[결과]나:",ask,"상대방:",choose2)
if ask == choose2:
    print("무승부")

elif ask == "가위" and choose2 == "바위" or \
     ask == "바위" and choose2 == "보" or \
     ask == "보" and choose2 == "가위":
         print("패배")

else:
    print("승리")