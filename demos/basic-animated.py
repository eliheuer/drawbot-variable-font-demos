# Render this specimen with DrawBot3: http://www.drawbot.com/

# Import modules:
import math

# Basic variables:
W, H, M, F = 1024, 1024, 128, 32

# Load font and print font info:
# print(installedFonts(supportsCharacters=None))
font("fonts/WoodbineGX.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))  # Get axis info from font


# Draw a grid from a given increment:
def grid(inc):
    stroke(0.6, 0, 0)  # Set grid line color
    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    for x in range(13):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX  # Set position for next gridline
    for y in range(13*4):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY/4  # Set position for next gridline


# Page loop
for frame in range(48):
    newPage(W, H)
    fill(0)           # Background color
    rect(0, 0, W, H)  # Draw the background

    # Draw the grid
    # grid(64)

    # Basic Style
    stroke(None)
    fill(1)

    # Calculate the weight, stepping through 360 degrees by frames
    angle = (frame/48)*360
    varAnim = (cos(radians(angle))*0.5+0.5)*100
    print("frame = ", frame)
    print("angle = ", angle)
    print("varAnim = ", varAnim)
    print(" ")

    # Set variations
    varWght = 100+varAnim
    fontVariations(wght=varWght)

    # Iterate through weight
    for i in range(6):
        # Draw headline text
        fill(1)
        font("fonts/WoodbineGX.ttf")
        fontSize(128)
        text("LANGUAGE", (M-2, (785)-(i*128)))

        # Draw secondary text
        fill(1, 0, 0)
        font("InputMonoCompressed-Light")
        fontSize(128)
        text(str(int(varWght)), ((W-64)-(M*2), (((H+16)-(M*2)))-(i*128)))

# Save GIF
saveImage("basic-animated.gif")
