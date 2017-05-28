from selectorHandler import selectorHandler

votHandler = selectorHandler(25,1)

while True:
	#votHandler.EXT_VOTRESREADY = True
	#votHandler.EXT_VOTRES = {"Name 1":1, "Name 2":3, "Name 1":8}
	#	votHandler.EXT_LIST = [0,1]
	votHandler.stateMachine()

