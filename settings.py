class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1  # 1.5
        self.ship_limit = 3

        # Настройки снаряда
        self.bullet_speed = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.2  # 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 это движение вправо, а -1 - влево
