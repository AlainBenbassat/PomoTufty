import time

class PomoTuftyModel:
    _workDurationGoal = 25
    _workDurationUpDown = 5
    
    _breakDurationGoal = 15
    _breakDurationUpDown = 5

    _remainingMinutes = 0
    _remainingSeconds = 0

    _currentScreen = "home"
    _tickCounter = 0
    
    def tick(self):
        refreshScreen = False
        
        t = time.ticks_ms()
        if time.ticks_diff(t, self._tickCounter) >= 1000:
            self._tickCounter = t
            self.updateRemainingTime()
            refreshScreen = True
        
        return refreshScreen
    
    def updateRemainingTime(self):
        self._remainingSeconds = self._remainingSeconds - 1
        if self._remainingSeconds < 0:
            self._remainingSeconds = 59
            self._remainingMinutes = self._remainingMinutes - 1
        if self._remainingMinutes == 0:
            self._remainingMinutes = 0
            
    def getRemainingTime(self):
        m = str(self._remainingMinutes)
        s = str(self._remainingSeconds)
        
        if len(m) == 1:
            m = "0" + m
        
        if len(s) == 1:
            s = "0" + s
            
        return m + ":" + s
    
    def toggleWorkDurationUpDown(self):
        self._workDurationUpDown += 5
        if self._workDurationUpDown == 20:
            self._workDurationUpDown = 30
        elif self._workDurationUpDown > 30:
            self._workDurationUpDown = 5

    def toggleBreakDurationUpDown(self):
        self._breakDurationUpDown += 5
        if self._breakDurationUpDown == 20:
            self._breakDurationUpDown = 30
        elif self._breakDurationUpDown > 30:
            self._breakDurationUpDown = 5
    
    def setCurrentScreen(self, currentScreen):
        self._currentScreen = currentScreen
        if currentScreen == "work":
            self._tickCounter = time.ticks_ms()
            self._remainingMinutes = self._workDurationGoal
            self._remainingSeconds = 0
        elif currentScreen == "break":
            self._tickCounter = time.ticks_ms()
            self._remainingMinutes = self._breakDurationGoal
            self._remainingSeconds = 0
    
    def getCurrentScreen(self):
        return self._currentScreen
    
    def getWorkDurationGoal(self):
        return self._workDurationGoal
    
    def getWorkDurationUpDown(self):
        return self._workDurationUpDown

    def getBreakDurationGoal(self):
        return self._breakDurationGoal
    
    def getBreakDurationUpDown(self):
        return self._breakDurationUpDown

    def incrementWorkDurationGoal(self):
        self._workDurationGoal += self._workDurationUpDown
        if self._workDurationGoal > 90:
            self._workDurationGoal = 90
            
    def decreaseWorkDurationGoal(self):
        self._workDurationGoal -= self._workDurationUpDown
        if self._workDurationGoal < 5:
            self._workDurationGoal = 5
    
    def incrementBreakDurationGoal(self):
        self._breakDurationGoal += self._breakDurationUpDown
        if self._breakDurationGoal > 90:
            self._breakDurationGoal = 90
            
    def decreaseBreakDurationGoal(self):
        self._breakDurationGoal -= self._breakDurationUpDown
        if self._breakDurationGoal < 5:
            self._breakDurationGoal = 5
            