import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests



# def fetch_poster(movie_title):
#     url = "https://imdb8.p.rapidapi.com/title/v2/get-chart-genre-teaser-posters"

#     querystring = {"titleType":"ALL","first":"20","genre1":"Comedy","genre2":"Horror","genre3":"Sci-Fi"}

#     headers = {
# 	    "X-RapidAPI-Key": "3541620677msh73ae794950d6e02p1e0036jsnbcfea45f3e44",
# 	    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     data=response.json()
#     return data['primaryImage']

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2M2NDE3ZWMxYWI1NzdkOGI4MzAxMWY0MzQ3ZjEyNiIsInN1YiI6IjY2MzVjY2E4NjY1NjVhMDEyODE1MTY4NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z4lPXhYjufiaVYmy0dCP_oi9-HaxSWSs6rUYXQH0GWg"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    # movie_index=np.where(movies_list==movie)[0][0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch  poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


# def recommend(movie):
#     movie_index = np.where(movies_list == movie)[0][0]
#     distances = similarity[movie_index]
#     movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     for i in movies_list1:
#         movie_id=i
#         recommended_movies.append(movies_list[i[0]])
#     return recommended_movies

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'Search the movie here',
 movies['title'].values  )

if st.button('Recommend'):
    st.text('Other Recommendations are:')
    names,posters=recommend(selected_movie_name)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        if len(names[0]) > 20:
            st.markdown(f"<b>{names[0][:20]}</b>" + '\n' + f"<b>{names[0][20:]}</b>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>{names[0]}</b>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        if len(names[1]) > 20:
            st.markdown(f"<b>{names[1][:20]}</b>" + '\n' + f"<b>{names[1][20:]}</b>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>{names[1]}</b>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        if len(names[2]) > 20:
            st.markdown(f"<b>{names[2][:20]}</b>" + '\n' + f"<b>{names[2][20:]}</b>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>{names[2]}</b>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        if len(names[3]) > 20:
            st.markdown(f"<b>{names[3][:20]}</b>" + '\n' + f"<b>{names[3][20:]}</b>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>{names[3]}</b>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        if len(names[4]) > 20:
            st.markdown(f"<b>{names[4][:20]}</b>" + '\n' + f"<b>{names[4][20:]}</b>", unsafe_allow_html=True)
        else:
            st.markdown(f"<b>{names[4]}</b>", unsafe_allow_html=True)
        st.image(posters[4])
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
   





