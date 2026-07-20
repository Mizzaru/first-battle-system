hhp = 100
hdmg = 10
hmp = 60
fbdmg = 40
fbcost = 30
heal = 25
healcost = 20
ehp = 100
edmg = 20
print("На вас напал гоблин. К оружию!")
while hhp>0 and ehp>0:
    print("Ваше HP: ", hhp,"  HP врага: ", ehp)
    print("Вашe MP: ", hmp,"  MP врага", " ")
    print("Ваш урон: ", hdmg, "Урон врага: ", edmg)
    print("Что делать? 1. Атака. 2. Лечение.[20 MP] 3. Огненный шар.[30 MP]")
    choice = input ("Введите цифру с выбранным действием: ")
    if choice == "1" and hhp>0:
        print("Вы наносите ",hdmg, "урона гоблину!")
        ehp -= hdmg
        if ehp >0:
         print("Теперь у него ",ehp, " HP! Так держать!")
        input("Нажмите Enter чтобы продолжить")
    elif choice == "2" and hhp>0 and hmp > healcost:
        print("Вы использовали заклинание лечения, -", healcost, "MP")
        hhp += heal
        hmp -= healcost
        input("Нажмите Enter чтобы продолжить")
    elif choice == "3" and hhp >0 and hmp>fbcost:
        print("Вы использовали огненный шар -",fbcost,"MP")
        print("Противник получает ",fbdmg,"урона!")
        ehp -= fbdmg
        hmp -= fbcost
        input("Нажмите Enter чтобы продолжить")
    else:
        print("Вы сломали код, потому что автор пока не умеет возвращать вас" \
        "обратно, в случае неправильного действия :)")
    if ehp>0:
        print("Враг наносит удар! - ", edmg, "HP")
        hhp -= edmg
        input("Нажмите enter чтобы продолжить")
if hhp>0 and ehp<=0:
    playerwin = True
    print("Вы победили своего первого врага, поздравляю!")
    input("Нажмите enter чтобы продолжить")
elif hhp<=0 and ehp>0:
    playerwin = False
    print("К сожалению, в этот раз гоблин оказался сильнее. Попробуйте ещё раз!")
    input("Нажмите enter чтобы продолжить")
else:
    print("Не знаю, как именно, но вы умерли одновременно. LOL")
if playerwin == True:
    print ("Бой окончен, вы победили")
elif playerwin == False:
    print ("Бой окончен, вы проиграли")