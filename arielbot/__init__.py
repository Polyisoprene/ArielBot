import click
from os import path, getcwd, mkdir
import dotenv
import nonebot
from .bot import app

env = {
    'HOST': '127.0.0.1',
    'PORT': '8080',
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
    nonebot.run(app=app)


main.add_command(run)


def create_config():
    env_file_path = path.join(getcwd(), ".env.prod")
    if not path.exists(env_file_path):
        for key, value in env.items():
            dotenv.set_key(
                env_file_path,
                key,
                str(value).replace(' ', ''),
                quote_mode="never",
            )


def create_plugins_dir():
    plugins_dir_path = path.join(getcwd(), "plugins")
    if not path.exists(plugins_dir_path):
        mkdir(plugins_dir_path)
