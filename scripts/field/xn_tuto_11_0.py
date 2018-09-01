# Video Field (931050990)  |  A Black Field used for Effects/Videos

def init():
    job = sm.getChr().getJob()
    if job == 2004: # Luminous Beginner Job ID
        sm.lockInGameUI(True)
        sm.showScene("Effect.wz/Direction8.img", "lightningTutorial", "Scene0")
        sm.invokeAfterDelay(5000, "warpInstanceIn", 927020000, 0) # Warp into Instance
        sm.invokeAfterDelay(4500, "showFadeTransition", 0, 500, 1500)