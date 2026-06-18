import requests

def movie(title_movie):

    answer = requests.get(f"http://www.omdbapi.com/?apikey=a726830&t={title_movie}")
    print("Looking movie...")
    try: 

        dates = answer.json()

        name_movie = dates["Title"]
        year_movie = dates["Year"]
        rating_movie = dates["imdbRating"]
        sipnosis_movie = dates["Plot"]

        return f"Name: {name_movie} \nRelease year: {year_movie} \nRating: {rating_movie} \nSipnosis: {sipnosis_movie}"
    except KeyError:
        return "ERROR: That movie doesn't exist"
    except requests.exceptions.ConnectionError:
        return "ERROR: Something went wrong with the connection, please try again later"
    except requests.exceptions.Timeout:
        return "ERROR: The wait time is too long. Please try again later."

movie_name = input("Enter movie: ")
print(movie(movie_name))