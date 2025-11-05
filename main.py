from modules.functional.differentiate.differentiate import Differentiate
from modules.system.inputProcessor.inputProcessor import InputProcessorMain
from modules.system.Startup.WelcomeMessage import WelcomeMessage
from modules.utils.logger.logger import LOG
from modules.base.signChangeScanner import SignChangeScanner

from modules.core.RootFinder.rootFinder import RootFinder



WelcomeMessage()

Polynomial = InputProcessorMain("Please Enter the Polynomial: ")

# LOG(Polynomial)
# LOG(Differentiate(Polynomial))

# [['2', 2], ['-5', 1], ['2', 0]]


# LOG(SignChangeScanner(0,10,[['1','1'],['-3.4343','0']],5))

LOG(RootFinder(Polynomial))