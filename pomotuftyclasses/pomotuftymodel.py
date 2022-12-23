class PomoTuftyModel:
    _workDurationGoal = 25
    _workDurationUpDown = 5
    
    _breakDurationGoal = 15
    _breakDurationUpDown = 5

    _remainingMinutes = 0
    _remainingSeconds = 0

    _overtimeMinutes = 0
    _overtimeSeconds = 0
    
    _currentScreen = "home"
    
    def tick(self):
        self.updateRemainingTime()
        return self.getRemainingTime()
    
    def overtimeTick(self):
        self.updateOvertime()
    
    def updateRemainingTime(self):
        if self._remainingMinutes == 0 and self._remainingSeconds == 0:
            return
        
        self._remainingSeconds = self._remainingSeconds - 1
        if self._remainingSeconds < 0:
            self._remainingSeconds = 59
            self._remainingMinutes = self._remainingMinutes - 1
        if self._remainingMinutes == 0:
            self._remainingMinutes = 0
    
    def updateOvertime(self):
        self._overtimeSeconds = self._overtimeSeconds + 1
        if self._overtimeSeconds > 59:
            self._overtimeSeconds = 0
            self._overtimeMinutes = self._overtimeMinutes + 1
            
    def getRemainingTime(self):
        return self.getFormattedMinSec(self._remainingMinutes, self._remainingSeconds)
    
    def getOvertime(self):
        return self.getFormattedMinSec(self._overtimeMinutes, self._overtimeSeconds)
    
    def getFormattedMinSec(self, m, s):
        strM = str(m)
        strS = str(s)
        
        if len(strM) == 1:
            strM = "0" + strM
        
        if len(strS) == 1:
            strS = "0" + strS
            
        return strM + ":" + strS
    
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
            self._remainingMinutes = self._workDurationGoal
            self._remainingSeconds = 0
        elif currentScreen == "break":
            self._remainingMinutes = self._breakDurationGoal
            self._remainingSeconds = 0
        elif currentScreen in ["post-work", "post-break"]:
            self._overtimeMinutes = 0
            self._overtimeSeconds = 0
            
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
            self._workDurationGoal = 1
    
    def incrementBreakDurationGoal(self):
        self._breakDurationGoal += self._breakDurationUpDown
        if self._breakDurationGoal > 90:
            self._breakDurationGoal = 90
            
    def decreaseBreakDurationGoal(self):
        self._breakDurationGoal -= self._breakDurationUpDown
        if self._breakDurationGoal < 5:
            self._breakDurationGoal = 1
            