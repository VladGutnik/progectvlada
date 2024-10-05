def length_converter(value, from_unit, to_unit):
    # значення
    factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    
    # конвертування
    meters = value * factors[from_unit]
    
    # конвертування у цыле число
    result = meters / factors[to_unit]
    
    return result

# отримання значень
value = float(input("введіть число: "))

from_unit = input("що конвертуємо ( km, mi, ft, т.д): ")

to_unit = input("у що конвертуємо: ")

result = length_converter(value, from_unit, to_unit)

print(f"{value} {from_unit} дорівнює {result:.4f} {to_unit}")