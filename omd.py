# Guido van Rossum <guido@python.org>
"""
    Before start:
    1. create app in "Creating an application" 
        on the https://my.telegram.org/apps
    2. create ".env" file (in same directory) 
        in which write:
        API_ID = API-ID
        API_HASH = "API-HASH"
        PHONE = "PHONE"
    3. use this script :)
"""

import time

from dotenv import dotenv_values
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest


class Telega:
    """
        Uses telegram's chat bots with GPT4
    """

    def __init__(self):
        """
            Load .env file and start TelegramClient 
        """
        env = dotenv_values('.env')
        api_id = int(env['API_ID'])
        api_hash = env['API_HASH']
        phone = env['PHONE']
        self.client = TelegramClient(phone, api_id, api_hash)
        self.client.start()

    def post_gpt(self, text: str, bot_name: str) -> list:
        """
            Post message to tg-channel
        """
        destination_channel_username = bot_name
        entity = self.client.get_entity(destination_channel_username)
        res = self.client.send_message(entity=entity, message=text)
        return res

    def get_last_msg(self, bot_name: str) -> str:
        """
            Get last message from tg-channel
        """
        destination_channel_username = bot_name
        entity = self.client.get_entity(destination_channel_username)
        posts = self.client(GetHistoryRequest(
            peer=entity,
            limit=1,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        return posts.messages[0].message


class GPT:
    """
        Uses telegram to gain access to GPT and asks him a question
    """

    def __init__(self, template: str, answer: bool):
        """
            The Telegram-client is initializing
        """
        self.tg = Telega()
        self.answer = answer
        self.template = template
        self.start = 'Продолжи историю:'
        self.default_no = 'Дождь не пошел и забытый зонтик'\
            + ' не помешал утке насладиться барной атмосферной.'
        self.default_yes = 'Оказалось, что у утки лапки, '\
            + 'и зонт она держать не умеет, от этого ей еще больше захотелось в бар.'
        self.template += 'Взяла зонтик.' if answer else 'Забыла зонтик.'

    def post_and_get(self, bot_name='Jarvis_IT_Assistant_bot') -> str:
        """
            Post and get message using the telegram-client
        """
        if bot_name == 'Jarvis_IT_Assistant_bot':
            entity = self.tg.client.get_entity(bot_name)
            self.tg.client.send_message(entity=entity,
                                        message='/context')
        elif bot_name == 'GPT4Telegrambot':
            entity = self.tg.client.get_entity(bot_name)
            self.tg.client.send_message(
                entity=entity, message='/deletecontext')
        else:
            return self.template + self.default_no if self.answer else self.default_yes
        time.sleep(0.5)

        text = self.start + self.template \
            + '\nВ конце сообщения напиши надпись "b.c.d."'
        self.tg.post_gpt(
            text, bot_name)
        flag = True
        while flag:
            resp = self.tg.get_last_msg(bot_name)
            flag = 'b.c.d.' not in resp if text not in resp else True
            time.sleep(0.2)
        resp = resp.split('b.c.d.')[0]
        return resp


def choice(options: dict, text: str):
    """
        Function for choice-activity
    """
    option = ''
    print(text)
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()
    return options[option]


def step1():
    """
        First step of story-creating
    """
    def step2_umbrella(template: str):
        """
            Second step (if answer is yes)
        """
        template += 'На улице был дождь.' if choice(
            options, 'А на улице был дождь?') else 'На улице не было дождя.'
        return step3(template, True)

    def step2_no_umbrella(template: str):
        """
            Second step (if answer is no)
        """
        template += 'Она пошла одна.' if choice(
            options, 'Она пошла одна?') else 'Она пошла не одна.'
        return step3(template, False)

    def step3(template: str, umbrella: bool):
        """
            Final step: create story
        """
        story = GPT(template, umbrella).post_and_get()
        print('История:\n', story)
        return story

    template = 'Утка-маляр 🦆 решила выпить зайти в бар. '
    question = 'Взять ей зонтик? ☂️'
    options = {'да': True, 'нет': False}

    if choice(options, template + question):
        return step2_umbrella(template)
    return step2_no_umbrella(template)


if __name__ == '__main__':
    step1()
