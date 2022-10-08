import time, cv2
from djitellopy import Tello

"""
qrコード探して、ポイント加算して、表示して、飛ばす

w=前に
s=後ろに
a=反時計周り
d=時計回り
t=離陸
l=着陸
esc=テロ制御の終了
"""

#a
change_kando=1#変えるやつ


cap=cv2.VideoCapture(1,cv2.CAP_DSHOW)

class FlightDroneClass():
    def __init__(self):
        #self.movesize = 70
        
        self.players = []

        #プレイ時間初期値
        self.gameTime = 30
        #QRコード読み込む準備
        self.qrDetector = cv2.QRCodeDetector()
        #ドローン準備
        self.tello = Tello()
        #メインループ
        self.whileCheck = True

    #接続開始
    def start(self):
        #a
        if change_kando==1:
            self.kando1=20
            self.kando2=30
            self.kando3=40
        elif change_kando==2:
            self.kando1=30
            self.kando2=50
            self.kando3=70
        elif change_kando==3:
            self.kando1=40
            self.kando2=70
            self.kando3=100

        #ドローンとの接続
        self.tello.connect()

        #バッテリー残量取得
        print("battry="+str(self.tello.get_battery()))

        #画像取得開始
        self.tello.streamon()


    #飛行時間の取得
    def getPlayTime(self,playTime):
        self.gameTime = playTime

    #画像取得、点数計算 
    def getImage(self):
        #ドローンからの画像の取得
        self.image = self.tello.get_frame_read().frame
        #QRコード読み取り
        data,bbox,rectifiedImage = self.qrDetector.detectAndDecode(self.image)

        #点数の計算、タイマーリセット
        if data:
            print(data)#qrコードの内容
                hight = 1
                for i in self.players:
                    #点数追加、タイマーリセット
                    if data == i[0]:
                    if time.time()-i[3]>=5 :
                        self.players[hight - 1][1] = self.players[hight - 1][1] + 1
                        self.players[hight - 1][3]=time.time()
                        return
                    hight = hight + 1
                #新規登録
            self.players.append([data,1,(50*hight),time.time()])

                


    #ディスプレイに表示
    def displayScreen(self) :
            print("players:")
            print(self.players)
            #点数表示の準備
            cv2.putText(self.image, (str(self.gameTime  - int(time.time()-self.timeStart)) + "seconds left"), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
            for i in self.players:
                cv2.putText(self.image, (i[0] + ":" +str(i[1])), (0, 50 + i[2]), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
            #表示
            cv2.imshow('SEE-DRO FIGHT!', self.image)
            
    #キーボード操作
    def droneControl(self,key):#left,rigth   back,foward   up,down   cw,ccw

        if key==-1:
            if ((time.time())-self.cont_time)>=0.8:
                self.tello.send_rc_control(0,0,0,0)

        if key==ord("w"):
            self.tello.send_rc_control(0,self.movesize,0,0)
            self.cont_time=time.time()

        elif key==ord('s'):
            self.tello.send_rc_control(0,-self.movesize,0,0)
            self.cont_time=time.time()

        elif key==ord("d"):
            self.tello.send_rc_control(self.movesize,0,0,0)
            self.cont_time=time.time()

        elif key==ord("a"):
            self.tello.send_rc_control(-self.movesize,0,0,0)
            self.cont_time=time.time()

        elif key==ord('e'):
            self.tello.send_rc_control(0,0,0,self.movesize)
            self.cont_time=time.time()

        elif key==ord('q'):
            self.tello.send_rc_control(0,0,0,-self.movesize)
            self.cont_time=time.time()

        elif key==ord('u'):
            self.tello.send_rc_control(0,0,10,0)
            self.cont_time=time.time()

        elif key==ord('j'):
            self.tello.send_rc_control(0,0,-10,0)
            self.cont_time=time.time()

        elif key==ord('t'):
            self.tello.takeoff()

        elif key==ord('l'):
            self.tello.land()

        elif key==ord('1'):
            self.movesize=50

        elif key==ord('2'):
            self.movesize=70
        
        elif key==ord('3'):
            self.movesize=100


        elif key==27:#27はEsc
            print("esc has pressed")
            self.displayTotalScore()
            self.tello.land()
            

    
    #時間制限で終了
    def quitScreen(self):
        #print(time.time()-self.timeStart)
        if time.time()-self.timeStart>=self.gameTime :
            self.displayTotalScore()
            self.tello.land()

    #リザルト表示
    def displayTotalScore(self) :
        self.image = self.tello.get_frame_read().frame
        #合計点数
        points = 0
        for i in self.players:
            points = points + i[1]
        #合計スコア表示
        cv2.putText(self.image, ("Total score:" + str(points)), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
        #各プレイヤーの点数表示
        for i in self.players:
                cv2.putText(self.image, (i[0] + ":" +str(i[1])), (0, 50 + i[2]), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
        
        cv2.imshow('SEE-DRO FIGHT!', self.image)
            

    def main(self):
        #タイマー開始
        self.cont_time=time.time()
        self.timePoint = time.time()#点数
        self.timeStart = time.time()#時間制限

        while self.whileCheck:
            self.getImage()#画像の取得、QRコードの読み取り
            self.displayScreen()#ドローンからの画像の表示

            #キー入力の受けとり、ドローンの操作
            key = cv2.waitKey(30)
            self.droneControl(key)

            self.quitScreen()#時間制限
        cv2.destroyAllWindows()
        return