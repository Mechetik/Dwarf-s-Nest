FigName = str(input("Input Chess name plz: "))
a= int(input("input start x: ",))    
b= int(input("input start y: ",))
c= int(input("input final x: ",))
d= int(input("input final y: ",))
ac = a-c
bd = b-d
ac_mod = abs(a-c)
bd_mod = abs(b-d)
print(ac,bd,ac_mod,bd_mod, sep=",")
if FigName == "Rook" or FigName == "rook":    # Ладья (Rook)
    if ((a==c) and not(b==d)) or ((b==d) and not(a==c)):
        print ("YES")
    else:
        print ("NO")
elif FigName == "King" or FigName == "king":   # Король (King)
    if (-1<=(a-c)<=1) and (-1<=(b-d)<=1):
        print ("YES")
    else:
        print ("NO")
elif FigName == "Bishop" or FigName == "bishop":   # Слон (Bishop)
    if (abs(a-c)==abs(b-d)):
        print ("YES")
    else:
        print ("NO")       
elif FigName == "Queen" or FigName == "queen":   # Ферзь (Queen)
    if ((a==c) and not(b==d)) or ((b==d) and not(a==c)) or (abs(a-c)==abs(b-d)):
        print ("YES")
    else:
        print ("NO")
if FigName == "Pawn" or FigName == "pawn":    # Пешка (Pawn)
    if not (2<=b<=7):
        print("Wrong start coordinates!")
    else:
        if (a==c) and (0<bd<=2):
            print ("YES")
        else:
            print ("NO")
if FigName == "Knight" or FigName == "knight":    # Конь (Knight)
    if ((ac_mod==1) and (bd_mod==2)) or ((ac_mod==2) and (bd_mod==1)):
        print ("YES")
    else:
        print ("NO")