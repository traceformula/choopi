from IEC import *
from ChromeC import CController
import win32api, win32con
from time import sleep

def Login(ie, username, password):
    ie.Navigate(url)
    
    sleep(8)
    ie.ClickElemByClassName('join-game-text')
    sleep(5)
    #ie.ClickElemById('toLoginForm')
    ie.ClickElemByClassName('switch-link link-command', 1)
    sleep(4)
    ie.SetInputValueByClass('username top-radius', username, 1)
    ie.SetInputValueByClass('password bottom-radius', password, 1)
    ie.ClickElemByClassName('login_but popover-link', 1)
    sleep(8)
    return 1

def Logout(ie):
    ie.ClickElemById('gameUserLogoutMenuItem')
    sleep(4)
    ie.ClickElemByDataId('okLabel')
    sleep(1)
    
def LoginTapsu(ie):
    ie.ClickElemByClassName('view-game-button join-game-beginner')
    sleep(10)
    
def CreateTable(ie):
    ie.ClickElemByClassName('new-table-but')
    sleep(4)
    ie.ClickElemByClassName('btn btn-warning new-game-right-element off')
    sleep(4)
    ie.ClickElemByClassName('lager-but create-new-game-largbtn')
    sleep(20)
    
def GetPassWord(ie):
    return ie.GetTextByClass('lock')
    
def GetMoney(ie):
    return ie.GetTextByClass('money').replace(',','')
    
def JoinTable(ie, username, pass_to_join):
    ie.ClickClassMatchText('player-of-table hostHere', username)
    sleep(1)
    ie.SetInputValueByClass('text-input medium-text-input form-control', pass_to_join)
    sleep(1)
    ie.ClickElemById('enterTablePasswordDialog_enterTableButton')
    sleep(10)
    
def ClickSanSang(ie):
    ie.ClickElemById('btnReady')
    sleep(2)
    
def ClickBatDau(ie):
    ie.ClickElemById('btnStart')
    sleep(2)

def MakeAMove(ie):
    ClickPosition(ie, 665, 340) 
    ClickPosition(ie, 708, 517)
    sleep(1)
    ClickPosition(ie, 667, 479)
    sleep(5)
    
def ChiuThua(ie):    
    ie.ClickElemByClassName('btnResign')
    sleep(2)
    ie.ClickElemByClassName('btnResign confirmation-text-color')
    sleep(3)
    
def ClickThoat(ie):
    ie.ClickElemByClassName('exit-button btnGotoLobby')
   
def ClickDongY(ie):
    ie.ClickElemByClassName('exit-button btnGotoLobby confirmation-text-color')
    
def Thoat(ie):
    ClickThoat(ie)
    sleep(2)
    ClickDongY(ie)
    sleep(1)
   
def ClickPosition(ie, x, y):
    win32api.SetCursorPos((x,y))
    #sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    #sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    sleep(1)
    
if __name__ == '__main__':
    url = 'http://cotuongup.com/'
    ShowMessage('Creating a new IE object....')
    
    main_ie = IEController(3)
    ie = IEController(4)
    
    #CreateTable(ie)
    main_username = ''
    main_password = ''
    
    #Login(main_ie, main_username, main_password)
    #LoginTapsu(main_ie)
    
    username_trunk = ''
    password = ''
    #ranges = [[8,21], [23,40]]
    ranges = [[4,60]] #46
    b = False
    for r in ranges:
        if b: break
        for x in range(r[0], r[1]):
            if b: break
            try:
                try:
                    username = username_trunk + str(x)
                    Login(ie, username, password)
                    LoginTapsu(ie)
                    
                    money = float(GetMoney(ie).replace(',',''))
                    if money < 5000:
                        print "There is only : $", money
                        Logout(ie)
                        continue
                        
                    CreateTable(ie)
                    pass_of_table = GetPassWord(ie)
                    
                    JoinTable(main_ie, username, pass_of_table)
                    
                    ClickSanSang(main_ie)
                    ClickBatDau(ie)
                    MakeAMove(main_ie)
                    ChiuThua(ie)
                    #MakeAMoveAndQuit(main_ie)
                    #ie.ClickElemByClassName('btnResign')
                    #ie.ClickElemByClassName('btnResign confirmation-text-color')
                    Logout(ie)
                    Thoat(main_ie)
                except Exception as e:
                    print " Inner Error for x = " + str(x) + ":" + str(e)
                    Logout(ie)
                    Thoat(main_ie)
            except KeyboardInterrupt , e:
                b = True
            except Exception as e:
                print "Error for x = " + str(x) + ":" + str(e)
    #ie.CloseWindow()
    