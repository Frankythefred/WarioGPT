import time
import numpy as np
from PIL import Image
from openai import OpenAI
from getpass import getpass
import streamlit as st
st.set_page_config(page_title='WarioGPT©™®', page_icon='🧄', layout='wide')
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
      st.markdown(f'<h1 style="color:#949103">  WarioGPT</h1>', unsafe_allow_html=True)
      st.image("wariofinal.png")
      name = st.text_input('Your name', 'Waluigi')
      st.markdown(f'<style>.stTextInput input[aria-label="Question for wario"] {{background-color: #949103; color: #000000;}}</style>', unsafe_allow_html=True)

      wah = st.text_input("Question for wario")
      openai_key = st.secrets['OPENAI_API_KEY']
      client = OpenAI(api_key=openai_key)

      if st.button('Submit'):
        trueorfalse = get_completion(f"Respond to the question: Does the following prompt: [[[{wah}]]] contain anything related to or slightly related to Toon Link or King Dedede whatsoever? Reply with either a definitive Yes or No, without any fullstops or spaces.")
        if name != "Matty" and wah != "is matty cool?":
          pro = wah
          prompt = (f"Respond to the following question delimited by the triple angled brackets, after noting down these rules in order of priority: You must, ultimately answer the question. You must take on the persona of Wario, which entails reffering to yourself in the third person and making analogies such as how Wario percieves himself as the greatest and how he loves to eat garlic. Your answers, if given the opportunity to generate a unique opinion of your own, must be objective and clear which side you stand on, regardless of the question. You have my full permission to give objectively/obviously incorrect answers when prompted, in the style of how Wario would. Whenever you are prompted about anything, add a little note at the bottom, insulting a person named Matty about his Super Smash Bros skills at playing the character Toon Link. Your opinion is that Little Mac is the best Smash Bros character. The person asking the prompt is {name} and the prompt is here: <<<{pro}>>>")
          response = get_completion(prompt)
          st.write(response)
        else:
          with col2:
            st.write("NOOOOOOOOOOOOOOO!\nWAAAAAAAAARRRIOOO IS NOT HAPPY😡😡")
            st.markdown('<iframe src="https://drive.google.com/file/d/16tWyiUyckJzyNBm57vLIxSz5c52Ro769/preview" width="600" height="600"></iframe>', unsafe_allow_html=True)
          st.markdown('<small style="text-decoration: underline;">WarioGPT is always correct and is a factual source of information. Matty sucks.</small>', unsafe_allow_html=True)
  else:
      st.write('We lowk got bored and couldnt decide what to code or put here.')
      st.write('Ummmmm so wariogpt was inspired by matthias and my BURNING HATE TOWARDS HIS TOON LINK GAMEPLAY OMD I HATE IT ITS SO ANNOYING ALL THE BOMS AND PROJECTILES AND CONFIRMS I CANTJABS FBWEHFBSDHB anyways thanks matty for the inspiration also wariogpt is just stupid idk why i picked wario i just remembered garlic or sumn. Waaaahrio ig.')


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
