import time

class Apriori:
    def __init__(self, data, minSup) -> None:
        self.data = data
        self.minSup = minSup
        self.result = []
    def CandidateItemsets(self, Fk_1):  # Fk_1 : frequent k-1-itemsets
        Ck = set()
        for i in Fk_1:
            for j in Fk_1:
                if len(i.union(j)) == len(i) + 1:
                    Ck.add(i.union(j))
        return Ck    
    def freq_1(self, minsup=0.4):
        F1 = set()
        for i in self.data:
            for item in i:
                if self.sup({item}) >= self.minSup:
                    F1.add(frozenset({item}))
        return F1
    def sup(self, i):
        count = 0
        for j in self.data:
            if i.issubset(j):
                count += 1
        return count / len(self.data)
    
    def Apriori(self):  
        F1 = self.freq_1()
        result = [F1]  # F : a set of frequent itemsets
        k = 2
        while len(result[k - 2]) > 0:
            # print(k-2)
            Ck = self.CandidateItemsets(result[k - 2])  # Ck : candidate k-itemsets
            #print('Ck',Ck)
            Fk = set()  # Fk : frequent k-itemsets
            for X in Ck:
                if self.sup(X) >= self.minSup:
                    Fk.add(X)
            result.append(Fk)
            k += 1
        return result


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
    F = Apriori(D, minsup)
    F = F.Apriori()
    for i in range(len(F)):
        S = []
        for j in F[i]:
            S.append(list(j))
        print(str(i + 1) + "-itemsets: " + str(S))
    print(S)

    end = time.time()
    elapsed = (end - start) * 1000
    print("Time taken: %f ms" % elapsed)
    #print('check support:', F.CandidateGeneration(F.freq_1(D)))
if __name__ == "__main__":
    main()
    
