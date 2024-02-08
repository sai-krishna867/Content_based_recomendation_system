import streamlit as st 
import pickle
import pandas as pd
import requests
def fetch_poster(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0b76181e030c158420d15af6b980efa0'.format(id))
    data= response.json()

    return "https://image.tmdb.org/t/p/original/"+data['poster_path']
    
def rec(opt):
    index= mv_[mv_['original_title']==opt].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    a=[]
    poster =[]
    for i in distances[1:6]:
        movie = mv_.iloc[i[0]].id
        #image fetching API
        a.append(mv_.iloc[i[0]].original_title)
        poster.append(fetch_poster(movie))
    return a,poster
similarity=pickle.load(open('similarity.pkl','rb'))
mv_list=pickle.load(open('movies_dict.pkl','rb'))
mv_= pd.DataFrame(mv_list)
st.title('Movie Recommendation System')
selected_option = st.selectbox(' Select a Movie from below:',mv_['original_title'].values)
if st.button('Recommend '):
    i,j = rec(selected_option)
    columns = st.columns(5)
    for val, col in enumerate(columns):
        col.image(j[val], caption=i[val], use_column_width=True)
    
    
