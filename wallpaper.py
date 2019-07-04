import os
import ctypes
import imagescrape


name_of_file = imagescrape.Scape()
path_to_file = os.path.realpath(name_of_file) # Returns the canonical path

print(path_to_file) # this printasC:\Users\WORK\Desktop\projects\wallpaper\wallpaper\color.png
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)