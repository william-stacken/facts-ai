from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

train = False

chatbot = ChatBot('Faccts')
trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)

if train:
	trainer.train(
	    "chatterbot.corpus.english"
	)

	list_trainer.train([
		"What is artificial intelligence?",
		"AI can be described as an area of computer science that simulates human intelligence in machines. It’s about smart algorithms making decisions based on the available data.",
		"What do you understand by Artificial Intelligence?",
		"Artificial intelligence is computer science technology that emphasizes creating intelligent machine that can mimic human behavior. Here Intelligent machines can be defined as the machine that can behave like a human, think like a human, and also capable of decision making. It is made up of two words, 'Artificial' and 'Intelligence,' which means the 'man-made thinking ability.'",
		"Why do we need Artificial Intelligence?",
		"The goal of Artificial intelligence is to create intelligent machines that can mimic human behavior. We need AI for today's world to solve complex problems, make our lives more smoothly by automating the routine work, saving the manpower, and to perform many more other tasks."
		"What are the dangers with AI?",
		"Tay was a chatbot developed by Microsoft intendend to learn from users on Twitter. However, trolls quickly started to teach it racist and conspiracy theorist ideas, making it support nazism and claiming that Bush did 9/11. As such, Microsoft closed it down after just a few hours, fearing that it would hurt their image. So make sure to not teach me anything bad!",
		"What was the first artificial intelligence?",
		"The first AI program to run in the United States was a checkers program, written in 1952 by Arthur Samuel for the prototype of the IBM 701",
		"Should I study artificial intelligence?",
		"You definitely should!",
		"What are artificial intelligence Neural Networks?",
		"Artificial intelligence Neural Networks can model mathematically the way biological brain works, allowing a machine to think and learn the same way the humans do, which makes them capable of recognizing things like speech, objects and animals just like humans.",
		"What is the difference between strong AI and weak AI?",
		"Strong AI makes strong claims that computers can be made to think on a level equal to humans while weak AI simply predicts that some features that are resembling to human intelligence can be incorporated to computer to make it more useful tools.",
	])

class SimpleChatbot(WebSocket):
	def handleMessage(self):
		try:
			print(self.data)
			resp = chatbot.get_response(self.data)
			print(resp)
			self.sendMessage(resp.text)
		except Exception as e:
			print(e)

	def handleConnected(self):
		print(self.address, 'connected')

	def handleClose(self):
		print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, SimpleChatbot)
server.serveforever()
