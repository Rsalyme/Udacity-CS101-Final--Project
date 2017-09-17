# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

#Using re module as a delimiter tool to manage data in example input#

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
# -----------------------------------------------------------------------------
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure



def create_data_structure(datafeed):
    delimiters = '.'
    data = split(delimiters,datafeed,maxsplit=200) #maxsplit allows control of how much data is entered into the structure.
    #this is used to build the structure on the fly
    network = build_network()
    #gets users
    users = get_users(data)
    #gets games
    games = get_games(data)
    add_games = add_game_data(users,games)
    friends = get_friends(data)
    add_friends = add_friend_data(users,friends)
    for player in users:
        network[player]['games'] = add_games[player]
        network[player]['friends'] = add_friends[player]
    print network
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #
# SPLIT PROCEDURE IS USED TO SEPERATE EACH LINE IN THE INPUT INTO ONE ENTRY

def build_network():
    #Found that this will build the initial data structure on the fly
    import collections
    return collections.defaultdict(dict)

def split(delimiters, string_input, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    datafeed = re.split(regexPattern, string_input, maxsplit)
    return datafeed

def get_users(datafeed):
    users = list()
    for update in datafeed:
        if update != '':
            new_list = update.split(' ')
            if new_list[0] not in users:
                users.append(new_list[0])
    return users

def get_games(datafeed):
    gameslog = list()
    for update in datafeed:
        if update != '':
            if ' likes to play ' in update:
                gameslog.append(update)
    return gameslog
#creates a list of games
def add_game_data(users,gameslog):
    users_games = {}
    user_count = 0
    for feed in gameslog:
        data = []
        #finds 'play' and uses that as a keyword to grab the right data
        position = feed.find('play ')
        value_data = feed[position + 5:]
        better_data = value_data.split(',')

        for dataentry in better_data:
            if dataentry.find(' ') == 0:
                data.append(dataentry[1:])
            else:
                data.append(dataentry)
        users_games[users[user_count]] = data
        user_count += 1
    return users_games
#creates a list of friends and organizes the data
def get_friends(datafeed):
    friendsfeed = list()
    for update in datafeed:
        if update != '':
            if ' is connected to ' in update:
                    friendsfeed.append(update)
    return friendsfeed
#takes the list of friends created by get_friends and is used to add the data to the dictionary
def add_friend_data(users,friendslist):
    friendlist = {}
    user_count = 0
    for feed in friendslist:
        data = []
        feedlist = feed.split()
        for i in range(4, len(feedlist)):
            if ',' in feedlist[i]:
                data.append(feedlist[i][0:-1])
            else:
                data.append(feedlist[i])
        friendlist[users[user_count]] = data
        user_count += 1
    return friendlist


#####################################################
#################################################


#####################################################

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.


def get_connections(network, user):
    empty = []
    if user not in network:
        return None
    elif network[user]["friends"] == empty:
        return empty
    else:
        return network[user]['friends']


# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    empty = []
    if user not in network:
        return None
    elif network[user]["games"] == empty:
        return empty
    else:
        return network[user]['games']

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        network = False
    if user_A in network and user_B in network:
        network[user_A]['friends'].append(user_B)
	return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network[user] = {"friends" : [], "games" : games}
        return network
    else:
        return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    friends_of_friends = []
    clean_data = []
    count = 0
    if user not in network:
        return None
    elif network[user]['friends'] == []:
        return []
    else:
        for player in network[user]['friends']:
            for friends in network[player]['friends']:
                if friends in friends_of_friends:
                    count += 1
                else:
                    friends_of_friends.append(network[player]['friends'])
                    count += 1
        #this takes all of that data and creates a clean list without repetition
        for list in friends_of_friends:
            for person in list:
                if person not in clean_data:
                    clean_data.append(person)
                else:
                    None
    return clean_data



# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    incommon =  0
    if user_A not in network or user_B not in network:
        return False
    for frienda in network[user_A]['friends']:
        for friendb in network[user_B]['friends']:
            if frienda == friendb:
                incommon = incommon + 1
    return incommon

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def path_to_friend(network, user_A, user_B, path=None):
#path is used so that the data is passed through on each iteration
    if (user_A not in network) or (user_B not in network):
        return None
    if (user_A == user_B):
        return None

    if path is None:
        path = []
        path = path + [user_A]

    if user_B in network[user_A]['friends']:
        return path + [user_B]
    for connection in network[user_A]['friends']:
        if connection not in path:
            newpath = path_to_friend(network, connection, user_B, path)
            if newpath:
                return newpath
    return None


# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------

def player_popularity_rank(network):
    import operator #used to sort the data later
    player_popularity_ranks = [] #master list of the current popularity ranks
    if player_popularity_ranks == []:
        for user in network:
            top_player = [user, len(network[user]['friends'])] #finds the first player and adds them as the top player
            player_popularity_ranks.append(top_player)
            #organizes players by the number of friends in their personal network
    player_popularity_ranks = sorted(player_popularity_ranks, key=operator.itemgetter(1), reverse= True )
    return player_popularity_ranks
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

net = create_data_structure(example_input)
print net
print path_to_friend(net, "John", "Ollie")
print get_connections(net, "Debra")
print add_new_user(net, "Debra", [])
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print add_connection(net, "John", "Freda")
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Mercedes", "John")
print player_popularity_rank(net)
