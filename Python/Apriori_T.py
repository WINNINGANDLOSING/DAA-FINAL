import time

# Class Apriori to find frequent pattern of itemsets
# Input: Dataset of the transaction and min support
# Output: List of of frequent pattern 

class Apriori:
    def __init__(self, data, minSup) -> None:
        self.data = data
        self.minSup = minSup
    def CandidateItemsets(self, itemset):  
        Ck = set()
        for i in itemset:
            for j in itemset:
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
        result = [F1]  
        k = 2
        while len(result[k - 2]) > 0:
            Ck = self.CandidateItemsets(result[k - 2])  # Ck : candidate k-itemsets
            Fk = set()  
            for X in Ck:
                if self.sup(X) >= self.minSup:
                    Fk.add(X)
            result.append(Fk)
            k += 1
        return result


def main():
    D = [{1, 3, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5}, {1, 2, 3, 5}]
    minsup = 0.4
    start = time.time()
    F = Apriori(D, minsup)


    a = F.Apriori()
    for i in range(len(a)):
        S = []
        for j in a[i]:
            S.append((list(j), F.sup(j)))
        print(str(i + 1) + "-itemsets: " + str(S))
    
    end = time.time()
    elapsed = (end - start) * 1000
    print("Time taken: %f ms" % elapsed)
    
if __name__ == "__main__":
    main()
