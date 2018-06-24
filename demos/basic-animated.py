# Render this specimen with DrawBot3: http://www.drawbot.com/ 

# Import modules:
import math

# Basic variables:
W, H, M, F = 1024, 1024, 128, 32

# Load font and print font info:
font("fonts/WoodbineGX.ttf")
for axis, data in listFontVariations().items():
    print((axis, data)) # Get axis info from font

# Draw a grid from given increment:
def grid(inc):
    stroke(0.6, 0, 0)           # Set grid line color
    stpX, stpY = 0, 0     # Step in sequence on x axis             
    incX, incY = inc, inc # Grid increment
    for x in range(13):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX      # Set position for next gridline
    for y in range(13*4):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY/4      # Set position for next gridline

# Page loop
for frame in range(24):
    newPage(W, H)
    fill(0) # Background color
    rect(0, 0, W, H) # Draw the background
    fill(0) # Background color
    rect(0, 0, W-257, H) # Draw the background
    rect(0, (256+128)+1, W, H) # Draw the background
    
    # Draw the grid
    # grid(64)
    
    stroke(None)
    fill(1) # White fill color


    varAnim = (((cos(frame/4))+1)/2)
    print("varAnim=", varAnim)

    for i in range(6):
        # Set variations
        # varWght = 100+(i*10)
        varWght = 100 
        fontVariations(wght=varWght)
        
        # Draw headline text
        font("fonts/WoodbineGX.ttf")
        fontSize(128)
        text("LANGUAGE", (M+(M-40), (785)-(i*128)))
        
        # Draw secondary text
        font("Helvetica-Light")
        fontSize(24)
        text("400", (M+664, (785)-(i*128)))

saveImage("basic-animated.gif")