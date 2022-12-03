class AprioriTID:

    def __init__(self, vertical_database: list[set[int]], minsup_percentage: float) -> None:
        self.database = vertical_database
        self.minsup = int(minsup_percentage * len(vertical_database))

    def generate_candidate(self, prelevel_frequent_itemsets: set) -> set[frozenset[int]]:

        candidates = set()
        for itemset1 in prelevel_frequent_itemsets:
            for itemset2 in prelevel_frequent_itemsets:
                candidate = itemset1.union(itemset2)
                if len(candidate) == len(itemset1) + 1:
                    candidates.add(candidate)
        
        return candidates

    def is_frequent(self, itemset: frozenset[int]) -> bool:
        LoT = list()        

        for item in itemset:
            LoT.append(self.database[item])

        intersection = set.intersection(*LoT)
        
        if len(intersection) >= self.minsup:
            return True
        return False


    def find_frequent_1_itemsets(self):
        for item in range(len(self.database)):
            if len(self.database[item]) >= self.minsup:
                yield frozenset([item])


    def run(self) -> set[set[int]]:
        
        F = [set([None]) for _ in range(len(self.database)+1)]
        k = 1
        F[k] = set(self.find_frequent_1_itemsets())
        result = F[k]
        
        while (F[k] != 0) and (k < len(self.database)):
            C = self.generate_candidate(F[k])
            k += 1

            F[k].clear()
            for itemset in C:
                if self.is_frequent(itemset):
                    F[k].add(itemset)
            
            result = result.union(F[k])
        
        return result


vertical_database = [{1,3,5},
                    {2,3,4,5},
                    {1,2,3,5},
                    {1},
                    {2,3,4,5}]        
aprioriTID = AprioriTID(vertical_database, 60/100)
print(aprioriTID.minsup)
print(list(aprioriTID.run()))