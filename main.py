from modules.differentiate.differentiate import Differentiate
from modules.inputProcessor.inputProcessor import InputProcessorMain
from modules.Startup.WelcomeMessage import WelcomeMessage
from modules.logger.logger import LOG


WelcomeMessage()

Polynomial = InputProcessorMain("Please Enter the Polynomial: ")

LOG(Polynomial)
# LOG(Differentiate(Polynomial))