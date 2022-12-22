from django.http import HttpResponse
import json
import pandas as pd
from sqlalchemy import create_engine


def index(request):
    engine = create_engine('postgresql://postgres:2OmzVQgpgalMdQOi506w@containers-us-west-18.railway.app:7041/railway')
    df = pd.read_sql_query("select * from books", con= engine)
    return HttpResponse(json.dumps(df.values.tolist()))
 

