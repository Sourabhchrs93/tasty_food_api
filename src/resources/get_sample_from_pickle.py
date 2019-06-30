from flask_restful import Resource
from services.random_sample import sample


class GetSampleFromPickle(Resource):
    def __init__(self):
        self.input_file = 'finefoods.txt'

    def get(self):

        return sample.load_sample_pickle_file(), 200
