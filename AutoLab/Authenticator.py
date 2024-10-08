# IMPORTANTE: se você achou este pen drive, NÃO EXECUTE OS COMANDOS, eles servem
# única e exclusivamente para auxílio de monitores, utilizá-los indevidamente pode acarretar
# em problemas sérios.
# ESTEJE AVISADO!
# Créditos: Victor Flávio Demarchi Viana
# Dia 19/09/2024

import subprocess
import sys
import os
import socket
import time
import msvcrt
import ctypes
from ctypes import wintypes

key_map = {
    'ENTER': 0x0D,
    'RETURN': 0x0D,
    'SHIFT': 0x10,
    'CONTROL': 0x11,
    'ALT': 0x12,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'A': [0x10, 0x41],
    'B': [0x10, 0x42],
    'C': [0x10, 0x43],
    'D': [0x10, 0x44],
    'E': [0x10, 0x45],
    'F': [0x10, 0x46],
    'G': [0x10, 0x47],
    'H': [0x10, 0x48],
    'I': [0x10, 0x49],
    'J': [0x10, 0x4A],
    'K': [0x10, 0x4B],
    'L': [0x10, 0x4C],
    'M': [0x10, 0x4D],
    'N': [0x10, 0x4E],
    'O': [0x10, 0x4F],
    'P': [0x10, 0x50],
    'Q': [0x10, 0x51],
    'R': [0x10, 0x52],
    'S': [0x10, 0x53],
    'T': [0x10, 0x54],
    'U': [0x10, 0x55],
    'V': [0x10, 0x56],
    'W': [0x10, 0x57],
    'X': [0x10, 0x58],
    'Y': [0x10, 0x59],
    'Z': [0x10, 0x5A],
    ' ': 0x20,
    'ç': 0xBA,
    '=': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    ';': 0xBF,
    '\'': 0xC0,
    '´': 0xDB,
    ']': 0xDC,
    '[': 0xDD,
    '~': 0xDE,
    '/': 0x6F,
    '\\': 0xE2,
    'Ç': [0x10, 0xBA],
    '!': [0x10, 0x31],
    '@': [0x10, 0x32],
    '#': [0x10, 0x33],
    '$': [0x10, 0x34],
    '%': [0x10, 0x35],
    '¨': [0x10, 0x36],
    '&': [0x10, 0x37],
    '*': [0x10, 0x38],
    '(': [0x10, 0x39],
    ')': [0x10, 0x30],
    '_': [0x10, 0xBD],
    '+': [0x10, 0xBB],
    ':': [0x10, 0xBF],
    '<': [0x10, 0xBC],
    '>': [0x10, 0xBE],
    '?': [0x10, 0xBF],
    '{': [0x10, 0xDB],
    '}': [0x10, 0xDD],
    '"': [0x10, 0xC0],
}

VK_KEY = 0x0001

user32 = ctypes.windll.user32

def press_key(hex_key_code):
    user32.keybd_event(hex_key_code, 0, 0, 0)
    user32.keybd_event(hex_key_code, 0, 2, 0)

def press_keys(key_codes):
    for key_code in key_codes:
        user32.keybd_event(key_code, 0, 0, 0)

    for key_code in key_codes:
        user32.keybd_event(key_code, 0, 2, 0)

def analyzeString(string):
    for char in string:
        if char in key_map:
            vk_key = key_map[char]
            if type(vk_key) != list:
                press_key(vk_key)
            else:
                press_keys(vk_key)

def startAuthentication():
    #Salva a palavra chave a ser digitada e os inputs da senha
    passcode = b'wly'
    seq = b''

    while True:
        if seq == passcode:
            break
        else:
            seq += msvcrt.getch()
            for i in range(0, len(seq)):
                if passcode[i] != seq[i]:
                    seq = b''


    #Inicia o prompt de comando com o comando do runas com login (trocar pelo seu)
    os.system((b'start cmd /k runas /noprofile /user:fiap\\trocarPeloSeuLogin cmd').decode())

    #Espera um tempo para execução do comando no terminal
    time.sleep(0.5)

    #Digita a senha (trocar pela sua)
    analyzeString('TrocarParaSuaSenha')
    press_key(0x0D)

startAuthentication()