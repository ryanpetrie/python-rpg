import pygame

class HUD(object):
    font_size = 18

    HEALTHBAR_LEFT = 45
    HEALTHBAR_TOP = 2
    HEALTHBAR_WIDTH = 100
    HEALTHBAR_HEIGHT = 7
    HEALTHBAR_BORDER = 2
    HEALTHBAR_BORDER_COLOR = (0,0,0)
    HEALTHBAR_COLOR = (100, 255, 100)
    
    def __init__(self, gui, game):
        self._gui = gui
        self._game = game
        self.color = (64, 64, 255)

    def draw(self, canvas):
        # Compute player health as a percentage.
        player = self._game.get_player()
        health = (player.health * self.HEALTHBAR_WIDTH) / player.MAX_HEALTH
        # Render the text.
        hud_text = "Health: "
        font = self._gui.get_font(self.font_size)
        text_surface = font.render(hud_text, True, self.color)
        canvas.blit(text_surface, text_surface.get_rect())

        # Draw the health bar.
        hb_rect = pygame.Rect(self.HEALTHBAR_LEFT, self.HEALTHBAR_TOP, health, self.HEALTHBAR_HEIGHT)
        pygame.draw.rect(canvas,
                         self.HEALTHBAR_COLOR,
                         hb_rect)
        hb_rect = pygame.Rect(self.HEALTHBAR_LEFT - 1, self.HEALTHBAR_TOP, self.HEALTHBAR_WIDTH + 1, self.HEALTHBAR_HEIGHT)
        pygame.draw.rect(canvas,
                         self.HEALTHBAR_BORDER_COLOR,
                         hb_rect,
                         self.HEALTHBAR_BORDER)
