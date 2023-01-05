# Lint as: python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""Example using PyCoral to classify a given image using an Edge TPU.

To run this code, you must attach an Edge TPU attached to the host and
install the Edge TPU runtime (`libedgetpu.so`) and `tflite_runtime`. For
device setup instructions, see coral.ai/docs/setup.

Example usage:
```
bash examples/install_requirements.sh classify_image.py

python3 examples/classify_image.py \
  --model test_data/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite  \
  --labels test_data/inat_bird_labels.txt \
  --input test_data/parrot.jpg
```
"""

import argparse
import time

import numpy as np
from PIL import Image
from pycoral.adapters import classify
from pycoral.adapters import common
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter


class Model:
  def __init__(self):
    self.model_path ="model.tflite" 
    self.labels_path="labels.txt" 
    self.labels = read_label_file(self.labels_path) 
    self.interpreter =make_interpreter(self.model_path)
    self.interpreter.allocate_tensors()


def predict(self, img):
  common.set_input(self.interpreter, img)
  self.interpreter.invoke()
  classes = classify.get_classes(self.interpreter, 1, 0)
  for c in classes:
    print('%s: %.5f' % (self.labels.get(c.id, c.id), c.score))



def main():
  image_path = "images/dog.jpg"
  image = Image.open(image_path).convert('RGB')
  model = Model()
  model.predict(image)
 
if __name__ == '__main__':
  main()
