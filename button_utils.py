import pygame

class ButtonUtils:
    def draw_text(screen, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        width = img.get_width()
        screen.blit(img, (x - (width / 2), y))

    def enlarge_button(screen, button_surf, button_rect, enlarge_scale):
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            enlarged_width = int(button_rect.width * enlarge_scale)
            enlarged_height = int(button_rect.height * enlarge_scale)

            enlarged_rect = pygame.Rect(
                button_rect.centerx - enlarged_width // 2,
                button_rect.centery - enlarged_height // 2,
                enlarged_width,
                enlarged_height
            )

            enlarged_surf = pygame.transform.scale(button_surf, (enlarged_width, enlarged_height))
            screen.blit(enlarged_surf, enlarged_rect)
        else:
            screen.blit(button_surf, button_rect)



