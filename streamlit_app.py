import streamlit as st

st.title("My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}!")

n = st.number_input("how many numbers?",
                    min_value=1,
                    max_value=20,
                    value=3,
                    step=1)
numbers = []

st.write("Enter your numbers:")

for i in range(int(n)):
    number = st.number_input(f"Entry {i+1}",
                             value=0.0,
                             key=f"number_{i}")
    numbers.append(number)

total = sum(numbers)

st.subheader("Result")
st.write("Your array:",numbers)
st.success(f"Sum={total}")
