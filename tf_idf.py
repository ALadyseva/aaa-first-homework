from collections import defaultdict
from typing import List
from math import log


class CountVectorizer():
    """ Converts a collection of strings to a matrix of token counts. """
    def __init__(self):
        self.keyword = []
        self.term_doc_matrix = []

    def fit_transform(self, corpus: List[list]) -> List[list]:
        """
        Transorms list of strings into term-document matrix.
        Parametres:
            -> corpus (list of strings).
        Output:
            -> matrix which consists of lists with amount of word reps;
               length of every list is equal to the length of keyword array.
        """
        self.keyword = []
        self.term_doc_matrix = []
        dicts_from_lines = []
        for line in corpus:
            temp_dict = defaultdict(int)
            for elem in line.lower().split():
                if elem not in self.keyword:
                    self.keyword.append(elem)
                temp_dict[elem] += 1
            dicts_from_lines.append(temp_dict)
        for i in range(len(corpus)):
            line_counter = []
            for kword in self.keyword:
                if kword in dicts_from_lines[i]:
                    line_counter.append(dicts_from_lines[i][kword])
                else:
                    line_counter.append(0)
            self.term_doc_matrix.append(line_counter)
        return self.term_doc_matrix

    def get_feature_names(self) -> list:
        """
        Returns array of keywords from all strings.
        If fit_transform has not been startes before, empty array is output.
        """
        return self.keyword


class TfidfTransformer():
    """
    Works with term-doc matrix. It can be list of documents/phrases.
    Output: matrix of tf-values, vector of idf-values and tf-idf matrix.
    """
    def tf_transform(self, matrix: List[list]) -> List[list]:
        """
        Returns matrix of tf-values.
        Parametres:
            -> matrix (list of lists with number of word reps).
        Output:
            -> matrix which consists of lists with tf-values.
        Calculation formula:
            -> number of word reps / amount of words in phrase.
        """
        tf_matrix = []
        for doc in matrix:
            tf_line = []
            for word in doc:
                tf = round(word / sum(doc), 3)
                tf_line.append(tf)
            tf_matrix.append(tf_line)
        return tf_matrix

    def idf_transform(self, matrix: List[list]) -> list:
        """
        Returns vector of idf-values.
        Parametres:
            -> matrix (list of lists with number of word reps).
        Output:
            -> list with of idf-values.
        Calculation formula:
            -> log((amount of docs + 1)/(amount of docs with a word + 1)) + 1
        """
        num_docs = len(matrix)
        idf_vector = []
        for j in range(len(matrix[0])):
            count = 0
            for doc in matrix:
                if doc[j]:
                    count += 1
            idf = log((num_docs + 1) / (count + 1)) + 1
            idf_vector.append(round(idf, 1))
        return idf_vector

    def fit_transform(self, matrix: List[list]) -> List[list]:
        """
        Returns matrix of tfidf-values.
        Parametres:
            -> matrix (list of lists with number of word reps).
        Output:
            -> matrix which consists of lists with tfidf-values.
        Calculation formula:
            -> tf * idf
        """
        tfidf_matrix = []
        tf_matrix = self.tf_transform(matrix)
        idf_vec = self.idf_transform(matrix)
        for tf_vec in tf_matrix:
            tfidf_vec = []
            for i, tf_i in enumerate(tf_vec):
                tfidf_vec.append(round(tf_i * idf_vec[i], 3))
            tfidf_matrix.append(tfidf_vec)
        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    """
    Works with list of lists. It can be list of documents/phrases.
    Inherited from CountVectorizer.
    """
    def __init__(self):
        super().__init__
        self.tfidf_matrix = TfidfTransformer()

    def fit_transform(self, corpus: List[list]) -> List[list]:
        """
        Returns matrix of tfidf-values.
        Parametres:
            -> matrix (list of documents/phrases).
        Output:
            -> matrix which consists of lists with tfidf-values.
        """
        doc_term_matrix = super().fit_transform(corpus)
        return self.tfidf_matrix.fit_transform(doc_term_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
