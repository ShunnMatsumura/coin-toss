import pyfiglet
import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# アニメーションのためのコインのアスキーアートのフレーム
coin_frames = [
    pyfiglet.figlet_format("Coin", font="slant"),
    pyfiglet.figlet_format("cOin", font="slant"),
    pyfiglet.figlet_format("coIn", font="slant"),
    pyfiglet.figlet_format("coiN", font="slant")
]

# アニメーションを表示（ここでは各フレームを0.2秒ごとに4回ずつ表示）
for _ in range(4):
    for frame in coin_frames:
        clear_screen()
        print(frame)
        time.sleep(0.2)

# コイントスの結果をランダムに決定
result = random.choice(['Head', 'Tail'])

# 結果に応じたアスキーアートの生成
result_art = pyfiglet.figlet_format(result, font="block")

circle = f"""
    {result_art}
"""

# 画面をクリアして最終結果を表示
clear_screen()
print(circle)
