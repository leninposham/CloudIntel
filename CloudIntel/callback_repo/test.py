class sample:
    
    def  testmethod(self, result):
        if result[0]==0:
            name = 'Iris Setosa'
        elif result[0]==1: 
            name = 'Iris Versicolour '
        else result[0]==2:
            name = 'Iris Virginica'
        
        return {"name":name,"outcome":result[0]}
        
    
        
    
