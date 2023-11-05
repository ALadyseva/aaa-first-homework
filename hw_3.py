from collections import defaultdict


class CountVectorizer:
    """Converts a collection of strings to a matrix of token counts."""
    def __init__(self):
        self.keyword = []
        self.term_doc_matrix = []

    def fit_transform(self, corpus: list):
        """Transorms list of strings into term-document matrix."""
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

    def get_feature_names(self):
        """Returns array of keywords from all strings."""
        return self.keyword


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
    print(vectorizer.get_feature_names())
