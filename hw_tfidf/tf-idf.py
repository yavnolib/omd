from typing import List, Dict
from collections.abc import Iterable
from numpy import log


class CountVectorizer:
    def __init__(self) -> None:
        self.vocabulary: Dict[str, int] = {}

    def fit_transform(self, data: list) -> List[list]:
        """
        Function to create document-term matrix
        using dictionary with features' names
        """

        assert isinstance(data, Iterable), "Not iterable"
        assert all(
            isinstance(i, str) for i in data
        ), "Only strings must be in data"
        index = 0
        dtm = []
        for string in data:
            string = self.clear_string(string)
            for word in string.split():
                if word not in self.vocabulary:
                    self.vocabulary[word] = index
                    index += 1
        for string in data:
            string = self.clear_string(string)
            row = [0] * len(self.vocabulary.keys())
            for word in string.split():
                row[self.vocabulary[word]] += 1
            dtm.append(row)

        return dtm

    def get_feature_names(self) -> List[str]:
        """
        Function to get features' names.
        """
        return list(self.vocabulary.keys())

    @staticmethod
    def clear_string(string: str) -> str:
        """
        Function to clear string.
        """
        return " ".join(
            [
                "".join([char for char in word if char.isalpha()])
                for word in string.split()
            ]
        ).lower()


class TfidfTransformer:
    def __init__(self):
        pass

    def tf_transform(self, data):
        """
        Function to count term frequency
        """
        assert isinstance(
            data, list
        ), "argument has wrong type: should be list"
        assert all(
            isinstance(i, list) for i in data
        ), "argument should contain only list"
        assert all(
            isinstance(num, int) for sublist in data for num in sublist
        ), "function can handle only integers"
        tf_matrix = []
        for row in data:
            summ = sum(row)
            tf_row = []
            for term in row:
                tf_row.append(round(term / summ, 3))
            tf_matrix.append(tf_row)
        return tf_matrix

    def idf_transform(self, data):
        """
        Function to get idf_vector
        """
        idf_vector = []
        docs_num = len(data)

        for el in zip(*data):
            idf_vector.append(
                round(
                    log((docs_num + 1) / (sum([bool(i) for i in el]) + 1)) + 1,
                    3,
                )
            )

        return idf_vector

    def fit_transform(self, data):
        """
        Function to apply tf-idf to data
        """
        assert isinstance(data, list), "Type of data is not list."
        assert all(
            isinstance(i, list) for i in data
        ), "Elements of data must be list."
        assert all(
            isinstance(num, int) for sublist in data for num in sublist
        ), "Elements of data must contain olny integers."
        result = []
        tf = self.tf_transform(data)
        idf = self.idf_transform(data)

        for row in tf:
            result.append([round(a * b, 3) for a, b in zip(idf, row)])
        return result


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform(self, data: list) -> List[list]:
        """
        Function to apply CountVectorizer and tf-idf to data
        """
        count_matrix = super().fit_transform(data)
        return self.tf_idf.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
