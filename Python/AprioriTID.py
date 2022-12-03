class AprioriTID:
    # the class the group all the function for the aprioriTID algorithm

    def __init__(self, vertical_database: list[set[int]], minsup_percentage: float) -> None:
        # constuctor that take in a vertical database as a list of sets of int, and minumun support in percentage.
        self.database = vertical_database
        self.minsup = int(minsup_percentage * len(vertical_database))

    def generate_candidate(self, prelevel_frequent_itemsets: set[frozenset[int]]) -> set[frozenset[int]]:
        # generate next level (k) set of itemsets based on the previous one (k-1) itemsets.
        # input: set of itemsets that has k-1 items
        # output: set of itemsets that has k items
        candidates = set()
        for itemset1 in prelevel_frequent_itemsets:
            for itemset2 in prelevel_frequent_itemsets:
                candidate = itemset1.union(itemset2)
                if len(candidate) == len(itemset1) + 1:
                    candidates.add(candidate)
        
        return candidates

    def is_frequent(self, itemset: frozenset[int]) -> bool:
        # check if a given itemset is frequent
        # input: an itemset
        # output: True is frequent, False if not

        LoT = list() # List of Transaction    

        for item in itemset:
            LoT.append(self.database[item]) # this list a made just for coding the intersection below

        intersection = set.intersection(*LoT)
        
        if len(intersection) >= self.minsup:
            return True
        return False

    def find_frequent_1_itemsets(self):
        # yield itemset that has only 1 item and meet the minimun support
        for item in range(len(self.database)):
            if len(self.database[item]) >= self.minsup:
                yield frozenset([item])


    # ALGORITHM FUNCTION
    def run(self) -> list[frozenset[int]]:
        # run apriori algorithm to find the frequent itemsets
        # return the list of frequent itemset found by aprioriTID algorithm
        
        F = [set([None]) for _ in range(len(self.database)+1)] # blank list of sets to store frequent i-itemset at i-th index
        k = 1
        F[k] = set(self.find_frequent_1_itemsets())
        result = F[k]
        
        while (F[k] != 0) and (k < len(self.database)):
            C = self.generate_candidate(F[k]) # set of candidates, each candidate is a frozenset
            k += 1

            F[k].clear() # clear initial value, which is None
            for itemset in C:
                if self.is_frequent(itemset):
                    F[k].add(itemset)
            
            result = result.union(F[k])
        
        return result


# TESTING
def main():
    vertical_database =[{1,3,5},
                        {2,3,4,5},
                        {1,2,3,5},
                        {1},
                        {2,3,4,5}]        
    aprioriTID = AprioriTID(vertical_database, 60/100)
    print(aprioriTID.minsup)
    print(list(aprioriTID.run()))

if __name__=="__main__":
    main()