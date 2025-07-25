from dataclasses import dataclass, field
from types import CellType
from constants import COLORS, MAP_NET_WIDTH, CELL_SIZE, MAZE_SIDE_CELL_AMOUNT
import pygame


@dataclass
class Map:
    screen: pygame.Surface
    maze_side_cell_amount: int = MAZE_SIDE_CELL_AMOUNT
    cell_size: int = CELL_SIZE
    net_width: int = MAP_NET_WIDTH
    obstacles: list[list[tuple]] = field(default_factory=lambda: [])

    def draw(self):
        for col in range(1, self.maze_side_cell_amount):
            pygame.draw.line(
                self.screen,
                COLORS["white"],
                start_pos=pygame.math.Vector2(col * self.cell_size, 0),
                end_pos=[col * self.cell_size, self.screen.get_width()],
                width=self.net_width,
            )

        for row in range(1, self.maze_side_cell_amount):
            pygame.draw.line(
                self.screen,
                COLORS["white"],
                start_pos=pygame.math.Vector2(0, row * self.cell_size),
                end_pos=pygame.math.Vector2(
                    self.screen.get_width(), row * self.cell_size
                ),
                width=self.net_width,
            )

        for obstacle in self.obstacles:
            start_pos, end_pos = obstacle
            pygame.draw.line(
                self.screen,
                COLORS["red"],
                start_pos=start_pos,
                end_pos=end_pos,
                width=self.net_width,
            )

    def set_obstacles_walls(self, mousePressedPosition: tuple):
        x, y = mousePressedPosition

        rounded_x = round(x / self.cell_size) * self.cell_size
        rounded_y = round(y / self.cell_size) * self.cell_size
        end_x, end_y = rounded_x, rounded_y

        if abs(x-rounded_x) > abs(y-rounded_y):
            if x-rounded_x > 0:
                end_x = rounded_x + self.cell_size
            else:
                end_x = rounded_x - self.cell_size
        else:
            if y-rounded_y > 0:
                end_y = rounded_y + self.cell_size
            else:
                end_y = rounded_y - self.cell_size

        self.obstacles.append(
            [(rounded_x, rounded_y), (end_x, end_y)]
        )

    def draw_obstacles(self):
        pass
