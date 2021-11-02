import turtle as t
import pandas

screen = t.Screen()
screen.title('U.S. States Game')
image = 'C:/Users/karey/Documents/Python/day25/blank_states_img.gif'
screen.addshape(image)
t.shape(image)
states = pandas.read_csv('C:/Users/karey/Documents/Python/day25/50_states.csv')

state_to_list = len(states['state'].to_list())

correct = 0
user_answer = screen.textinput(title='Guess the State', prompt="What's another state")
game_is_on = True
while game_is_on:
    
    user_answer = user_answer.capitalize()
    us_states = states['state'].to_list()
    lenth_of_list = len(us_states)


    if user_answer == 'Exit':
        game_is_on = False


    if user_answer in us_states:
        us_states = states[states['state'] == user_answer]
        x_of_state = us_states['x']
        y_of_state = us_states['y']
        correct+=1
        state_name = t.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(x_of_state), int(y_of_state))
        state_name.write(user_answer.capitalize())

    elif user_answer not in us_states:
        state_name = t.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(0,300)
        state_name.write('you suck! try again!')

    user_answer = screen.textinput(title=f'{correct}/{lenth_of_list} States Correct', prompt="What's another state")
