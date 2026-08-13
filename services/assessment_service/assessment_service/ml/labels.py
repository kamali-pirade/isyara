import json

from ..config import LABEL_MAP_PATH


DEFAULT_LABELS = [
    "a", 
    "anda", 
    "apa",
    "b", 
    "berhenti",
    "bodoh", 
    "c",
    "cantik",
    "d",
    "e",
    "f",
    "g",
    "h",
    "halo",
    "hati-hati",
    "i", 
    "j",
    "k",
    "l",
    "lelah",
    "m",
    "maaf",
    "makan",
    "mau",
    "membaca",
    "n",
    "nama",
    "o",
    "p",
    "q",
    "r",
    "s",
    "sama_sama",
    "saya",
    "siapa",
    "sombong",
    "t",
    "takut",
    "terima_kasih",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]

DISPLAY_LABELS = {
    "a" : "A", 
    "anda": "Anda", 
    "apa": "Apa",
    "b":  "B", 
    "berhenti": "Berhenti",
    "bodoh":  "Bodoh", 
    "c": "C",
    "cantik":"Cantik",
    "d":"D",
    "e": "E",
    "f": "F",
    "g": "G",
    "h": "H",
    "halo": "Halo",
    "hati_hati": "Hati-hati",
    "i":  "I", 
    "j": "J",
    "k": "K",
    "l": "L",
    "lelah": "Lelah",
    "m": "M",
    "maaf": "Maaf",
    "makan": "Makan",
    "mau": "Mau",
    "membaca": "Membaca",
    "n": "N",
    "nama": "Nama",
    "o": "O",
    "p": "P",
    "q": "Q",
    "r": "R",
    "s": "S",
    "sama_sama": "Sama-sama",
    "saya": "Saya",
    "siapa": "Siapa",
    "sombong": "Sombong",
    "t": "T",
    "takut": "Takut",
    "terima_kasih": "Terima kasih",
    "u": "U",
    "v": "V",
    "w": "W",
    "x": "X",
    "y": "Y",
    "z":"Z"
}


def load_labels():
    if LABEL_MAP_PATH.exists():
        return json.loads(LABEL_MAP_PATH.read_text())
    return DEFAULT_LABELS


def display_text(label):
    return DISPLAY_LABELS.get(label, label.replace("_", " ").title())
