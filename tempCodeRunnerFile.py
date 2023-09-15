        if self.type == 0:
            self.collideRect.y = self.rect.y + 100
            self.collideRect.x = SCREEN_WIDTH + 48
        elif self.type == 1:
            self.collideRect.y = self.rect.y + 100
            self.collideRect.x = SCREEN_WIDTH + 60
        else:
            self.collideRect.y = self.rect.y + 100
            self.collideRect.x = SCREEN_WIDTH + 27