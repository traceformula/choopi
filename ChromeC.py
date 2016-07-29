from win32com.client import Dispatch
from IEC import IEController
import time

class CController(IEController): 
    #Chrome Controller
    def __CreateNewIE(self):
        chrome = Dispatch("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        chrome.Visible = 1
        return chrome