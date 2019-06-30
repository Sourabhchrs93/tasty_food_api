from flask_restful import Resource
from flask import request
from services.random_sample import sample
# import _pickle as pkl

import json


class FetchTopReviews(Resource):
    def __init__(self):
        # self.file = open("sample_review.p", 'rb')
        # self.reviews = pkl.load(self.file)
        pass

    def post(self):
        queries = json.loads(request.data.decode('utf-8'))['data']

        query_length = len(queries)

        k = int(request.args.get("k", 20))
        sample_reviews = sample.get_sample()
        # sample_reviews = self.reviews
        top_k = []
        queries_set = set()
        for word in queries:
            queries_set.add(word.lower())
        for index, review in enumerate(sample_reviews):
            review_set = review['review/text1']
            review_score = review['review/score']

            diff_set = queries_set - review_set
            score = query_length - len(diff_set)

            top_k = self.insert_ele(top_k, k, (index, score/query_length, review_score))

        print(top_k)
        output = []
        for ki in top_k:
            out_doc = dict()
            out_doc['_id'] = sample_reviews[ki[0]]['_id']
            out_doc['product/productId'] = sample_reviews[ki[0]]['product/productId']
            out_doc['review/userId'] = sample_reviews[ki[0]]['review/userId']
            out_doc['review/profileName'] = sample_reviews[ki[0]]['review/profileName']
            out_doc['review/helpfulness'] = sample_reviews[ki[0]]['review/helpfulness']
            out_doc['review/score'] = sample_reviews[ki[0]]['review/score']
            out_doc['review/time'] = sample_reviews[ki[0]]['review/time']
            out_doc['review/summary'] = sample_reviews[ki[0]]['review/summary']
            out_doc['review/text'] = sample_reviews[ki[0]]['review/text']

            output.append(out_doc)

        return output

    def insert_ele(self, sorted_listed, k, n):
        # Searching for the position
        i = 0
        while i < len(sorted_listed):
            if sorted_listed[i][1] <= n[1]:
                break
            i += 1

        while i < len(sorted_listed) and sorted_listed[i][1] == n[1]:
            if sorted_listed[i][2] <= n[2]:
                break
            i += 1

        # Inserting n in the list
        sorted_listed = sorted_listed[:i] + [n] + sorted_listed[i:]

        if len(sorted_listed) > k:
            return sorted_listed[:k]
        return sorted_listed
