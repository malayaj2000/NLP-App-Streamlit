from textblob import TextBlob
import pandas as pd
df = pd.read_excel("lang_id.xlsx")
def translation(text,to_lang):
    blob = TextBlob(text)
    present_lang = blob.detect_language()
    lang = to_lang
    id_ = df[df.lang == lang].id.values[0]
    trans=blob.translate(to=str(id_))
    return trans
def id_(text):
    blob = TextBlob(text)
    present_lang_id = blob.detect_language()
    return df[df.id == present_lang_id].lang.values[0]
