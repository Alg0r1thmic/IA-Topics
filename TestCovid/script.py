from PIL import Image
j=1
for i in range(20):
    im = Image.open("test"+str(j)+".png").convert("RGB")
    im.save("test+"+str(j)+".jpg","jpeg")
    j=j+1