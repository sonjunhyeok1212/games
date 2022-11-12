import random
www = ["3", "4"]
kkk = ["on", "off"]

#결과창
s1 = 0
b11 = 0
o1 = 0
s2 = 0
b2 = 0
o2 = 0
s3 = 0
b3 = 0
o3 = 0
s4 = 0
b4 = 0
o4 = 0
b01 = 0
b02 = 0
b03 = 0
b04 = 0
b21 = 0
b22 = 0
b23 = 0
b24 = 0
# 3 or 4?
while True:
    qqq = input("3자리와 4자리중에 고르시오:")
    if qqq in www:
        break
    else:
        print("3과 4중에 입력하세요")

if qqq == "4":
    while True:
        sjh = input("중복 on off:")
        if sjh in kkk:
            break
        else:
            print("on off 중 하나를 적으시오")

    jjj = random.randrange(1000, 10000) 
    a0 = int(jjj) // 1000
    b0 = (int(jjj) - int(a0)*1000)//100
    c0 = (int(jjj) - int(a0)*1000 - int(b0)*100)//10
    d0 = int(jjj) % 10
    if sjh == "off":
        while True:
            a0 = int(jjj) // 1000
            b0 = (int(jjj) - int(a0)*1000)//100
            c0 = (int(jjj) - int(a0)*1000 - int(b0)*100)//10
            d0 = int(jjj) % 10
            if a0 == b0:
                jjj = random.randrange(1000, 10000)
            elif a0 == c0:
                jjj = random.randrange(1000, 10000)
            elif a0== d0:
                jjj = random.randrange(1000, 10000)
            elif b0 == c0:
                jjj = random.randrange(1000, 10000)
            elif b0== d0:
                jjj = random.randrange(1000, 10000)
            elif c0 == d0:
                jjj = random.randrange(1000, 10000)
            else:
                print("꺼짐")
                break
    else:
        print("켜짐")

    #숫자가 맞는지 확인 
    while True:
        s1 = 0
        b11 = 0
        o1 = 0
        s2 = 0
        b2 = 0
        o2 = 0
        s3 = 0
        b3 = 0
        o3 = 0
        s4 = 0
        b4 = 0
        o4 = 0
        b01 = 0
        b02 = 0
        b03 = 0
        b04 = 0
        b21 = 0
        b22 = 0
        b23 = 0
        b24 = 0

        while True:
            me = input("숫자를 적으시오:")
            check = me.isdigit()

            if int(check) == True:
                if 1000 <= int(me) <= 9999:
                    break
                else:
                    print("4자리수를 적으시오")

        #숫자 나누기
        a1 = int(me) // 1000
        b1 = (int(me) - int(a1)*1000)//100
        c1 = (int(me) - int(a1)*1000 - int(b1)*100)//10
        d1 = int(me) % 10
        
        if int(a1) == int(a0):
            s1 = 1 
        elif int(a1) == int(b0):
            b11 = 1
        elif int(a1) == int(c0):
            b01 = 1
        elif int(a1) == int(d0):
            b21 = 1
        else:
            o1 = 1


        if int(b1) == int(b0):
            s2 = 1
        elif int(b1) == int(a0):
            b2 = 1
        elif int(b1) == int(c0):
            b02 = 1
        elif int(b1) == int(d0):
             b22 = 1
        else:
            o2 = 1


        if int(c1) == int(c0):
            s3 = 1
        elif int(c1) == int(a0):
            b3 = 1
        elif int(c1) == int(b0):
            b03 = 1
        elif int(c1) == int(d0):
           b23 = 1
        else:
            o3 = 1
        
        if int(d1) == int(d0):
            s4 = 1
        elif int(d1) == int(a0):
            b4 = 1
        elif int(d1) == int(b0):
            b04 = 1
        elif int(d1) == int(c0):
           b24 = 1
        else:
            o4 = 1

        finals = int(s1) + int(s2) + int(s3) + int(s4)
        finalb = int(b11) + int(b2) + int(b3) + int(b01) + int(b02) + int(b03) + int(b04) + int(b21) + int(b22) + int(b23) + int(b24)
        finalo = int(o1) + int(o2) + int(o3) + int(o4)
        print ("S:", finals,)
        print ("B:",finalb,)
        print ("O:",finalo,)
        
        if int(finals) == 4:
            print("정답")
            print("숫자:",me,)
            break
        else:
            finals = 0
            finalb = 0
            finalo = 0
else:
    while True:
        sjh = input("중복 on off:")
        if sjh in kkk:
            break
        else:
            print("on off 중 하나를 적으시오")

    jjj = random.randrange(100, 1000) 
    a0 = int(jjj) // 100
    b0 = (int(jjj) - int(a0)*100)//10
    c0 = int(jjj) % 10
    if sjh == "off":
        while True:
            a0 = int(jjj) // 100
            b0 = (int(jjj) - int(a0)*100)//10
            c0 = int(jjj) % 10
            if a0 == b0:
                jjj = random.randrange(100, 1000)
            elif a0 == c0:
                jjj = random.randrange(100, 1000)
            elif b0 == c0:
                jjj = random.randrange(100, 1000)
            else:
                print("꺼짐")
                break
    else:
        print("켜짐")
    while True:
        s1 = 0
        b11 = 0
        o1 = 0
        s2 = 0
        b2 = 0
        o2 = 0
        s3 = 0
        b3 = 0
        o3 = 0
        b01 = 0
        b02 = 0
        b03 = 0

        while True:
            me = input("숫자를 적으시오:")
            check = me.isdigit()

            if int(check) == True:
                if 100 <= int(me) <= 999:
                    break
                else:
                    print("3자리수를 적으시오")

        #숫자 나누기
        a1 = int(me) // 100
        b1 = (int(me) - int(a1)*100)//10
        c1 = int(me) % 10

        if int(a1) == int(a0):
            s1 = 1 
        elif int(a1) == int(b0):
            b11 = 1
        elif int(a1) == int(c0):
            b01 = 1
        else:
            o1 = 1


        if int(b1) == int(b0):
            s2 = 1
        elif int(b1) == int(a0):
            b2 = 1
        elif int(b1) == int(c0):
            b02 = 1
        else:
            o2 = 1


        if int(c1) == int(c0):
            s3 = 1
        elif int(c1) == int(a0):
            b3 = 1
        elif int(c1) == int(b0):
            b03 = 1
        else:
            o3 = 1

        finals = int(s1) + int(s2) + int(s3)
        finalb = int(b11) + int(b2) + int(b3) + int(b01) + int(b02) + int(b03)
        finalo = int(o1) + int(o2) + int(o3)
        print ("S:", finals,)
        print ("B:",finalb,)
        print ("O:",finalo,)
        
        if int(finals) == 3:
            print("정답")
            print("숫자:",me,)
            break
        else:
            finals = 0
            finalb = 0
            finalo = 0