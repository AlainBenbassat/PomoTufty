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
        self._clearScreen()

        screen = self._pomoModel.getCurrentScreen()
        
        if screen == "home":
            self._drawScreenHome()
        elif screen == "pre-work":
            self._drawScreenPreWork()
        elif screen == "work":
            self._drawScreenWork()
        elif screen == "post-work":
            self._drawScreenPostWork()
        elif screen == "pre-break":
            self._drawScreenPreBreak()
        elif screen == "break":
            self._drawScreenBreak()
        elif screen == "post-break":
            self._drawScreenPostBreak()
        
        self._display.update()
            
    def showError(self, msg):
        self._clearScreen()
        self._display.set_pen(self._WHITE)        
        self._display.text("error", 0, 70, 320, self._FONT_SIZE_NORMAL, 0, 1)
        self._display.text(msg, 0, 100, 320, self._FONT_SIZE_NORMAL, 0, 1)
        self._display.update()
        
    def _drawScreenHome(self):
        self._writeTextTitle("PomoTufty", 80)
        self._writeTextLine("Press button:", 1, 0)
        self._writeTextLine("(A) to start focused work", 2, 15)
        self._writeTextLine("(B) to take a break", 3, 15)

    def _drawScreenPreWork(self):
        title = "Focus for " + str(self._pomoModel.getWorkDurationGoal()) + " min."
        self._writeTextTitle(title, 0)
        self._writeTextLine("Press button:", 1, 0)
        self._writeTextLine("(A) to start", 2, 15)
        self._writeTextLine("(B) for home screen", 3, 15)
            
        steps = str(self._pomoModel.getWorkDurationUpDown())
        self._writeTextLine("(Up/Down) +" + steps + " / -" + steps, 4, 15)
        self._writeTextLine("(C) to toggle +/- steps", 5, 15)
        
    def _drawScreenWork(self):
        self._writeTextTitle("Focus", 120)
        self._writeTextTime(self._pomoModel.getRemainingTime())
        
    def _drawScreenPostWork(self):
        title = "Focused for " + str(self._pomoModel.getWorkDurationGoal()) + " min."
        self._writeTextTitle(title, 0)
        self._writeTextSuccess("Good job!")
        self._writeTextOvertime("Overtime: +" + self._pomoModel.getOvertime())
        self._writeTextLine("Press button:", 4, 0)
        self._writeTextLine("(B) for home screen", 5, 15)
        
    def _drawScreenPreBreak(self):
        title = "Pause for " + str(self._pomoModel.getBreakDurationGoal()) + " min."
        self._writeTextTitle(title, 0)
        self._writeTextLine("Press button:", 1, 0)
        self._writeTextLine("(A) to start", 2, 15)
        self._writeTextLine("(B) for home screen", 3, 15)
            
        steps = str(self._pomoModel.getBreakDurationUpDown())
        self._writeTextLine("(Up/Down) +" + steps + " / -" + steps, 4, 15)
        self._writeTextLine("(C) to toggle +/- steps", 5, 15)
        
    def _drawScreenBreak(self):
        self._writeTextTitle("Enjoy your break!", 18)
        self._writeTextTime(self._pomoModel.getRemainingTime())
        
    def _drawScreenPostBreak(self):
        title = "Paused for " + str(self._pomoModel.getBreakDurationGoal()) + " min."
        self._writeTextTitle(title, 0)
        self._writeTextSuccess("Feeling refreshed?")
        self._writeTextOvertime("Overtime: +" + self._pomoModel.getOvertime())
        self._writeTextLine("Press button:", 4, 0)
        self._writeTextLine("(B) for home screen", 5, 15)
        
    def _writeTextTitle(self, msg, indent):
        self._display.set_font("sans")
        self._display.set_pen(self._RED)
        self._display.text(msg, indent, 25, 320, self._FONT_SIZE_LARGE, 0, 1)

    def _writeTextLine(self, msg, line, indent):
        textY = 70
        lineHeight = 30

        self._display.set_pen(self._WHITE)
        self._display.text(msg, indent, textY + (line - 1) * lineHeight, 320, self._FONT_SIZE_NORMAL, 0, 1)

    def _writeTextTime(self, msg):
        self._display.set_pen(self._WHITE)
        self._display.text(msg, 30, 120, 320, self._FONT_SIZE_TIME, 0, 1)
        
    def _writeTextOvertime(self, msg):
        textY = 70
        lineHeight = 30

        self._display.set_pen(self._WHITE)
        self._display.text(msg, 0, 120, 320, self._FONT_SIZE_NORMAL, 0, 1)    
        
    def _writeTextSuccess(self, msg):
        self._display.set_pen(self._GREEN)
        self._display.text(msg, 0, 70, 320, self._FONT_SIZE_LARGE, 0, 1)
        
    def _clearScreen(self):
        self._display.set_pen(0)
        self._display.clear()
        