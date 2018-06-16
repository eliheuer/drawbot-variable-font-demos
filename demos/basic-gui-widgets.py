# Layout
size(1024, 512)

# Fonts
font("fonts/Woodbine.ttf")
fontSize(200)
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

# Set variation 
fontVariations(wght=slider)
# draw text!
text(input_text, (100, 100))
