from picographics import PicoGraphics, DISPLAY_TUFTY_2040

class PomoTuftyView:
    _display = PicoGraphics(display=DISPLAY_TUFTY_2040)
    _WHITE = _display.create_pen(255, 255, 255)
    _RED = _display.create_pen(255, 0, 0)
    _GREEN = _display.create_pen(0, 255, 0)
    _FONT_SIZE_NORMAL = 0.7
    _FONT_SIZE_LARGE = 1
    _FONT_SIZE_TIME = 3

    def __self__(self):
        self._display.set_font("sans")
        
    def setModel(self, pomoModel):
        self._pomoModel = pomoModel
    
    def drawScreen(self):
        screen = self._pomoModel.getCurrentScreen()
        if screen == "home":
            self.drawScreenHome()
        elif screen == "pre-work":
            self.drawScreenPreWork()
        elif screen == "work":
            self.drawScreenWork()
        elif screen == "post-work":
            self.drawScreenPostWork()
        elif screen == "pre-break":
            self.drawScreenPreBreak()
        elif screen == "break":
            self.drawScreenBreak()
        elif screen == "post-break":
            self.drawScreenPostBreak()
        else:
            self.showError("invalid screen " + screen)
            
    def drawScreenHome(self):
        self.__clearScreen()

        self.writeTextTitle("PomoTufty", 80)
        self.writeTextLine("Press button:", 1, 0)
        self.writeTextLine("(A) to start focused work", 2, 15)
        self.writeTextLine("(B) to take a break", 3, 15)

        self._display.update()
    
    def drawScreenPreWork(self):
        self.__clearScreen()
    
        title = "Focus for " + str(self._pomoModel.getWorkDurationGoal()) + " min."
        self.writeTextTitle(title, 0)
        self.writeTextLine("Press button:", 1, 0)
        self.writeTextLine("(A) to start", 2, 15)
        self.writeTextLine("(B) for home screen", 3, 15)
            
        steps = str(self._pomoModel.getWorkDurationUpDown())
        self.writeTextLine("(Up/Down) +" + steps + " / -" + steps, 4, 15)
        self.writeTextLine("(C) to toggle +/- steps", 5, 15)
        
        self._display.update()
        
    def drawScreenWork(self):
        self.__clearScreen()
    
        self.writeTextTitle("Focus", 120)
        self.writeTextTime(self._pomoModel.getRemainingTime())
        
        self._display.update()
        
    def drawScreenPostWork(self):
        self.__clearScreen()
    
        title = "Focused for " + str(self._pomoModel.getWorkDurationGoal()) + " min."
        self.writeTextTitle(title, 0)
        self.writeTextSuccess("Good job!")
        self.writeTextOvertime("Overtime: +" + self._pomoModel.getOvertime())
        self.writeTextLine("Press button:", 4, 0)
        self.writeTextLine("(B) for home screen", 5, 15)
        
        self._display.update()
        
    def drawScreenPreBreak(self):
        self.__clearScreen()
    
        title = "Pause for " + str(self._pomoModel.getBreakDurationGoal()) + " min."
        self.writeTextTitle(title, 0)
        self.writeTextLine("Press button:", 1, 0)
        self.writeTextLine("(A) to start", 2, 15)
        self.writeTextLine("(B) for home screen", 3, 15)
            
        steps = str(self._pomoModel.getBreakDurationUpDown())
        self.writeTextLine("(Up/Down) +" + steps + " / -" + steps, 4, 15)
        self.writeTextLine("(C) to toggle +/- steps", 5, 15)
        
        self._display.update()
        
    def drawScreenBreak(self):
        self.__clearScreen()
    
        self.writeTextTitle("Enjoy your break!", 18)
        self.writeTextTime(self._pomoModel.getRemainingTime())
        
        self._display.update()
        
    def drawScreenPostBreak(self):
        self.__clearScreen()
    
        title = "Paused for " + str(self._pomoModel.getBreakDurationGoal()) + " min."
        self.writeTextTitle(title, 0)
        self.writeTextSuccess("Feeling refreshed?")
        self.writeTextOvertime("Overtime: +" + self._pomoModel.getOvertime())
        self.writeTextLine("Press button:", 4, 0)
        self.writeTextLine("(B) for home screen", 5, 15)
        
        self._display.update()
    
    def writeTextTitle(self, msg, indent):
        self._display.set_font("sans")
        self._display.set_pen(self._RED)
        self._display.text(msg, indent, 25, 320, self._FONT_SIZE_LARGE, 0, 1)

    def writeTextLine(self, msg, line, indent):
        textY = 70
        lineHeight = 30

        self._display.set_pen(self._WHITE)
        self._display.text(msg, indent, textY + (line - 1) * lineHeight, 320, self._FONT_SIZE_NORMAL, 0, 1)

    def writeTextTime(self, msg):
        self._display.set_pen(self._WHITE)
        self._display.text(msg, 30, 120, 320, self._FONT_SIZE_TIME, 0, 1)
        
    def writeTextOvertime(self, msg):
        textY = 70
        lineHeight = 30

        self._display.set_pen(self._WHITE)
        self._display.text(msg, 0, 120, 320, self._FONT_SIZE_NORMAL, 0, 1)    
        
    def writeTextSuccess(self, msg):
        self._display.set_pen(self._GREEN)
        self._display.text(msg, 0, 70, 320, self._FONT_SIZE_LARGE, 0, 1)
        
    def showError(self, msg):
        self.__clearScreen()
        self._display.set_pen(self._WHITE)        
        self._display.text("error", 0, 70, 320, self._FONT_SIZE_NORMAL, 0, 1)
        self._display.text(msg, 0, 100, 320, self._FONT_SIZE_NORMAL, 0, 1)
        self._display.update()
        
    def __clearScreen(self):
        self._display.set_pen(0)
        self._display.clear()
        