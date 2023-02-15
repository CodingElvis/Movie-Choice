#SE Bootcamp T 38 Semantic Similarity (Intro to NLP) - Task 2 Movie Choice

#we import spacy and load its detailed language model
import spacy
nlp = spacy.load('en_core_web_md')

#we set up a dictionary of movies, initially empty. Movie title will be the key and the description the value
movie_dictionary = {}

#we populate the dictionary with the data in movies.txt
with open('movies.txt', 'r') as file:
    for line in file:
        line = line.strip("\n")
        split_line = line.split(":")
        movie_dictionary[split_line[0]] = split_line[1]


#this function takes a string that should be a description of a movie
#it returns the title of the movie that is deemed "most similar"
def next_movie(description):
    
    #we set up variables to track the currently "most similar" movie and its similarity value
    high_similarity = 0
    closest_movie = ""

    # we apply the nlp model to the input description
    has_watched=nlp(description)
    
    #we loop through each movie in the dictionary
    for movie in movie_dictionary:

        #we apply the nlp model to the movie description and find its similarity to our input
        movie_nlp = nlp(movie_dictionary[movie])
        similarity_number = movie_nlp.similarity(has_watched)
        
        # if the current movie is "more similar" than the current highest, we set the current movie to be the most similar and track the value
        if similarity_number > high_similarity:
            high_similarity = similarity_number
            closest_movie = movie
    
    #when we've looped right through the list we return the title of the "most similar" movie
    return closest_movie



test_phrase = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in 
peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

print(next_movie(test_phrase))







