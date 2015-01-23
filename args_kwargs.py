__author__ = 'rsukla'


#this program will demostrate the use of arguement and keyword arguement

#Args -- is called as ARGUEMENT

#kwargs is known as Keyword ARGUEMENT

def unlimited(*args):  # here I don't know how many arguements will the user be passing

    for arg in args:

        print arg

def kaw(x = 67, y = 87):

    print x, y

def kawk(**kwargs):

    for item in kwargs.items():

        print item

def combined(*args, **kwargs):

    for arg in args:

        print arg

    for item in kwargs.items():

        print item

l = [1,2,3,4,5,6,7,87]

unlimited(1,2,3,4,5,6,7,8,9,'Ham')

unlimited(l)

unlimited(*l)  #it is passing as indivual arguments not as the whole group

kaw()

kaw(x = 100, y = 456)  #now here I am passing the keyword arguements

kawk(x = 456, y = 456)


combined(1,2,3,4,5,56,6,6,76,7,7,8, x= 34)

