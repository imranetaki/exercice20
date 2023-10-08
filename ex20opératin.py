a=float(input("entrer un réel svp :  "))
b=float(input("entrer un autre réel svp :  "))
op=input("entrer une opération svp : ")
match op :
    case "+" : 
        print(a ,"+", b ,"=" , a+b)
    case "-" :
        print(a ,"-", b ,"=" , a-b)
    case "*" :
        print(a ,"*", b ,"=" , a*b)
    case "/" :
        print(a ,"/", b ,"=" , a/b)
    case "la moyenne" :
        print("la moyenne est : ", (a+b)/2)
    case other :
        print("entrer une autre opération  ")