

import pygame
from settings import Settings
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并初始化其位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()

        # 对于每艘飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.midbottom = self.screen_rect.center

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

        # print('x:',self.rect.x)
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞机在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
