import _pickle as pkl


class Sample:
    def __init__(self, filename):
        self.sample_list = []
        self.filename = filename

    def create_sample_from_txt(self, k):
        self.sample_list = []
        count = 0
        with open(self.filename, 'rb') as f:
            while count < k:
                new_line = str(f.readline())
                while 'product/productId:' not in new_line:
                    new_line = str(f.readline())
                doc = dict()
                doc['_id'] = count
                doc['product/productId'] = new_line.split("product/productId: ", 1)[-1][:-3]
                doc['review/userId'] = str(f.readline()).split("review/userId: ", 1)[-1][:-3]
                doc['review/profileName'] = str(f.readline()).split("review/profileName: ", 1)[-1][:-3]
                doc['review/helpfulness'] = str(f.readline()).split("review/helpfulness: ", 1)[-1][:-3]
                doc['review/score'] = float(str(f.readline()).split("review/score: ", 1)[-1][:-3])
                doc['review/time'] = str(f.readline()).split("review/time: ", 1)[-1][:-3]
                doc['review/summary'] = str(f.readline()).split("review/summary: ", 1)[-1][:-3]
                doc['review/text'] = str(f.readline()).split("review/text: ", 1)[-1][:-3]
                doc['review/text1'] = set()
                review = doc['review/summary'] + " " + doc['review/text']

                review_length = len(review)
                review_index = 0
                word = ''
                while review_index < review_length:
                    # search in list of special chars. we might get something like 'good.'
                    if review[review_index] not in ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                                                    '_', '-', '+', '=', '{', '[', '}', '}', '|', '\\', ':', ';',
                                                    '"', "'", '<', ',', '>', '.', '?', '/', ' ']:
                        word += review[review_index]
                    else:
                        word = word.lower()
                        doc['review/text1'].add(word)
                        word = ''
                    review_index += 1

                self.sample_list.append(doc)
                count += 1

        filehandler = open('sample_review.p', 'wb')
        pkl.dump(self.sample_list, filehandler)
        filehandler.close()

        return len(self.sample_list)

    def get_sample(self):
        return self.sample_list

    def load_sample_pickle_file(self):
        file = open("sample_review.p", 'rb')
        self.sample_list = pkl.load(file)
        return {"message": "sample loaded"}


sample = Sample('finefoods.txt')