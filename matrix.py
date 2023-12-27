import time
import board
import neopixel
import random
import math
import json
from flask import Flask, request, flash, jsonify, session
from multiprocessing import Process
from flask_cors import CORS, cross_origin

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
        self.pixel_pin = pixel_pin
        self.pixels = None

    def initialize(self, rows, cols) -> None:
        if not self.pixels:
            self.rows = rows
            self.cols = cols
            self.pixels = neopixel.NeoPixel(
                self.pixel_pin, rows * cols, brightness = 0.1, auto_write=self.auto_write
                )

    def color_from_hex(self, hex_str) -> (int, int, int):
        h = hex_str.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    
    def hex_from_rgb_color(self, *args) -> str:
        hex_str = "#"
        for arg in args:
            hex_str = hex_str + str(hex(int(arg))).replace('0x', '').zfill(2)
        return hex_str
    
    def get_pixel_location(self, row, col) -> int:
        if row % 2 == 0:
            return row * self.cols + col
        return (row * self.cols) + (self.cols - col - 1)

    def change_pixel_color(self, color, row, col) -> None:
        if self.pixels:
            self.pixels[self.get_pixel_location(row, col)] = color
            if not self.auto_write:
                self.pixels.show()

    def change_pixel_colors(self, pixel_data_json) -> None:
        if self.pixels:
            pixel_data_map = json.loads(pixel_data_json)
            if 'data' in pixel_data_map:
                for pixel in pixel_data_map['data']:
                    self.pixels[self.get_pixel_location(pixel['row'], pixel['col'])] = self.color_from_hex(pixel['color'])
                if not self.auto_write:
                    self.pixels.show()

    def matrix_fill_rgb(self, r, g, b) -> None:
        if self.pixels:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.pixels[self.get_pixel_location(i,j)] = (r, g, b)
            if not self.auto_write:
                self.pixels.show()

    def matrix_fill_color(self, color) -> None:
        self.matrix_fill_rgb(color[0], color[1], color[2])

    def apply_mask(self, mask_matrix, mask_rows, mask_cols):
        if self.pixels:
            for i in range(mask_rows):
                for j in range(mask_cols):
                    self.pixels[self.get_pixel_location(i, j)] = mask_matrix[i][j]

            if not self.auto_write:
                self.pixels.show()

    def deinit(self):
        if self.pixels:
            self.pixels.deinit()
            self.pixels = None

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))





def pixel_data_diag(hex_color_str) -> str:
    x = {
            "data": [ 
                { "color": f"{hex_color_str}", "row": 0, "col": 0 },
                { "color": f"{hex_color_str}", "row": 1, "col": 1 },
                { "color": f"{hex_color_str}", "row": 2, "col": 2 },
                { "color": f"{hex_color_str}", "row": 3, "col": 3 },
                { "color": f"{hex_color_str}", "row": 4, "col": 4 },
                { "color": f"{hex_color_str}", "row": 5, "col": 5 },
                { "color": f"{hex_color_str}", "row": 6, "col": 6 }
            ] 
        }
    return json.dumps(x)

def pixel_data_vert(hex_color_str) -> str: 
    x = {
            "data": [ 
                { "color": f"{hex_color_str}", "row": 0, "col": 3 },
                { "color": f"{hex_color_str}", "row": 1, "col": 3 },
                { "color": f"{hex_color_str}", "row": 2, "col": 3 },
                { "color": f"{hex_color_str}", "row": 3, "col": 3 },
                { "color": f"{hex_color_str}", "row": 4, "col": 3 },
                { "color": f"{hex_color_str}", "row": 5, "col": 3 },
                { "color": f"{hex_color_str}", "row": 6, "col": 3 }
            ] 
        }
    return json.dumps(x)

def pixel_data_hor(hex_color_str) -> str:
    x = {
            "data": [ 
                { "color": f"{hex_color_str}", "row": 3, "col": 0 },
                { "color": f"{hex_color_str}", "row": 3, "col": 1 },
                { "color": f"{hex_color_str}", "row": 3, "col": 2 },
                { "color": f"{hex_color_str}", "row": 3, "col": 3 },
                { "color": f"{hex_color_str}", "row": 3, "col": 4 },
                { "color": f"{hex_color_str}", "row": 3, "col": 5 },
                { "color": f"{hex_color_str}", "row": 3, "col": 6 }
            ] 
        }
    return json.dumps(x)


def pixel_data_diag_rev(hex_color_str) -> str:
    x = {
        "data": [ 
            { "color": f"{hex_color_str}", "row": 0, "col": 6 },
            { "color": f"{hex_color_str}", "row": 1, "col": 5 },
            { "color": f"{hex_color_str}", "row": 2, "col": 4 },
            { "color": f"{hex_color_str}", "row": 3, "col": 3 },
            { "color": f"{hex_color_str}", "row": 4, "col": 2 },
            { "color": f"{hex_color_str}", "row": 5, "col": 1 },
            { "color": f"{hex_color_str}", "row": 6, "col": 0 }
        ] 
    }
    return json.dumps(x)

def clockwise_spin_animation(matrix, loop_iterations, fill_color, line_color_hex):
    for i in range(loop_iterations):
        time.sleep(1/15)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_diag(line_color_hex))
        time.sleep(1/15)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_vert(line_color_hex))
        time.sleep(1/15)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_diag_rev(line_color_hex))
        time.sleep(1/15)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_hor(line_color_hex))
        time.sleep(1/15)

def counter_clockwise_spin_animation(matrix, loop_iterations, fill_color,  line_color_hex) -> None:
    for i in range(loop_iterations):
        time.sleep(1/30)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_diag(line_color_hex))
        time.sleep(1/30)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_hor(line_color_hex))
        time.sleep(1/30)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_diag_rev(line_color_hex))
        time.sleep(1/30)
        matrix.matrix_fill_color(fill_color)
        matrix.change_pixel_colors(pixel_data_vert(line_color_hex))
        time.sleep(1/30)
        

if __name__ == '__main__':
 
    app = Flask(__name__); 
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.secret_key = 'BAD_SECRET_KEY'

    cors = CORS(app, resources={r"/picker-change|/logout|/connect": {"origins": "http://localhost:port"}})
    pixel_matrix = None

    @app.route('/picker-change', methods = ['POST'])
    @cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
    def picker_change(origin='localhost',headers=['Content-Type','Authorization']):
        if pixel_matrix:
            if request.content_type == 'application/json':
                print(f"request.json type: {request.json}")
                pixel_matrix.change_pixel_colors(json.dumps(request.json))
                return json.dumps({ "status": 200, "statusText": "OK", "connection-id": session['current_connection_uuid']})

            else:
                flash("Request must be type application/json.")
                return json.dumps({ "status": 200, "statusText": "OK", "connection-id": session['current_connection_uuid']})
        else:
            return jsonify({"error": "No connection. Please connect."}), 501
        

    @app.route('/connect', methods = ['POST'])
    @cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
    def connect():
        if 'current_connection_uuid' in session:
            return jsonify({"connection-id": session['current_connection_uuid']}), 409
        else:
            if request.content_type == 'application/json':
                data = request.get_json()
                try:
                    session['current_connection_uuid'] = data['connection-id']
                    pixel_matrix = NeopixelMatrix(ROWS, COLS, PIXEL_PIN, False)
                    pixel_matrix.initialize(ROWS,COLS)
                    print("current_connection_uuid: ", session['current_connection_uuid'])
                    return jsonify({"connection-id", session['current_connection_uuid']}), 200
                except KeyError as ke:
                    return jsonify({"error": "Missing connection-id"}), 411
            else:
                return jsonify({"error": "Server only excepts application/json requests."}), 411

    @app.route('/logout')
    @cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
    def logout():
        if pixel_matrix:
            try:
                pixel_matrix.deinit() # maybe return a server error code if this is problematic. 
            finally:
                pixel_matrix = None
                conn_id = session.pop('current_connection_uuid', default="")
                return jsonify({"connection-id": conn_id}), 200


    app.run(host="10.0.0.110")
    
    # clockwise_spin_animation(pixel_matrix, 20, (0, 255, 0), pixel_matrix.hex_from_rgb_color(0, 0, 0))
    # clockwise_spin_animation(pixel_matrix, 20, (255, 0, 0), pixel_matrix.hex_from_rgb_color(0, 0, 0))
    # clockwise_spin_animation(pixel_matrix, 20, (0, 0, 255), pixel_matrix.hex_from_rgb_color(0, 0, 0))
    # clockwise_spin_animation(pixel_matrix, 20, (0, 255, 0), pixel_matrix.hex_from_rgb_color(0, 0, 0))
    # clockwise_spin_animation(pixel_matrix, 20, (0, 0, 255), pixel_matrix.hex_from_rgb_color(0, 0, 0))
    # clockwise_spin_animation(pixel_matrix, 20, (100, 50, 100), pixel_matrix.hex_from_rgb_color(0, 0, 0))
    # counter_clockwise_spin_animation(pixel_matrix, 20, (0, 255, 0), pixel_matrix.hex_from_rgb_color(3, 252, 232))
    # counter_clockwise_spin_animation(pixel_matrix, 20, (255, 0, 0), pixel_matrix.hex_from_rgb_color(3, 252, 232))
    # counter_clockwise_spin_animation(pixel_matrix, 20, (0, 0, 255), pixel_matrix.hex_from_rgb_color(3, 252, 232))
    # counter_clockwise_spin_animation(pixel_matrix, 20, (0, 255, 0), pixel_matrix.hex_from_rgb_color(3, 252, 232))
    # counter_clockwise_spin_animation(pixel_matrix, 20, (0, 0, 255), pixel_matrix.hex_from_rgb_color(3, 252, 232))
    # counter_clockwise_spin_animation(pixel_matrix, 20, (100, 50, 100), pixel_matrix.hex_from_rgb_color(3, 252, 232))
    # pixel_matrix.deinit()

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


