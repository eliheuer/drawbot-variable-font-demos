# Layout
size(1024, 512)

# Fonts
font("Skia")
fontSize(200)
# Set axis from font
for axis, data in listFontVariations().items():
    print((axis, data))

# Set variation 
fontVariations(wght=3)
# draw text!
text("Test", (100, 100))

# Set variation
fontVariations(wght=1, wdth=.8)
# draw text!
text("Test", (100, 300))