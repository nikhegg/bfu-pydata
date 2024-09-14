from PIL import Image, ImageDraw, ImageFont

width, height = 100, 100
color = (0,0,255,255)
arial = ImageFont.truetype("arial.ttf", 72)
for i in range(1,4):
    print(i)
    with Image.new("RGB", (width, height)) as image:
        draw = ImageDraw.Draw(image)
        draw.rectangle([0,0,width,5], fill=color)
        draw.rectangle([0,0,5,height], fill=color)
        draw.rectangle([0,height - 5, width, height], fill=color)
        draw.rectangle([width - 5, 0, width, height], fill=color)
        
        draw.text((width//2, height//2), str(i), fill=(255,0,0,255), anchor="mm", font=arial)
        image.show()
        image.save(f"card-{i}.png", "PNG")