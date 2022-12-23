# Bits Data science and Engineering assignment-1

## 1. Problem Statement

Consider a tree with input data value given as a string for each node. Follow the constraints while taking the input (no white space in between the character) , it can be with any of the combination i.e. special character/alphabets/numeric value/all in one word (example: 2345/implement/the123&/789abcde/2@entry/@$!)...
Construct a BST by comparing each input word by following the given ordered rules i.e., high priority given to Special character(! (least) @ # $ ^(highest)) only use these 5 special characters in the same order of priority as mentioned, next priority to numeric values ( 0 (least) to 9 (highest) ) and last priority to alphabets (small letters (least), capital letters (highest)). If the same/duplicate word is given as input then add a counter value of that node and increment it, and arrange rest of the tree nodes in the same fashion based on the rules (i.e., each character of the word to be compared and need to arrange them accordingly. example: 2345 and 2@entry as first character is same in both words then compare second character Which is 3 and @ from each word. Similarly, arrogance and arrange as the first 3 characters were the same in both the string, so compare next character o and a of both words) and place them in the binary search tree structure...
For example, given
1. [ 80186356719, $we456try, Arrogance, 9type21#jr, arrogance, !9n6lq0@p74jxaal, Imple1983^4#@ ]

### Let us use the above constraints to answer the below questions:

1. Figure out how many characters in each input value of all the nodes in the tree?
2. Identify how many nodes in the tree are with the same string count and mention those words under the relevant count list.
3. List out all the given input words based on the order of priority as mentioned in the problem statement from highest to least/least to highest.
4. Find out the largest string count and the duplicate string after comparing all the nodes in the tree and those nodes position/level in the binary search tree.
5. Specify all the node input values in the preorder traversal of BST.

### Requirements:

1. Read the input from a file (inputPS9.txt), where each Node should be with input given as string.
2. You will output your answers to a file (outputPS9.txt) for each line.
3. Perform an analysis for the features above and give the running time in terms of input size: n.


## Design Document for Binary Search Tree Construction and Traversal

#### Introduction
The purpose of this design document is to outline the steps for constructing a binary search tree (BST) and performing various traversals on the tree. The BST will be constructed using a list of strings and a priority order, where the priority of each string is determined by the first character in the string. The traversals will include pre-order traversal, which prints the values of the nodes pre order from smallest to largest, and finding the number of nodes in the tree with the same string count, the largest string count and the duplicate strings, and the level or height of a node in the tree.

#### Data Structures
    Node class: This class represents a single node in the BST. It has the following attributes:

    value: The value of the node, which is a string.
    priority: The priority of the node, which is determined by the first character in the value.
    left: A reference to the left child of the node.
    right: A reference to the right child of the node.

#### BinaryTree class: This class represents the BST and has the following methods:

    init: This method initializes the root node of the BST.
    insert: This method inserts a new node into the BST. It takes a value and a priority as input and creates a new node with these values. It then traverses the tree to find the correct position for the new node based on the priority.
    in_order_traversal: This method performs an pre-order traversal of the BST, printing the values of the nodes pre order from smallest to largest.
    count_nodes: This method counts the number of nodes in the BST with the same string count and returns a dictionary with the string count as the key and a list of strings with that count as the value.
    find_largest_string_count: This method finds the largest string count in the BST and returns the count and a list of strings with that count.
    find_duplicates: This method finds the duplicate strings in the BST and returns a list of these strings.
    find_level: This method finds the level or height of a node in the BST and returns the level.

#### Algorithms

Insertion: To insert a new node into the BST, the following steps are performed:

Create a new node with the given value and priority.
    If the root node is None, set the root node to the new node.
    Otherwise, set the current node to the root node.
    While True:
        If the new node's priority is greater than the current node's priority:
        If the current node's right child is None, set the right child to the new node and break the loop.
        Otherwise, set the current node to the right child.
        Otherwise:
        If the current node's left child is None, set the left child to the new node and break the loop.
        Otherwise, set the current node to the left child.

#### Pre-order traversal: 
    To perform an Pre-order traversal of the BST, the following steps are performed:

    If the current node is None, return.
    Recursively traverse the left subtree.
    Print the value of the current node.
    Recursively traverse the right subtree.

## Run time analysis

The time complexity of constructing the binary search tree is O(n*l),
 where n is the number of strings and l is the average length of the strings. 
 This is because each string needs to be inserted into the tree, 
 which requires traversing the tree to find the correct position for the new node. 
 The time complexity for each insertion is O(l), 
 because the priority of each string is determined by the first character, which has a maximum length of 1.

The time complexity of the pre-order traversal is O(n), because it visits each node in the tree exactly once.

The time complexity of finding the number of nodes in the tree with the same string count is O(n), 
because it visits each node in the tree exactly once.

The time complexity of finding the largest string count and the duplicate strings is O(n), 
because it visits each node in the tree exactly once.

The time complexity of finding the level or height of a node in the tree is O(l), 
because it requires traversing the tree to find the node.

Overall, the time complexity of the above operations is O(nl + n + n + n + l) = O(nl), 
which is linear in the number of strings and the average length of the strings.

It is important to note that these time complexities are in terms of the asymptotic notation, 
which means that they represent the worst-case time complexity. 
In practice, the actual time required to perform these operations may be significantly lower,
depending on the specific input data and the implementation of the algorithms.