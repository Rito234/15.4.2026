from PIL import Image, ImageDraw


image = Image.new("RGB", (400, 400), "white")


draw = ImageDraw.Draw(image)
for x in range(20, 120, 20):
    draw.ellipse((300-x, 100-x, 300+x, 100+x),  outline="black", width=1)
draw.ellipse((300,100,300,100), outline="black", width=3)
for x in range(0, 200,20):
    draw.line((0, 201, x, 0), fill="blue", width=1)
for x in range(-1,200,20):
    draw.line((200, 200, 200-x, 0), fill="red", width=1)
for x in range(0, 200, 20):
    for y in range(200, 400, 20):
        if x//20%2 == y//20%2:
            draw.rectangle((x, y, x+20, y+20), fill="cyan", outline="black", width=1)
        else:
            draw.rectangle((x, y, x+20, y+20), fill="magenta", outline="black", width=1)
draw.rectangle((200, 200, 220, 220), fill="yellow", outline="black", width=1)
draw.rectangle((220, 220, 240, 240), fill="yellow", outline="black", width=1)
draw.rectangle((240, 240, 260, 260), fill="yellow", outline="black", width=1)
draw.rectangle((260, 260, 280, 280), fill="yellow", outline="black", width=1)
draw.rectangle((280, 280, 300, 300), fill="yellow", outline="black", width=1)
draw.rectangle((300, 300, 320, 320), fill="yellow", outline="black", width=1)
draw.rectangle((320, 320, 340, 340), fill="yellow", outline="black", width=1)
draw.rectangle((340, 340, 360, 360), fill="yellow", outline="black", width=1)
draw.rectangle((360, 360, 380, 380), fill="yellow", outline="black", width=1)
draw.rectangle((380, 380, 400, 400), fill="yellow", outline="black", width=1)
draw.rectangle((380, 200, 400, 220), fill="cyan", outline="black", width=1)
draw.rectangle((360, 220, 380, 240), fill="cyan", outline="black", width=1)
draw.rectangle((340, 240, 360, 260), fill="cyan", outline="black", width=1)
draw.rectangle((320, 260, 340, 280), fill="cyan", outline="black", width=1)
draw.rectangle((300, 280, 320, 300), fill="cyan", outline="black", width=1)
draw.rectangle((280, 300, 300, 320), fill="cyan", outline="black", width=1)
draw.rectangle((260, 320, 280, 340), fill="cyan", outline="black", width=1)
draw.rectangle((240, 340, 260, 360), fill="cyan", outline="black", width=1)
draw.rectangle((220, 360, 240, 380), fill="cyan", outline="black", width=1)
draw.rectangle((200, 380, 220, 400), fill="cyan", outline="black", width=1)


    


image.show("white_canvas.png")


