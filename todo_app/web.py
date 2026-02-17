import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    new_todo = st.session_state["new_todo_input"]
    todos.append(new_todo)

    write_todos(todos)

    st.session_state["new_todo_input"] = ""


def complete_task(todo_key):
    todo = st.session_state[todo_key]
    todo = todo.strip()

    todos = get_todos()
    todos.remove(todo)


st.title("My ToDo app")
st.subheader("Get your shit together! 💩")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")

    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()


st.text_input(label="",
              placeholder="Add a new ToDo...", key="new_todo_input", on_change=add_todo)
