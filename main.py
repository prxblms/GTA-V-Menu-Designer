from menu import *

# Função para setar imagem no fundo da app.
def AppBGImage():
    app_background = customtkinter.CTkImage(
        dark_image = Image.open(bg_img_path),
        size = (app_width, app_height)
    )
    return app_background

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BlackHorizon™ GTAV (PS3) Menu Designer ver. 1.0.1 (beta)")
        self.geometry(app_window)
        self.resizable(False, False)
        
        # Imagem de fundo do app.
        self.app_background = AppBGImage()
        self.app_bg_image = customtkinter.CTkLabel(self, image = self.app_background, text = "")
        self.app_bg_image.grid(row = 0, column = 0)

        # DrawBackground.
        self.MenuBGYCoord = DrawBGYCoord()
        self.MenuBGWidth = DrawBGWidth()
        self.MenuBGLenght = DrawBGLenght()
        self.DrawBackground = DrawRect(self, width = self.MenuBGWidth, height = self.MenuBGLenght, fg_color = MenuBGColor, MenuBGImage = menu_set_bg_img)
        self.DrawBackground.place(x = GtaXCoord3, y = self.MenuBGYCoord)

        # DrawBanner.
        self.MenuBannerYCoord = DrawBannerYCoord()
        self.MenuBannerHeight = DrawBannerHeight()
        self.DrawBanner = DrawRect(self, width = self.MenuBGWidth, height = self.MenuBannerHeight, fg_color = MenuBannerColor, MenuBGImage = False)
        self.DrawBanner.place(x = GtaXCoord3, y = self.MenuBannerYCoord)

        # DrawTitle, AddTitle.
        self.DrawTitle = AddTitle(self, text = menu_name)
        self.DrawTitle.place(x = AddTitleXCoord, y = AddTitleYCoord)

        # DrawScrollbar.
        self.DrawScrollbaer = DrawRect(self, width = ScrollbarWidth, height = self.MenuBGLenght, fg_color = MenuBGColor, MenuBGImage = False)
        self.DrawScrollbaer.place(x = ScrollbarXCoord, y = self.MenuBGYCoord)

if __name__ == '__main__':
    app = App()
    app.mainloop()