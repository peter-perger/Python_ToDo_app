import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    new_todo = st.session_state["new_todo_input"]
    todos.append(new_todo)

    write_todos(todos)

    st.session_state["new_todo_input"] = ""


st.set_page_config(layout="wide")

st.title("My ToDo app")
st.subheader("Get your shit together! 💩")

st.text_input(label="",
              placeholder="Add a new ToDo...", key="new_todo_input", on_change=add_todo)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)

    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.write("Powered by <strong>Perger Peter</strong>", unsafe_allow_html=True)
