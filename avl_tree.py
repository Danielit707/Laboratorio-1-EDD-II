# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VVexKJKla6rG1yedGcRNbwt1uzqpRco6
"""

!pip install graphviz
from IPython.display import Image

from graphviz import Digraph

class NodoPelicula:
    def __init__(self, titulo, año, worldwide_earnings, domestic_earnings, foreign_earnings, domestic_percent, foreign_percent):
        self.titulo = titulo
        self.año = año
        self.worldwide_earnings = worldwide_earnings
        self.domestic_earnings = domestic_earnings
        self.foreign_earnings = foreign_earnings
        self.domestic_percent = domestic_percent
        self.foreign_percent = foreign_percent
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, nodo):
        if not nodo:
            return 0
        return nodo.height

    def get_balance(self, nodo):
        if not nodo:
            return 0
        return self.get_height(nodo.left) - self.get_height(nodo.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, titulo, año, worldwide_earnings, domestic_earnings, foreign_earnings, domestic_percent, foreign_percent):
        if not root:
            return NodoPelicula(titulo, año, worldwide_earnings, domestic_earnings, foreign_earnings, domestic_percent, foreign_percent)

        if titulo < root.titulo:
            root.left = self.insert(root.left, titulo, año, worldwide_earnings, domestic_earnings, foreign_earnings, domestic_percent, foreign_percent)
        else:
            root.right = self.insert(root.right, titulo, año, worldwide_earnings, domestic_earnings, foreign_earnings, domestic_percent, foreign_percent)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and titulo < root.left.titulo:
            return self.rotate_right(root)

        if balance < -1 and titulo > root.right.titulo:
            return self.rotate_left(root)

        if balance > 1 and titulo > root.left.titulo:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and titulo < root.right.titulo:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root):
        if not root:
            return

        print(f"{root.titulo} ({root.año})")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def visualize_tree(self, root):
        dot = Digraph()

        def add_node(nodo):
            if nodo:
                dot.node(nodo.titulo, f"{nodo.titulo} ({nodo.año})")
                if nodo.left:
                    dot.edge(nodo.titulo, nodo.left.titulo)
                if nodo.right:
                    dot.edge(nodo.titulo, nodo.right.titulo)
                add_node(nodo.left)
                add_node(nodo.right)

        add_node(root)
        return dot

    def save_tree(self, filename='avl_tree'):
        dot = self.visualize_tree(self.root)
        dot.render(filename, format='png', cleanup=True)

# Ejemplo de uso
avl = AVLTree()
avl.root = avl.insert(avl.root, "Mission: Impossible II", 2000, 546388108, 215409889, 330978219, 39.4, 60.6)

# Visualiza y guarda el árbol
dot = avl.visualize_tree(avl.root)
dot.render('avl_tree', format='png', cleanup=True)
Image('avl_tree.png')