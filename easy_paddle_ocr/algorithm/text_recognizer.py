import shutup; shutup.please()
from ..tools.infer.predict_rec import TextRecognizer as PaddleTextRecognizer
from ..tools.infer import utility
import os


class TextRecognizer:
    def __init__(self, weights=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'weights'), image_shape='3, 32, 320', algorithm='CRNN', device='cpu'):
        args = utility.parse_args()
        args.rec_model_dir = weights
        args.rec_image_shape = image_shape
        args.rec_char_dict_path = os.path.join(weights, 'dictionary.txt')
        args.use_gpu = device == 'gpu'
        args.rec_algorithm = algorithm
        self.recognizer = PaddleTextRecognizer(args)

    def read(self, image):
        result, _ = self.recognizer([image])
        text, confidence = result[0]
        prediction = {
            'text': text,
            'confidence': confidence
        }
        return prediction