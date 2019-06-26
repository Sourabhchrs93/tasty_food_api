import random


class Sample:
    def __init__(self, filename):
        self.sample_list = []
        self.filename = filename

    def random_sampler(self, k):
        self.sample_list = []
        with open(self.filename, 'rb') as f:
            f.seek(0, 2)
            filesize = f.tell()
            random_set = sorted(random.sample(range(filesize), k))
            count = 0
            for i in range(k):
                f.seek(random_set[i])
                # Skip current line (because we might be in the middle of a line.
                f.readline()
                # Append the next line to the sample set
                new_line = str(f.readline())
                while 'product/productId:' not in new_line:
                    new_line = str(f.readline())
                doc = dict()
                doc['_id'] = count
                doc['product/productId'] = new_line.split("product/productId: ", 1)[-1][:-3]
                doc['review/userId'] = str(f.readline()).split("review/userId: ", 1)[-1][:-3]
                doc['review/profileName'] = str(f.readline()).split("review/profileName: ", 1)[-1][:-3]
                doc['review/helpfulness:'] = str(f.readline()).split("review/helpfulness: ", 1)[-1][:-3]
                doc['review/score'] = str(f.readline()).split("review/score: ", 1)[-1][:-3]
                doc['review/time'] = str(f.readline()).split("review/time: ", 1)[-1][:-3]
                doc['review/summary'] = str(f.readline()).split("review/summary: ", 1)[-1][:-3]
                doc['review/text'] = str(f.readline()).split("review/text: ", 1)[-1][:-3]

                self.sample_list.append(doc)
                count += 1

        return len(self.sample_list)

    def get_sample(self):
        return self.sample_list


sample = Sample('finefoods.txt')