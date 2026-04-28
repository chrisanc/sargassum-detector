import torch
from torch.utils.data import Dataset
import rasterio
"""
Script used to define a dataset of images and labels for classification purposes.
"""
class SatelitalImages(Dataset):
    def __init__(self, paths: list[str], labels: list[str]):
        super().__init__()
        self.__paths = paths
        self.__labels = labels
        
    
    def __len__(self):
        return len(self.__paths)
    
    
    def __getitem__(self, index) -> tuple[torch.tensor, str]:
        image = self.__normalize_tensor(
            self.__extract_tensor(self.__paths[index])
        )
        label = self.__labels[index]
        
        return image, label
        
        
    def __normalize_tensor(self, tensor) -> torch.tensor:
        """
        Applies the min-max normalization to the dataset
        Avoid weird behavior on the data treatment by making every
        data in the same range of values
        """
        return (tensor - tensor.min()) / (tensor.max() - tensor.min())
    
    
    def __extract_tensor(self, path: str) -> torch.tensor:
        
        """
        Loads a .tiff image and parse it into a tensor
        """
        with rasterio.open(path) as file:
            arr = file.read()
            tensor = torch.tensor(arr)
        return tensor