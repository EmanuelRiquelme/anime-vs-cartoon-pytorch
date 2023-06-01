import torch
from torch.utils.data import Dataset
from  torchvision import transforms
import os
from PIL import Image

class Anime_Cartoons(Dataset):
    def __init__(self,root_dir = 'data',transform = None):
        self.root_dir = root_dir
        self.transform = transform if transform else transforms.Compose([
            transforms.PILToTensor(),
            transforms.ConvertImageDtype(torch.float),
            transforms.Resize((192,192)),
        ])
    def __files__(self):
        sub_dirs = [file for file in os.listdir(f'{self.root_dir}/Anime')]
        img_names = []
        for sub_dir in sub_dirs:
            img_names.extend(f'{self.root_dir}/Anime/{sub_dir}/{file}' for file in os.listdir(f'{self.root_dir}/Anime/{sub_dir}'))
        sub_dirs = [file for file in os.listdir(f'{self.root_dir}/Cartoon')]
        for sub_dir in sub_dirs:
            img_names.extend(f'{self.root_dir}/Cartoon/{sub_dir}/{file}' for file in os.listdir(f'{self.root_dir}/Cartoon/{sub_dir}'))
        return img_names

    def __len__(self):
        return len(self.__files__())

    def __getitem__(self,idx):
        file_name = self.__files__()[idx]
        label = torch.tensor(0) if file_name.split('/')[1] == 'Anime' else torch.tensor(1)
        img = self.transform(Image.open(file_name))
        return img,label
