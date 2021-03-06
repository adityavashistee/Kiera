
from skimage import io
from skimage.transform import resize
from scipy import misc
import numpy as np
import glob
import os
from configparser import ConfigParser


class Sampler:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
            os.sep +
            'config' +
            os.sep +
            'appConfig.ini')
        self.score = 0
        self.input_data = None
        self.out_labels = None

    def read_and_process_images(self, location):
        output_labels = []
        input_data = []
        for filename in glob.glob(location):
            # print(filename.split('/'))
            im = io.imread(filename)
            img_size = int(self.config['img']['frame_size'])
            g = resize(im, (img_size, img_size), mode='reflect')
            #save_name = '/home/rachit/project/resizeImage/' + filename.split('/')[6]
            output_labels.append(int(filename.split('/')[6].split('_')[1]) - 1)
            input_data.append(g)
            #misc.imsave(save_name, g)
        self.input_data = np.array(input_data)
        self.out_labels = np.array(output_labels)
        # return np.array(input_data), np.array(output_labels)

    def get_images_and_labels(self):
        return self.input_data, self.out_labels

    def process_image(self, im):
        img_size = int(self.config['img']['frame_size'])
        return np.array(resize(im, (img_size, img_size), mode='reflect'))
