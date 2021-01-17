#  ______                  _    ___                _     _                   
 #/ _____)             _  (_)  / __)           _  | |   (_)                  
#( (____  ____   ___ _| |_ _ _| |__ _   _    _| |_| |__  _ ____   ____       
 #\____ \|  _ \ / _ (_   _| (_   __| | | |  (_   _|  _ \| |  _ \ / _  |      
 #_____) | |_| | |_| || |_| | | |  | |_| |    | |_| | | | | | | ( (_| |_ _ _ 
#(______/|  __/ \___/  \__|_| |_|   \__  |     \__|_| |_|_|_| |_|\___ (_(_(_)
#        |_|                       (____/                       (_____|    



import tkinter as tk
import webbrowser

myWindow = tk.Tk()
myWindow.title("Smart Music")
myWindow.geometry("750x650")
myWindow.configure(background="skyblue")

#functions

def openSpotify():
	print ("opening Spotify")
	webbrowser.open("https://www.spotify.com/ca-en/")


      

#widgets
def openPlaylist1():

	genreChoice = clicked.get()

	if genreChoice == "Country":		
		print ("Opening Playlist Shortly")
		webbrowser.open("https://open.spotify.com/playlist/6nU0t33tQA2i0qTI5HiyRV")

	elif genreChoice == "EDM":
		print ("Opening your EDM playlist")
		webbrowser.open("https://open.spotify.com/album/37bu5iGP8qyG50MbFUKbGi")

	elif genreChoice == "Dubstep":
		print ("Opening your Dubstep playlist")
		webbrowser.open("https://open.spotify.com/playlist/3ObJ6Qra3CkV0gNCRTtK0c")

	elif genreChoice == "Rock":
		print ("Opening your playlist")
		webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U")

	elif genreChoice == "Jazz":
		print ("Opening your playlist")
		webbrowser.open("https://open.spotify.com/album/3CyBEjSTEzyWpy4TiYqUG7")

	elif genreChoice == "Rythme and Blues":
		print ("Opening your playlist")
		webbrowser.open("https://open.spotify.com/playlist/4LGAv0NaO26BRUt8Qb1z9w")

	elif genreChoice == "Techno":
		print ("Techno")
		webbrowser.open("https://open.spotify.com/playlist/18vUeZ9BdtMRNV6gI8RnR6")

	elif genreChoice == "Electro":
		print ("Electro")
		webbrowser.open("https://open.spotify.com/playlist/317O0e8iWJLClLGDKtieRe")

	elif genreChoice == "Indie Rock":
		print ("Indie Rock")
		webbrowser.open("https://open.spotify.com/playlist/7MqwKicbWkSqg8NqTlRPoe")

	elif genreChoice == "pop":
		print ("Finding a pop playlist for you")
		webbrowser.open("https://open.spotify.com/playlist/6mtYuOxzl58vSGnEDtZ9uBe")

	elif genreChoice == "rap":
		print ("Opening a rap playlist for you")
		webbrowser.open("https://open.spotify.com/album/2tqwPdJ1mkF9r6WWJjg1d4")

	elif genreChoice == "Hip Hop":
		print ("Hip Hop")
		webbrowser.open("https://open.spotify.com/album/1tIioq32KjWlt5vvk5rhqX")

	elif genreChoice == "60s":
		print ("opening 60s Playlist")
		webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DXaKIA8E7WcJj")

	elif genreChoice == "70s":
		print ("70s")
		webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DWTJ7xPn4vNaz")

	elif genreChoice == "80s":
		print ("Opening 80s playlist for you")
		webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DX4UtSsGT1Sbe")

	elif genreChoice == "90s":
		print ("Opening a Playlist for you")
		webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l")

	elif genreChoice == "00s":
		print ("2000s")
		webbrowser.open("https://open.spotify.com/album/3XTLNIxNWyqxOWBSfS6bw5")

	elif genreChoice == "10s":
		print ("10s Genre playlist opening now")
		webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DX5Ejj0EkURtP")

	elif genreChoice == "Trending Now":
		print ("A playlist for you!")
		webbrowser.open("https://open.spotify.com/playlist/1pMB5VwjH6fzf8ldHch1IG")

#button
myButton0 = tk.Button(myWindow, text = "Spotify Main Page", height = 10, width = 30, fg="Gray", font="none 15 bold",command = openSpotify)
myButton1 = tk.Button(myWindow, text = "Open a playlist for you", height = 10, width = 30, fg="Gray", font="none 25 bold", command = openPlaylist1)


#Label
myLabel1 = tk.Label(myWindow, text="Welcome to Smart Music", bg="skyblue", fg="white", font="none 64 bold")

#Drop Down Menu
clicked = tk.StringVar()
clicked.set("Trending Now")
drop = tk.OptionMenu(myWindow, clicked, "Country", "EDM", "Dubstep", "Rock", "Jazz", "Rythme and Blues", "Techno", "Electro", "Indie Rock", "pop", "rap", "Hip Hop", "60s", "70s", "80s", "90s", "00s", "10s", "Trending Now")

#grid
drop.grid(row=0, column=0)
myLabel1.grid(row=1, column=0)
myButton0.grid(row=2, column=0)
myButton1.grid(row=3, column=0)


myWindow.mainloop()