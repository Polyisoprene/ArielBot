import nonebot
from nonebot.adapters.satori import Adapter as SatoriAdapter
from os import path, getcwd, listdir
import sys

sys.path.append(path.join(getcwd(), "plugins"))
nonebot.init()
# nonebot.load_plugin("arielbot.plugins.Core")
nonebot.load_all_plugins([i for i in listdir(path.join(getcwd(), "plugins"))], [])
driver = nonebot.get_driver()
driver.register_adapter(SatoriAdapter)
config = nonebot.get_driver().config

