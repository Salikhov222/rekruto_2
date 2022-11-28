from fastapi import FastAPI
import random
import string

app = FastAPI ()

@app.get("/")
def read_root():
    code = "".join(random.choices(string.ascii_uppercase + string.digits, k = 4))
    return code