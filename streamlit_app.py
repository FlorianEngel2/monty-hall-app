import streamlit as st
import random

st.title("Monty Hall Spiel")

if "stage" not in st.session_state:
    st.session_state.stage = "start"
    st.session_state.choice = None
    st.session_state.prize = None
    st.session_state.revealed = None

if st.session_state.stage == "start":
    st.write("Wähle eine Tür:")
    if st.button("Tür 1"):
        st.session_state.choice = 1
    if st.button("Tür 2"):
        st.session_state.choice = 2
    if st.button("Tür 3"):
        st.session_state.choice = 3

    if st.session_state.choice:
        st.session_state.prize = random.randint(1, 3)
        possible_doors = [d for d in [1, 2, 3] if d != st.session_state.choice and d != st.session_state.prize]
        st.session_state.revealed = random.choice(possible_doors)
        st.session_state.stage = "reveal"
        st.experimental_rerun()

elif st.session_state.stage == "reveal":
    st.write(f"Du hast Tür {st.session_state.choice} gewählt.")
    st.write(f"Der Moderator öffnet Tür {st.session_state.revealed} – da ist nichts.")

    st.write("Willst du wechseln?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Wechseln"):
            remaining = [d for d in [1, 2, 3] if d != st.session_state.choice and d != st.session_state.revealed][0]
            st.session_state.choice = remaining
            st.session_state.stage = "result"
            st.experimental_rerun()
    with col2:
        if st.button("Bleiben"):
            st.session_state.stage = "result"
            st.experimental_rerun()

elif st.session_state.stage == "result":
    if st.session_state.choice == st.session_state.prize:
        st.success(f"Glückwunsch! Du hast gewonnen. Der Gewinn war hinter Tür {st.session_state.prize}.")
    else:
        st.error(f"Leider verloren. Der Gewinn war hinter Tür {st.session_state.prize}.")
    if st.button("Nochmal spielen"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
