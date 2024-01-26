import json, os, inspect

# --- App Vars ---
app_width = 960
app_height = 540
app_window = f'{app_width}x{app_height}'

# Local atual do app.
get_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Carregar as configurações do config.json.
local_path = f'{get_path}\config.json'
with open(local_path) as config_file:
    menu_config = json.load(config_file)
# Seta os valores do config.json para as variaveis.
menu_name = menu_config['menu_name']
menu_bg_color = menu_config['menu_bg_color']
menu_banner_color = menu_config['menu_banner_color']
menu_set_bg_img = menu_config['menu_set_bg_img']
menu_custom_img = menu_config['menu_custom_img']
menu_left_sided = menu_config['menu_left_sided']
menu_number_options = menu_config['menu_number_options']

# Imagem de fundo do app.
bg_img_path = f'{get_path}\\src\\background.png'
# Imagem que pode ser alterada, imagem do bg do menu.
bg_custom_img_path = f'{get_path}\\src\\{menu_custom_img}'

# --- GTA Vars ---
NumberOfOptions = int(menu_number_options)
LeftSided = menu_left_sided

# Criando zona segura na tela do app, conforme no GTA.
# GET_SAFE_ZONE_SIZE = 0x3BDC44 (em decimal = 3894012)
safezoneSizeX = app_width * 0.6 / 2
safezoneSizeY = app_height * 0.9 / 2

# Setando as coordenadas do GTA conforme a posição do menu.
if LeftSided == '1':
    MenuXCoord1 = 0.5061
    MenuXCoord2 = 0.7211
    MenuXCoord3 = 0.6136
    # Convertendo para a resolução do app.
    GtaXCoord1 = int(app_width * MenuXCoord1) - safezoneSizeX - 220
    GtaXCoord2 = int(app_width * MenuXCoord2) - safezoneSizeX - 220
    GtaXCoord3 = int(app_width * MenuXCoord3) - safezoneSizeX - 220
else:
    MenuXCoord1 = 0.2789
    MenuXCoord2 = 0.4939
    MenuXCoord3 = 0.3864
    # Convertendo para a resolução do app.
    GtaXCoord1 = int(app_width * MenuXCoord1) + safezoneSizeX
    GtaXCoord2 = int(app_width * MenuXCoord2) + safezoneSizeX
    GtaXCoord3 = int(app_width * MenuXCoord3) + safezoneSizeX

# Titulo do menu.
AddTitleXCoord = GtaXCoord3 + 20
AddTitleYCoord = int(app_height * 0.5346) - safezoneSizeY + 24 # Correção feito no DrawBackground do app, não afeta o jogo.

# Cor do Banner do Menu.
MenuBannerColor = menu_banner_color

# Cor, Largura, Altura do Background do Menu.
MenuBGColor = menu_bg_color
GtaMenuBGHeight = 0.035
GtaMenuBGWidth = 0.2250 # Width conforme base do NYD.

# Draw Scrollbar.
ScrollbarWidth = int(app_width * 0.010)
ScrollbarXCoord = GtaXCoord3 + int(app_width * 0.2360)