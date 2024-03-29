import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
gussed_states = []

while len(gussed_states) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states=[]
        for state in all_states:
            if state not in gussed_states:
                missing_states.append(state)
        print(missing_states)
        break

    if answer_state in all_states:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())   

# states to learn csv