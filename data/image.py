"""
Image Pack

Upload an image to telegram and retrieve this image's id and save here your image's id to send it
Or, you can store your images on './assets' directory and save here filename with directory, so you can fast declare
your image without showing full directory on your codes!

Be precise and don't trash your beautiful codes! - A.Sakhib
"""

class Image:
    images = 'assets/images'

    # Logo of BSBA as an example import
    logo = open(images+'logo.png', 'rb')