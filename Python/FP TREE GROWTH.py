
import pandas as pd
from csv import reader
from collections import defaultdict


class NODE:
     def __init__(self, word, word_count=0, parent=None, link=None):
        self.word = word
        self.word_count = word_count
        self.parent = parent
        self.link = link
        self.children = {}
      


#tree traversal
     def visittree(self):
    

#        if self is None:
#            return None
        output=[]
        output.append(str(vocabdic[self.word]) + " " +str(self.word_count))
        if len(list(self.children.keys()))>0:
            for i in (list(self.children.keys())):
                output.append(self.children[i].visittree())
        return output
  
              
'''      Build FPTREE class and method       '''        
class fptree:
  def __init__(self, data, min_sup):
    self.data = data
    self.min_sup = min_sup

    self.root = NODE(word = "null", word_count=1)

    # items with > min_sup
    self.sortdic = []
    # items with their sups
    self.dicwithsup = {}
    # items and their rank in the descending order
    self.dicorder = {}

    # a table containing items, their counts, and their link node
    self.table = []

    # transactions with new order according to the supports in descending order
    self.newtrans = []

    self.temp = []
    self.construct(data)

  def construct(self, data):
    for transactions in data:
      for item in transactions:
        if item in self.dicwithsup.keys():
          self.dicwithsup[item] += 1
        else:
          self.dicwithsup[item] = 1
          # if item not yet exists, assign item with a support 1; if exist, increment the sup
    # create an item list
    itemlist = list(self.dicwithsup.keys())

    # if item < minsup, remove it
    for item in itemlist:
      if self.dicwithsup[item] < self.min_sup:
        del self.dicwithsup[item]
    # key = lambda x: (-x[1], x[0])
    self.sortdic = sorted(self.dicwithsup.items(), key=lambda x: (-x[1], x[0]))
    item_order = 0
    for i in self.sortdic:
      item = i[0]
      item_count = i[1]
      self.dicorder[item] = item_order
      item_order += 1
      item_info = {'item': item, 'item count': item_count, 'linknode': None}
      self.table.append(item_info)
    
    for line in data:
      word_sup = []
      for item in line:
        # only append items with > min_sup
        if item in self.dicwithsup.keys():
          word_sup.append(item)
      
      if len(word_sup) > 0:
        # reorder the word_sup in the new order
        sort_word_sup = sorted(word_sup, key=lambda k: self.dicorder[k])
        self.newtrans.append(sort_word_sup)

        R = self.root
        # loop through sort_word_sup, if there exists items in sort_word_sup found in children node, add up 1
        # else create new branch of the tree
        for i in sort_word_sup:
          if i in R.children.keys():
            R.children[i].word_count += 1
            R = R.children[i]
          else:
            R.children[i] = NODE(word = i, word_count=1, parent=R, link=None)
            R = R.children[i]
            # if there is no linknode then R is linknode itself
            # else find the last node of the  node linklist
            for item_info in self.table:
              if item_info['item'] == R.word:
                if item_info['linknode'] is None:
                  item_info['linknode'] = R
                else:
                  # n_node is a node
                  n_node = item_info['linknode']
                  while(n_node.link is not None):
                    n_node = n_node.link
                  n_node.link = R


  def treecondtransaction(self,N):
    if N.parent is None:
      return None
    else:
      condtree = []

      while N is not None:
        line = []
        parentN = N.parent
        while parentN.parent is not None:
          line.append(parentN.word)
          parentN = parentN.parent
        line = line[::-1]
        for i in range(N.word_count):
          condtree.append(line)
            
        N = N.link
      return condtree

  
#Find frequent word list by creating conditional tree
  def findfqt(self,parentnode=None):
      if len(list(self.root.children.keys()))==0:
          return None
      result=[]
      sup=self.min_sup
      final = {}
      reversetable = self.table[::-1]
      
      for i in reversetable:
        
        
        frequent_set = [set(), 0]
        if parentnode is not None:
          frequent_set[0] = {i['item']}.union(parentnode[0])
        else:
          frequent_set[0] = {i['item'], }
        frequent_set[1] = i['item count']
        result.append(frequent_set)
        

        
        condition_transactions = self.treecondtransaction(i['linknode'])

        condition_tree = fptree(condition_transactions, sup)
        condition_items = condition_tree.findfqt(frequent_set)
        if condition_items is not None:
          
          for item in condition_items:
            
            self.temp.append([i['item'] + ':', item])
            result.append(item)
            

      
      return result
  def printTB(self):
    return self.temp

#check if tree hight is larger than 1 
  def checkheight(self):
      if len(list(self.root.children.keys()))==0:
          return False
      else:
          return True


def remove_blank(S):
  for i in S:
    while "" in i:
      i.remove("")
  return S          
min_sup=2




# def main():
#   test_data = [['I1','I2','I5'],
#              ['I2','I4'],
#              ['I2','I3'],
#              ['I1','I2','I4'],
#              ['I1','I3'],
#              ['I2','I3'],
#              ['I1','I3'],
#              ['I1','I2','I3','I5'],
#              ['I1','I2','I3']]

#   dataset1 = []
#   dataset2 = []
#   with open('dataset1.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     for row in csv_reader:
#       dataset1.append(row)
#   dataset1 = remove_blank(dataset1)

#   with open('dataset2.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     for row in csv_reader:
#       dataset2.append(row)
#   dataset2 = remove_blank(dataset2)
  
#  # set 1
#   a = fptree(dataset1, min_sup)
#   a.findfqt()
#   # print(main1(test_data))
#   patterns = (a.printTB())
#   for i in patterns:
#     print(i)
#   print()
#   # set 2
#   a = fptree(dataset2, min_sup)
#   a.findfqt()
#   # print(main1(test_data))
#   patterns = (a.printTB())
#   for i in patterns:
#     print(i)

# if __name__ == "__main__":
#   main()

