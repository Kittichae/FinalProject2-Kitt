from PyQt5.QtWidgets import *
from Project2 import *
import random, csv, os


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    Defines the controller class and sets default variables that are used in the following functions.
    """
    player_wins = 0
    player_grandtotal = 0
    computer_wins = 0
    computer_grandtotal = 0
    computer_choice = 0
    windividual = ''

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the class, sets the home_page as the default widget stack for the GUI, and calls the file_check
        function.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.file_check()

    def file_check(self) -> None:
        """
        Function to check for the presence of a scoresheet.csv, or create it if there is none found.
        :return:
        """
        if os.path.isfile('./scoresheet.csv'):
            pass
        else:
            with open('scoresheet.csv', 'a', newline='') as scoresheet:
                score_sheet = csv.writer(scoresheet)

    def play(self) -> None:
        """
        When activated, changes the displayed page to the game_page and resets the page to default settings.
        :return:
        """
        self.stackedWidget.setCurrentWidget(self.game_page)
        self.resetgame()

    def results(self) -> None:
        """
        When activated, sets the displayed page to the resultpage.
        :return:
        """
        self.stackedWidget.setCurrentWidget(self.resultpage)

    def home(self) -> None:
        """
        When activated, sets the displayed page to the home_page
        :return:
        """
        self.stackedWidget.setCurrentWidget(self.home_page)

    def computer_rand(self) -> None:
        """
        When called, this function determines the computer_choice and sets the Computerimage widget to the appropriate
        image.
        :return:
        """
        self.computer_choice = random.randint(1, 5)
        if self.computer_choice == 1:
            self.Computerimage.setIcon(QtGui.QIcon("Rock.jpg"))
        elif self.computer_choice == 2:
            self.Computerimage.setIcon(QtGui.QIcon("Paper.jpg"))
        elif self.computer_choice == 3:
            self.Computerimage.setIcon(QtGui.QIcon("Scissors.jpg"))
        elif self.computer_choice == 4:
            self.Computerimage.setIcon(QtGui.QIcon("Lizard.jpg"))
        elif self.computer_choice == 5:
            self.Computerimage.setIcon(QtGui.QIcon("Spock.jpg"))


    def rockpush(self) -> None:
        """
        Function to select the player's choice as rock and call the computer_rand function, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 3:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Rock crushes scissors, player wins.')
        elif self.computer_choice == 4:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Rock crushes lizard, player wins.')
        elif self.computer_choice == 2:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Rock is covered by paper, computer wins.')
        elif self.computer_choice == 5:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Rock is vaporized by Spock, computer wins.')
        elif self.computer_choice == 1:
            self.Message_box.setPlainText('Draw, both chose Rock')
        self.update_scores()

    def paperpush(self) -> None:
        """
        Function to select the player's choice as paper and call the computer_rand function, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 1:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Paper covers rock, player wins.')
        elif self.computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Paper disproves Spock, player wins.')
        elif self.computer_choice == 3:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Paper is cut by scissors, computer wins.')
        elif self.computer_choice == 4:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Paper is eaten by lizard, computer wins.')
        elif self.computer_choice == 2:
            self.Message_box.setPlainText('Draw, both chose Paper')
        self.update_scores()

    def scissorpush(self) -> None:
        """
        Function to select the player's choice as scissors and call the computer_rand function, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Scissors cut paper, player wins.')
        elif self.computer_choice == 4:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Scissors decapitate lizard, player wins.')
        elif self.computer_choice == 1:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Scissors are smashed by rock, computer wins.')
        elif self.computer_choice == 5:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Scissors are smashed by Spock, computer wins.')
        elif self.computer_choice == 3:
            self.Message_box.setPlainText('Draw, both chose Scissors')
        self.update_scores()

    def lizardpush(self) -> None:
        """
        Function to select the player's choice as lizard and call the computer_rand function, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 2:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Lizard eats paper, player wins.')
        elif self.computer_choice == 5:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Lizard poisons Spock, player wins.')
        elif self.computer_choice == 1:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Lizard is smashed by rock, computer wins.')
        elif self.computer_choice == 3:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Lizard is decapitated by scissors, computer wins.')
        elif self.computer_choice == 4:
            self.Message_box.setPlainText('Draw, both chose Lizard')
        self.update_scores()

    def spockpush(self) -> None:
        """
        Function to select the player's choice as spock and call the computer_rand function, then determine the
        outcome and update the scores.
        :return: None
        """
        self.computer_rand()
        if self.computer_choice == 1:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Spock vaporizes rock, player wins.')
        elif self.computer_choice == 3:
            Controller.player_wins += 1
            self.Message_box.setPlainText('Spock smashes scissors, player wins.')
        elif self.computer_choice == 2:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Spock is disproven by paper, computer wins.')
        elif self.computer_choice == 4:
            Controller.computer_wins += 1
            self.Message_box.setPlainText('Spock is poisoned by lizard, computer wins.')
        elif self.computer_choice == 5:
            self.Message_box.setPlainText('Draw, both chose Spock')
        self.update_scores()

    def resetgame(self) -> None:
        """
        Function to reset the scores, the message box message, and the Computerimage, as well as call the update_scores
        function.
        :return: None
        """
        Controller.computer_wins = 0
        Controller.player_wins = 0
        self.update_scores()
        self.Computerimage.setIcon(QtGui.QIcon(""))
        self.Message_box.setPlainText('The rules are simple:\n'
                                 'Scissors cut paper, paper covers rock, rock crushes lizard,\n'
                                 'lizard poisons Spock, Spock smashes scissors, scissors decapitate lizard,\n'
                                 'lizard eats paper, paper disproves Spock, Spock vaporizes rock,\n'
                                 'and as it always has, rock crushes scissors.')

    def update_scores(self) -> None:
        """
        Function to update the scores displayed on the GUI and call the win_check function.
        :return: None
        """
        self.Player_wins.setText(f'Player wins: {self.player_wins}')
        self.Computer_wins.setText(f'Computer wins: {self.computer_wins}')
        self.win_check()

    def win_check(self) -> None:
        """
        Function to check for a winner (best out of 5 rounds) and set the resultbox to the appropriate winner. Function
        also calls the results and update_text functions, and sets the windividual variable accordingly.
        :return:
        """
        if self.player_wins >= 3:
            self.player_grandtotal += 1
            self.resultbox.setText("Player Wins")
            self.windividual = 'Player'
            self.results()
            self.update_text()
        elif self.computer_wins >= 3:
            self.computer_grandtotal += 1
            self.resultbox.setText("Computer Wins")
            self.windividual = 'Computer'
            self.results()
            self.update_text()
        self.Message_box2.setPlainText(self.Message_box.toPlainText())

    def update_text(self) -> None:
        """
        Function to add the game information to the scoresheet.csv for record keeping.
        :return:
        """
        with open('scoresheet.csv', 'a', newline='') as scoresheet:
            score_list = csv.writer(scoresheet)
            fields = [self.player_wins, self.computer_wins, self.windividual, self.player_grandtotal, self.computer_grandtotal]
            score_list.writerow(fields)

    def previousscores(self) -> None:
        """
        Function to set the displayed page to the score_page, and to read the scoresheet.csv file to the score_box in
        order to display previous game scores. The try/except block is in place to stop a rangeError in the event
        that the scoresheet.csv is empty, i.e. if it has just been created or reset.
        :return:
        """
        self.stackedWidget.setCurrentWidget(self.score_page)
        self.score_box.setText('Player rounds\t Computer rounds\t\tWinner\t\tPlayer wins\tComputer wins\t')
        with open('scoresheet.csv', 'r') as scoresheet:
            score_sheet = csv.reader(scoresheet)
            try:
                for row in score_sheet:
                    if row[2] == 'Player':
                        self.score_box.setText(f'{self.score_box.text()}\n{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}\t\t\t{row[3]}\t\t{row[4]}')
                    elif row[2] == 'Computer':
                        self.score_box.setText(f'{self.score_box.text()}\n{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}')
            except:
                pass

    def reset_data(self) -> None:
        """
        Function to reset the player_grandtotal and computer_grandtotal variables to 0, reset scoresheet.csv to empty,
        and call the previousscores function.
        :return:
        """
        self.player_grandtotal = 0
        self.computer_grandtotal = 0
        with open('scoresheet.csv', 'w+', newline='') as scoresheet:
            score_sheet = csv.writer(scoresheet)
        self.previousscores()
