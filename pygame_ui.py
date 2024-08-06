from base import *
import pygame
from pygame.locals import *


screen = None

bindings = []


def init_graphisme():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(title="Yam's")


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

    FGCOLOR_INACTIVE = None
    BGCOLOR_INACTIVE = None
    FGCOLOR_ACTIVE = None
    BGCOLOR_ACTIVE = None

    h_padding = 10
    v_padding = 10

    def __init__(self, w=None, h=None, input="", font=pygame.font.Font(None, 32)):
        self.w = w
        self.h = h
        # Coordonnées du coin haut gauche
        if self.w is None:
            self.x = None
        else:
            self.x = (screen.get_width() - self.w) / 2
        if self.h is None:
            self.y = None
        else:
            self.y = (screen.get_height() - self.h) / 2
        self.surf = pygame.Rect(w, h)
        self.active = False
        self.fgcol = self.FGCOLOR_INACTIVE
        self.bgcol = self.BGCOLOR_INACTIVE
        self.input = input
        self.font = font
        self.input_surf = self.font.render(self.input, True, self.fgcol, self.bgcol)
        self.code = 0  # Etat de la requête

        # Premier dessin de la zone

        # Etape 1: on calcule toutes les longueurs
        if self.w is None:
            # On adapte la largeur de la fenêtre à celle de l'input
            self.w = self.input_surf.get_width() + 2 * self.h_padding
        else:
            self.text_zone_w = self.w - 2 * self.h_padding
            self.text_w = self.text_zone_w - 2 * self.h_padding

        if self.h is None:
            # On adapte la hauteur de la fenêtre à celle de l'input
            pass

        # Etape 2: On crée tous les objets

    def set_active(self):
        self.active = True
        self.fgcol = self.FGCOLOR_ACTIVE
        self.bgcol = self.BGCOLOR_ACTIVE

    def set_inactive(self):
        self.active = False
        self.fgcol = BoiteDialogue.FGCOLOR_INACTIVE
        self.bgcol = BoiteDialogue.BGCOLOR_INACTIVE

    def event_handler(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.text_wrapper_surf.collidepoint(event.pos):
                self.set_active()
            else:
                self.set_inactive()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.response = self.text
                self.code = 200
            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
                self.txt_surf = self.font.render(
                    self.text, True, self.fgcol, self.bgcol
                )

    def update(self):
        pass


def game_loop():
    global STOP, MODFS
    while STOP:
        MODFS = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                ...
            if event.type == QUIT:
                STOP = True
        if MODFS:
            pygame.display.flip()


if __name__ == "__main__":
    init_graphisme()
    game_loop()
