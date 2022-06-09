from Sat import Sat,CalculSat

calc = CalculSat()
Clauses =[]

def AddClause(clause):
    Clauses.append(clause)


with open('bmc-ibm-7.txt') as f:
    i = 0

    while(i<1500):
        c = f.readline()
        s = Sat(c)
        AddClause(s)
        i=i+1
       
    sol=[]
    nbVar=len( Clauses[0].ListVariable)
    for i in range(len( Clauses[0].ListVariable)):
        sol.append(0) 
    # for clause in Clauses:
    #     print(clause.Display())
            

    open = True
    score = calc.score(Clauses,sol)

    if score == len(Clauses):
        open = False
        print("Sol is the first : ")
        print(sol)

    k = 0
  
    fin = 100+ (len(Clauses)/2);
    print(fin)
    while open and k<fin :
        k=k+1
        print("k = "+str(k))
        print( i<fin )
        scores=[]
        for i in range(nbVar):
            scores.append(0)
            Newsol= calc.GetOneSol(sol,i)
            scores[i]=calc.score(Clauses,Newsol)

        MIndex = calc.max(scores)    
        sol= calc.GetOneSol(sol,MIndex)
        if scores[MIndex]== len(Clauses):
            open=False
            print("is True so the sol in : " )
            print(sol)
        else:
            open=True
        
    print("sol : ")
    print(sol)
    print("score: ")
    print(calc.score(Clauses,sol))