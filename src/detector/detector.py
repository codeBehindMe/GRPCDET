from abc import ABCMeta
from abc import abstractmethod
import tensorflow as tf
import tensorflow_hub as hub
from enum import Enum

class IDetector:

    @abstractmethod
    def detect_image(self, img: object) -> tf.Tensor:
        pass

    @abstractmethod
    def load_detector_to_memory(self):
        pass

class TensorflowHubModel(Enum):
    CenterNetHourGlass512x512 = "https://tfhub.dev/tensorflow/centernet/hourglass_512x512/1"

class TensorflowHubDetector(IDetector):

    def __init__(self, model: TensorflowHubModel):
        self.model = model
        self.detector = None

    def _load_model(self, model: TensorflowHubModel) -> object:
        return hub.load(model.value)

    def detect_image(self, img: object) -> tf.Tensor:
        raise NotImplementedError() 

    def load_detector_to_memory(self):
        self.detector = self._load_model(self.model)

