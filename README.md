Find the current opened app in android
1) List all devices and find yours
# adb devices
List of devices attached
RZCX10WSYZF	device

2) Connect to the device
# adb shell
a54x:/ $

3) Get the current active displayed app
a54x:/ $ dumpsys window displays | grep -E mCurrentFocus                                     
  mCurrentFocus=Window{a873dc u0 com.sec.android.app.popupcalculator/com.sec.android.app.popupcalculator.Calculator}
a54x:/ $ 

appPackage = com.sec.android.app.popupcalculator
appActivity = com.sec.android.app.popupcalculator.Calculator
