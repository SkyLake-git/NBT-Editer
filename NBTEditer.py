from nbt import nbt
from pathlib import Path
import os
import sys

def str_int_covert(text):
    try:
        value = int(text)
    except:
        value = f"\"{text}\""
    return value  

def arg_subscript(args):
    length = len(args)
    text = ""
    for i in range(0,length):
        value = str_int_covert(args[i]) #convert for TAG_List
        text = text + f"[{value}]"
        
    return text

def subscript(data, args):
    evalText = arg_subscript(args)
    return eval(data + evalText)

parent = Path(__file__).parent.parent

pmmpFolder = parent / "PocketMine-MP"
while True:
    player_name = input("編集するパスを入力してください ")
    player_path = pmmpFolder / f"{player_name}.dat"
    
    if not os.path.exists(player_path):
        print(f"プレイヤー {player_name} のデータは見つかりませんでした")
        continue
    
    nbtfile = nbt.NBTFile(player_path,'rb')
    
    os.system("cls")
    
    while True:
        command = input("NBT>")
        args = command.split(" ")
        main = args[0]
        arg = args[1:]
    
        if main == 'set':
            if len(arg) > 1:
                text = arg_subscript(arg[:-1])
                setValue = str_int_covert(arg[-1])
                exec(f"nbtfile{text}.value = {setValue}")
                print(f"nbt{text} キーに {arg[-1]} をセットしました")
        elif main == 'view':
            if len(arg) > 0:
                print(subscript('nbtfile', arg))
            else:
                print(nbtfile)
        elif main == 'info':
            if len(arg) > 0:
                text = arg_subscript(arg)
                exec(f"print(nbtfile{text}.tag_info())")
    
        elif main == 'exec':
            exec(''.join(arg))
        elif main == 'exit':
            break
        elif main == 'save':
            nbtfile.write_file(player_path)
            print("変更を保存しました")
        elif main == 'reload':
            nbtfile = nbt.NBTFile(player_path,'rb')
            print("現在のデータを破棄してリロードしました")
            continue
        