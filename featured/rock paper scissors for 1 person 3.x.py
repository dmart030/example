import random as rand

class generator:
    
    def __init__(self, player_choice, computer_choice):
        self.computer_choice = computer_choice
        self.player_choice = player_choice
    def comp_gen_c(self):
        print('Your choice: ', self.player_choice, '\nComputer choice: ', self.computer_choice)
        if self.player_choice == self.computer_choice:
            print('draw')
        elif self.player_choice == 'paper' and self.computer_choice != 'paper':
            if self.computer_choice == 'rock':
                print('You win!')
            else:
                print('You lose!')
        elif self.player_choice == 'rock' and self.computer_choice != 'rock':
            if self.computer_choice == 'paper':
                print('You lose!')
            else:
                print('You win!')
        elif self.player_choice == 'scissors' and self.computer_choice != 'scissors':
            if self.computer_choice == 'rock':
                print('You lose!')
            else:
                print('You win!')
    def comp_choice_rand(self):
        self.computer_choice = rand.choice(r_p_s)
    def check_pchoice(self):
        while True:
            if self.player_choice == 'rock' or self.player_choice == 'paper' or self.player_choice == 'scissors':
                break
            elif self.player_choice == 'exit':
                exit()
            else:
                self.player_choice = raw_input('Please input rock, paper or scissors correctly... type in exit to exit the program. \n').lower()
                continue
    def exit_check(self):
        if self.player_choice == 'exit':
            exit()
r_p_s = ['rock', 'paper', 'scissors']
while True:
    g1 = generator(input('Please input rock paper or scissors only: ').lower(), rand.choice(r_p_s))
    g1.exit_check()
    g1.check_pchoice()
    g1.comp_choice_rand()
    g1.comp_gen_c()


