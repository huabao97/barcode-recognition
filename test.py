import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
import torch
import torchvision
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name())
print(torch.cuda.current_device())
