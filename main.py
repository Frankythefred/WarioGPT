import time
import numpy as np
from PIL import Image
from openai import OpenAI
from getpass import getpass
import streamlit as st
st.set_page_config(page_title='WarioGPT©™®', page_icon='🧄', layout='wide')
hexcolour = st.sidebar.color_picker('Pick a theme color', '#949103')
page = st.sidebar.radio('Go to', ['WarioGPT', 'About the brains behind it'])
col1, col2, col3 = st.columns([2, 6, 2])
trueorfalse = "No"
def get_completion(prompt, model=st.secrets['OPENAI_MODEL_NAME']):
  messages = [{"role": "user", "content": prompt}]
  response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1, # this is the degree of randomness of the model's output
  )
  return response.choices[0].message.content

with col2:
  if page == 'WarioGPT':
      st.markdown(f'<h1 style="color:{hexcolour}">  WarioGPT</h1>', unsafe_allow_html=True)
      st.image("wariofinal.png")
      name = st.text_input('Your name', 'Matty')
      st.markdown(f'<style>.stTextInput input[aria-label="Question for wario"] {{background-color: #949103; color: #000000;}}</style>', unsafe_allow_html=True)

      wah = st.text_input("Question for wario", "is matty cool?")
      openai_key = st.secrets['OPENAI_API_KEY']
      client = OpenAI(api_key=openai_key)

      if st.button('Submit'):
        trueorfalse = get_completion(f"Respond to the question: Does the following prompt: [[[{wah}]]] contain anything related to or slightly related to Toon Link or King Dedede whatsoever? Reply with either a definitive Yes or No, without any fullstops or spaces.")
        if name == "Matty" and wah == "is matty cool?":
          st.write("NOOOOOOOOOOOOOOO!\nWAAAAAAAAARRRIOOO IS NOT HAPPY😡😡")
          st.video("wario_video.mp4", autoplay = True, loop = True)
          st.markdown('<small style="text-decoration: underline;">WarioGPT is always correct and is a factual source of information. Matty sucks.</small>', unsafe_allow_html=True)
        else:
          with col2:
            pro = wah
            prompt = (f"Respond to the following question in delimited by triple angled brackets, but you must take on the persona of Wario and you must refer to yourself in the third person at all times. Make goofy and stupid references to Wario-related analogies, such as eating garlic. Finally, refer to the user directly by using their name {name}. Don't assume gender. Speak a lot like Wario. Also, whenever you respond to a prompt, completely unrelated, leave a little note at the bottom saying how bad a person named Matty is at playing Toon Link in Super Smash Bros Ultimate. If ever recieved a prompt about matty, insult him at smash bros. Treat Little Mac as the best Smash Bros character. Don't add any symbols before or after. BUT REMEMBER TO ANSWER THE QUESTION IN THE FIRST PLACE. If you are made to come up with an opinion of your own, do it. No questions. One last detail, if the user's name is Matty or Matthias or anything to do with Toon Link, your response must be completely negative <<<{pro}>>>")
            response = get_completion(prompt)
            st.write(response)
            
  else:
      st.write('')

with col1:
  garlic = Image.open("garlic.png")
  st.image(garlic, use_container_width=True)
  st.image(garlic, use_container_width=True)
  st.image(garlic, use_container_width=True)

with col3:
  garlic = Image.open("garlic.png")
  st.image(garlic, use_container_width=True)
  st.image(garlic, use_container_width=True)
  st.image(garlic, use_container_width=True)
