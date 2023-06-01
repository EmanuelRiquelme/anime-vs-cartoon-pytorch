import torch
from torch.utils.data import Dataset
from  torchvision import transforms
import os
from PIL import Image

transform = transforms.Compose([
            transforms.PILToTensor(),
            transforms.ConvertImageDtype(torch.float),
            transforms.Resize((192,192)),
            transforms.Normalize(mean = (.5,.5,.5),std = (.5,.5,.5))
])

def clear(root_dir = 'data',transform = transform):
    sub_dirs = [file for file in os.listdir(f'{root_dir}/Anime')]
    files = []
    for sub_dir in sub_dirs:
        files.extend(f'{root_dir}/Anime/{sub_dir}/{file}' for file in os.listdir(f'{root_dir}/Anime/{sub_dir}'))
    sub_dirs = [file for file in os.listdir(f'{root_dir}/Cartoon')]
    for sub_dir in sub_dirs:
        files.extend(f'{root_dir}/Cartoon/{sub_dir}/{file}' for file in os.listdir(f'{root_dir}/Cartoon/{sub_dir}'))
    for file in files:
        try:
            transform(Image.open(file))
        except:
            print(file)
            os.remove(file)

if __name__ == '__main__':
    clear()
