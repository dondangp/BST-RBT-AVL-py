# Tree Data Structures

This repository contains implementations of three common types of tree data structures: Binary Search Tree (BST), Red-Black Tree, and AVL Tree. Each tree implementation supports operations such as insertion, deletion, and traversal, with particular attention to maintaining specific properties like balance and search efficiency.

## Binary Search Tree (BST)

A Binary Search Tree is a node-based binary tree data structure which has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.

### Operations and Examples

**Insertion**
- Input: Insert 50, 30, 20, 40, 70, 60, 80
- Expected Output: Inorder traversal of BST: `[20, 30, 40, 50, 60, 70, 80]`

**Deletion**
- Input: Delete 50
- Expected Output: Inorder traversal after deletion: `[20, 30, 40, 60, 70, 80]`

**Search**
- Input: Search for 60
- Expected Output: `Found`

## Red-Black Tree

Red-Black Tree is a kind of self-balancing binary search tree. Each node of the binary tree has an extra bit, and that bit is often interpreted as the color (red or black) of the node. These color bits are used to ensure the tree remains approximately balanced during insertions and deletions.

### Operations and Examples

**Insertion**
- Input: Insert 55, 40, 65, 60, 75, 57
- Expected Output: Inorder traversal of Red-Black Tree: `[40, 55, 57, 60, 65, 75]`

## AVL Tree

An AVL tree is a self-balancing binary search tree, and it was the first such data structure to be invented. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.

### Operations and Examples

**Insertion**
- Input: Insert 10, 20, 30, 40, 50, 25
- Expected Output: Inorder traversal of AVL tree: `[10, 20, 25, 30, 40, 50]`

**Deletion**
- Input: Delete 20
- Expected Output: Inorder traversal after deletion: `[10, 25, 30, 40, 50]`

## Getting Started

To run these examples:
1. Clone the repository.
2. Run the Python files corresponding to each tree type.
3. Modify the test inputs in the source code as needed to see different results.



