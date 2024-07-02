import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S state games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_states_name = states_data.state.to_list()
guessed_state = []


def process_result(guessed_state):
    missed_state = [s for s in all_states_name if s not in guessed_state]
    df = pandas.DataFrame(missed_state)
    df.to_csv("learn.csv")


while len(guessed_state) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state", prompt="What's the another state name?").title()
    if answer_state == "Exit":
        process_result(guessed_state)
        break
    if answer_state in all_states_name:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
        coor = states_data[states_data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(coor.x), int(coor.y))
        t.write(answer_state.capitalize(), move=False, font=("Courier", 8, "bold"))



screen.exitonclick()
