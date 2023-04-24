# import ora
import ora
import streamlit as st
from streamlit_chat import message

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

# create model
model = ora.CompletionModel.create(
    system_prompt="""You are ChatGPT, a large language model trained by 
                    OpenAI. Answer as descriptively as possible""",
    description="ChatGPT Openai Language Model",
    name="gpt-3.5",
)


@st.cache_data
def generate_response(prompt, model):
    response = ora.Completion.create(
        model=model,
        prompt=prompt,
        includeHistory=True,  # remember history
        conversationId=init.id,
    )

    return response.completion.choices[0].text


st.title("chatBot: streamlit + ora")


def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = generate_response(user_input, model)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i],
                is_user=True,
                key=str(i) + "_user")
