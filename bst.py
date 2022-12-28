import sys

# Redirect stdout to a file
sys.stdout = open('outputPS9.txt', 'w')

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
#construction a tree
    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.priority > current_node.priority:
                    # insert to the right
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    # insert to the left
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
# pre-order traversal
    def pre_order_traversal(self, node):
        if node is not None:
            print(node.value)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
            
#function counting characters in each input value of all the nodes in the tree
dupwords = [ ]
def charcount(root):
    if root is None:
        return None
    
    # print(root.value,end="\n")
    dupwords.append(root.value)
    print(root.value+"--->has "+str(len(root.value))+" Characters",end="\n")
    charcount(root.left)
    charcount(root.right)

#function for Listing all the given input words based on the order of priority from highest to least
from functools import cmp_to_key
def sort_strings(words, order):
  # Create a mapping from alphabet to its position in the order
  alphabet_map = {c: i for i, c in enumerate(order)}
  
  # Define a custom comparator function
  def compare(word1, word2):
    # Iterate through the characters in the two words
    for c1, c2 in zip(word1, word2):
      # If the characters have different positions in the order, return the result of the comparison
      if alphabet_map[c1] != alphabet_map[c2]:
        return alphabet_map[c1] - alphabet_map[c2]
    # If the words have the same characters, return the result based on the length of the words
    return len(word1) - len(word2)
  
  # Sort the array of strings using the custom comparator function
  sorted_words = sorted(words, key=cmp_to_key(compare))
  
  return sorted_words

#function for counting the nodes in the tree with the same count
counts = {}
def count_nodes(node):
    if node is None:
        return

    # add the node to the counts dictionary
    if len(node.value) not in counts:
        counts[len(node.value)] = [node.value]
    else:
        counts[len(node.value)].append(node.value)

    # recursively count the nodes in the left and right subtrees
    count_nodes(node.left)
    count_nodes(node.right)

#function for finding the level
def find_level(node, value, level):
    if node is None:
        return -1

    if node.value == value:
        return level

    # search the left and right subtrees
    left_level = find_level(node.left, value, level+1)
    right_level = find_level(node.right, value, level+1)

    # return the level if found, or -1 if not found
    if left_level != -1:
        return left_level
    else:
        return right_level

#function for finding the duplicates
def find_duplicates(node):
    if node is None:
        return []

    # find the duplicates in the left and right subtrees
    left_duplicates = find_duplicates(node.left)
    right_duplicates = find_duplicates(node.right)

    # check for duplicates in the current node
    current_duplicates = []
    if node.left is not None and node.left.value == node.value:
        current_duplicates.append(node.left.value)
    if node.right is not None and node.right.value == node.value:
        current_duplicates.append(node.right.value)

    # return the list of duplicates
    return left_duplicates + right_duplicates + current_duplicates


#create the priority order
order = "^$#@!9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
ss =''
for i in order:
  ss = i + ss


#initialize the binary tree
bt = BinaryTree()

#reading the input from file
import os
# file = open(os.path.join(os.path.curdir, 'input.txt'),'r')
strings = []
file = open("inputPS9.txt",'r')
lines = file.readlines()
for i in lines:
    strings.append(i.strip())

#inserting values in to binary tree based on priority
for s in strings:
    priority = ss.index(s[0])
    # insert the values into the binary tree
    bt.insert(s, priority)

print("1. Figure out how many characters in each input value of all the nodes in the tree?",end="\n\n")
#counting characters in each input value of all the nodes in the tree
charcount(bt.root)
print()
#printing total numbers of nodes in BST
print("These are the total "+str(len(dupwords))+" nodes in the tree with character count of each node as above",end="\n\n")

print("2. Identify how many nodes in the tree are with the same string count and mention those words under the relevant count list.",end="\n")
#counting the nodes in the tree are with the same string count
count_nodes(bt.root)

print()
for count,words in counts.items():
    if len(words)>=2:
        # print("\n")
        print("There are "+str(len(words))+" nodes with same string count as "+str(count),end="\n")
        print(str(words) + "--->"+ str(count),end="\n\n")

print("3. List out all the given input words based on the order of priority as mentioned in the problem statement from highest to least/least to highest.",end="\n\n")
#Listing all the given input words based on the order of priority from highest to least
print("List of input word based on the order of Priority(higest to least)",end="\n\n")
sorted_words = sort_strings(strings, order)
for i in sorted_words:
  print(i,end="\n")
print("\n")

#counting character and appending the counts
l = [ ]
for i in dupwords:
  l.append(len(i))

print("4. Find out the largest string count and the duplicate string after comparing all the nodes in the tree and those nodes position/level in the binary search tree.",end="\n\n")
#Finding the largest string count and level in the binary search tree.
for j in range(len(strings)):
  if len(strings[j])==max(l):
    level = find_level(bt.root, i, 0)
    print("Largest string in all the nodes is with "+str(max(l))+ " as string count and it is at level "+str(level)+" in the BST..!",end="\n\n")

#Finding the duplicate string and level in the binary search tree.
duplicates = find_duplicates(bt.root)
print("Duplicate input string in all the nodes is/are ",end="\n\n")
for s in duplicates:
    level = find_level(bt.root, s, 0)
    print(s +" node repeated for "+str(dupwords.count(s))+ " times is at level ", str(level) +" in the BST..!",end="\n")
print("\n")
print("5. Specify all the node input values in the preorder traversal of BST.",end="\n\n")
# printing the values in preorder
print("Preorder traversal of the BST is",end="\n\n")
bt.pre_order_traversal(bt.root)

#closing the output file
sys.stdout.close()
