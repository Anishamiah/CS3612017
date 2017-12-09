print ("Exercise 11: \n");

def iteration(L):
       i =1;
       result=L[0];

       if len(L)==0:
        return 0;

       while i < len(L):
           result = result * L[i];

           i = i+1;
       return result;

def recursion (L):

       result=1;
       if len(L) == 0:
            return result;
       else:
            result =L[0];
            del L[0];
            return result * recursion(L);


Sample_List= [1,4,3,5];
print ("Sample List is", Sample_List);       
print("Iterative way: " , iteration(Sample_List));
print("Recursive way: ", recursion(Sample_List));
       
