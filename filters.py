'''
@author: Hongwei Shao
'''

import numpy as np
import pydicom
import scipy

def resample(pixels, slices, new_spacing=[1.0, 1.0, 1.0]):
    spacing = np.array([slices[0].SliceThickness] + slice[0].PixelSpacing, dtype=np.float32)

    resize_factor = spacing / new_spacing
    new_real_shape = pixels.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / pixels.shape
    new_spacing = spacing / real_resize_factor

    pixels = scipy.ndimage.interpolation.zoom(pixels, real_resize_factor, mode='nearest')

    return pixels, new_spacing

    if __name__ == "__main__":
        pass