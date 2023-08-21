pip install pyyaml==5.2
pip install scipy
pip install numpy
pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113

import torch
print(torch.__version__)
import yaml, scipy, os
print(yaml.__version__)
print(scipy.__version__)