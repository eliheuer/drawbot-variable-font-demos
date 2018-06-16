# Layout
size(1024, 1024)

# Fonts
font("fonts/Woodbine.ttf")
fontSize(170)
# Set axis from font
for axis, data in listFontVariations().items():
    print((axis, data))

# Variables using vanilla ui widgets.
Variable([
    dict(name="input_text", ui="EditText", args=dict(text='hello world')),
    dict(name="slider", ui="Slider", args=dict(value=100, minValue=100, maxValue=200)),
], globals())

print("Slider-:",int(slider))
print("Text---:",text)


gridpoints = [128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320, 336, 352, 368, 384]
canvas     = 512  # size of the gif in pixels
margin     = 128  # distance from edge of canvas 
num_frames =  16  # number of frames in the animation
step       =   0  # steps in looping animation


# draw the grid
fill(None)
stroke(0.5)
strokeWidth(1)
lineCap("round")
lineJoin("round")
  
# grid X-axis
stepx  = -16  # step in sequence on x axis             
incx   =  16  # grid increment
for x in range(17):
    save()
    stepx = stepx + incx
    polygon((margin + stepx, margin), (margin+stepx, canvas-margin))
    restore()
    
# grid Y-axis
stepy  = -16  # step in sequence on y axis 
incy   =  16  # grid increment
for y in range(17):
    save()
    stepy = stepy + incy
    polygon((margin, margin + stepy), (canvas-margin, margin+stepy))
    restore()


# Set variation 
fontVariations(wght=slider)
# draw text!
text(input_text, (100, 450))