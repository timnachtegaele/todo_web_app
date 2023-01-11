import streamlit as st
from Modules import functions
todos = functions.get_write_todos('r')


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+'\n')
    functions.get_write_todos('w', todos)


st.title("My todo app")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=i)
    if checkbox:
        todos.pop(i)
        functions.get_write_todos('w', todos)
        del st.session_state[i]
        st.experimental_rerun()

st.text_input(label=" ",placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

#st.session_state
