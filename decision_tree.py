import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        pass

    def _grow_tree(self, X, y, depth=0):
        pass

    def _best_split(self, X, y, feat_idxs):
      best_gain = -1
      best_feat, best_thresh = None, None
      for feat in feat_idxs:    #pętla zagnieżdżona, która pozwoli nam znaleźć najlepszy split, w zależnosci od najlepszego zysku informacyjnego
          X_column = X[:, feat]
          thresholds = np.unique(X_column)
          for threshold in thresholds:
            gain = self._information_gain(y, X_column, threshold)
            if gain > best_gain:
                best_gain = gain
                best_feat = feat
                best_thresh = threshold
    return best_feat, best_thresh

    def _information_gain(self, y, X_column, threshold):
        parent_entropy = self._entropy(y)    #liczymy zysk informayjny, zaczynając od zysku parenta, przechodząc do child i na koniec odejmujemy, żeby dostać zysk
        left_idxs, right_idxs = self._split(X_column, threshold)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        n = len(y)
        n_left, n_right = len(left_idxs), len(right_idxs)
        entropy_left = self._entropy(y[left_idxs])
        entropy_right = self._entropy(y[right_idxs])

        child_entropy = (n_left / n) * entropy_left + (n_right / n) * entropy_right

        return parent_entropy - child_entropy

    def _split(self, X_column, split_threshold):
        left_idxs = np.argwhere(X_column <= split_threshold).flatten() #funkcja do zbudowania nowego węzła na podstawie znalezionej cechy
        right_idxs = np.argwhere(X_column > split_threshold).flatten()
        return left_idxs, right_idxs

    def _entropy(self, y):
        hist = np.bincount(y) #liczenie wartości entropii
        ps = hist / len(y)
        return -np.sum([p * np.log(p) for p in ps if p > 0])

    def _traverse_tree(self, x, node):
      pass

    def predict(self, X):
      return np.array([self._traverse_tree(x, self.root) for x in X])

