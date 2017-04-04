#Global variables to be used
board=[]
player1_numbers = []
player2_numbers = []
winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
tie = 0

#create the board
def create_board():
    global board
    board = list(range(0,9))
    print_board()

#print the board
def print_board():    
    print (board[:3])
    print (board[3:6])
    print (board[6:])

#Create Players
def create_players(num):
    return input("Player no %d Username: " % (num))
    

#Play the game
def change_board(players):
    global board
    win = False
    global tie
    index = 0
    while (win == False or tie < 9):
        number =(input("Choose a number %s bewtween 0-8 " % (players[index])))
        if (number.isalpha()):
            print("Choose a number not a letter " + players[index])
            continue
        
        elif (int(number) in player1_numbers or number in player2_numbers):
            print("Number already picked " + players[index])
            continue
            
        elif (int(number) >= 10):
            print("Choose a number between 0-8 " + players[index])
            continue
        else:
            number = int(number)
            if index == 0:
                board[number] = 'X'
                player1_numbers.append(number)
                print_board()
                win = check_win(player1_numbers,players[index])
                index = 1
            else:
                board[number] = 'O'
                player2_numbers.append(number)
                print_board()
                win = check_win(player2_numbers,players[index])
                index = 0
        tie+=1
    else:
        start_new()


        
#Check winning conditions
def check_win(numbers,player):
    if (tie == 8):
        print ("You are tied")
        return True
    for win in winning_combos:
        counter = 0;
        for  number in numbers:
            if number in win:
                counter+=1
                if counter == 3:
                    print("Congratulations you win " + player)
                    return True

    else:
        
        return False

def start_new():
    if input("You want a new game(Y/n)?") != 'n':
        global player1_numbers
        global player2_numbers
        player1_numbers = []
        player2_numbers = []
        start_the_game()
    else:
        print ("Thanks for playing the first game i made")



def start_the_game():
    player1 = create_players(1)
    player2 = create_players(2)
    players = [player1,player2]
    create_board()
    change_board(players)

start_the_game()




