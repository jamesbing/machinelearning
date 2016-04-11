class Song(object):
    def __init__(self, lyrics):
       self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday toy you",
                  "I don't want to get sued.",
                  "So I will stop right there"])

country_roads = Song(["Country roads,",
                     "take me home",
                     "to the place",
                     "I belong~~~OHOHO"])

happy_bday.sing_me_a_song()

country_roads.sing_me_a_song()
