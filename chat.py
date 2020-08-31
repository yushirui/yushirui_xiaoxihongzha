# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-08-31
# Message：聊天语句，从网络获取句子

import requests
import os
import json
from lxml import etree

# 聊天语句，从网络获取句子
class Chat:
	''' 聊天语句，从网络获取句子 '''

	def __init__(self, type):

		# 聊天类型
		self.type = type

		# 请求头
		self.headers = {
			'method': 'GET',
			'path': '/api.php',
			'scheme': 'https',
			'accept': '*/*',
			# 此请求头会导致乱码
			# 'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'zh-CN,zh;q=0.9',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400',
			'x-requested-with': 'XMLHttpRequest',
		}

		# 类型
		if type == '诗词':
			self.url = 'https://v1.jinrishici.com/all.json'

		elif type == '甜言蜜语':
			self.url = 'https://api.lovelive.tools/api/SweetNothings/1/Serialization/Json'
			self.headers['path'] = '/api/SweetNothings/1/Serialization/Json'
			self.headers['referer'] = 'https://lovelive.tools/'
			self.headers['origin'] = 'https://lovelive.tools'

		elif type == '鸡汤':
			self.url = 'https://8zt.cc/'
			self.headers['path'] = '/'

		elif type == '马屁精':
			self.url = 'https://chp.shadiao.app/api.php'
			self.headers['authority'] = 'chp.shadiao.app'
			self.headers['referer'] = 'https://chp.shadiao.app/'

		# 忽视ssl警告
		# requests.packages.urllib3.disable_warnings()

	# 线程执行方法
	def run(self):
		# 请求
		r = requests.get(url=self.url, headers=self.headers)

		# 状态码不是200，返回
		if r.status_code != 200:
			return

		# 有的返回json，有的返回字符串
		try:
			r = json.loads(r.content.decode('utf-8', 'ignore'))
		except:
			pass

		# 诗词，解析
		if self.type == '诗词':
			r = r['content']

		# 甜言蜜语，解析
		if self.type == '甜言蜜语':
			r = r['returnObj'][0]

		# 鸡汤，解析
		if self.type == '鸡汤':
			tree = etree.HTML(r.replace('\\n', '').replace('\\', ''))
			r = tree.xpath('//span/text()')[0].replace(' ', '')

		# 马屁精，返回的是字符串
		if self.type == '马屁精':
			r = r.content.decode('utf-8', 'ignore')

		# 返回结果
		return r


if __name__ == '__main__':
	print(Chat('诗词').run())
	print(Chat('甜言蜜语').run())
	print(Chat('鸡汤').run())
	print(Chat('马屁精').run())

