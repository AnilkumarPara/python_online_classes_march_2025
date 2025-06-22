# Variable length Keyword arguments (**kwargs)
def introduce_myself(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} is {v} ")


introduce_myself(name='Anil', location='Bengaluru')
# introduce_myself(name='Anil', team_name="Dev team", designation="Lead")