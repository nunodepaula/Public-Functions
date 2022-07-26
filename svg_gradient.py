import numpy as np

from colors import Rgb

def get_color(coefficients: dict, x_value: float):
    return Rgb(
        red=int(coefficients["red"][0] * x_value + coefficients["red"][0]),
        green=int(coefficients["green"][0] * x_value + coefficients["green"][0]),
        blue=int(coefficients["blue"][0] * x_value + coefficients["blue"][0])
    )

def gradient(color_min: Rgb, color_max: Rgb, x_min: int, x_max:int, n_colors: int) -> list:
    x_values = [x_min, x_max]

    y_values = {}
    coefficients = {}
    for code in color_min.to_dict.keys():
        y_values[code] = [getattr(color_min, code), getattr(color_max, code)]

        coefficients[code] = np.polyfit(x_values, y_values[code], 1)

    x_gradient = np.linspace(x_min, x_max, n_colors)

    return [get_color(coefficients, i).to_hex for i in x_gradient]