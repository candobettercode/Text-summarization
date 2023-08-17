import streamlit as st
from text_summarize import summarizer

st.set_page_config(page_title="Text Summarization!!!", page_icon=":pencil:", layout="centered")
# giving a title
st.title(":fire: Text Summarization")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

st.text("Tecknowcode @Tecknowcode")
st.text("Siddhesh M.(candobettercode)")

def main():
            
    message = st.text_area("Enter your text","Type here",height=400)

    submit = st.button("Summarize")

    if submit:
        sumary, inputdata, summary_len, data_len = summarizer(message)  
        st.text("Text is being Summarized ... ")
        st.markdown("## Summarized output")
        st.warning('Number of characters in Input data: {}'.format(data_len))
        st.error('Number of characters in Summarized data: {}'.format(summary_len))
        st.success(sumary)
      
if __name__ == '__main__':
    main()

  