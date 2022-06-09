class Sat:

    ListVariable= []
    
    def __Forma(self,varibles,var):
        self.clause={}
        for i in range(len(var)):
            self.clause[varibles[i]]=var[i]
        
    def __init__(self,file):
        self.clause={}
        after = file.split(sep=' ')
        after = after[0:(len(after)-1)]
       
        varibles = []
        var=[]
        for i in after:
            value = int(i)
            if value > 0 :
                varibles.append(abs(value))
                var.append(1)
            else:
                varibles.append(abs(value))
                var.append(0)
        self.AddVar(varibles)
        self.__Forma(varibles,var)

    def AddVar(self,Var):

        for i in Var:
            if i not in Sat.ListVariable:
                Sat.ListVariable.append(i)
        
    def GetClause(self):
        return self.clause    

    def GetValidation(self,Solution):
        sol=[]
        for i in list(self.clause.keys()):
            if self.clause[i] ==1 :
                # X
                sol.append(Solution[i-1])

            else:
                # !x
                if Solution[i-1] == 1 :
                    sol.append(0)
                else:
                    sol.append(1)    
        if 1 in sol:
            return True
        else:
            return False


    def Display(self):
        for i in list(self.clause.keys()):
            print('X'+str(i)+" : "+str(self.clause[i])) 

   
class CalculSat:

    def __init__(self):
        self.Sol=[]

    def GetOneSol(self,sol,index):
        
        solR=sol
  
        if sol[index] == 0 :
            solR[index] = 1
        else:
            solR[index]=0
        return solR 

    def max(self,listm):
        maxval=0
        maxindex=0
        for i in range(len(listm)):
            if listm[i]>maxval:
                maxval=listm[i]
                maxindex=i

        return maxindex 

    def score(self,clauses,Sol):
        score=0
        for item in clauses:
            if item.GetValidation(Sol):
                score= score+1
        return score 
