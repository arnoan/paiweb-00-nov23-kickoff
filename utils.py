import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler


def make_streamlit_ui_clean():
    """Make Streamlit UI "clean"."""
    st.set_page_config(
        page_title="Page Title",
        # layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown(
        """
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """,
        unsafe_allow_html=True,
    )


class StreamHandler(BaseCallbackHandler):
    """StreamHandler to facilitate fluid response rendering as LLM tokens arrive."""

    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)
