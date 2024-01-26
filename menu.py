import customtkinter
from PIL import Image
from vars import *

def DrawBannerHeight():
    MenuBannerHeight = int(app_height * 0.09)
    return MenuBannerHeight

def DrawBannerYCoord():
    MenuBannerYCoord = int(app_height * 0.5596) - safezoneSizeY
    return MenuBannerYCoord

def DrawBGWidth():
    MenuBGWidth = int(app_width * GtaMenuBGWidth) # Convertido para a resolução do app.
    return MenuBGWidth

def DrawBGLenght():
    # Comprimento conforme o número de opções.
    GtaMenuBGLenght = NumberOfOptions * GtaMenuBGHeight
    MenuBGLenght = int(app_height * GtaMenuBGLenght)
    return MenuBGLenght

def DrawBGYCoord():
    # Background Y Coord.
    bg_y_calc = NumberOfOptions * GtaMenuBGHeight
    bg_y_calc_1 = int(app_height * bg_y_calc)
    bg_y_calc_2 = int(app_height * 2.0)
    bg_y_calc_3 = int(app_height * 0.6046) - safezoneSizeY + 24 # correção do background no app, não afeta no jogo.
    bg_y_calc_4 = bg_y_calc_1 / bg_y_calc_2
    MenuBGYCoord = bg_y_calc_4 + bg_y_calc_3
    return MenuBGYCoord

# Função para setar imagem em rect do menu.
def DrawImage(image_path, width, height):
    app_background = customtkinter.CTkImage(
        dark_image = Image.open(image_path),
        size = (width, height)
    )
    return app_background

class AddTitle(customtkinter.CTkLabel):
    def __init__(self, master, text):
        super().__init__(master, font = ('Impact', 24), text = text, fg_color = MenuBannerColor) 

class DrawRect(customtkinter.CTkFrame):
    def __init__(self, master, height, width, fg_color, MenuBGImage):
        super().__init__(master, width = width, height = height, fg_color = fg_color, corner_radius = 0)
        if MenuBGImage == '1':
            self.image_path = bg_custom_img_path
            self.GetBGImage = DrawImage(self.image_path, width = width, height = height)
            self.DrawBGImage = customtkinter.CTkLabel(self, image = self.GetBGImage, text = "")
            self.DrawBGImage.grid(row = 0, column = 0)