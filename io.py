'''
@author: Hongwei Shao
'''

import os
import numpy as np
import pydicom
import vtk

def load_scan(path):
    slices = [pydicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x : float(x.ImagePositionPatient[2]))

    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness

    return slices

def get_pixels(slices):
    image = np.stack([s.pixel_array for s in slices])
    image = image.astype(np.int16)

    for i in range(len(slices)):
        if not hasattr(slices[i], 'RescaleIntercept'):
            continue
    
        intercept = slices[i].RescaleIntercept
        slope = slices[i].RescaleSlope

        if slope != 1:
            image[i] = slope * image[i].astype(np.float64)
            image[i] = image[i].astype(np.int16)

        image[i] += np.int16(intercept)

        return np.array(image, dtype=np.int16)

if __name__ == "__main__":
    pass