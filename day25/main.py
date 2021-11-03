import turtle as t
import pandas

screen = t.Screen()
screen.title('U.S. States Game')
image = 'C:/Users/karey/Documents/Python/day25/blank_states_img.gif'
screen.addshape(image)
t.shape(image)
states = pandas.read_csv('C:/Users/karey/Documents/Python/day25/50_states.csv')


us_states = states['state'].to_list()
guessed_states = []

correct = 0
user_answer = screen.textinput(title='Guess the State', prompt="guess a state")

while guessed_states < 50:
    user_answer = user_answer.capitalize()
    lenth_of_list = len(us_states)
    

    if user_answer == 'Exit':
        game_is_on = False

        missing_states = [state for state in us_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('C:/Users/karey/Documents/Python/day25/missed.csv')
        break


    if user_answer in us_states:
        guessed_states.append(user_answer)
       
        state_name = t.Turtle()
        state_name.hideturtle()
        state_name.penup()
        x_and_y = states[states['state'] == user_answer]
        x_of_state = x_and_y['x']
        y_of_state = x_and_y['y']
        correct+=1
        state_name.goto(int(x_of_state), int(y_of_state))
        state_name.write(user_answer.capitalize())
        

    elif user_answer not in us_states:
        state_name = t.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(0,300)
        state_name.write('you suck! try again!')

    user_answer = screen.textinput(title=f'{correct}/{lenth_of_list} States Correct', prompt="What's another state")

