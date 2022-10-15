import time
from pimoroni import Button


class PomoTuftyController:
    buttonA = Button(7, invert=False)
    buttonB = Button(8, invert=False)
    buttonC = Button(9, invert=False)
    buttonUp = Button(22, invert=False)
    buttonDown = Button(6, invert=False)
    
    def setView(self, pomoView):
        self._pomoView = pomoView
    
    def setModel(self, pomoModel):
        self._pomoModel = pomoModel
    
    def buttonAPressed(self):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen == "home":
            self._pomoModel.setCurrentScreen("pre-work")
        elif currentScreen == "pre-work":
            self._pomoModel.setCurrentScreen("work")
        elif currentScreen == "work":
            self._pomoModel.setCurrentScreen("work")
        elif currentScreen == "post-work":
            self._pomoModel.setCurrentScreen("pre-break")
        elif currentScreen == "pre-break":
            self._pomoModel.setCurrentScreen("break")
        elif currentScreen == "break":
            self._pomoModel.setCurrentScreen("break")
        elif currentScreen == "post-break":
            self._pomoModel.setCurrentScreen("pre-work")
        else:
            self._pomoView.showError("Unknown screen")

    def buttonBPressed(self):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen == "home":
            self._pomoModel.setCurrentScreen("pre-break")
        elif currentScreen in ["pre-work", "work", "post-work", "pre-break", "break", "post-break"]:
            self._pomoModel.setCurrentScreen("home")
        else:
            self._pomoView.showError("Unknown screen")
    
    def buttonCPressed(self):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen in ["pre-work", "work"]:
            self._pomoModel.toggleWorkDurationUpDown()
        elif currentScreen in ["pre-break", "break"]:
            self._pomoModel.toggleBreakDurationUpDown()

    def buttonUpPressed(self):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen in ["pre-work", "work"]:
            self._pomoModel.incrementWorkDurationGoal()
        elif currentScreen in ["pre-break", "break"]:
            self._pomoModel.incrementBreakDurationGoal()
            
    def buttonDownPressed(self):
        currentScreen = self._pomoModel.getCurrentScreen()

        if currentScreen in ["pre-work", "work"]:
            self._pomoModel.decreaseWorkDurationGoal()
        elif currentScreen in ["pre-break", "break"]:
            self._pomoModel.decreaseBreakDurationGoal()
            
    def waitForInput(self):
        self._pomoView.drawScreen()

        while True:
            if self.buttonA.is_pressed:
                self.buttonAPressed()
                self._pomoView.drawScreen()
                time.sleep(0.1)
                
            elif self.buttonB.is_pressed:
                self.buttonBPressed()
                self._pomoView.drawScreen()
                time.sleep(0.1)
                
            elif self.buttonC.is_pressed:
                self.buttonCPressed()
                self._pomoView.drawScreen()
                time.sleep(0.1)
                
            elif self.buttonUp.is_pressed:
                self.buttonUpPressed()
                self._pomoView.drawScreen()
                
            elif self.buttonDown.is_pressed:
                self.buttonDownPressed()
                self._pomoView.drawScreen()

            if self._pomoModel.getCurrentScreen() in ["work", "break"]:
                if self._pomoModel.getRemainingTime() == "00:00":
                    self._pomoModel.setCurrentScreen("post-" + self._pomoModel.getCurrentScreen())
                    self._pomoView.drawScreen()
                else:
                    refreshScreen = self._pomoModel.tick()
                    if refreshScreen == True:
                        self._pomoView.drawScreen()
            
            time.sleep(0.1)
