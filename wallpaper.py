import os
import ctypes

name_of_file = 'color.png'
path_to_file = os.path.realpath(name_of_file) # Returns the canonical path

print(path_to_file) # this printa C:\Users\WORK\Desktop\projects\wallpaper\wallpaper\color.png
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)