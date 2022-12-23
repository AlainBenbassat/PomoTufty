from pomotuftyclasses.pomotuftymodel import PomoTuftyModel
from pomotuftyclasses.pomotuftyview import PomoTuftyView
from pomotuftyclasses.pomotuftycontroller import PomoTuftyController

pomoModel = PomoTuftyModel()
pomoView = PomoTuftyView()
pomoController = PomoTuftyController()

pomoController.setView(pomoView)
pomoController.setModel(pomoModel)

pomoView.setModel(pomoModel)

pomoController.start()

