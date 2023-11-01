"""
    Implementation of CountVectorizer
"""
from typing import Dict, Iterable, List, Set


class CountVectorizer:
    """
    CountVectorizer class
    """

    def __init__(self):
        self.vocab = None
        self.processed_docs = None

    def fit_transform(self, raw_documents: Iterable):
        """
        Fit on raw_documents and return document-term matrix
        """
        docs_is_string = self.get_vocabulary(raw_documents)
        assert self.vocab is not None
        assert self.processed_docs is not None

        counter_tmp: Dict = {k: 0 for k in self.vocab}
        feature_names = self.get_feature_names()
        assert feature_names is not None

        if docs_is_string:
            for word in self.processed_docs:
                counter_tmp[word] += 1

            arr = list(feature_names)
            for ind, word in enumerate(arr):
                arr[ind] = counter_tmp[word]
            data = arr
        else:
            data = []
            for doc in self.processed_docs:
                counter = dict(counter_tmp)
                for word in doc:
                    counter[word] += 1
                arr = list(feature_names)
                for j, word in enumerate(arr):
                    arr[j] = counter[word]
                data.append(list(arr))
        return data

    def get_feature_names(self):
        """
        Get output feature names for transformation.
        """
        return self.vocab if self.vocab is not None else []

    @staticmethod
    def process_str(line: str) -> List[str]:
        """
        Function to remove delimeters from string
        """
        line = line.lower()
        delims = """!()-—[]{};?@#$%:'"\\,./^&;*_\n\t\r\b """
        new_l = line
        for delim in delims:
            new_l = new_l.replace(delim, " ")
        return new_l.split()

    def get_vocabulary(self, raw_documents: Iterable) -> int:
        """
        Get vocabulary from raw_documents

        return status: 1 if raw_documents is str else 0
        """
        if not isinstance(raw_documents, Iterable):
            raise TypeError('"raw_documents" is not iterable')

        vocab: Set[str] = set()
        _process = self.__class__.process_str
        if isinstance(raw_documents, str):
            self.processed_docs = _process(raw_documents)
            vocab |= set(self.processed_docs)
            status = 1
        else:
            status = 0
            self.processed_docs = []
            for document in raw_documents:
                doc_proc = _process(document)
                self.processed_docs.append(doc_proc)
                vocab |= set(doc_proc)
        self.vocab = list(vocab)
        return status


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    if isinstance(corpus, list):
        for i in count_matrix:
            print(list(zip(vectorizer.get_feature_names(), i)))
    else:
        print(list(zip(vectorizer.get_feature_names(), count_matrix)))
