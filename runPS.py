"""
Created in May 2022

@author: KhadijaHammawa Aug 2022
"""
import win32com.client

psApp = win32com.client.Dispatch('Photoshop.Application')
psApp.Open("C:/Users/Khadija_Hammawa/Documents/GitHub/background_subtraction/remove-bg.jsx")
psApp.Quit()


