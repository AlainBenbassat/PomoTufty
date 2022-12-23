import time
import machine

class PomoTuftyController:    
    def setView(self, pomoView):
        self._pomoView = pomoView
    
    def setModel(self, pomoModel):
        self._pomoModel = pomoModel
        
    def start(self):
        self._registerButtonHandlers()
        self._pomoView.drawScreen()
        self._loop()        
    
    def _buttonAPressed(self, pin):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen == "home":
            self._pomoModel.setCurrentScreen("pre-work")
        elif currentScreen == "pre-work":
            self._pomoModel.setCurrentScreen("work")
        elif currentScreen == "pre-break":
            self._pomoModel.setCurrentScreen("break")
            
        self._pomoView.drawScreen()

    def _buttonBPressed(self, pin):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen == "home":
            self._pomoModel.setCurrentScreen("pre-break")
        else:
            self._pomoModel.setCurrentScreen("home")
    
        self._pomoView.drawScreen()
        
    def _buttonCPressed(self, pin):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen == "pre-work":
            self._pomoModel.toggleWorkDurationUpDown()
        elif currentScreen == "pre-break":
            self._pomoModel.toggleBreakDurationUpDown()

        self._pomoView.drawScreen()
        
    def _buttonUpPressed(self, pin):
        currentScreen = self._pomoModel.getCurrentScreen()
        
        if currentScreen == "pre-work":
            self._pomoModel.incrementWorkDurationGoal()
        elif currentScreen == "pre-break":
            self._pomoModel.incrementBreakDurationGoal()
        
        self._pomoView.drawScreen()
        
    def _buttonDownPressed(self, pin):
        currentScreen = self._pomoModel.getCurrentScreen()

        if currentScreen == "pre-work":
            self._pomoModel.decreaseWorkDurationGoal()
        elif currentScreen == "pre-break":
            self._pomoModel.decreaseBreakDurationGoal()
        
        self._pomoView.drawScreen()
        
    def _registerButtonHandlers(self):
        buttonA = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
        buttonA.irq(trigger=machine.Pin.IRQ_RISING, handler=self._buttonAPressed)
        
        buttonB = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
        buttonB.irq(trigger=machine.Pin.IRQ_RISING, handler=self._buttonBPressed)
        
        buttonC = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
        buttonC.irq(trigger=machine.Pin.IRQ_RISING, handler=self._buttonCPressed)
        
        buttonUp = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
        buttonUp.irq(trigger=machine.Pin.IRQ_RISING, handler=self._buttonUpPressed)
        
        buttonDown = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
        buttonDown.irq(trigger=machine.Pin.IRQ_RISING, handler=self._buttonDownPressed)
        
    def _loop(self):
        while True:
            currentScreen = self._pomoModel.getCurrentScreen()
            
            if currentScreen in ["work", "break"]:
                remainingTime = self._pomoModel.tick()
                
                if remainingTime == "00:00":
                    self._pomoModel.setCurrentScreen("post-" + currentScreen)
                
                self._pomoView.drawScreen()

            elif currentScreen in ["post-work", "post-break"]:
                self._pomoModel.overtimeTick()
                self._pomoView.drawScreen()
            
            time.sleep(1)
