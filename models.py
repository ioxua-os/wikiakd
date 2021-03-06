from datetime import date
class Article:
	def __init__(self, id, title, subtitle=None, blocks=[], author=None, leader=None, publishDate=date.today()):
		self.publishDate = publishDate
		self.subtitle 	= subtitle
		self.blocks		= blocks
		self.author		= author
		self.leader		= leader
		self.title		= title
		self.id 		= id

	def contains(self, query):
		where_to_look = [self.title, self.author, self.leader, self.subtitle]
		where_to_look = [each.upper() for each in where_to_look]
		has = False
		for each in where_to_look:
			has = has or each.__contains__(query)
		#if not has:
		#	has = reduce((lambda temp, each: each.upper().contains(query, [each.paragraphs for each in self.blocks])))
		return has

	def __repr__(self):
		return "<Article title:{} subtitle:{} leader:{} author:{}>".format(self.title, self.subtitle, self.leader, self.author)

class ArticleBlock:
	def __init__(self, title=None, paragraphs=[]):
		self.title 		= title
		self.paragraphs = paragraphs
	
	def __repr__(self):
		return "<Block title:{} paragraphs:{}>".format(self.title, self.paragraphs)
