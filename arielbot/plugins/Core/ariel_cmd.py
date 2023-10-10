from nonebot.adapters.satori import Bot,MessageEvent
from nonebot import on_message
from nonebot.log import logger


a = on_message()

@a.handle()
async def _(bot:Bot,event:MessageEvent):
    result = await bot.guild_role_list(guild_id=event.guild.id)
    logger.info(result)