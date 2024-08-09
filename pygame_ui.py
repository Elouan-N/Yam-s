from base import *
import pygame
from pygame.locals import *

# Objet pygame représentant l'écran
screen = None

# Fonctions gérant les évènements (clic de souris, appuis sur des touches), doivent prendre en paramètre un évènement
# Les handlers doivent changer la variable globale MODFS si un évènement a provoqué la modification de l'affichage
handlers: list = []

# Fonctions redessinant la fenêtre si besoin
updaters: list = []


pygame.init()


def init_graphisme():
    global screen, BD
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(title="Yam's")
    BD = BoiteDialogue(None, None, "Entrez le nombre de joueurs:", "2")
    handlers.append(BD.event_handler)
    updaters.append(BD.update)


class BoiteDialogue:
    """Génère une boîte de dialogue avec une input et une zone de retour


    +----------------------------------+
    |                                  |
    |        INPUT                     |
    |                                  |
    |   +--------------------------+   |
    |   | ZONE D'ECRITURE          |   |
    |   +--------------------------+   |
    +----------------------------------+


    """

    FGCOLOR_INACTIVE = "dark grey"
    BGCOLOR_INACTIVE = "dark grey"
    FGCOLOR_ACTIVE = "white"
    BGCOLOR_ACTIVE = "white"

    h_padding = 10
    w_padding = 10

    def __init__(
        self, w=None, h=None, input="", default_text="", font=pygame.font.Font(None, 32)
    ):
        self.w = w
        self.h = h
        self.active = False
        self.fgcol = self.FGCOLOR_INACTIVE
        self.bgcol = self.BGCOLOR_INACTIVE
        self.input = input
        self.text = default_text
        self.font = font
        self.input_surf = self.font.render(self.input, True, "black", self.bgcol)
        self.code = 0  # Etat de la requête

        # Premier dessin de la zone
        # Etape 1: on calcule toutes les longueurs
        if self.w is None:
            # On adapte la largeur de la fenêtre à celle de l'input
            self.w = self.input_surf.get_width() + 2 * self.w_padding
        # Padding: 1 à gauche, 1 à droite
        self.text_zone_w = self.w - 2 * self.w_padding
        # Padding: 1/2 de chaque côté
        self.text_w = self.text_zone_w - self.w_padding

        if self.h is None:
            # On adapte la hauteur de la fenêtre à celle de l'input
            # Padding: 1 en haut et en bas, 1 entre les deux elts, 1/2 en haut et en bas de la zone de texte
            self.h = 2 * self.input_surf.get_height() + 4 * self.h_padding
        self.text_zone_h = self.h - self.input_surf.get_height() - 3 * self.h_padding

        # Coordonnées du coin haut gauche
        self.x = (screen.get_width() - self.w) / 2
        self.y = (screen.get_height() - self.h) / 2

        self.text_zone_x = self.x + self.w_padding
        self.text_zone_y = self.y + 2 * self.h_padding + self.input_surf.get_height()

        # Etape 2: On crée tous les objets
        self.surf = pygame.Rect(self.x, self.y, self.w, self.h)
        self.text_zone_surf = pygame.Rect(
            self.text_zone_x, self.text_zone_y, self.text_zone_w, self.text_zone_h
        )
        self.text_zone_outline = pygame.Rect(
            self.text_zone_x - 1,
            self.text_zone_y - 1,
            self.text_zone_w + 2,
            self.text_zone_h + 2,
        )

        # Etape 3: on les dessine
        pygame.draw.rect(screen, self.bgcol, self.surf)
        screen.blit(self.input_surf, (self.x + self.w_padding, self.y + self.h_padding))
        pygame.draw.rect(screen, "black", self.text_zone_outline)
        pygame.draw.rect(screen, self.fgcol, self.text_zone_surf)

    def set_active(self):
        self.active = True
        self.fgcol = self.FGCOLOR_ACTIVE
        self.bgcol = self.BGCOLOR_ACTIVE

    def set_inactive(self):
        self.active = False
        self.fgcol = BoiteDialogue.FGCOLOR_INACTIVE
        self.bgcol = BoiteDialogue.BGCOLOR_INACTIVE

    def event_handler(self, event):
        global MODFS
        if event.type == MOUSEBUTTONDOWN:
            MODFS = True
            if self.surf.collidepoint(event.pos):
                self.set_active()
            else:
                self.set_inactive()
        elif event.type == KEYDOWN and self.active:
            MODFS = True
            if event.key == K_RETURN:
                self.response = self.text
                self.code = 200
            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
                self.text_surf = self.font.render(
                    self.text, True, self.fgcol, self.bgcol
                )

    def update(self):
        pygame.draw.rect(screen, self.bgcol, self.surf)
        self.input_surf = self.font.render(self.input, True, "black")
        screen.blit(self.input_surf, (self.x + self.w_padding, self.y + self.h_padding))
        pygame.draw.rect(screen, "black", self.text_zone_outline)
        pygame.draw.rect(screen, self.fgcol, self.text_zone_surf)
        self.text_surf = self.font.render(self.text, True, "black", self.fgcol)
        screen.blit(
            self.text_surf,
            (
                self.x + 1.5 * self.w_padding,
                self.y + 2.5 * self.h_padding + self.input_surf.get_height(),
            ),
        )


def game_loop():
    global STOP, MODFS
    MODFS = True
    while not STOP:
        for event in pygame.event.get():
            for h in handlers:
                h(event)
            if event.type == QUIT:
                STOP = True
        if MODFS:
            for u in updaters:
                u()
            pygame.display.flip()
            MODFS = False


if __name__ == "__main__":
    init_graphisme()
    handlers.append(game_handler)
    game_loop()
