#!/usr/bin/python
# -*- coding: latin-1 -*-
import pprint
import sys
import os
import subprocess
import time
import spotipy

import spotipy.util as util
from ast import literal_eval

date=time.strftime("%d/%m/%Y")
#bash
#export CLIENT_ID={yourclient}
#export CLIENT_SECRET={yoursecret}
#export REDIRECT_URI={your redirect uri}

def fix_enc(data):
 name= data
 try:
  data=name.decode("utf-8")
  final_name = data.encode("latin-1","ignore")
  return final_name 
 except: 
  final_name =name.encode("latin-1","ignore")
  return final_name

def show_tracks(tracks):
    dictop={}
    dictjson={}
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    date=time.strftime("%d/%m/%Y")
    dictjson["day"]=date
    list_items=[]
    #elements=[]
    for i, item in enumerate(tracks['items']):
        track = item['track']
        song_info = track['external_urls']['spotify']
        song_info = song_info.split("/")
        urn_g = 'spotify:artist:'+track['artists'][0]['id']
        genre=sp.artist(urn_g)
        genre = str(genre['genres']).replace("u","")
        id_Artists= track['artists'][0]['id']
        #print track['artists'][0]['name'].encode('utf-8').strip(),"->", track['name'].encode('utf-8').strip()
        #print genre
        id = track['external_urls']['spotify'].split("/")
        id=id[-1]
        #listlist
        list1=[fix_enc(track['artists'][0]['name']),fix_enc(track['name'])]
        list2.append(list1)
        list3=[fix_enc(id),fix_enc(track['artists'][0]['name']),fix_enc(track['name'])]
        list4.append(list3)
        list1=[]
        list3=[]
        #json
        list_items.append('"name:"'+fix_enc(track['artists'][0]['name'])+","+'"artist:"'+fix_enc(track['name']))
        dictjson['"items"']=list_items
        #dict
        a=fix_enc(track['artists'][0]['name'])
        b=fix_enc(track['name'])
        dictop[id]=a+","+b
            
    #json
    with open('data.json',"w") as data_file:
     data_file.write("{"+fix_enc(str(dictjson)) +"}")
    #lists
    with open('data.txt',"w") as data_file:
     data_file.write(fix_enc(str(dictop)))  
    #listsof list
    with open('fromSpotify',"w") as data_file:
     data_file.write(fix_enc(str(list2)))
    with open('datos2',"w") as data_file:
     data_file.write(fix_enc(str(list4)))


def get_tracks_oplaylist(sp,selec_playlist):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
     if(playlist['name']==selec_playlist):
      playlist_set=playlist['id'] 
      results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
      tracks = results['tracks']
      show_tracks(tracks)
      while tracks['next']:
        tracks = sp.next(tracks)
        show_tracks(tracks)

def create_newplaylist(username,sp):
 date=time.strftime("%d/%m/%Y")
 playlist_name=date
 new_playlists = sp.user_playlist_create(username, playlist_name)
 return new_playlists['id']

def add_song(username,sp,tracks_add,playlist_set):
 sp.user_playlist_add_tracks(username,playlist_set,tracks_add)
 


username = 'ramrodo'
scope='playlist-modify-private playlist-modify playlist-read-private	user-top-read' 
token = util.prompt_for_user_token(scope,scope)
sp = spotipy.Spotify(auth=token)

#opcional, testing
#playlists = sp.user_playlists(username)
#for playlists in playlists['items']:
 #print playlists['name']

if token:
 #selec_playlist=raw_input("playlist: ")
 #elements=[]
 new_playlistsid=create_newplaylist(username,sp)
 get_tracks_oplaylist(sp,"botrock")
    
 #tracks_add= ['spotify:track:1zHlj4dQ8ZAtrayhuDDmkY']    
 
 #archivofromHandler
 #nombre,artist,true
 elements={}
 num=0
 listplay=[]
 list_play=[]
 with open("datos2","r") as data_file:
   dat=data_file.read()
   dat=literal_eval(dat)

 for item in dat:
  list_play.append(item[0])
 while(1):
  try:
   with open('fromHandler',"r") as data_file:
    winner=data_file.read()
    winner=literal_eval(winner)
   for id in dat:
   #print winner[0] 
   #print id[0]
    if(winner[0]==id[1] and winner[1]==id[2]):
     if id[0] in list_play:
     #print id[0]   
     #print list_play
     
      id_ad="spotify:track:"+str(id[0])
      tracks_add= [id_ad]
      add_song(username,sp,tracks_add,new_playlistsid)
      indexdel=list_play.index(id[0])
      del list_play[indexdel]
  except:
   nada=0
 #analysis = sp.audio_analysis(tid)

else:
    print("Can't get token for", username)