import json
import time
from streamlit_lottie import st_lottie
import requests
import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st
import json
import time
from streamlit_lottie import st_lottie
import requests
import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st
from fonction import *
import base64
import streamlit as st
import plotly.express as px
from PIL import Image
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import base64
import streamlit as st
import plotly.express as px
from PIL import Image
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
from googletrans import Translator
from languages import *

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



audio_url = "https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg"


st.markdown(
    f'<div style="position: absolute; bottom: -1500px; left: 600px;"><audio src="{audio_url}" controls autoplay></audio></div>',
    unsafe_allow_html=True
)

css_path1 = "C:/Users/hp/Desktop/project/nlp/style.css"
local_css(css_path1)



animation_symbol = "🍁"
#animation_symbol1="🍂"
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,

 )


def main():
    st.markdown(
     "<p><span style='font-family: Matura MT Script Capitals; font-size: 70px;'>" +
     "<span style='color: #214321;'>S</span>" +
     "<span style='color: #214321;'>e</span>" +
     "<span style='color: #214321;'>n</span>" +
     "<span style='color: #214321;'>t</span>" +
     "<span style='color: #214321;'>i</span>" +
     "<span style='color: #214321;'>m</span>" +
     "<span style='color: #214321;'>e</span>" +
     "<span style='color: #214321;'>n</span>" +
     "<span style='color: #214321;'>t</span>" +
     "<span style='color: #214321;'> </span>" +
     "<span style='color: #214321;'>A</span>" +
     "<span style='color: #214321;'>n</span>" +
     "<span style='color: #214321;'>a</span>" +
     "<span style='color: #214321;'>l</span>" +
     "<span style='color: #214321;'>y</span>" +
     "<span style='color: #214321;'>s</span>" +
     "<span style='color: #214321;'>i</span>" +
     "<span style='color: #214321;'>s</span>" +
     "</span></p>",


     unsafe_allow_html=True
      )

    st.subheader(":smiley::angry:")
    menu = ["About", "Home", "traduction", "amicoeur"]
    choice = st.sidebar.selectbox("Menu", menu)
    

    if choice=="traduction":

        background_image = f'''
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("http://www.photo-paysage.com/albums/userpics/10001/De-beaux-nuages-d-altitude-dans-un-ciel-d-aurore.jpg");
            background-size: 180%;
            background-position: top left;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(background_image, unsafe_allow_html=True)
        st.title("🌐 Language Translation App - 语言翻译应用")
        source_text = st.text_area("Enter text to translate:")
        target_language = st.selectbox("Select target language:", languages)
        translate = st.button('Translate')
        if translate:
            translator = Translator()
            out = translator.translate(source_text, dest=target_language)
            st.text(out.text)







   
    if choice =="amicoeur":
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
    
   
    if choice == "Home":
        # Utilisez st.markdown pour appliquer le style de police personnalisé
        st.markdown('<p style="font-family: Rockwell Extra Bold; font-size: 24px;">Home</p>', unsafe_allow_html=True)
        with st.form(key='nlpForm'):
            search_emoji = "🔍"
            raw_text = st.text_area(f"{search_emoji} how do you feel")
            submit_button = st.form_submit_button(label='Analyser')
        page_bg_img2 = """
    <style>
   [data-testid="stAppViewContainer"] {
background-image: url("https://www.hdwallpapers.in/download/green_trees_with_green_covered_mountain_scenery_morning_sun_rays_4k_hd_nature-HD.jpg");
background-size: cover;

}
[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
[data-testid="stSidebar"]  {
    background-image: url("https://www.naturephotographie.com/wp-content/uploads/2018/11/www.naturephotographie.com-garden-of-nature.jpg");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
}



    </style>


"""
    
        st.markdown(page_bg_img2, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if submit_button:
            with col1:
                st.info("Results")
                translator = Translator()
                target_lang='en'
                translated_sentence = translator.translate(raw_text, dest=target_lang).text
                sentiment = TextBlob(translated_sentence).sentiment
                st.write(sentiment)
                # Emoji
                if sentiment.polarity > 0:
                    st.markdown("Sentiment: Positive :smiley:")

                    # Animation des ballons
                    st.balloons()
                    time.sleep(40)

                elif sentiment.polarity < 0:
                    st.markdown("Sentiment: Negative :angry:")

                else:
                    st.markdown("Sentiment: Neutral 😐")

                # Dataframe
                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)

                # Visualization
                c = alt.Chart(result_df).mark_bar().encode(
                    x='metric',
                    y='value',
                    color='metric')
                st.altair_chart(c, use_container_width=True)

            with col2:
                st.info("Token Sentiment")
                token_sentiments =analyze_token_sentiment(raw_text, target_lang='en')
                st.write(token_sentiments)

    else :
        page_bg_img3= """
    <style>
        [data-testid="stSidebar"]  {
    background-image: url("https://www.naturephotographie.com/wp-content/uploads/2018/11/www.naturephotographie.com-garden-of-nature.jpg");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
}



    </style>


"""

        st.markdown(page_bg_img3, unsafe_allow_html=True)
    if choice == "About":

        lottie_hello = load_url("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            # renderer="svg",  # canvas
            height=None,
            width=None,
            key=None,
        )

        st.subheader(
            "Notre projet de traitement automatique du langage naturel (NLP) vise à développer un modèle capable de déterminer le sentiment (positif, négatif ou neutre) d'une phrase en temps réel. Ce système sera utile pour évaluer rapidement le ton et le contexte des messages textuels dans diverses applications, allant de la surveillance des réseaux sociaux à l'analyse des commentaires des clients.")
        
            

           
          
if __name__ == '__main__':
    main()