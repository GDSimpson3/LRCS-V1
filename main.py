from modules.differentiate.differentiate import Differentiate
from modules.inputProcessor.inputProcessor import InputProcessorMain
from modules.Startup.WelcomeMessage import WelcomeMessage
from modules.logger.logger import LOG
from modules.roots.SignChangeScanner import SignChangeScanner


WelcomeMessage()

Polynomial = InputProcessorMain("Please Enter the Polynomial: ")

# LOG(Polynomial)
# LOG(Differentiate(Polynomial))

# [['2', 2], ['-5', 1], ['2', 0]]


SignChangeScanner(0,5,[['1','1'],['-3.4343','0']],3)