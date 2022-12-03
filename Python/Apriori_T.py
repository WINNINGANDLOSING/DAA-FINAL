import time

def CandidateItemsets(Fk_1):  # Fk_1 : frequent k-1-itemsets
    Ck = set()
    for i in Fk_1:
        for j in Fk_1:
            if len(i.union(j)) == len(i) + 1:
                Ck.add(i.union(j))
    return Ck

# Create 1-itemsets
def freq_1(D, minsup=0.4):
    F1 = set()
    for i in D:
        for item in i:
            if sup({item}, D) >= minsup:
                F1.add(frozenset({item}))
    return F1


def Apiori(D, minsup):  
    F1 = freq_1(D)
    F = [F1]  # F : a set of frequent itemsets
    k = 2
    while len(F[k - 2]) > 0:
        # print(k-2)
        Ck = CandidateItemsets(F[k - 2])  # Ck : candidate k-itemsets
        #print('Ck',Ck)
        Fk = set()  # Fk : frequent k-itemsets
        for X in Ck:
            if sup(X, D) >= minsup:
                Fk.add(X)
        F.append(Fk)
        k += 1
    return F
   
    # ===============




def sup(i, D):
    count = 0
    for j in D:
        if i.issubset(j):
            count += 1
    res = count / len(D)
    return res

def main():
    D = [{1, 3, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5}, {1, 2, 3, 5}]
    # D = [{0, 1},
    #           {0, 2, 3, 4},
    #           {1, 2, 3, 5},
    #           {0, 1, 2, 3},
    #           {0, 1, 2, 5}]

    X =        [{0, 1},
              {0, 2, 3, 4},
              {1, 2, 3, 5},
              {0, 1, 2, 3},
              {0, 1, 2, 5}]
    minsup = 0.4
    start = time.time()
    F = Apiori(D, minsup)
   
    for i in range(len(F)):
        S = []
        for j in F[i]:
            S.append(list(j))
        print(str(i + 1) + "-itemsets: " + str(S))
    end = time.time()
    elapsed = (end - start) * 1000
    print("Time: %f ms" % elapsed)
    
if __name__ == "__main__":
    main()
    
