from fastapi import FastAPI
import spacy 
from pydantic import BaseModel

app = FastAPI()


class QueryInput(BaseModel):
    query: str

txt = "The tallest living man is 37-year-old Sultan Kosen, from Turkey, who is 8 feet, 2.8 inches, who set the record in 2009."

# Create the Language object
nlp = spacy.load("en_core_web_sm")

doc = nlp(txt)
for ent in doc.ents:
    print(ent.text+':',ent.label_)
print(nlp.pipe_names)

@app.post('/model')
def get_entities(text: str):
    doc = nlp(text)
    entities = [f'{ent.text}->{ent.label_}' for ent in doc.ents]
    return {'entities':entities}