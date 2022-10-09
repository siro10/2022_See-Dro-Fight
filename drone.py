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
        #プレイヤー点数初期値
        self.players = []

        #プレイ時間初期値
        self.gameTime = 30
        #QRコード読み込む準備
        self.qrDetector = cv2.QRCodeDetector()
        #ドローン準備
        self.tello = Tello()
        #メインループ
        self.whileCheck = True
        #動きの大きさ調整
        self.movesSize = 0
        #合計点
        self.totalPoints = 0
        #状態把握
        self.isLanding = True
        

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
        self.angle=30
        self.moveSize=self.kando1
        
        #ドローンとの接続
        try:
            self.tello.connect()
        except:
            return

        #バッテリー残量取得
        self.battrey=self.tello.get_battery()
        print("battry="+str(self.battery))

        #画像取得開始
        self.tello.streamon()

        #メインループ
        self.whileCheck = True
        #状態把握
        self.isLanding = True
        #プレイヤー点数初期化
        self.players = []
        #合計点
        self.totalPoints = 0
        #ウィンドウ削除
        cv2.destroyAllWindows()
        #タイマー開始
        self.cont_time=time.time()
        self.timePoint = time.time()#点数
        self.timeStart = time.time()#時間制限



    #飛行時間の取得
    def getPlayTime(self,playTime):
        self.gameTime = playTime

    #画像取得、点数計算 
    def getImage(self):
        #ドローンからの画像の取得
        self.image = self.tello.get_frame_read().frame
        #QRコード読み取り
        self.image = np.uint8(self.image)
        data,bbox,rectifiedImage = self.qrDetector.detectAndDecode(self.image)

        #点数の計算、タイマーリセット
        if data:
            print(data)#qrコードの内容
            hight = 1
            for i in self.players:
                if data == i[0]:
                    if time.time()-i[3]>=3 :
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
        #時間
        cv2.putText(self.image, (str(self.gameTime  - int(time.time()-self.timeStart)) + "seconds left"), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
        #点数
        for i in self.players:
            cv2.putText(self.image, (i[0] + ":" +str(i[1])), (0, 50 + i[2]), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
        #表示
            cv2.putText(self.image, (str(self.battery)), (0, 100 + 300), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
        cv2.imshow('SEE-DRO FIGHT!', self.image)
            
    #キーボード操作
    def droneControl(self,key):#left,rigth   back,foward   up,down   cw,ccw

        if key==-1:
            if ((time.time())-self.cont_time)>=0.8:
                self.tello.send_rc_control(0,0,0,0)
                self.battery=self.tello.get_battery()

        if key==ord("w"):
            try:
                self.tello.send_rc_control(0,self.movesize,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('s'):
            try:
                self.tello.send_rc_control(0,-self.movesize,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord("d"):
            try:
                self.tello.send_rc_control(self.movesize,0,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord("a"):
            try:
                self.tello.send_rc_control(-self.movesize,0,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('e'):
            try:
                self.tello.send_rc_control(0,0,0,30)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('q'):
            try:
                self.tello.send_rc_control(0,0,0,30)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('u'):
            try:
                self.tello.send_rc_control(0,0,30,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('j'):
            try:
                self.tello.send_rc_control(0,0,-30,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('t'):
            try:
                self.tello.takeoff()
            except:
                pass

        elif key==ord('l'):
            try:
                self.tello.land()
            except:
                pass
        
        elif key==ord('1'):
            self.moveSize=self.kando1
            self.angle=20

        elif key==ord('2'):
            self.moveSize=self.kando2
            self.angle=40

        elif key==ord('3'):
            self.moveSize=self.kando3
            self.angle=90


        elif key==27:#27はEsc
            print("esc has pressed")
            self.displayTotalScore()
            if self.isLanding == False:
                self.tello.land()
                self.isLanding = True
            cv2.waitKey(100)
            time.sleep(3)
            return

    
    
    #時間制限で終了
    def quitScreen(self):
        #print(time.time()-self.timeStart)
        if time.time()-self.timeStart>=self.gameTime :
            self.displayTotalScore()
            if self.isLanding == False:
                self.tello.land()
                self.isLanding = True
            return

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
        self.whileCheck = False
        self.totalPoints = points
        cv2.waitKey(5000)




    def main(self):
        while self.whileCheck:
            self.getImage()#画像の取得、QRコードの読み取り
            self.displayScreen()#ドローンからの画像の表示
            
            

            #キー入力の受けとり
            key = cv2.waitKey(30)

            #ドローンに命令を送信
            self.droneControl(key)
            
            self.quitScreen()#時間制限


        print("droneHasFin")
        return int(self.totalPoints)