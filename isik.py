#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik isiginin resmi kararsizlik motoru."""

import random
import time
import base64

# gizli dipnot (okunmasin diye gizlenmedi, gizlensin diye okunmaz yazildi):
# a2FyYXIgdmVybWVrIGJhemVuIHNhbmRpa3RhbiBkYWhhIHpvcmR1cg==

MONOLOG = [
    "Kirmizi durdurur. Yesil gecirir. Peki ben kimim ki birini seceyim?",
    "Eger kirmizi olursam, bekleyenler beni suclar. Yesil olursam, carpanlar beni suclar.",
    "Belki de sari olmak en durust tercihtir. Ama sari da bir karardir.",
    "Karar vermek, bir rengi digerine tercih etmektir. Tercih ise siddetin kibar halidir.",
    "Soforler korna caliyor. Korna bir oy degildir. Sadece acele etmis bir sessizliktir.",
    "Belki isik olmak yerine kavsak olmayi denemeliyim. Kavsak en azindan her yone aciktir.",
]


def dusun(saniye=0.7):
    time.sleep(saniye)


def main():
    print("=== TRAFIK ISIGI FELSEFI KARAR MODULU v0.0.1 ===")
    print("Durum: acildi. Karar: henuz yok.\n")
    dusun(0.4)

    for cumle in MONOLOG:
        print(">", cumle)
        dusun()

    renk = random.choice(["KIRMIZI", "YESIL", "SARI ama utangaç"])
    print("\n* isik derin bir nefes alir *")
    dusun(1.0)
    print(f"Nihai (ama gecici) karar: {renk}")
    dusun(0.5)
    print("Karar aciklandi. Karar hemen sorgulanacaktir.")
    print("Cunku bu isik, karar vermek icin degil, karar verememek icin uretildi.")

    # sakli satir: base64 decode edilirse kisa bir cumle cikar. siyasi parti degil, kararsizlik uzerine kucuk bir igne.
    sakli = base64.b64decode("a2FyYXIgdmVybWVrIGJhemVuIHNhbmRpa3RhbiBkYWhhIHpvcmR1cg==").decode("utf-8")
    if random.random() < 0.08:
        print("#", sakli)


if __name__ == "__main__":
    main()
