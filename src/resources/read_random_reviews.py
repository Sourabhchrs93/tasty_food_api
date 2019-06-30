from flask_restful import Resource
from flask import request
from services.random_sample import sample


class CreateSampleReviews(Resource):
    def __init__(self):
        self.input_file = 'finefoods.txt'

    def get(self):
        limit = int(request.args.get("limit", 20))
        reviews_count = sample.create_sample_from_txt(limit)
        return reviews_count


class GetTestSample(Resource):
    def __init__(self):
        pass

    def get(self):
        sample_list = sample.get_sample()
        if len(sample_list) == 0:
            return 'generate samples first', 400

        out = []
        for samples in sample_list[:20]:
            out_doc = dict()
            out_doc['_id'] = samples['_id']
            out_doc['product/productId'] = samples['product/productId']
            out_doc['review/userId'] = samples['review/userId']
            out_doc['review/profileName'] = samples['review/profileName']
            out_doc['review/helpfulness'] = samples['review/helpfulness']
            out_doc['review/score'] = samples['review/score']
            out_doc['review/time'] = samples['review/time']
            out_doc['review/summary'] = samples['review/summary']
            out_doc['review/text'] = samples['review/text']
            out.append(out_doc)
        return out

