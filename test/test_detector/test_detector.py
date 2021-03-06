from io import BytesIO

import numpy as np
import pytest
import requests

from src.detector.detector import TensorflowHubDetector
from src.detector.detector import TensorflowHubModel


@pytest.fixture(scope='class')
def image():
    url = "https://images.unsplash.com/photo-1532362996300-fbce5a30bd6d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"

    return BytesIO(requests.get(url).content)


@pytest.mark.usefixtures('image')
class TestTensorflowHubDetector:

    def test_load_hub_model(self):
        """
        Check's that the hub model loads correctly.
        """
        # FIXME: High memory usage on test
        ssd_net = TensorflowHubDetector(TensorflowHubModel.SSDMobilNetV2)
        ssd_net.load_detector()

        assert ssd_net.detector

    def test_preprocess_function_makes_tensorflow_ready_image(self,
                                                              image: BytesIO):
        """
        Check's that the preprocess_image method correctly returns a tensorflow
        type.
        Returns:

        """
        ssd_net = TensorflowHubDetector(TensorflowHubModel.SSDMobilNetV2)
        ssd_net.load_detector()
        assert isinstance(ssd_net.preprocess_image(image), np.ndarray)

    def test_detection_with_byte_io_success(self, image:BytesIO):
        """
        Check's that a BytesIO image data can be be detected on.
        Args:
            image: BytesIO interfaced image data.

        Returns:

        """
        ssd_net = TensorflowHubDetector(TensorflowHubModel.SSDMobilNetV2)
        ssd_net.load_detector()

        assert ssd_net.detect(image)