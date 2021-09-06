"""
徘徊者カウンター
"""
import tkinter
import tkinter.ttk

lblR = [0]*8  # 右側の残り数
txtbox = [0]*8
txtboxV = [0]*8


def btn_click_set():
    total = 0
    for i in range(8):
        txtboxV[i] = int(txtbox[i].get())
        lblR[i]["text"] = txtboxV[i]
        # 合計左側1度だけ実行
        total += int(txtboxV[i])
        lbl_totalL["text"] = total
        kousin()


def kousin():
    total = 0
    for i in range(8):
        total += int(txtboxV[i])
        lbl_totalR["text"] = total


def btn_click_min(i):
    def aaa():
        if 0 < int(txtboxV[i]):
            txtboxV[i] -= 1
            lblR[i]["text"] = txtboxV[i]
            kousin()
    return aaa


def btn_click_plus(i):
    def bbb():
        txtboxV[i] += 1
        lblR[i]["text"] = txtboxV[i]
        kousin()
    return bbb


def key_down(e):  # キーボード対応//Enter -> set
    key = e.keysym
    if key == "Return":
        btn_click_set()


# //画面作成//
tki = tkinter.Tk()
tki.geometry("300x300+1160+60")
tki.configure(bg="#38b48b")
tki.title("影廊-徘徊者カウンター")
tki.attributes("-topmost", True)
tki.resizable(False, False)

##################################################################################################
# 作成 //徘徊者一覧
names = ["神楽鈴", "ランナー", "徘徊女", "蜘蛛", "警鐘", "梅", "固定女", "憎悪"]
name_pos = []
for i in range(8):  # テキストボックスとボタンの方を一緒に実行しちゃうとTABキー押したとき面倒だから先にbox先作る
    lblL = tkinter.Label(text=names[i], bg="#ffff00")
    name_pos.append(20+i*30)
    lblL.place(x=10, y=name_pos[i])
    # テキストボックスの作成
    txtbox[i] = tkinter.Entry(width=20)
    txtbox[i].place(x=60, y=name_pos[i], width=50)

for i in range(8):
    # 残り数ラベル初期値
    lblR[i] = tkinter.Label(text="", bg="white")
    lblR[i].place(x=230, y=name_pos[i])
    # ±1ボタン作成
    btn = tkinter.Button(tki, text="-1", command=btn_click_min(i))
    btn.place(x=130, y=name_pos[i], width=50)
    btn = tkinter.Button(tki, text="+1", command=btn_click_plus(i))
    btn.place(x=250, y=name_pos[i], width=50)

# 合計ラベルの作成
lblL = tkinter.Label(text="#-合計-#", bg="#00ff00")
lblL.place(x=10, y=260)
lbl_totalL = tkinter.Label(text="", bg="#00ff00")
lbl_totalL.place(x=100, y=260)
lbl_totalR = tkinter.Label(text="", bg="#00ff00")
lbl_totalR.place(x=230, y=260)

# キー設定
tki.bind("<KeyPress>", key_down)

# 画面をそのまま表示
tki.mainloop()
