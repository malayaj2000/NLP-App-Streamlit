import warnings
warnings.filterwarnings('ignore')
import transformers
summarizer=transformers.pipeline('summarization')
def summary_transformer(text,max_length,min_length):
    summary_text= summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return str(summary_text[0]['summary_text'])

