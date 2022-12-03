import time
true_res = []
def _list(i,j):
        temp_list = []
        temp_list.append(i)
        temp_list.append(j)
        final_list = []
        for x in temp_list:
            for x_ in x:
                if x_ not in final_list:
                    final_list.append(x_)
        return final_list

def sorted_res(list,max_length):
        my_list = []
        true_list = []
        for x in list:
            my_list.append(sorted(x))
        for x in my_list:
            if x not in true_list and len(x)==max_length+1:
                true_list.append(sorted(x))
        return true_list
        
def printRes(res):
    for i in res:
        print(i)
        
def eclat(R, minsup):
    if R=={}:
        printRes(true_res)
        return
    res = []
    for i in R:
        max_length = (len(i))
    if max_length==1:
        itemset_1 = []
        for i in R:
            if len(R[i])>=minsup:
                itemset_1.append(i)
        true_res.append([itemset_1])
        
    check_repeat = []
    R_ = {}
    for i in R.copy():
        for j in R.copy():
            if i != j:
                temp_set = R[i]&R[j]
                if len(temp_set) >=minsup and ([i,j]) not in check_repeat:
                    #print("i", i, "j", j,"R[i]", R[i], "R[j]",R[j], "R[i] & R[j]", temp_set, len(temp_set))
                    final_list = _list(i,j)
                    final_list = sorted(final_list)
                    res.append(final_list)
                    if(len(tuple(final_list)))==max_length+1:
                        R_[tuple(final_list)] = {st for st in temp_set}
                    check_repeat.append([i,j])
                    check_repeat.append([j,i])
    
    res = sorted_res(res,max_length)
    true_res.append(res)
    eclat(R_,minsup)
    
def main(): 
    """Main function."""
    #R = {'a': {1, 3, 4}, 'b': {2, 3, 5}, 'c': {1, 2, 3, 5}, 'd': {2, 5}, 'f': {1, 2, 3, 5}}
    R = {'1': {'t1', 't3', 't5'}, '2': {'t2', 't3', 't4', 't5'} , '3': {'t1', 't2', 't3', 't5'}, '4': {'t1'}, '5': {'t2', 't3', 't4', 't5'}}
    
    start = time.time()
    eclat(R,minsup=2)
    end = time.time()
    print ('Time: ', end - start)
   
                
                    
                    
    
if __name__ == "__main__":
    main()