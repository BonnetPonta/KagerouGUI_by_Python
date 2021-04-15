import tkinter
import tkinter.ttk
##############################################################################################################################
# 変数定義 -> 関数 -> クリックイベント -> 画面作成 -> マッピングGUI
##############################################################################################################################
# 徘徊者カウンター
# 変数定義 //lblがname //lbl_が残り数 //Aをリストかしてる
A = [0]*8
lbl_ = [0]*8
txtbox = [0]*8

##############################################################################################################################
# //クリックイベント//
# ##############################################################################################################################
# 徘徊者カウンター：click時のイベント関数


def btn_click_set():  # setのs
    goukei = 0
    for s in range(8):
        A[s] = int(txtbox[s].get())
        lbl_[s]["text"] = A[s]
        # 合計左側1度だけ実行
        goukei = int(goukei) + int(A[s])
        lbl_gou2["text"] = goukei
        kousin()


def kousin():
    goukei = 0
    for k in range(8):
        goukei = int(goukei) + int(A[k])
        lbl_gou["text"] = goukei


def btn_click_min(i):
    def aaa():
        if 0 < int(A[i]):
            A[i] = int(A[i])-1
            lbl_[i]["text"] = A[i]
            kousin()
    return aaa


def btn_click_plus(i):
    def bbb():
        A[i] = int(A[i])+1
        lbl_[i]["text"] = A[i]
        kousin()
    return bbb


##############################################################################################################################
# //画面作成//
tki = tkinter.Tk()
tki.geometry("300x300+1160+60")
tki.configure(bg="#38b48b")
tki.title("影廊-徘徊者カウンター")
tki.attributes("-topmost", True)
tki.resizable(False, False)

##################################################################################################
# 作成 //徘徊者一覧
name = ["神楽鈴", "ランナー", "徘徊女", "蜘蛛", "警鐘", "梅", "固定女", "憎悪"]
name_pos = []
for n in range(8):  # テキストボックスとボタンの方を一緒に実行しちゃうとTABキー押したとき面倒だから先にbox先作る
    lbl = tkinter.Label(text=name[n], bg="#ffff00")
    name_pos.append(20+n*30)
    lbl.place(x=10, y=name_pos[n])
    # テキストボックスの作成
    txtbox[n] = tkinter.Entry(width=20)
    txtbox[n].place(x=60, y=name_pos[n], width=50)

for i in range(8):
    # ラベル初期値
    lbl_[i] = tkinter.Label(text="", bg="white")
    lbl_[i].place(x=230, y=name_pos[i])
    # ボタン作成
    # -1
    btn = tkinter.Button(tki, text="-1", command=btn_click_min(i))
    btn.place(x=130, y=name_pos[i], width=50)
    # +1
    btn = tkinter.Button(tki, text="+1", command=btn_click_plus(i))
    btn.place(x=250, y=name_pos[i], width=50)

# 合計ラベルの作成
lbl = tkinter.Label(text="#-合計-#", bg="#00ff00")
lbl.place(x=10, y=260)
lbl_gou2 = tkinter.Label(text="", bg="#00ff00")
lbl_gou2.place(x=100, y=260)
lbl_gou = tkinter.Label(text="", bg="#00ff00")
lbl_gou.place(x=230, y=260)


# キーボード対応//Enter -> set
key = ""


def key_down(e):
    key = e.keysym
    if key == "Return":
        btn_click_set()


# キー設定
tki.bind("<KeyPress>", key_down)


# 画面をそのまま表示
tki.mainloop()
