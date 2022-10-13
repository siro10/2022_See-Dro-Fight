import time, cv2,sys
from djitellopy import Tello



class FlightDrone():
    def __init__(self):
        #プレイヤー点数初期値
        self.players = []
        #プレイヤー人数初期値
        self.playerNumbers = 4
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
        #全体の感度調整
        self.ReactionSensitivity = 0
        
        

    #接続開始
    def start(self):
        if self.ReactionSensitivity == 0:
            self.kando1=20
            self.kando2=30
            self.kando3=40
        elif self.ReactionSensitivity == 1:
            self.kando1=30
            self.kando2=50
            self.kando3=70
        elif self.ReactionSensitivity == 2:
            self.kando1=40
            self.kando2=70
            self.kando3=100
        self.angle=30
        self.moveSize=self.kando1
        
        #ドローンとの接続
        try:
            self.tello.connect()
        except:
            sys.exit()

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

    #<セッティング画面>感度の取得
    def getReactionSensitivity(self,sens):
        self.ReactionSensitivity = sens

    #プレイヤー人数設定
    def getPlayerNumbers(self,nom):
        self.playerNumbers = nom
        print(self.playerNumbers)


    #画像取得、点数計算
    def getImage(self):
        #ドローンからの画像の取得
        self.image = self.tello.get_frame_read().frame
        #QRコード読み取り
        qrText,_,_ = self.qrDetector.detectAndDecode(self.image)

        #点数の計算、タイマーリセット
        if qrText:
            print(qrText)#qrコードの内容
            hight = 1
            for i in self.players:
                if qrText == i[0]:
                    if time.time()-i[3]>=3 :
                        self.players[hight - 1][1] = self.players[hight - 1][1] + 1
                        self.players[hight - 1][3]=time.time()
                    return
                hight = hight + 1
            #新規登録
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(len(self.players))
            print(self.playerNumbers)
            if len(self.players) < self.playerNumbers:
                self.players.append([qrText,1,(50*hight),time.time()])




    #ディスプレイに表示
    def displayScreen(self) :
        
        #点数表示の準備
        #時間
        cv2.putText(self.image, (str(self.gameTime  - int(time.time()-self.timeStart)) + "seconds"), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5, cv2.LINE_AA)
        #点数
        for i in self.players:
            cv2.putText(self.image, (i[0] + ":" +str(i[1])), (0, 50 + i[2]), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5, cv2.LINE_AA)
        #表示
        cv2.putText(self.image,("batt:" + str(self.tello.get_battery())), (0, 710), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5, cv2.LINE_AA)


        cv2.imshow('SEE-DRO FIGHT!', self.image)
            
    #キーボード操作
    def droneControl(self,key):
        if key==-1:
            if ((time.time())-self.cont_time)>=0.8:
                self.tello.send_rc_control(0,0,0,0)
                #self.cont_time=time.time()

        if key==ord("w"):
            try:
                self.tello.send_rc_control(0,self.moveSize,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('s'):
            try:
                self.tello.send_rc_control(0,-self.moveSize,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord("d"):
            try:
                self.tello.send_rc_control(self.moveSize,0,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord("a"):
            try:
                self.tello.send_rc_control(-self.moveSize,0,0,0)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('e'):
            try:
                self.tello.send_rc_control(0,0,0,self.angle)
            except:
                pass
            self.cont_time=time.time()

        elif key==ord('q'):
            try:
                self.tello.send_rc_control(0,0,0,-self.angle)
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
                if self.isLanding:
                    takeOffTime = time.time()
                    self.tello.takeoff()
                    self.isLanding = False
                    self.gameTime += int(time.time() - takeOffTime)
            except:
                pass

        elif key==ord('l'):
            try:
                self.tello.land()
                self.isLanding=True
            except:
                pass

        elif key==ord('1'):
            self.moveSize=self.kando1
            self.angle=30

        elif key==ord('2'):
            self.moveSize=self.kando2
            self.angle=60

        elif key==ord('3'):
            self.moveSize=self.kando3
            self.angle=90


        elif key==27:#27はEsc
            print("esc has pressed")
            self.displayTotalScore()
            if self.isLanding == False:
                try:
                    self.tello.land()
                    self.isLanding = True
                except:
                    pass
            return



    #時間制限で終了
    def timeLimit(self):
        #print(time.time()-self.timeStart)
        if time.time()-self.timeStart>=self.gameTime :
            self.displayTotalScore()
            if self.isLanding == False:
                self.tello.land()
                self.isLanding = True
            return

    #リザルトの表示
    def displayTotalScore(self) :
        self.image = self.tello.get_frame_read().frame
        #合計点数
        points = 0
        for i in self.players:
            points = points + i[1]
        #合計スコア表示
        cv2.putText(self.image, ("Total score:" + str(points)), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5, cv2.LINE_AA)
        #各プレイヤーの点数表示
        for i in self.players:
                cv2.putText(self.image, (i[0] + ":" +str(i[1])), (0, 50 + i[2]), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5, cv2.LINE_AA)

        cv2.imshow('SEE-DRO FIGHT!', self.image)
        self.whileCheck = False
        self.totalPoints = points
        #cv2.waitKey(5000)
        ##################################################3
        ##waitKeyいらないかも(検証)
        #############################################




    def main(self):
        while self.whileCheck:
            #画像の取得、QRコードの読み取リ、点数の計算
            self.getImage()
            #ドローンからの画像、点数の表示
            self.displayScreen()

            #キー入力の受けとり
            key = cv2.waitKey(30)
            #操作受け付け、ドローンに命令を送信
            self.droneControl(key)
            
            #時間制限で終了
            self.timeLimit()

        print("droneHasFin")
        return self.totalPoints