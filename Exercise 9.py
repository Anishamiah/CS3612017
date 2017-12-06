print("Exercise 9: \n");

def list(l):
    x = [];
    i = 0;
    while i < len(l):
        try:
            if len(l[i]) >  1:
                counter = 0;
                smallerlist = l[i];

                while counter < len(smallerlist):
                    x.append(smallerlist[counter]);
                    counter = counter+ 1;
        except(TypeError):
            ans_list.append(l[iterator]);
        i = i+ 1;
    return(x);

n  = [[3,4],[1,6],[5,2]];

print("Original list: " , n);
print("New List: " , list(n));
