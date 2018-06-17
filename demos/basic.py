# Layout
size(1024, 512)

# gird variables
origin = (32, 32)
height = 256
width = 768
center = width/2
num_x_units = 24
num_y_units = 16
gut = 8 
col = 25
col_num = 8

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(0.5)
    stroke(0.9, 0.1, 0.1, 0.7)  
    fill(None)

    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
        
    step_col = 0 
    stroke(0.1, 0.1, 0.9, 0.7)
    for column in range(8): 
        rect(step_col, 0, col, height)
        step_col += (col + gut)


# newpage
fill(0.7) # color of background
rect(0, 0, 1024, 512) # draw the background

#fill(0.8, 0.8, 0.8)
#stroke(None)
#rect(0, 0, 288, 216)

# translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# Debug 
x, y, w, h = 0, 0, ((col * 8)+(gut *7)), 173

# Fonts
font("fonts/WoodbineGX.ttf")
fontSize(160)
# Set axis from font
for axis, data in listFontVariations().items():
    print((axis, data))

# Set variation 
fontVariations(wght=100)
# draw text!
text("LANGUAGE", (64, 256))

# Set variation 
fontVariations(wght=200)
# draw text!
text("LANGUAGE", (64, 128))
