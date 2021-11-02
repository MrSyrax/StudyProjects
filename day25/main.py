import turtle as t
import pandas

screen = t.Screen()
screen.title('U.S. States Game')
image = 'C:/Users/karey/Documents/Python/day25/blank_states_img.gif'
screen.addshape(image)
t.shape(image)
states = pandas.read_csv('C:/Users/karey/Documents/Python/day25/50_states.csv')


us_states = states['state'].to_list()

correct = 0
user_answer = screen.textinput(title='Guess the State', prompt="guess a state")
game_is_on = True
while game_is_on:
    
    user_answer = user_answer.capitalize()
    lenth_of_list = len(us_states)
    

    if user_answer == 'Exit':
        game_is_on = False
        


    if user_answer in us_states:
        us_states.remove(user_answer)
        x_and_y = states[states['state'] == user_answer]
        x_of_state = x_and_y['x']
        y_of_state = x_and_y['y']
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

m_states = {
    'missed': us_states
}

missed_states = pandas.DataFrame(m_states)
missed_states.to_csv('C:/Users/karey/Documents/Python/day25/missed.csv')

print(f'great job, but you missed {us_states}')