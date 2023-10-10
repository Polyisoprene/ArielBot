import click
import json
from os import path, getcwd, mkdir
import dotenv


env = {
    'DRIVER':'~aiohttp',
    'SUPERUSERS': [],
    'DynTextFont': '',
    'DynEmojiFont': '',
    'DynFontStyle': ''

}


@click.group()
def main():
    pass


@click.command()
def run():
    create_config()
    create_plugins_dir()
    from .bot import nonebot
    nonebot.run()


main.add_command(run)


def create_config():
    env_file_path = path.join(getcwd(), ".env.prod")
    if not path.exists(env_file_path):
        red_bots= [{"port": "16530","token": "xxx","host": "localhost"}]
        token = input("请输入token：")
        red_bots[0]["token"] = token
        for key, value in env.items():
            dotenv.set_key(
                env_file_path,
                key,
                str(value).replace(' ', ''),
                quote_mode="never"
            )
        dotenv.set_key(env_file_path,"RED_BOTS",json.dumps(red_bots),quote_mode='never')


def create_plugins_dir():
    plugins_dir_path = path.join(getcwd(), "plugins")
    if not path.exists(plugins_dir_path):
        mkdir(plugins_dir_path)
