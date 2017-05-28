# coding=utf-8
from random import choice
from time import time
from enum import Enum
from ast import literal_eval
from random import random

class selectorHandler:
	# Initialization
	def __init__(self, idleTime, waitForRespTime):
		self.staticList = {}
		self.selectedSong = None

		self.idleTime = idleTime
		self.waitForRespTime = waitForRespTime
		self.timer = Timer()
		self.state = state.INIT
		self.procResState = state.REQVOTRES

		self.votationResult = None	

		# INTERFACE VARIABLES
		self.EXT_REQVOT = False
		self.EXT_REQVOTRES = False
		self.EXT_VOTRESREADY = False
		self.EXT_VOTRES = None
		self.EXT_LIST = []

	# Main function
	def stateMachine(self):
		if state.INIT == self.state:
			# Check if the list is received
			if True == self.listGot():
				# Send request to clients to vote
				self.processRequest()
				self.state = state.WAIT_RESPONSE
				self.timer.setTimer(self.waitForRespTime)

		elif state.IDLE == self.state:
			# Wait for response
			if True == self.timer.finished():
				# Timeout. Now do a new request to client
				self.processRequest()

				# Change to WAIT_RESPONSE state
				self.state = state.WAIT_RESPONSE
				self.timer.setTimer(self.waitForRespTime)

		elif state.WAIT_RESPONSE == self.state:
			# Wait for response
			if True == self.timer.finished():
				# Timeout. Process the response
				if True == self.processResponse():
					# Change to IDLE when the process is done
					self.state = state.IDLE
					self.timer.setTimer(self.idleTime)

	def	processRequest(self):
		print("\nREQUEST: Chatbot to do their thing.")
		#self.requestToClient()

	def	processResponse(self):
		print("PROCESS: the response from the Chatbot.")
		rtn = False

		if state.REQVOTRES == self.procResState:
			# Tell that you need the votation results
			# self.reqVotationRes();
			self.procResState = state.GETBOTRES;
			
		elif state.GETBOTRES == self.procResState:
			# check if the response is ready
			if True == self.votationResultReady():
				songs = self.getVotationResult()
				winner = self.getWinnerFromVotationResult(songs)
				print('    Result got:', winner)
				
				self.sendSelectedSong( winner )
				
				# leave ready the state
				self.procResState = state.GETBOTRES
				
				rtn = True

		return rtn
		
	def getWinnerFromVotationResult(self, songsList):
		songNameList = []
		totalVoteList = []
		
		# Get elements
		for songName, totalVote in songsList:
			songNameList.append(songName)
			totalVoteList.append(totalVote)
		
		# Get max and return
		winnerIdx = totalVoteList.index( max(totalVoteList) )
		winner = songNameList[winnerIdx]
		
		return winner


	##### INTERFACE FUNCTIONS #####

	# Chatbot
	def requestToClient(self):
		self.EXT_REQVOT = True
		
	def reqVotationRes(self):
		self.EXT_REQVOTRES = True
		
	def votationResultReady(self):
		# return self.EXT_VOTRESREADY
		return True

	def getVotationResult(self):
		# self.votationResult = self.EXT_VOTRES
		with open('fromChatbot','r') as f:
			txt = f.read()
			if [] != txt:
				# self.votationResult = literal_eval(txt)
				self.votationResult = []
				temp = literal_eval(txt)
				for nameAndArt in temp:
					self.votationResult.append([nameAndArt, random()])
					
				
		self.EXT_REQVOT = False;
		self.EXT_REQVOTRES = False;
		self.EXT_VOTRESREADY = False;
		self.EXT_VOTRES = None;
		
		return self.votationResult

	# Spotify
	def listGot( self ):
		rtn = False
		# self.staticList = self.EXT_LIST
		with open('fromSpotify','r') as f:
			txt = f.read()
			if [] != txt:
				self.staticList = literal_eval(txt) 
		if [] != self.staticList:
			rtn = True
		return rtn
		
	def getList( self ):
		return self.staticList

	def sendSelectedSong( self, winner ):
		# self.EXT_SELECTEDSONG = songId
		with open('fromHandler','w') as f:
			f.write(str(winner))


class state(Enum):
	INIT = 1
	IDLE = 2
	WAIT_RESPONSE = 3
	
	REQVOTRES = 4
	GETBOTRES = 5

class Timer():
	def __init__(self):
		self.target = 0.0
		self.counter = 0.0
		self.sample1 = 0.0
		
	def finished(self):
		rtn = False
				
		if self.target > self.counter:
			sample2 = time()
			
			self.counter = self.counter + (sample2 - self.sample1)
			self.sample1 = sample2
		else:
			rtn = True

		return rtn
		
	def setTimer(self, target):
		self.target = target;
		self.counter = 0.0;
		self.sample1 = time();
