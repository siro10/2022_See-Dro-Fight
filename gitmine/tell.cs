using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using TelloLib;
using System.Threading.Tasks;
using System.Threading;

namespace tello_control_test
{

    class Program
    {
        static void Main(string[] args)
        {
            Tello.onConnection += Tello_onConnection;

            Tello.onUpdate += Tello_onUpdate;

            Tello.onVideoData += Tello_onVideoData;

            Tello.startConnecting();//接続開始

            var inputStr = "";
            while (inputStr != "exit")
            {


                inputStr = Console.ReadLine().ToLower();

                //離陸
                //Telloと接続中、かつ、飛行していない
                if (inputStr == "takeoff" && Tello.connected && !Tello.state.flying)
                {
                    Tello.takeOff();
                }

                //着陸
                //Telloと接続中、かつ、飛行中
                if (inputStr == "land" && Tello.connected && Tello.state.flying)
                {
                    Tello.land();
                }



                //inputStrの内容に応じた処理を書く
            }

            Tello.land();

            Thread.Sleep(1000);

        }
        private static void Tello_onConnection(TelloLib.Tello.ConnectionState newState)
        {
            if (newState == Tello.ConnectionState.Connected)
            {
                Tello.queryAttAngle();//???
                Tello.setMaxHeight(1);//最大高度？メートル？
            }
        }

        private static void Tello_onVideoData(byte[] data)
        {
        }

        private static void Tello_onUpdate(int cmdId)
        {
        }
    }
}
