import random

#리스트
List = ["묵", "찌", "빠"]
me = 0
ai = 0
#첫번쨰
while True:
    while True:
        ask = input("안 내면 진다 가위바위보:")
        if ask in List:
            break
        else:
            print("")
            print("묵 찌 빠 중 하나를 입력하세요.")
    a = random.choice(List)
    if ask == a:
        print("[결과]나:",ask,"상대방:",a)
        print("다시")

    elif ask == "찌" and a == "묵" or \
         ask == "묵" and a == "빠" or \
         ask == "빠" and a == "찌":
             print("[결과]나:",ask,"상대방:",a)
             print("ai차례")
             ai =+1
             break

    else:
        print("[결과]나:",ask,"상대방:",a)
        print("당신차례")
        me =+1
        break
  
while True:
    if ai==1:
        while True:
            choice = input("안내면 진다 가위바위보:")
            if choice in List:
                break
            else:
                print("")
                print("묵 찌 빠 중 하나를 입력하세요.") 
        b = random.choice(List)
        if choice == b:
            print("[결과]나:",choice,"상대방:",b)
            print("패배")
            break

        elif choice == "찌" and b == "묵" or \
             choice == "묵" and b == "빠" or \
             choice == "빠" and b == "찌":
                 print("[결과]나:",choice,"상대방:",b)
                 print("ai차례")

        else:
            print("[결과]나:",choice,"상대방:",b)
            print("당신차례")
            ai =-1
            me =+1
            
    if me == 1:
        while True:
            choice = input("안내면 진다 가위바위보:")
            if choice in List:
                break
            else:
                print("")
                print("묵 찌 빠 중 하나를 입력하세요.")
        b = random.choice(List)
        if choice == b:
            print("[결과]나:",choice,"상대방:",b)
            print("승리")
            break

        elif choice == "찌" and b == "묵" or \
             choice == "묵" and b == "빠" or \
             choice == "빠" and b == "찌":
                 print("[결과]나:",choice,"상대방:",b)
                 print("ai차례")
                 ai =+1
                 me =-1

        else:
            print("[결과]나:",choice,"상대방:",b)
            print("당신차례")