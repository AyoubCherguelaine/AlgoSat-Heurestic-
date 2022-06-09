def GetOneSol(sol,index):
    solR=sol
  
    if sol[index] == 0 :
        solR[index] = 1
    else:
        solR[index]=0
    return solR    

def TestClause(clause,sol,nbVar):
    check=[]
     
    for i in range(nbVar):
       
        if clause[i]==1:
            #X
            check.append(sol[i])
        else:
            if clause[i] == -1:
                #!X   
                if sol[i] == 1:
                    check.append(0)
                else:
                    check.append(1)    
            
    if 1 in check:
        return True
    else:
        return False    

def score(clauses,Sol,nbVar):
    score=0
    for item in clauses:
        if TestClause(item,Sol,nbVar):
            score= score+1
    return score            


def max(listm):
    maxval=0
    maxindex=0
    for i in range(len(listm)):
        if listm[i]>maxval:
            maxval=listm[i]
            maxindex=i

    return maxindex

#nbVar = int(input("Variable : "))
nbVar=4
clauses = [[1, 1, 0, 1], [0, -1, 1, 0], [1, 0, -1, -1], [1, 0, 0, 1],[-1 , 1, -1, -1],[ 1, 1, 1, 0]]

#for i in range(4):
#    clause=[]
#    for j in range(nbVar):
#        key = 'X'+ str(j)
#        print(key)
        
#        clause.append(int(input("1 or 0 or -1 in "+key)))
        #clause.key = 

#    clauses.append(clause);    



sol=[0,0,0,0]
var= True

print(sol)

if score(clauses,sol,nbVar)== len(clauses):
    print("valide")
else:
    print(score(clauses,sol,nbVar))
    while var:
        scores=[]
        for i in range(nbVar):
            scores.append(0)
            Newsol=GetOneSol(sol,i)
            scores[i]=score(clauses,Newsol, nbVar)
        print("Score :")
        print(scores)
        MIndex = max(scores)
        print("max = " + str( scores[MIndex]))  
        sol= GetOneSol(sol,MIndex)
        print(sol)
        if scores[MIndex]== len(clauses) :
            var=False    
        else:
            var=True


#for i in range(nbVar):
#    sol.i = 0


