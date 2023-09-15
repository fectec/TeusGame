SUBTITLE_TEXT = menuSubtitleFont.render("Press any Key to Restart", True, (0, 0, 0))
    MENU_SCORE_TEXT = menuSubtitleFont.render("Your Score: " + str(points), True, (0, 0, 0))
    MENU_SCORE_TEXT_RECT = MENU_SCORE_TEXT.get_rect()
    MENU_SCORE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)