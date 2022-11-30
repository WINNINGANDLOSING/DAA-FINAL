import time
"""
The Apiori algorithm
input: D: a set of transactions database, minsup: a user-specified threshold
output: the set of frequent itemsets
Scan the database to calculate the support of all items in I;
F1 = {i|i ∈ I ∧ sup({i}) ≥ minisup }; // F1 : frequent 1-itemsets
k = 2;
while Fk = ∅ do
    Ck = CandidateGeneration (Fk - 1) ; // Ck : candidate k-itemsets
    Remove each candidate X ∈ Ck that contains a (k - 1)-itemset that is not in Fk-1;
    Scan the database to calculate the support of each candidate X ∈ Ck;
    Fk = {X|X ∈ Ck ∧ sup(X) ≥ minsup} ; // Fk : frequent k-itemsets
    k = k + 1;
end
return Uk = 1...k Fk;
"""

# Create 1-itemsets
def freq_1(D, minsup=0.4):
    F1 = set()
    for i in D:
        for item in i:
            if sup({item}, D) >= minsup:
                F1.add(frozenset({item}))
    return F1


def Apiori(D, minsup):  # D: a set of transactions database, minsup: a user-specified threshold
    # I = set()  # I: a set of items
    # for t in D:
    #     for i in t:
    #         I.add(i)
    # F1 = set()  # F1 : frequent 1-itemsets
    # for i in I:
    #     if sup({i}, D) >= minsup:
    #         F1.add(frozenset({i}))
    F1 = freq_1(D)
    F = [F1]  # F : a set of frequent itemsets
    k = 2
    while len(F[k - 2]) > 0:
        # print(k-2)
        Ck = CandidateGeneration(F[k - 2])  # Ck : candidate k-itemsets
        #print('Ck',Ck)
        Fk = set()  # Fk : frequent k-itemsets
        for X in Ck:
            if sup(X, D) >= minsup:
                Fk.add(X)
        F.append(Fk)
        k += 1
    return F
    # ==============
    k = 0
    while len(F[k]) > 0:
        freq_item = F[k]
        ck = CandidateGeneration(freq_item)       
        freq_item, item_support = create_freq_item(X, ck, min_support = 0.4)
        freq_items.append(freq_item)
        item_support_dict.update(item_support)
        k += 1
    # ===============

def CandidateGeneration(Fk_1):  # Fk_1 : frequent k-1-itemsets
    Ck = set()
    for i in Fk_1:
        for j in Fk_1:
            if len(i.union(j)) == len(i) + 1:
                Ck.add(i.union(j))
    return Ck


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
        print("Frequent " + str(i + 1) + "-itemsets: " + str(F[i]))
    end = time.time()
    elapsed = (end - start) * 1000
    print("Time taken: %f ms" % elapsed)
    
if __name__ == "__main__":
    main()
    
