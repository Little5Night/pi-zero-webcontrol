
from PIL import Image, ImageDraw
# from waveshare_lcd import LCD_1inch3 # Waveshare library installieren!

class LCDDisplay:
    def __init__(self):
        # self.lcd = LCD_1inch3()
        # self.lcd.init()
        pass

    def show_status(self, devices):
        image = Image.new("RGB", (240, 240), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        y = 10
        for name, dev in devices.items():
            draw.text((10, y), f"{name}: {dev['state']}", fill=(255,255,255))
            y += 20
        # self.lcd.ShowImage(image)
