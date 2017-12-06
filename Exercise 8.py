print("Exercise 8a) \n:");
a=[1,2,3]
print ("list a=", a);
print("Exercise 8b) \n:");
b=a
print("list b=a is",b);

print("Exercise 8c) \n:");
b[1]=3

print("Exercise 8d) \n:");
print(a, "list a is changed when a value is changed in the same position in b");
print("Exercise 8e) \n:");
c=a[:]

print("Exercise 8f) \n:");
c[2]=0
print("Exercise 8g) \n:");
print ("list a:",a, "No changes were made to a. \n");
 

def set_first_elem_to_zero(l):

    l[0] = 0;
    return l;
n = [1,2,3];
print("List: " , n);
print("After changing first entry to zero:" , set_first_elem_to_zero(n), "the original list can still be called, even though a new version exists.") ;

