import streamlit as st
from text_sentiment import sentiment
from summarizer import gensim_summary
from translation import tranalate
import pandas as pd
from PIL import Image
df = pd.read_excel("lang_id.xlsx")
lang_list=df.lang.values
def main():
    st.sidebar.title("NLP App")
    st.sidebar.header("About app..")
    st.sidebar.text("This is a NLP App")
    st.sidebar.text("For finding")
    st.sidebar.text("1. Sentiment")
    st.sidebar.text("2. Summary")
    st.sidebar.text("3. Translation")
    option=st.sidebar.radio("Features", ["Sentiment Analysis", "Summarizer", "Translation", "Language Identification"])
    ############################################33
    if option=="Sentiment Analysis":
        st.title("Natural Language Processing App")
        st.subheader("Sentiment Analysis")
        msg = st.text_area("Enter the text for sentiment analysis", "Type here ...")
        if st.button("Analysis"):
            sentiment_score = sentiment.cleaning(msg)
            if (sentiment_score == "pos"):
                st.success("Positive 😄")
            elif (sentiment_score == "neg"):
                st.error("Negative 😠")
            elif (sentiment_score == "neu"):
                st.info("Neutral 😎")
                ###############################################3
    if option == "Summarizer":
        st.title("Natural Language Processing App")
        st.subheader("Summarizer Your Long Text ")
        summ = st.text_area("Enter the text to be summarizer", "Type here...")
        summ_opt = st.selectbox("choice your summarizer", ["gensim", "transformer"])
        summ_btn = st.button("summarizer")
        if summ_btn and summ:
            if summ_opt:
                summary = ""
                if (summ_opt == "gensim"):
                    st.text("using gensim to summary your text ....")
                    summary = gensim_summary.summarize(summ)
                    st.write("summariztion successful 🤩")
                    st.write("displaying Your text In a second")
                    st.success(summary)

                if (summ_opt == "transformer"):
                    st.error("Sry we are working on it speed 🙁")
            else:
                st.warning("pls select any option")
        elif (summ_btn):
            st.warning("pls enter the text to be summarized")

            ###########################################
    if option == "Translation":
        st.title("Natural Language Processing App")
        st.subheader("Translation Section")
        trans = st.text_area("Enter thr text to be translated")
        to_lang = st.selectbox("choice language to which you want to translate", lang_list)
        trans_but = st.button("Translate")
        if (trans_but):
            st.write("Translation is in progress...")
            res = tranalate.translation(trans, to_lang)
            st.write("Translation Successful")
            st.success(res)

    if option == "Language Identification":
        st.title("Natural Language Processing App")
        st.subheader("Identify Language")
        text = st.text_area("Enter thr text to be identified")
        iden_lang = st.button("Identity Language")
        if (iden_lang):
            st.write("Identifying Language ...")
            lang = tranalate.id_(text)
            st.success(lang)


    st.sidebar.header("About Me")
    Linkedin_img = Image.open("linkedin.png")
    st.sidebar.image(Linkedin_img)
    st.sidebar.info("[Linkedin](https://www.linkedin.com/in/malayaj-rath-6858411b1/)")
    Github_img = Image.open("github.png")
    st.sidebar.image(Github_img)
    st.sidebar.info("[Github](https://github.com/malayaj2000)")









if __name__ == '__main__':
    main()