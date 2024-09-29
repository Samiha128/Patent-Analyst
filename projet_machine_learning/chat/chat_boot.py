from dataclasses import dataclass
from typing import Literal
import streamlit as st
from langchain import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
import streamlit.components.v1 as components
import base64
from PIL import Image
import streamlit as st
import io
from openai import OpenAI









@dataclass
class Message:

    origin: Literal["human", "ai"]
    message: str


def load_css():
    with open("C:\\Users\\hp\\Desktop\\projet_machine_learning\\chat\\style1.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "token_count" not in st.session_state:
        st.session_state.token_count = 0
    if "conversation" not in st.session_state:
        llm = OpenAI(
            temperature=0,
            openai_api_key=st.secrets["openai_api_key"],
            model_name="text-davinci-003"
        )
        st.session_state.conversation = ConversationChain(
            llm=llm,
            memory=ConversationSummaryMemory(llm=llm),
        )


def on_click_callback():
    with get_openai_callback() as cb:
        human_prompt = st.session_state.human_prompt
        llm_response = st.session_state.conversation.run(
            human_prompt
        )
        st.session_state.history.append(
            Message("human", human_prompt)
        )
        st.session_state.history.append(
            Message("ai", llm_response)
        )
        st.session_state.token_count += cb.total_tokens


load_css()
initialize_session_state()


styled_title = "<span style='color: #214321; font-family: Matura MT Script Capitals; font-size: 50px;'>AmiCœur : Partagez Vos Sentiments</span>"
st.markdown(f"<h1 style='text-align: center;'>{styled_title}</h1>", unsafe_allow_html=True)



chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")
credit_card_placeholder = st.empty()


with chat_placeholder:
    for chat in st.session_state.history:
        div = f"""
    <div class="chat-row {'row-reverse' if chat.origin != 'ai' else ''}">
        <div class="chat-bubble {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
            &#8203;{chat.message}
        </div>
    </div>
    """



        st.markdown(div, unsafe_allow_html=True)

    for _ in range(3):
        st.markdown("")

with prompt_placeholder:
    st.markdown("**exprimer vos sentiment**")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        #value="Hello bot",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Submit",
        type="primary",
        on_click=on_click_callback,
    )

credit_card_placeholder.caption(f"""
Used {st.session_state.token_count} tokens \n
Debug Langchain conversation: 
{st.session_state.conversation.memory.buffer}
""")

components.html("""
<script>
const streamlitDoc = window.parent.document;

const buttons = Array.from(
    streamlitDoc.querySelectorAll('.stButton > button')
);
const submitButton = buttons.find(
    el => el.innerText === 'Submit'
);

streamlitDoc.addEventListener('keydown', function(e) {
    switch (e.key) {
        case 'Enter':
            submitButton.click();
            break;
    }
});
</script>
""",
                height=0,
                width=0,
                )
background_image = f'''
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://images2.alphacoders.com/110/1107094.jpg");
            background-size: 180%;
            background-position: top left;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        '''
st.markdown(background_image, unsafe_allow_html=True)