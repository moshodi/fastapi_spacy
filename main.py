from fastapi import FastAPI
import spacy 
from spacy import displacy


app = FastAPI()




txt = "The tallest living man is 37-year-old Sultan Kosen, from Turkey, who is 8 feet, 2.8 inches, who set the record in 2009."

# Create the Language object
nlp = spacy.load("en_core_web_sm")

doc = nlp(txt)
for ent in doc.ents:
    print(ent.text+':',ent.label_)
print(nlp.pipe_names)

# @app.get('/model/{text}')
# def get_entities(text: )