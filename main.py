import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime, date, time
from sqliter import SQLighter
import asyncio
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SQLighter(os.path.join(BASE_DIR, 'db.db'))
logging.basicConfig(level=logging.INFO)

bot = Bot(token = config.API)
dp = Dispatcher(bot)
@dp.message_handler(commands = ['timetable'])
async def echo(message: types.Message):
	day = datetime.today().isoweekday()
	messageLesson = ''
	if(day == 1):
		day = 'Monday'
	elif (day == 2):
		day = 'Tuesday'
	elif (day == 3):
		day = 'Wednesday'
	elif (day == 4):
		day = 'Thursday'
	elif (day == 5):
		day = 'Friday'
	else:
		day = 0
	if(day != 0):
		lesson = db.getLessonList(day)
		for item in lesson:
			messageLesson += item[0] + '\nВремя: '+ item[1] + '\n' + item[2] + '\nZOOM логин: ' + str(item[3]) + '\nZOOM пароль: ' + str(item[4]) + '\n----------------\n'  
		await message.answer(messageLesson)
	else: 
		await message.answer('Уроков нет')

if __name__ == '__main__':
	executor.start_polling(dp,skip_updates=True)