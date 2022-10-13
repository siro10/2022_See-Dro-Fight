import tkinter as tk
from tkinter import *
import sys
import pygame
import time
import drone

############################################################################################
timeset=1 #ゲーム時間の初期値
volume=1.0#音量の初期値、音量関係は後でプログラミング
point=0#ゲームポイント初期ポイント
member_count=1#人数入力したかどうか
gamemode_count=0#ボタン降下時のカウント
gamemodenow=2#選択中のゲームモード
memcount=2#逃げる人の数
pygame.mixer.init(frequency = 44100)    # 初期設定
pygame.mixer.music.load(".//images//決定ボタンを押す34.mp3")     # 音楽ファイルの読み込み
droneFight = drone.FlightDrone()#ドローンプログラムの準備
########################################################################################################
    

def frame_change(frame):
    global volume
    frame.tkraise()#フレーム切り替え
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(volume)

def frame_change2(frame,frame2):
    global volume
    frame.tkraise()#フレーム切り替え
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(volume)
    time.sleep(5)
    frame2.tkraise()#フレーム切り替え
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(volume)



def Volume_change(waven):#ボリュームを変える
    global wave0_img,wave1_img,wave2_img,wave3_img,wave4_img,volume
    if waven==0:
        wave0_img = PhotoImage(file = f".//images//wave0-2.png")
        wave0 = Button(frame_setting,image = wave0_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(0),relief = "flat")

        wave0.place(x = 172, y = 175,width = 82,height = 82)

        wave1_img = PhotoImage(file = f".//images//wave1-2.png")
        wave1 = Button(frame_setting,image = wave1_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(1),relief = "flat")

        wave1.place(x = 325, y = 183,width = 38,height = 65)

        wave2_img = PhotoImage(file = f".//images//wave2-2.png")
        wave2 = Button(frame_setting,image = wave2_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(2),relief = "flat")

        wave2.place(x = 434, y = 175,width = 46,height = 89)

        wave3_img = PhotoImage(file = f".//images//wave3-2.png")
        wave3 = Button(frame_setting,image = wave3_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(3),relief = "flat")

        wave3.place(x = 551, y = 166,width = 55,height = 100)

        wave4_img = PhotoImage(file = f".//images//wave4-2.png")
        wave4 = Button(frame_setting,image = wave4_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(4),relief = "flat")

        wave4.place(x = 677, y = 156,width = 64,height = 128)

        volume=0.0
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(volume)

    elif waven==1:
        wave0_img = PhotoImage(file = f".//images//wave0-1.png")
        wave0 = Button(frame_setting,image = wave0_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(0),relief = "flat")

        wave0.place(x = 172, y = 175,width = 82,height = 82)

        wave1_img = PhotoImage(file = f".//images//wave1-1.png")
        wave1 = Button(frame_setting,image = wave1_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(1),relief = "flat")

        wave1.place(x = 325, y = 183,width = 38,height = 65)

        wave2_img = PhotoImage(file = f".//images//wave2-2.png")
        wave2 = Button(frame_setting,image = wave2_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(2),relief = "flat")

        wave2.place(x = 434, y = 175,width = 46,height = 89)

        wave3_img = PhotoImage(file = f".//images//wave3-2.png")
        wave3 = Button(frame_setting,image = wave3_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(3),relief = "flat")

        wave3.place(x = 551, y = 166,width = 55,height = 100)

        wave4_img = PhotoImage(file = f".//images//wave4-2.png")
        wave4 = Button(frame_setting,image = wave4_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(4),relief = "flat")

        wave4.place(x = 677, y = 156,width = 64,height = 128)

        volume=0.1
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(volume)
    elif waven==2:
        wave0_img = PhotoImage(file = f".//images//wave0-1.png")
        wave0 = Button(frame_setting,image = wave0_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(0),relief = "flat")

        wave0.place(x = 172, y = 175,width = 82,height = 82)

        wave1_img = PhotoImage(file = f".//images//wave1-1.png")
        wave1 = Button(frame_setting,image = wave1_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(1),relief = "flat")

        wave1.place(x = 325, y = 183,width = 38,height = 65)

        wave2_img = PhotoImage(file = f".//images//wave2-1.png")
        wave2 = Button(frame_setting,image = wave2_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(2),relief = "flat")

        wave2.place(x = 434, y = 175,width = 46,height = 89)

        wave3_img = PhotoImage(file = f".//images//wave3-2.png")
        wave3 = Button(frame_setting,image = wave3_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(3),relief = "flat")

        wave3.place(x = 551, y = 166,width = 55,height = 100)

        wave4_img = PhotoImage(file = f".//images//wave4-2.png")
        wave4 = Button(frame_setting,image = wave4_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(4),relief = "flat")

        wave4.place(x = 677, y = 156,width = 64,height = 128)

        volume=0.3
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(volume)
    elif waven==3:
        wave0_img = PhotoImage(file = f".//images//wave0-1.png")
        wave0 = Button(frame_setting,image = wave0_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(0),relief = "flat")

        wave0.place(x = 172, y = 175,width = 82,height = 82)

        wave1_img = PhotoImage(file = f".//images//wave1-1.png")
        wave1 = Button(frame_setting,image = wave1_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(1),relief = "flat")

        wave1.place(x = 325, y = 183,width = 38,height = 65)

        wave2_img= PhotoImage(file = f".//images//wave2-1.png")
        wave2 = Button(frame_setting,image = wave2_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(2),relief = "flat")

        wave2.place(x = 434, y = 175,width = 46,height = 89)

        wave3_img = PhotoImage(file = f".//images//wave3-1.png")
        wave3 = Button(frame_setting,image = wave3_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(3),relief = "flat")

        wave3.place(x = 551, y = 166,width = 55,height = 100)

        wave4_img = PhotoImage(file = f".//images//wave4-2.png")
        wave4 = Button(frame_setting,image = wave4_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(4),relief = "flat")

        wave4.place(x = 677, y = 156,width = 64,height = 128)

        volume=0.5
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(volume)
    elif waven==4:
        wave0_img = PhotoImage(file = f".//images//wave0-1.png")
        wave0 = Button(frame_setting,image = wave0_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(0),relief = "flat")

        wave0.place(x = 172, y = 175,width = 82,height = 82)

        wave1_img = PhotoImage(file = f".//images//wave1-1.png")
        wave1 = Button(frame_setting,image = wave1_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(1),relief = "flat")

        wave1.place(x = 325, y = 183,width = 38,height = 65)

        wave2_img = PhotoImage(file = f".//images//wave2-1.png")
        wave2 = Button(frame_setting,image = wave2_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(2),relief = "flat")

        wave2.place(x = 434, y = 175,width = 46,height = 89)

        wave3_img = PhotoImage(file = f".//images//wave3-1.png")
        wave3 = Button(frame_setting,image = wave3_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(3),relief = "flat")

        wave3.place(x = 551, y = 166,width = 55,height = 100)

        wave4_img = PhotoImage(file = f".//images//wave4-1.png")
        wave4 = Button(frame_setting,image = wave4_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(4),relief = "flat")

        wave4.place(x = 677, y = 156,width = 64,height = 128)

        volume=1.0
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(volume)
    else:
        pass

def kando_change(kando):#感度を変える
    global kando0_img,kando1_img,kando2_img
    if kando==0:
        kando0_img = PhotoImage(file = f".//images//kando1-1.png")
        kando0 = Button(frame_setting,image = kando0_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(0),relief = "flat")

        kando0.place(x = 181, y = 420,width = 121,height = 126)

        kando1_img = PhotoImage(file = f".//images//kando2-2.png")
        kando1 = Button(frame_setting,image = kando1_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(1),relief = "flat")

        kando1.place(x = 366, y = 421,width = 121,height = 126)

        kando2_img = PhotoImage(file = f".//images//kando3-2.png")
        kando2 = Button(frame_setting,image = kando2_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(2),relief = "flat")

        kando2.place(x = 551, y = 420,width = 121,height = 126)
        droneFight.getReactionSensitivity(0)
    elif kando==1:
        kando0_img = PhotoImage(file = f".//images//kando1-2.png")
        kando0 = Button(frame_setting,image = kando0_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(0),relief = "flat")

        kando0.place(x = 181, y = 420,width = 121,height = 126)

        kando1_img = PhotoImage(file = f".//images//kando2-1.png")
        kando1 = Button(frame_setting,image = kando1_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(1),relief = "flat")

        kando1.place(x = 366, y = 421,width = 121,height = 126)

        kando2_img = PhotoImage(file = f".//images//kando3-2.png")
        kando2 = Button(frame_setting,image = kando2_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(2),relief = "flat")

        kando2.place(x = 551, y = 420,width = 121,height = 126)
        droneFight.getReactionSensitivity(1)
    elif kando==2:
        kando0_img = PhotoImage(file = f".//images//kando1-2.png")
        kando0 = Button(frame_setting,image = kando0_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(0),relief = "flat")

        kando0.place(x = 181, y = 420,width = 121,height = 126)

        kando1_img = PhotoImage(file = f".//images//kando2-2.png")
        kando1 = Button(frame_setting,image = kando1_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(1),relief = "flat")

        kando1.place(x = 366, y = 421,width = 121,height = 126)

        kando2_img = PhotoImage(file = f".//images//kando3-1.png")
        kando2 = Button(frame_setting,image = kando2_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(2),relief = "flat")

        kando2.place(x = 551, y = 420,width = 121,height = 126)
        droneFight.getReactionSensitivity(2)
    else:
        pass


def timeup():#制限時間を増やす
    global timeset,sankaku_img,sitasankaku_img,time_img
    if timeset==1:#0:30
        sitasankaku_img = PhotoImage(file = f".//images//sitasankaku.png")
        sitasankakkei = Button(frame_befodesetting,image = sitasankaku_img,borderwidth = 0,highlightthickness = 0,command =lambda:timedown(),relief = "flat")

        sitasankakkei.place(x = 806, y = 273,width = 98,height = 87)

        time_img = PhotoImage(file = f".//images//1.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset+1
        droneFight.getPlayTime(60)
    elif timeset==2:#1:00
        time_img = PhotoImage(file = f".//images//1.30.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset+1
        droneFight.getPlayTime(90)
    elif timeset==3:#1:30
        time_img = PhotoImage(file = f".//images//2.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset+1
        droneFight.getPlayTime(120)
    elif timeset==4:#2:00
        time_img = PhotoImage(file = f".//images//2.30.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset+1
        droneFight.getPlayTime(150)
    elif timeset==5:#2:30
        time_img = PhotoImage(file = f".//images//3.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset+1
        droneFight.getPlayTime(180)
    elif timeset==6:#3:00
        sankaku_img = PhotoImage(file = f".//images//sankakukuro.png")
        sankakkei = Button(frame_befodesetting,image = sankaku_img,borderwidth = 0,highlightthickness = 0,relief = "flat")
        droneFight.getPlayTime(300)
        

        sankakkei.place(x = 340, y = 273,width = 98,height = 87)
        time_img = PhotoImage(file = f".//images//5.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset+1
    else:
        pass


def timedown():#制限時間を減らす
    global timeset,sankaku_img,sitasankaku_img,time_img
    if timeset==7:#5.00
        time_img = PhotoImage(file = f".//images//3.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        sankaku_img = PhotoImage(file = f".//images//sankaku.png")
        sankakkei = Button(frame_befodesetting,image = sankaku_img,borderwidth = 0,highlightthickness = 0,command = lambda:timeup(),relief = "flat")
        droneFight.getPlayTime(180)

        sankakkei.place(x = 340, y = 273,width = 98,height = 87)
        timeset=timeset-1
    elif timeset==6:#3.00
        time_img = PhotoImage(file = f".//images//2.30.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset-1
        droneFight.getPlayTime(150)
    elif timeset==5:#2.30
        time_img = PhotoImage(file = f".//images//2.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset-1
        droneFight.getPlayTime(120)
    elif timeset==4:#2.00
        time_img = PhotoImage(file = f".//images//1.30.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset-1
        droneFight.getPlayTime(90)
    elif timeset==3:#1.30
        time_img = PhotoImage(file = f".//images//1.00.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        timeset=timeset-1
        droneFight.getPlayTime(60)
    elif timeset==2:#1.00
        sitasankaku_img = PhotoImage(file = f".//images//sitasankakukuro.png")
        sitasankakkei = Button(frame_befodesetting,image = sitasankaku_img,borderwidth = 0,highlightthickness = 0,relief = "flat")
        droneFight.getPlayTime(30)

        sitasankakkei.place(x = 806, y = 273,width = 98,height = 87)
        time_img = PhotoImage(file = f".//images//0.30.png")
        timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)
        
        timeset=timeset-1
    else:
        pass


def gamemode_change(muki):#ゲームモードを変える
    global gamemode_count,Gamemodechoose_img,gamemodenow,member_count
    frame_change(frame_gamemode)
    #さいしょはAll Together
    if muki==1:#みぎさんかく
        if gamemode_count%2==0:#All Togetherのとき
            Gamemodechoose_img = PhotoImage(file = f".//images//Two players.png")
            b2 = Button(frame_gamemode, image = Gamemodechoose_img, borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_syou2),relief = "flat")

            b2.place(x = 415, y = 275,width = 450,height = 80)
            gamemode_count=gamemode_count+1
            gamemodenow=1
            droneFight.getPlayerNumbers(1)
        elif gamemode_count%2==1:#Two playersのとき
            Gamemodechoose_img = PhotoImage(file = f".//images//All Together.png")
            b2 = Button(frame_gamemode, image = Gamemodechoose_img, borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_syou1),relief = "flat")

            b2.place(x = 415, y = 275,width = 450,height = 80)
            gamemode_count=gamemode_count+1
            gamemodenow=2
            droneFight.getPlayerNumbers(2)
        else:
            pass
    elif muki==-1:#ひだりさんかく
        if gamemode_count%2==0:#All Together
            Gamemodechoose_img = PhotoImage(file = f".//images//Two players.png")
            b2 = Button(frame_gamemode, image = Gamemodechoose_img, borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_syou2),relief = "flat")

            b2.place(x = 415, y = 275,width = 450,height = 80)
            gamemode_count=gamemode_count-1
            gamemodenow=1
            droneFight.getPlayerNumbers(1)
        elif gamemode_count%2==1:#Two players
            Gamemodechoose_img = PhotoImage(file = f".//images//All Together.png")
            b2 = Button(frame_gamemode, image = Gamemodechoose_img, borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_syou1),relief = "flat")

            b2.place(x = 415, y = 275,width = 450,height = 80)
            gamemode_count=gamemode_count-1
            gamemodenow=2
            droneFight.getPlayerNumbers(2)
        else:
            pass
    

def pointimage_change():#リザルト画面のポイントを変える　変数pointに入っている値をドット絵で表示する
    global point,niketa_img,itiketa_img
    if 0<=point<=99:
        if point//10==0:
            niketa_img = PhotoImage(file = f".//images//0_dot.png")
        elif point//10==1:
            niketa_img = PhotoImage(file = f".//images//1_dot.png")
        elif point//10==2:
            niketa_img = PhotoImage(file = f".//images//2_dot.png")
        elif point//10==3:
            niketa_img = PhotoImage(file = f".//images//3_dot.png")
        elif point//10==4:
            niketa_img = PhotoImage(file = f".//images//4_dot.png")
        elif point//10==5:
            niketa_img = PhotoImage(file = f".//images//5_dot.png")
        elif point//10==6:
            niketa_img = PhotoImage(file = f".//images//6_dot.png")
        elif point//10==7:
            niketa_img = PhotoImage(file = f".//images//7_dot.png")
        elif point//10==8:
            niketa_img = PhotoImage(file = f".//images//8_dot.png")
        elif point//10==9:
            niketa_img = PhotoImage(file = f".//images//9_dot.png")
        else:
            niketa_img = PhotoImage(file = f".//images//0_dot.png")
        
        if point%10==0:
            itiketa_img = PhotoImage(file = f".//images//0_dot.png")
        elif point%10==1:
            itiketa_img = PhotoImage(file = f".//images//1_dot.png")
        elif point%10==2:
            itiketa_img = PhotoImage(file = f".//images//2_dot.png")
        elif point%10==3:
            itiketa_img = PhotoImage(file = f".//images//3_dot.png")
        elif point%10==4:
            itiketa_img = PhotoImage(file = f".//images//4_dot.png")
        elif point%10==5:
            itiketa_img = PhotoImage(file = f".//images//5_dot.png")
        elif point%10==6:
            itiketa_img = PhotoImage(file = f".//images//6_dot.png")
        elif point%10==7:
            itiketa_img = PhotoImage(file = f".//images//7_dot.png")
        elif point%10==8:
            itiketa_img = PhotoImage(file = f".//images//8_dot.png")
        elif point%10==9:
            itiketa_img = PhotoImage(file = f".//images//9_dot.png")
        else:
            itiketa_img = PhotoImage(file = f".//images//0_dot.png")
    elif point>=99:
         niketa_img = PhotoImage(file = f".//images//9_dot.png")
         itiketa_img = PhotoImage(file = f".//images//9_dot.png")
    else:
        niketa_img = PhotoImage(file = f".//images//0_dot.png")
        itiketa_img = PhotoImage(file = f".//images//0_dot.png")

    itiketa=canvas_result.create_image(514+80,287+126,image=itiketa_img)#アンカーが画像の左端の場合、(514+80,287+126)

    niketa=canvas_result.create_image(317+80,287+126,image=niketa_img)#アンカーが画像の左端の場合、(317+80,287+126)



def member_change(muki):#メンバーの人数（逃げる人）を変える 変数mencountの数＝逃げる人の数
    global member_img,memcount
    if muki==1:
        if memcount==2:
            memcount=3
            member_img = PhotoImage(file = f".//images//3syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(3)
        elif memcount==3:
            memcount=4
            member_img = PhotoImage(file = f".//images//4syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(4)
        elif memcount==4:
            memcount=5
            member_img = PhotoImage(file = f".//images//5syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(5)
        elif memcount==5:
            memcount=2
            member_img = PhotoImage(file = f".//images//2syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(2)
        else:
            pass
    elif muki==-1:
        if memcount==5:
            memcount=4
            member_img = PhotoImage(file = f".//images//4syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(4)
        elif memcount==4:
            memcount=3
            member_img = PhotoImage(file = f".//images//3syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(3)
        elif memcount==3:
            memcount=2
            member_img = PhotoImage(file = f".//images//2syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(2)
        elif memcount==2:
            memcount=5
            member_img = PhotoImage(file = f".//images//5syou.png")
            member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)
            droneFight.getPlayerNumbers(5)
        else:
            pass
    else:
        print('memcount Error')

def frame_change3(frame1,frame2):#条件付きフレーム切り替え
    global member_count,gamemodenow
    if member_count==1 and gamemodenow==2:
        frame_change(frame1)
    elif member_count==2 and gamemodenow==2:
        frame_change(frame2)
    elif member_count==1 and gamemodenow==1:
        frame_change(frame2)
    elif member_count==2 and gamemodenow==1:
        frame_change(frame2)
    else:
        pass

def frame_change4(n,frame):#カウントを変えながらフレーム切り替え
    global member_count
    member_count=n
    frame_change(frame)


def frame_change5(n,frame):
    global member_count,memcount,gamemodenow,point
    print(droneFight.start())
    point = droneFight.main()
    pointimage_change()
    if gamemodenow==1:
        memcount=n
    frame_change(frame)

def frame_change6(n,frame):
    global memcount
    memcount=n
    frame_change(frame)


#ウィンドウの上にフレーム、その上にキャンバス、その上に写真やボタンやテキストを貼り付ける　順番もこれ
    
root = tk.Tk()
root.title('SEE-DRO FIGHT!')#ウィンドウの作成、貼り付け

root.geometry("1280x720")#ウィンドウの大きさ
root.configure(bg = "#ffffff")

frame_title=tk.Frame(root,height = 720,width = 1280)#タイトル画面のフレーム作成、貼り付け(ウィンドウに貼り付け、以下のフレームも同様)
frame_title.grid(row=0,column=0,sticky='nsew')

frame_setting=tk.Frame(root,height = 720,width = 1280)#設定画面のフレーム
frame_setting.grid(row=0,column=0,sticky='nsew')

frame_befodesetting=tk.Frame(root,height = 720,width = 1280)#タイトル画面でスタートを押した後の設定の画面(画面遷移のスライド参照)
frame_befodesetting.grid(row=0,column=0,sticky='nsew')#sticky='nsew'でウィンドウと同じ大きさまでフレームを引き延ばす

frame_gamemode=tk.Frame(root,height = 720,width = 1280)#ゲームモード選択画面
frame_gamemode.grid(row=0,column=0,sticky='nsew')

frame_syou1=tk.Frame(root,height = 75,width = 565)#ゲーム画面
#frame_syou1.grid(row=0,column=0)
frame_syou1.place(x=640-565/2,y=380)

frame_syou2=tk.Frame(root,height = 75,width = 565)#ゲーム画面
#frame_syou2.grid(row=0,column=0)
frame_syou2.place(x=640-565/2,y=380)

frame_tellowait=tk.Frame(root,height = 360,width = 640)
frame_tellowait.grid(row=0,column=0)

frame_game=tk.Frame(root,height = 720,width = 1280)#ゲーム画面
frame_game.grid(row=0,column=0,sticky='nsew')

frame_result=tk.Frame(root,height = 720,width = 1280)#リザルト画面
frame_result.grid(row=0,column=0,sticky='nsew')

frame_guide=tk.Frame(root,height = 720,width = 1280)#ガイド画面
frame_guide.grid(row=0,column=0,sticky='nsew')

frame_memberchange=tk.Frame(root,height = 500,width = 400)#人数調整画面
frame_memberchange.grid(row=0,column=0)



frame_change(frame_title)#最初のフレームはタイトル画面
################################################################################################################################フレームタイトル

###########
#start画面#
###########
canvas_title = Canvas(frame_title,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_title.place(x = 0, y = 0)

background1_img = PhotoImage(file = f".//images//background_title2.png")
background1 = canvas_title.create_image(640.0, 360.0,image=background1_img)

SATRT1_img = PhotoImage(file = f".//images//STARTButton2.png")#startボタン
START1 = Button(frame_title,image = SATRT1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_befodesetting),relief = "flat")

START1.place(x = 441, y = 450,width = 269,height = 88)

SETTING1_img = PhotoImage(file = f".//images//SETTINGButton2.png")#settingボタン
SETTING1 = Button(frame_title,image = SETTING1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_setting),relief = "flat")

SETTING1.place(x = 441, y = 558,width = 269,height = 88)

EXIT1_img = PhotoImage(file = f".//images//EXITButton2.png")#exit
EXIT1 = Button(frame_title,image = EXIT1_img,borderwidth = 0,highlightthickness = 0,command = sys.exit,relief = "flat")

EXIT1.place( x = 954, y = 580, width = 269, height = 88)

GUIDE1_img = PhotoImage(file = f".//images//GUIDEbutton.png")#guide
GUIDE1 = Button(frame_title,image = GUIDE1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_guide),relief = "flat")

GUIDE1.place( x = 20, y = 15, width = 60, height = 64)

######################################################################################################################フレームガイド
canvas = Canvas(frame_guide,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background2_img = PhotoImage(file = f".//images//background_guide.png")
background2 = canvas.create_image(640.0, 360.0,image=background2_img)

OK5_img = PhotoImage(file = f".//images//OKbutton5.png")
OK5 = Button(frame_guide,image = OK5_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_title),relief = "flat")

OK5.place(x = 931, y = 576,width = 242,height = 75)
######################################################################################################################フレームセッティング
##########
#設定#
##########

canvas_Setting = Canvas(frame_setting,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_Setting.place(x = 0, y = 0)

background3_img = PhotoImage(file = f".//images//background_setting.png")
background3 = canvas_Setting.create_image(640.0, 360.0,image=background3_img)

OK1_img = PhotoImage(file = f".//images//Okbutton.png")
OK = Button(frame_setting,image = OK1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_title),relief = "flat")

OK.place(x = 910, y = 553,width = 242,height = 75)

#img33 = PhotoImage(file = f".//images//ConnectButton.png")
#b33 = Button(frame_Setting,image = img33,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_tellowait),relief = "flat")

#b33.place(x = 902, y = 345,width = 257,height = 159)

###ボリューム

wave0_img = PhotoImage(file = f".//images//wave0-1.png")
wave0 = Button(frame_setting,image = wave0_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(0),relief = "flat")

wave0.place(x = 172, y = 175,width = 82,height = 82)

wave1_img = PhotoImage(file = f".//images//wave1-1.png")
wave1 = Button(frame_setting,image = wave1_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(1),relief = "flat")

wave1.place(x = 325, y = 183,width = 38,height = 65)

wave2_img = PhotoImage(file = f".//images//wave2-1.png")
wave2 = Button(frame_setting,image = wave2_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(2),relief = "flat")

wave2.place(x = 434, y = 175,width = 46,height = 89)

wave3_img = PhotoImage(file = f".//images//wave3-1.png")
wave3 = Button(frame_setting,image = wave3_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(3),relief = "flat")

wave3.place(x = 551, y = 166,width = 55,height = 100)

wave4_img = PhotoImage(file = f".//images//wave4-1.png")
wave4 = Button(frame_setting,image = wave4_img,borderwidth = 0,highlightthickness = 0,command = lambda:Volume_change(4),relief = "flat")

wave4.place(x = 677, y = 156,width = 64,height = 128)

####反応感度

kando0_img = PhotoImage(file = f".//images//kando1-1.png")
kando0 = Button(frame_setting,image = kando0_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(0),relief = "flat")

kando0.place(x = 181, y = 420,width = 121,height = 126)

kando1_img = PhotoImage(file = f".//images//kando2-2.png")
kando1 = Button(frame_setting,image = kando1_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(1),relief = "flat")

kando1.place(x = 366, y = 421,width = 121,height = 126)

kando2_img = PhotoImage(file = f".//images//kando3-2.png")
kando2 = Button(frame_setting,image = kando2_img,borderwidth = 0,highlightthickness = 0,command = lambda:kando_change(2),relief = "flat")

kando2.place(x = 551, y = 420,width = 121,height = 126)

########################################################################################################################フレームビフォーセッティング
###########
##startまえ　時計##
###########
canvas_BeforeSetting = Canvas(frame_befodesetting,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_BeforeSetting.place(x = 0, y = 0)

background4_img = PhotoImage(file = f".//images//background_beforesetting.png")
background4 = canvas_BeforeSetting.create_image(640.0, 360.0,image=background4_img)

############################

sankaku_img = PhotoImage(file = f".//images//sankaku.png")
sankakkei = Button(frame_befodesetting,image = sankaku_img,borderwidth = 0,highlightthickness = 0,command = lambda:timeup(),relief = "flat")

sankakkei.place(x = 340, y = 273,width = 98,height = 87)

sitasankaku_img = PhotoImage(file = f".//images//sitasankakukuro.png")
sitasankakkei = Button(frame_befodesetting,image = sitasankaku_img,borderwidth = 0,highlightthickness = 0,relief = "flat")

sitasankakkei.place(x = 806, y = 273,width = 98,height = 87)

time_img = PhotoImage(file = f".//images//0.30.png")
#timehyouzi = Button(frame_befodesetting,image = time_img,borderwidth = 0,highlightthickness = 0,relief = "flat")

#timehyouzi.place(x = 482, y = 273,width = 280,height = 87)
timehyuzi=canvas_BeforeSetting.create_image(622, 316.5,image=time_img)#482+140,273+43.5

#############################

#Connect1_img = PhotoImage(file = f".//images//ConnectButton.png")
#Connect1 = Button(frame_BeforeSetting,image = Connect1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_tellowait),relief = "flat")

#Connect1.place(x = 893, y = 476,width = 257,height = 159)

Back1_img = PhotoImage(file = f".//images//BackButton.png")
Back1 = Button(frame_befodesetting,image = Back1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_title),relief = "flat")

Back1.place(x = 110, y = 476,width = 255,height = 159)

NEXT1_img = PhotoImage(file = f".//images//NEXTbutton.png")
NEXT1 = Button(frame_befodesetting,image = NEXT1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change6(2,frame_gamemode),relief = "flat")

NEXT1.place(x = 860, y = 531,width = 300,height = 90)

########################################################################################################################ゲームモードの説明
#################
###ゲームモードの説明画面(2種)
##################
canvas_syou1 = Canvas(frame_syou1,bg = "#ffffff",height = 75,width = 565,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_syou1.place(x = 0, y = 0)

background5_img = PhotoImage(file = f".//images//background_syou1.png")
background5 = canvas_syou1.create_image(282.5, 37.5,image=background5_img)

canvas_syou2 = Canvas(frame_syou2,bg = "#ffffff",height = 75,width = 565,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_syou2.place(x = 0, y = 0)

background6_img = PhotoImage(file = f".//images//background_syou2.png")
background6 = canvas_syou2.create_image(282.5, 37.5,image=background6_img)

#######################################################################################################################フレーム注意書き
##########
###ゲーム前の注意書き
##########

canvas_gamemode = Canvas(frame_tellowait,bg = "#ffffff",height = 360,width = 640, bd = 0,highlightthickness = 0,relief = "ridge")
canvas_gamemode.place(x = 0, y = 0)

background7_img = PhotoImage(file = f".//images//background_tellowait.png")
background7 = canvas_gamemode.create_image(320.0, 180.0,image=background7_img)#大きさは640*360

OK2_img = PhotoImage(file = f".//images//OKButton2.png")
OK2 = Button(frame_tellowait,image = OK2_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change5(1,frame_result), relief = "flat")

OK2.place(x = 411, y = 258,width = 182,height = 56)

Back2_img = PhotoImage(file = f".//images//BACKButton2.png")
Back2 = Button(frame_tellowait,image = Back2_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_gamemode),relief = "flat")

Back2.place(x = 51, y = 258,width = 186,height = 56)


###################################################################################################################フレームゲームモード
########################
#####ゲームモード切り替え
########################
canvas_gamemode = Canvas(frame_gamemode,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_gamemode.place(x = 0, y = 0)

background8_img = PhotoImage(file = f".//images//background_gamemode.png")
background8 = canvas_gamemode.create_image(640.0, 360.0,image=background8_img)

hidarisankaku_img = PhotoImage(file = f".//images//hidarisankaku.png")
hidarisankaku = Button(frame_gamemode,image = hidarisankaku_img,borderwidth = 0,highlightthickness = 0,command = lambda:gamemode_change(-1),relief = "flat")

hidarisankaku.place(x = 302, y = 275,width = 72,height = 81)

migisankaku_img = PhotoImage(file = f".//images//migisankaku.png")
migisankaku = Button(frame_gamemode,image = migisankaku_img,borderwidth = 0,highlightthickness = 0,command = lambda:gamemode_change(1),relief = "flat")

migisankaku.place(x = 906, y = 275,width = 72,height = 81)

Gamemodechoose_img = PhotoImage(file = f".//images//All Together.png")
Gamemodechoose = Button( frame_gamemode,image = Gamemodechoose_img, borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_syou1),relief = "flat")

Gamemodechoose.place(x = 415, y = 275,width = 450,height = 80)

#img3 = PhotoImage(file = f".//images//Two players.png")
#b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = btn_clicked, relief = "flat")

#b3.place( x = 410, y = 161, width = 450, height = 80)

Connect1_img = PhotoImage(file = f".//images//ConnectButton.png")
Connect1 = Button(frame_gamemode,image = Connect1_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change3(frame_memberchange,frame_tellowait),relief = "flat")

Connect1.place(x = 893, y = 476,width = 257,height = 159)

BACK3_img = PhotoImage(file = f".//images//BACKbutton3.png")
BACK3 = Button(frame_gamemode,image = BACK3_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change4(1,frame_befodesetting),relief = "flat")

BACK3.place(x = 126, y = 531,width = 300,height = 90)
######################################################################################################################フレーム人数変更
########################
####All Together選択時の人数切り替え
#######################
canvas_memberchange = Canvas(frame_memberchange,bg = "#ffffff",height = 500,width = 400,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_memberchange.place(x = 0, y = 0)

background9_img = PhotoImage(file = f".//images//background_alltogetherselect.png")
background9 = canvas_memberchange.create_image(200.0, 250.0,image=background9_img)

sankaku2_img = PhotoImage(file = f".//images//sankaku2.png")
sankaku2 = Button(frame_memberchange,image = sankaku2_img,borderwidth = 0,highlightthickness = 0,command = lambda:member_change(1),relief = "flat")

sankaku2.place(x = 177, y = 140,width = 45,height = 40)

sitasankaku2_img = PhotoImage(file = f".//images//sitasankaku2.png")
sitasankaku2 = Button(frame_memberchange,image = sitasankaku2_img,borderwidth = 0,highlightthickness = 0,command = lambda:member_change(-1),relief = "flat")

sitasankaku2.place(x = 177, y = 312,width = 45,height = 40)

BACK5_img = PhotoImage(file = f".//images//BACKbutton5.png")
BACK5 = Button(frame_memberchange,image = BACK5_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change(frame_gamemode),relief = "flat")

BACK5.place(x = 17, y = 425,width = 167,height = 50)

OK4_img = PhotoImage(file = f".//images//OKbutton4.png")
OK4 = Button(frame_memberchange,image = OK4_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change4(2,frame_gamemode),relief = "flat")

OK4.place(x = 216, y = 425,width = 167,height = 50)

member_img = PhotoImage(file = f".//images//2syou.png")
#memeber = Button(frame_memberchange,image = member_img,borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")
#memeber.place(x = 170, y = 203,width = 60,height = 94)
member = canvas_memberchange.create_image(170+30, 203+47,image=member_img)

#######################################################################################################################フレームリザルト
#######################
###リザルト画面
#######################
canvas_result = Canvas(frame_result,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas_result.place(x = 0, y = 0)

background10_img = PhotoImage(file = f".//images//background_result.png")
background10 = canvas_result.create_image(640.0, 360.0,image=background10_img)

pointimage_change()


BACK4_img = PhotoImage(file = f".//images//BACKbutton4.png")

BACK4 = Button(frame_result,image = BACK4_img,borderwidth = 0,highlightthickness = 0,command = lambda:frame_change4(1,frame_title),relief = "flat")
BACK4.place( x = 926, y = 487, width = 256, height = 159)

####################################################################################################################################################

root.resizable(False, False)
root.mainloop()

#img30から
