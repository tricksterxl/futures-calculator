# Diccionario de instrumentos con su valor por punto
instruments = {
    "es": {"valor_p": 50},
    "nq": {"valor_p": 20},
    "btc": {"valor_p": 0.10},
    "eth": {"valor_p": 0.10},
    "mes": {"valor_p": 5},
    "mnq": {"valor_p": 2},
    "mgc": {"valor_p": 10},
    "cl": {"valor_p": 10},
    "zn": {"valor_p": 15.625},
    "6b": {"valor_p": 0.625},
    "6j": {"valor_p": 1.25},
    "6a":{"valor_p": 1},
    "qi": {"valor_p": 31.25},
    "zc": {"valor_p": 50},
    "zs": {"valor_p": 50},
    }

def get_list(symbol):
    return instruments.get(symbol.lower())

def get_instruments():
    return instruments
