from PIL import Image
im = Image.open("Nitro_Wallpaper_5000x2813.jpg")
print(im.format,im.size,im.seek(5),im.tell)