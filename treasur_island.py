print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("トレジャーアイランドによく来たな！\n"
      "これかお前たちにはお宝を探してきてもらう！\n"
      "道中には危険が多いから心してかかれよ！")
print("お前たち準備はいいな？"
      "早速出発だ！")
print("早速分かれ道だ。右か左どっちに行くかえらべ！")
road = input('      "右" or "左"\n')
if road == "左" or road == "ひだり":
    print("良かったな、安全な道を通れたみたいだな！\n"
          "お、湖についたな！真ん中に島があるぞ！")
    lake = input("ボートが見えるな！待つか？泳ぐか？"
                 "どちらか入力してくれ！\n"
                 '"待つ" or "泳ぐ"\n')
    if lake == "待つ" or lake == "まつ":
        print("良かったな、無傷で島に着いたぞ！最後の試練だ！"
              "ドアが3つある城だ!")
        door = input("  赤い扉、黄色い扉、青い扉、好きな色を選べ！\n"
                    '"赤" or "黄色" or "青"\n')
        if door == "黄色" or door == "きいろ":
            print("宝を見つけたな!おめでとうお前たちの勝ちだ!")
        elif door == "赤" or door == "あか":
            print("炎に包まれた ゲームオーバー")
        elif door == "青" or door == "あお":
            print("野獣に襲われた ゲームオーバー")
        else:
            print("真面目に選ばなかったな ゲームオーバー")
    else:
        print("ワニに襲われた ゲームオーバー")
elif road == "右" or road == "みぎ":
    print("穴に落ちた ゲームオーバー")
else:
    print("迷いの森に入った ゲームオーバー")    