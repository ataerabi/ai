import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image
#scipy.imageio.imread
from skimage.segmentation import clear_border
from skimage.morphology import label
from skimage.measure import regionprops


#image = imread('./page.png',1)
image = Image.open('./page.png')

#apply threshold in order to make the image binary
bw = image < 120

# remove artifacts connected to image border
cleared = bw.copy()
clear_border(cleared)

# label image regions
label_image = label(cleared,neighbors=8)
borders = np.logical_xor(bw, cleared)
label_image[borders] = -1

print (label_image.max())

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(16, 16))
ax.imshow(bw, cmap='jet')



for region in regionprops(label_image):
    # skip small images
    if region.area > 50:
    
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

plt.show()
