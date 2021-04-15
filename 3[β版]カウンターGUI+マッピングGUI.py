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

# マッピングGUI
# //変数定義// //2:瓦礫 //3:勾玉 //_1:cnt //_2:max
B1 = [0]*5
B2 = [0]*5
B3 = [0]*5
B4 = [0]*5
mapping_text2_1sumi = [0]*4
mapping_text2_1hasi = [0]*10
mapping_text2_1naka = [0]*11
mapping_text2_2sumi = [0]*4
mapping_text2_2hasi = [0]*10
mapping_text2_2naka = [0]*11
mapping_text3_1sumi = [0]*4
mapping_text3_1hasi = [0]*10
mapping_text3_1naka = [0]*11
mapping_text3_2sumi = [0]*4
mapping_text3_2hasi = [0]*10
mapping_text3_2naka = [0]*11
###############################################################
# 合計値
i_area_cnt = 0
i_area_max = 25
i_gareki_cnt = 0
i_gareki_max = 0
i_magatama_cnt = 0
i_magatama_max = 0

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
# //コンボボックス//


def area_get_sumi(self):
    # 毎回リセット、2:ダミーに代入してダミーから消してあまったやつを候補として作成する
    area_reikon_name_sumi_2 = area_reikon_name_sumi_1
    area_reikon_name_sumi_3 = []

    # ダミーと今回選択したやつが一致したらダミーから削除
    # sumi
    for ag_sumi1 in range(4):
        area_reikon_name_sumi_3.append(var_sumi[ag_sumi1].get())
    for ag_sumi2 in range(4):
        # print("var", var_sumi[ag_sumi2].get())
        # print("3", area_reikon_name_sumi_3)
        kekka_sumi = list(set(area_reikon_name_sumi_2) -
                          set(area_reikon_name_sumi_3))
        combo_sumi[ag_sumi2]["values"] = kekka_sumi

    # 連動 //エリアを選択した時、瓦礫数と勾玉数をセット
    for X1 in range(4):
        for X2 in range(4):
            if area_reikon_name_sumi_3[X1] == area_reikon_name_sumi_1[X2]:
                #print("その選択したエリアの瓦礫", area_reikon_gareki[X2])
                #print("その選択したエリアの勾玉", area_reikon_magatama[X2])
                mapping_text2_1sumi[X1]["text"] = area_reikon_gareki[X2]
                mapping_text3_1sumi[X1]["text"] = area_reikon_magatama[X2]


def area_get_hasi(self):
    # 毎回リセット、2:ダミーに代入してダミーから消してあまったやつを候補として作成する
    area_reikon_name_hasi_2 = area_reikon_name_hasi_1
    area_reikon_name_hasi_3 = []

    # ダミーと今回選択したやつが一致したらダミーから削除
    # hasi
    for ag_hasi1 in range(10):
        area_reikon_name_hasi_3.append(var_hasi[ag_hasi1].get())
    for ag_hasi2 in range(10):
        # print("var", var_hasi[ag_hasi2].get())
        # print("3", area_reikon_name_hasi_3)
        kekka_hasi = list(set(area_reikon_name_hasi_2) -
                          set(area_reikon_name_hasi_3))
        combo_hasi[ag_hasi2]["values"] = kekka_hasi

    # 連動 //エリアを選択した時、瓦礫数と勾玉数をセット
    # hasi
    for X1 in range(10):
        for X2 in range(10):
            if area_reikon_name_hasi_3[X1] == area_reikon_name_hasi_1[X2]:
                mapping_text2_1hasi[X1]["text"] = area_reikon_gareki[X2+4]
                mapping_text3_1hasi[X1]["text"] = area_reikon_magatama[X2+4]


def area_get_naka(self):
    # 毎回リセット、2:ダミーに代入してダミーから消してあまったやつを候補として作成する
    area_reikon_name_naka_2 = area_reikon_name_naka_1
    area_reikon_name_naka_3 = []

    # ダミーと今回選択したやつが一致したらダミーから削除
    # naka
    for ag_naka1 in range(11):
        area_reikon_name_naka_3.append(var_naka[ag_naka1].get())
    for ag_naka2 in range(11):
        # print("var", var_naka[ag_naka2].get())
        # print("3", area_reikon_name_naka_3)
        kekka_naka = list(set(area_reikon_name_naka_2) -
                          set(area_reikon_name_naka_3))
        combo_naka[ag_naka2]["values"] = kekka_naka

    # 連動 //エリアを選択した時、瓦礫数と勾玉数をセット
    # naka
    for X1 in range(11):
        for X2 in range(11):
            if area_reikon_name_naka_3[X1] == area_reikon_name_naka_1[X2]:
                mapping_text2_1naka[X1]["text"] = area_reikon_gareki[X2+14]
                mapping_text3_1naka[X1]["text"] = area_reikon_magatama[X2+14]


##############################################################################################################################
# //画面作成//
tki = tkinter.Tk()
tki.geometry("300x300+1160+60")
tki.configure(bg="#38b48b")
tki.title("影廊-徘徊者カウンター")
tki.attributes("-topmost", True)
tki.resizable(False, False)

# マッピングGUI作成
tki_map = tkinter.Toplevel()
tki_map.geometry("1450x800+40+0")
tki_map.configure(bg="#222222")
tki_map.title("影廊-マッピング")
#tki_map.attributes("-topmost", True)
tki_map.resizable(False, False)
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


# キーボード対応//Enter -> set //1つだけでいいから別に作成
key = ""


def key_down(e):
    key = e.keysym
    if key == "Return":
        btn_click_set()


# キー設定
tki.bind("<KeyPress>", key_down)
##################################################################################################
# 作成
# x,yラベル作成
mapping_x_label = ["A", "B", "C", "D", "E"]
mapping_y_label = ["1", "2", "3", "4", "5"]
for mx in range(5):
    lbl_map = tkinter.Label(tki_map, text=mapping_x_label[mx], bg="red")
    lbl_map.place(x=140+mx*200, y=10)
for my in range(5):
    lbl_map = tkinter.Label(tki_map, text=mapping_y_label[my], bg="blue")
    lbl_map.place(x=10, y=140+my*140)


mapping_text2_1sumi_pos_list = [110, 110, 910, 910, 80, 640, 80, 640]
mapping_text2_1hasi_pos_list = [110, 110, 110, 910, 910, 910, 310, 710, 310,
                                710, 220, 360, 500, 220, 360, 500, 80, 80, 640, 640]
mapping_text2_1naka_pos_list = [310, 310, 310, 710, 710, 710, 510, 510, 510,
                                510, 510, 220, 360, 500, 220, 360, 500, 80, 220, 360, 500, 640]

###---------------------------------------------------------------------------------------------------------------###
# 瓦礫
for a2 in range(4):  # sumi:1~4 //hasi:5~14 //naka:15~25
    mapping_text2_1sumi[a2] = tkinter.Label(
        tki_map, text="")
    mapping_text2_1sumi[a2].place(
        x=mapping_text2_1sumi_pos_list[a2], y=mapping_text2_1sumi_pos_list[a2+4]+40, width=20)
    mapping_text2_2sumi[a2] = tkinter.Label(
        tki_map, text="")
    mapping_text2_2sumi[a2].place(
        x=mapping_text2_1sumi_pos_list[a2]+50, y=mapping_text2_1sumi_pos_list[a2+4]+40, width=20)
for a2 in range(10):
    mapping_text2_1hasi[a2] = tkinter.Label(
        tki_map, text="")
    mapping_text2_1hasi[a2].place(
        x=mapping_text2_1hasi_pos_list[a2], y=mapping_text2_1hasi_pos_list[a2+10]+40, width=20)
    mapping_text2_2hasi[a2] = tkinter.Label(
        tki_map, text="")
    mapping_text2_2hasi[a2].place(
        x=mapping_text2_1hasi_pos_list[a2]+50, y=mapping_text2_1hasi_pos_list[a2+10]+40, width=20)
for a2 in range(11):
    mapping_text2_1naka[a2] = tkinter.Label(
        tki_map, text="")
    mapping_text2_1naka[a2].place(
        x=mapping_text2_1naka_pos_list[a2], y=mapping_text2_1naka_pos_list[a2+11]+40, width=20)
    mapping_text2_2naka[a2] = tkinter.Label(
        tki_map, text="")
    mapping_text2_2naka[a2].place(
        x=mapping_text2_1naka_pos_list[a2]+50, y=mapping_text2_1naka_pos_list[a2+11]+40, width=20)
# 勾玉
for a3 in range(4):
    mapping_text3_1sumi[a3] = tkinter.Label(
        tki_map, text="")
    mapping_text3_1sumi[a3].place(
        x=mapping_text2_1sumi_pos_list[a3], y=mapping_text2_1sumi_pos_list[a3+4]+80, width=20)
    mapping_text3_2sumi[a3] = tkinter.Label(
        tki_map, text="")
    mapping_text3_2sumi[a3].place(
        x=mapping_text2_1sumi_pos_list[a3]+50, y=mapping_text2_1sumi_pos_list[a3+4]+80, width=20)
for a3 in range(10):
    mapping_text3_1hasi[a3] = tkinter.Label(
        tki_map, text="")
    mapping_text3_1hasi[a3].place(
        x=mapping_text2_1hasi_pos_list[a3], y=mapping_text2_1hasi_pos_list[a3+10]+80, width=20)
    mapping_text3_2hasi[a3] = tkinter.Label(
        tki_map, text="")
    mapping_text3_2hasi[a3].place(
        x=mapping_text2_1hasi_pos_list[a3]+50, y=mapping_text2_1hasi_pos_list[a3+10]+80, width=20)
for a3 in range(11):
    mapping_text3_1naka[a3] = tkinter.Label(
        tki_map, text="")
    mapping_text3_1naka[a3].place(
        x=mapping_text2_1naka_pos_list[a3], y=mapping_text2_1naka_pos_list[a3+11]+80, width=20)
    mapping_text3_2naka[a3] = tkinter.Label(
        tki_map, text="")
    mapping_text3_2naka[a3].place(
        x=mapping_text2_1naka_pos_list[a3]+50, y=mapping_text2_1naka_pos_list[a3+11]+80, width=20)
###---------------------------------------------------------------------------------------------------------------###
# テキスト入力欄作成
for lx in range(5):
    for ly in range(5):
        # エリア
        mapping_text1 = tkinter.Label(tki_map, text="エリア", bg="#00FFFF")
        mapping_text1.place(x=70+lx*200, y=80+ly*140, width=30)
        # 瓦礫
        mapping_text2_3 = tkinter.Label(tki_map, text="瓦礫", bg="#FF1A6F")
        mapping_text2_3.place(x=70+lx*200, y=120+ly*140, width=30)
        # 勾玉
        mapping_text3_3 = tkinter.Label(tki_map, text="勾玉", bg="#7CFC00")
        mapping_text3_3.place(x=70+lx*200, y=160+ly*140, width=30)
        # /
        mapping_text4_1 = tkinter.Label(tki_map, text="/", width=10, bg="gray")
        mapping_text4_1.place(x=140+lx*200, y=120+ly*140, width=10)
        mapping_text4_2 = tkinter.Label(tki_map, text="/", width=10, bg="gray")
        mapping_text4_2.place(x=140+lx*200, y=160+ly*140, width=10)
###---------------------------------------------------------------------------------------------------------------###


def btn_click_gareki_min(lx):  # lx = 0~24
    def aaa():
        btn_click_get()
        print("gareki-btn-click-lx", lx)
        if 0 <= lx <= 3:
            B2_1_sumi[lx] = int(B2_1_sumi[lx])-1
        elif 4 <= lx <= 13:
            B2_1_hasi[lx-4] = int(B2_1_hasi[lx-4])-1
        elif 14 <= lx <= 24:
            B2_1_naka[lx-4] = int(B2_1_naka[lx-4])-1
        map_kousin(lx)
    return aaa


def btn_click_magatama_min(lx):
    def bbb():
        btn_click_get()
        print("magatama-btn-click-lx", lx)
        if 0 <= lx <= 3:
            B3_1_sumi[lx] = int(B3_1_sumi[lx])-1
        elif 4 <= lx <= 13:
            print("ここ勾玉", B3_1_hasi)
            B3_1_hasi[lx-4] = int(B3_1_hasi[lx-4])-1
        elif 14 <= lx <= 24:
            B3_1_naka[lx-14] = int(B3_1_naka[lx-14])-1
        map_kousin(lx)
    return bbb


def btn_click_get():
    global B2_1_sumi, B3_1_sumi, B2_1_hasi, B3_1_hasi, B2_1_naka, B3_1_naka
    B2_1_sumi = [0]*4
    B3_1_sumi = [0]*4
    B2_1_hasi = [0]*10
    B3_1_hasi = [0]*10
    B2_1_naka = [0]*11
    B3_1_naka = [0]*11
    for g1 in range(4):
        #print("get-lblsumi text-befot", mapping_text2_1sumi[g1].cget("text"))
        #print("get-B2-befor", B2_1_sumi)
        B2_1_sumi[g1] = mapping_text2_1sumi[g1].cget("text")
        B3_1_sumi[g1] = mapping_text3_1sumi[g1].cget("text")
        #print("get-lblsumi text-after", mapping_text2_1sumi[g1].cget("text"))
        #print("get-B2-after", B2_1_sumi)
    for g1 in range(10):
        B2_1_hasi[g1] = mapping_text2_1hasi[g1].cget("text")
        B3_1_hasi[g1] = mapping_text3_1hasi[g1].cget("text")
    for g1 in range(11):
        B2_1_naka[g1] = mapping_text2_1naka[g1].cget("text")
        B3_1_naka[g1] = mapping_text3_1naka[g1].cget("text")


def map_kousin(lx):  # 0~24の数字が入るため-4や-14を使用。また、1つ更新するのに他のも更新するため未選択があるとエラーが出てしまうためそれ以降の処理ができていない！！！(要修正)
    print("ここ前 : lx", lx)
    print("ここ前 : B2_1_sumi", B2_1_sumi)
    print("ここ前 : B2_1_hasi", B2_1_hasi)
    # print("ここ前 : mapping_text2_1sumi[lx]['text']",mapping_text2_1sumi[lx]["text"])
    # print("ここ前 : mapping_text2_1hasi[lx-4]['text']",mapping_text2_1hasi[lx-4]["text"])
    if 0 <= lx <= 3:
        mapping_text2_1sumi[lx]["text"] = B2_1_sumi[lx]
        mapping_text3_1sumi[lx]["text"] = B3_1_sumi[lx]
    elif 4 <= lx <= 13:
        mapping_text2_1hasi[lx-4]["text"] = B2_1_hasi[lx-4]
        mapping_text3_1hasi[lx-4]["text"] = B3_1_hasi[lx-4]
    elif 14 <= lx <= 24:
        mapping_text2_1naka[lx-14]["text"] = B2_1_naka[lx-14]
        mapping_text3_1naka[lx-14]["text"] = B3_1_naka[lx-14]
    print("ここ後 : B2_1_sumi", B2_1_sumi)
    print("ここ後 : B2_1_hasi", B2_1_hasi)
    print("ここ後 : mapping_text2_1sumi[lx]['text']",
          mapping_text2_1sumi[lx]["text"])
    print("ここ後 : mapping_text2_1hasi[lx-4]['text']",
          mapping_text2_1hasi[lx-4]["text"])


# -1ボタン作成
print("1")
for lx in range(4):
    mapping_btn_min_B2_1_sumi = tkinter.Button(
        tki_map, text="-1", command=btn_click_gareki_min(lx))
    mapping_btn_min_B2_1_sumi.place(
        x=mapping_text2_1sumi_pos_list[lx]+80, y=mapping_text2_1sumi_pos_list[lx+4]+40, width=40)
    mapping_btn_min_B3_1_sumi = tkinter.Button(
        tki_map, text="-1", command=btn_click_magatama_min(lx))
    mapping_btn_min_B3_1_sumi.place(
        x=mapping_text2_1sumi_pos_list[lx]+80, y=mapping_text2_1sumi_pos_list[lx+4]+80, width=40)
print("2")
for lx in range(10):
    mapping_btn_min_B2_1_hasi = tkinter.Button(
        tki_map, text="-1", command=btn_click_gareki_min(lx+4))
    mapping_btn_min_B2_1_hasi.place(
        x=mapping_text2_1hasi_pos_list[lx]+80, y=mapping_text2_1hasi_pos_list[lx+10]+40, width=40)
    mapping_btn_min_B3_1_hasi = tkinter.Button(
        tki_map, text="-1", command=btn_click_magatama_min(lx+4))
    mapping_btn_min_B3_1_hasi.place(
        x=mapping_text2_1hasi_pos_list[lx]+80, y=mapping_text2_1hasi_pos_list[lx+10]+80, width=40)
for lx in range(11):
    mapping_btn_min_B2_1_naka = tkinter.Button(
        tki_map, text="-1", command=btn_click_gareki_min(lx+14))
    mapping_btn_min_B2_1_naka.place(
        x=mapping_text2_1naka_pos_list[lx]+80, y=mapping_text2_1naka_pos_list[lx+11]+40, width=40)
    mapping_btn_min_B3_1_naka = tkinter.Button(
        tki_map, text="-1", command=btn_click_magatama_min(lx+14))
    mapping_btn_min_B3_1_naka.place(
        x=mapping_text2_1naka_pos_list[lx]+80, y=mapping_text2_1naka_pos_list[lx+11]+80, width=40)
# 下に合計値ラベル出力
# 1度だけ実行
mapping_area_goukei = tkinter.Label(
    tki_map, text=f"エリア数 : {i_area_cnt} / {i_area_max}", width=15, bg="#00FFFF", font=("", 30))
mapping_area_goukei.place(x=1100, y=400)
mapping_gareki_goukei = tkinter.Label(
    tki_map, text=f"瓦礫数 : {i_gareki_cnt} / {i_gareki_max}", width=15, bg="#FF1A6F", font=("", 30))
mapping_gareki_goukei.place(x=1100, y=450)
mapping_magatama_goukei = tkinter.Label(
    tki_map, text=f"勾玉数 : {i_magatama_cnt} / {i_magatama_max}", width=15, bg="#7CFC00", font=("", 30))
mapping_magatama_goukei.place(x=1100, y=500)
##############################################################################################
##################################################################################################
# エリア候補名
# 霊魂の淵叢
area_reikon_name_sumi_1 = ["1鍵付き水門エリア",
                           "2棚迷路エリア", "3階段横勾玉エリア", "4水門3連レバーエリア"]
area_reikon_name_hasi_1 = ["飛び出し泣き女エリア", "地下移動神楽鈴罠エリア", "ダブル勾玉エリア",
                           "レバー無料勾玉泣き女", "長通路神楽鈴罠エリア", "シンメトリーダルダルエリア", "祭壇泣き女瓦礫ハメ", "細い板から落ちるエリア", "大勾玉エリア", "障子に登れるエリア"]
area_reikon_name_naka_1 = ["スタート地点", "固定女瓦礫ハメエリア", "神楽鈴競争罠エリア", "瓦礫階段手鏡ワープエリア",
                           "中央泣き女H字エリア", "聖域入口レバーエリア", "光石エリア", "木の板先に確定鍵エリア", "水路ゴミエリア", "H字神楽鈴罠エリア", "2階U字エリア"]

var_sumi = combo_sumi = [0]*4
var_hasi = combo_hasi = [0]*10
var_naka = combo_naka = [0]*11

area_reikon_gareki = [0, 1, 0, 1, 2, 0, 0, 0, 0,
                      0, 1, 2, 0, 0, 0, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0]
area_reikon_magatama = [1, 1, 1, 1, 1, 1, 2, 1, 1,
                        1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# コンボボックス作成
# sumi //左上、左下、右上、右下
list_co_sumi = [110, 110, 910, 910, 80, 640, 80, 640]

for i_co_sumi in range(4):
    var_sumi[i_co_sumi] = tkinter.StringVar()
    combo_sumi[i_co_sumi] = tkinter.ttk.Combobox(
        tki_map, values=area_reikon_name_sumi_1, textvariable=var_sumi[i_co_sumi], state="readonly")
    combo_sumi[i_co_sumi].bind("<<ComboboxSelected>>", area_get_sumi)
    combo_sumi[i_co_sumi].place(
        x=list_co_sumi[i_co_sumi], y=list_co_sumi[i_co_sumi+4])
# hasi //左3つ、右3つ、上2、下2
list_co_hasi = [110, 110, 110, 910, 910, 910, 310, 710, 310,
                710, 220, 360, 500, 220, 360, 500, 80, 80, 640, 640]
for i_co_hasi in range(10):
    var_hasi[i_co_hasi] = tkinter.StringVar()
    combo_hasi[i_co_hasi] = tkinter.ttk.Combobox(
        tki_map, values=area_reikon_name_hasi_1, textvariable=var_hasi[i_co_hasi], state="readonly")
    combo_hasi[i_co_hasi].bind("<<ComboboxSelected>>", area_get_hasi)
    combo_hasi[i_co_hasi].place(
        x=list_co_hasi[i_co_hasi], y=list_co_hasi[i_co_hasi+10])
# naka //左、右、中央縦列
list_co_naka = [310, 310, 310, 710, 710, 710, 510, 510, 510,
                510, 510, 220, 360, 500, 220, 360, 500, 80, 220, 360, 500, 640]
for i_co_naka in range(11):
    var_naka[i_co_naka] = tkinter.StringVar()
    combo_naka[i_co_naka] = tkinter.ttk.Combobox(
        tki_map, values=area_reikon_name_naka_1, textvariable=var_naka[i_co_naka], state="readonly")
    combo_naka[i_co_naka].bind("<<ComboboxSelected>>", area_get_naka)
    combo_naka[i_co_naka].place(
        x=list_co_naka[i_co_naka], y=list_co_naka[i_co_naka+11])


# 画面をそのまま表示
tki.mainloop()
