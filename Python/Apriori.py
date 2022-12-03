class Apriori:
    # the class the group all the function for the aprioriTID algorithm
    
    def __init__(self, horizontal_database: list[set[int]], minsup_percentage: float) -> None:
        # constuctor that take in a horizontal database as a list of sets of int, and minumun support in percentage.
        self.database = horizontal_database
        self.minsup = int(minsup_percentage * len(horizontal_database))

    def generate_candidate(self, prelevel_frequent_itemsets: set) -> set:  
        # generate next level (k) set of itemsets based on the previous one (k-1) itemsets.
        # input: set of itemsets that has k-1 items
        # output: set of itemsets that has k items
        Ck = set()
        for i in prelevel_frequent_itemsets:
            for j in prelevel_frequent_itemsets:
                if len(i.union(j)) == len(i) + 1:
                    Ck.add(i.union(j))
        return Ck   

    def find_frequent_1_itemsets(self):
        # find itemsets that has only 1 item and meet the minimun support
        F1 = set()
        for i in self.database:
            for item in i:
                if self.find_support({item}) >= self.minsup:
                    F1.add(frozenset({item}))
        return F1

    def find_support(self, i):
        # find support of the given itemset
        count = 0
        for j in self.database:
            if i.issubset(j):
                count += 1
        return count
    
    # ALGORITHM FUNCTION
    def run(self):
        # run apriori algorithm to find the frequent itemsets
        # return the list of frequent itemset found by apriori algorithm

        F1 = self.find_frequent_1_itemsets()
        result = [F1]  
        k = 2
        while len(result[k - 2]) > 0:
            Ck = self.generate_candidate(result[k - 2])  # candidate k-itemsets
            Fk = set()  
            for X in Ck:
                if self.find_support(X) >= self.minsup:
                    Fk.add(X)
            result.append(Fk)
            k += 1
        return result


def main():
    horizontal_database =  [{1, 3, 4}, 
                            {2, 3, 5}, 
                            {1, 2, 3, 5}, 
                            {2, 5}, 
                            {1, 2, 3, 5}]
    apriori = Apriori(horizontal_database, 40/100)
    print(apriori.minsup)
    print(list(apriori.run()))
    
if __name__ == "__main__":
    main()