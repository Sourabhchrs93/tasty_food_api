from flask_restful import Resource
import services.random_sample as rs


class CreateSampleReviews(Resource):
    def __init__(self):
        self.input_file = 'finefoods.txt'

    def get(self):
        global sample_reviews
        sample_reviews = rs.random_sampler(self.input_file, 100000)
        return len(sample_reviews)


class GetSampleSize(Resource):
    def __init__(self):
        pass

    def get(self):
        global sample_reviews
        try:
            len(sample_reviews)
        except Exception as e:
            return 'generate samples first', 400
        return sample_reviews
