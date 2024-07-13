from skimage import io
import imexam
img = io.imread('SamplePhoto.jpeg')
viewer = imexam.econnect()   # this will begin 'ds9' on the background
viewer.view(img[:,:,0])      # display only the first channel (i.e., "R" channel)
# Then, using the middle mouse button to pan and mouse wheel to zoom onto a star
viewer.imexam()              # this will begin an imexam session. use options displayed on the screen
# press 'j' will show a Gaussian fit along the line, 'k' along the column
# 'r' will be useful to display a radial profile but prone to crash with an error
# 'a' will do a quick aperture photometry that gives a brightness measurement (record "flux" value).
