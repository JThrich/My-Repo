
# coding: utf-8

# Function accepts state name as string and output is the two main cities of the state..

def State(State):
    import numpy as np
    import pandas as pd
    state_data = pd.read_csv("India States & Cities.csv")
    state_data['State/UT']=   state_data['State/UT'].apply(lambda state : state.lower())
    cities = list(state_data[state_data['State/UT'].isin([State])]['Major Cities'])
    main_city = cities[:2]
    if len(main_city) ==0: 
        return 'Invalid State Entered ! Please enter valid State'
    else:
        return ', '.join(main_city)

if __name__ == "__main__":
    s= input()
    print(State(s.lower().strip()))

