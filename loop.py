# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-08-26
# Message：测试工具

# 休眠
from time import sleep

# 键盘操作，按键、控制器
from pynput.keyboard import Key, Controller

# 剪切板操作
from pyperclip import copy


# 聊天语句，从网络获取句子
from chat import Chat

# 循环
class Loop:

	# 初始化（时间，队列，数据源类型）
	def __init__(self, time, queue,t):

		# 时间
		self.time = time

		# 队列
		self.queue = queue

		# 聊天语句，从网络获取句子（数据源类型）
		self.chat = Chat(t)

		# 键盘控制器
		self.k = Controller()

	# 线程启动函数
	def run(self):

		# 死循环
		while True:

			# 队列不为空
			if not self.queue.empty():

				# 返回
				return

			# 捕获异常
			try:
				# 文本 = 聊天.请求文本()
				str = self.chat.run()

			# 处理异常
			except Exception:
				# 返回
				return

			# 发送文本
			try:
				self.send(str)
			except:
				pass

			# 休眠
			sleep(self.time)

	# 发送文本
	def send(self, str):
		# 休眠
		sleep(0.01)

		# 复制
		copy(str)

		# 休眠
		sleep(0.01)

		# 键盘控制器，按下ctrl
		with self.k.pressed(Key.ctrl):

			# 键盘控制器，按下v
			self.k.press('v')

			# 键盘控制器，松开v
			self.k.release('v')

		# 按下enter发送
		self.k.press(Key.enter)

		# 松开enter
		self.k.release(Key.enter)
