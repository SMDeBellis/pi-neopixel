import time
import board
import neopixel
import random
import math

PIXEL_PIN = board.D18
ROWS = 7
COLS = 7
running = False
#pixels = neopixel.NeoPixel(
#        pixel_pin, num_pixels, brightness = 0.1, auto_write=True, pixel_order=ORDER
#)

class Entry:
    def __init__(self, rgb_color, row, col, max_row, max_col):
        self.rgb_color = rgb_color
        self.row = row
        self.col = col
        self.max_row = max_row
        self.max_col = max_col

    def __str__(self):
        return f'Entry[{self.rgb_color}, {self.row}, {self.col}]'

    def __repr__(self):
        return str(self)

    def shift_red(self, val):
        self.rgb_color = (self.rgb_color[0] + val % 255, self.rgb_color[1], self.rgb_color[2])

    def shift_green(self, val):
        self.rgb_color = (self.rgb_color[0], self.rgb_color[1] + val % 255, self.rgb_color[2])

    def shift_blue(self, val):
        self.rgb_color = (self.rgb_color[0], self.rgb_color[1], self.rgb_color[2] + val % 255)

    def get_pixel_location(self) -> int:
        if self.row % 2 == 0:
            return (self.row * self.max_col) + self.col
        return (self.row * self.max_col) + (self.max_col - self.col - 1)

    def get_color(self):
        return self.rgb_color
    

class Matrix:
    def __init__(self,rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = self.create_blank_matrix(rows, cols)

    def __str__(self):
        s = ""
        for m in range(self.rows):
            if m != 0:
                s += "\n| "
            else:
                s += "| "
            for n in range(self.cols):
                s += " " + str(self.matrix[m][n]) + " |"
        return s        
    
    def __repr__(self):
        return str(self)

    def create_blank_matrix(self, m, n):
        matrix = []
        for i in range(m):
            for j in range(n):
                if j == 0:
                    matrix.append([Entry((0,0,0), i, j, m, n)])
                else:
                    matrix[i].append(Entry((0,0,0), i, j, m, n))
        return matrix

    def get_pixel_location(self, row, col) -> int:
        if row % 2 == 0:
            return row * self.cols + col
        return (row * self.cols) + (self.cols - col - 1)

    def get_center_pixel(self):
        return self.get_pixel_location(math.floor(self.rows / 2), math.floor(self.cols / 2))

    def get_center_entry(self):
        return self.matrix[math.floor(self.rows / 2)][math.floor(self.cols / 2)]


class NeopixelMatrix:
    def __init__(self, rows, cols, pixel_pin, auto_write=True):
        self.rows = rows
        self.cols = cols
        self.auto_write = auto_write
        self.pixels = neopixel.NeoPixel(
            pixel_pin, rows * cols, brightness = 0.1, auto_write=auto_write
        )

    def get_pixel_location(self, row, col) -> int:
        if row % 2 == 0:
            return row * self.cols + col
        return (row * self.cols) + (self.cols - col - 1)

    def matrix_fill(self, r, g, b):
        for i in range(self.rows):
            for j in range(self.cols):
                self.pixels[self.get_pixel_location(i,j)] = (r, g, b)
        if not self.auto_write:
            self.pixels.show()

    def apply_mask(self, mask_matrix, mask_rows, mask_cols):
        for i in range(mask_rows):
            for j in range(mask_cols):
                self.pixels[self.get_pixel_location(i, j)] = mask_matrix[i][j]

        if not self.auto_write:
            self.pixels.show()

    def deinit(self):
        self.pixels.deinit()

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))


pixel_matrix = NeopixelMatrix(ROWS, COLS, PIXEL_PIN, False)
pixel_matrix.matrix_fill(255, 0, 0)
time.sleep(10)
pixel_matrix.matrix_fill(0, 255, 0)
time.sleep(10)
pixel_matrix.matrix_fill(0, 0, 255)
time.sleep(10)
pixel_matrix.deinit()

#try:
#    while(True):
#        if not running:
#            running = False
#            for i in range(4):
#                for j in range(25):
#                    if j % 3 == 0 or j % 5 == 0:
#                        pixels[i * 25 + j] = (0,155,0)
#                    else:
#                        pixels[i * 25 + j] = (0,0,0)
#
#            pixels.show()
#            time.sleep(1)
#            pixels.fill((0,0,0))
#            pixels.show()
#            time.sleep(1)
#
#except KeyboardInterrupt:
#    pixels.deinit()


