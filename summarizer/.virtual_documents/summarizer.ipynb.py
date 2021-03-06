import warnings
warnings.filterwarnings('ignore')
import transformers
summary=transformers.pipeline('summarization')


article ="""
Water vapor. The most abundant greenhouse gas, but importantly, it acts as a feedback to the climate. Water vapor increases as the Earth's atmosphere warms, but so does the possibility of clouds and precipitation, making these some of the most important feedback mechanisms to the greenhouse effect.
Carbon dioxide (CO2). A minor but very important component of the atmosphere, carbon dioxide is released through natural processes such as respiration and volcano eruptions and through human activities such as deforestation, land use changes, and burning fossil fuels. Humans have increased atmospheric CO2 concentration by 47% since the Industrial Revolution began. This is the most important long-lived "forcing" of climate change.
Methane. A hydrocarbon gas produced both through natural sources and human activities, including the decomposition of wastes in landfills, agriculture, and especially rice cultivation, as well as ruminant digestion and manure management associated with domestic livestock. On a molecule-for-molecule basis, methane is a far more active greenhouse gas than carbon dioxide, but also one which is much less abundant in the atmosphere.
Nitrous oxide. A powerful greenhouse gas produced by soil cultivation practices, especially the use of commercial and organic fertilizers, fossil fuel combustion, nitric acid production, and biomass burning.
Chlorofluorocarbons (CFCs). Synthetic compounds entirely of industrial origin used in a number of applications, but now largely regulated in production and release to the atmosphere by international agreement for their ability to contribute to destruction of the ozone layer. They are also greenhouse gases.
"""


x =summary(article,max_length =100,min_length = 30,do_sample=False)


x


x[0]['summary_text']


from gensim.summarization import summarize
print(summarize(article))



