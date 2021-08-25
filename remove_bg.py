import numpy as np
from PIL import Image
import pixellib
from pixellib.tune_bg import alter_bg

def remove_background(input_path):
    print('\n')
    img_file = Image.open(input_path)
    img_file.save('inputs\modified_img.jpg')
    change_bg = alter_bg()
    change_bg.load_pascalvoc_model('deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')
    output_path = 'outputs\only_object.jpg'
    change_bg.color_bg('inputs\modified_img.jpg', colors=(255, 255, 255), output_image_name=output_path)
    return output_path

print('\n\nYour file is saved at: ', remove_background(input('\n\nEnter the image file path: ')))
input('Press enter to exit')
