#ex40

class Song(object):

    def __init__(self, entered_words):
        self.lyrics = entered_words

    def sing_me_a_song(self):
        for words in self.lyrics:
            print (words)


birthday_song = Song (['Jingle bells, jingle bells',
'Jingle all the way',
'Oh, what fun it is to ride',
'In a one horse open sleigh']) #it is a list of 4 elements

print ('\n')

birthday_song.sing_me_a_song() #every of 4 elements is printed on a separete line

birthday_1 = Song('Jingle bells, jingle bells\n') #it is a string and every element is printed on a separete line, like
#J
#i
#n
#g
#l
#e
#...

birthday_2 = Song(['Jingle all the way'])
birthday_3 = Song(['Oh, what fun it is to ride'])
birthday_4 = Song(['In a one horse open sleigh'])

print ('\n')

birthday_1.sing_me_a_song()
birthday_2.sing_me_a_song()
birthday_3.sing_me_a_song()
birthday_4.sing_me_a_song()

print ('\n')

song = ['Jingle', 'bells,', 'jingle', 'bells' ]
for ignore in song:
    print (ignore)
