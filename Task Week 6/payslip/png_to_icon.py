from PIL import Image

logo = Image.open(r"C:\Users\yatim\Documents\YoShop\Task Week 6\banner_logo.png")

logo.save(r"C:\Users\yatim\Documents\YoShop\Task Week 6\banner_logo_40.ico", format='ICO',
		sizes=[(40, 40)])
