from flask_restful import Resource
from flask import request
from services.random_sample import sample


class CreateSampleReviews(Resource):
    def __init__(self):
        self.input_file = 'finefoods.txt'

    def get(self):
        limit = int(request.args.get("limit", 20))
        reviews_count = sample.random_sampler(limit)
        return reviews_count


class GetSampleSize(Resource):
    def __init__(self):
        pass

    def get(self):
        sample_list = sample.get_sample()
        if len(sample_list) == 0:
            return 'generate samples first', 400
        return sample_list[:20]

