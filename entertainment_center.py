import media
import fresh_tomatoes


interstellar = media.Movie("Interstellar",
                        "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life..",
                        "https://pre00.deviantart.net/a570/th/pre/f/2014/213/3/b/interstellar__2014____poster___2_by_camw1n-d7t74io.png",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E")


prestige = media.Movie("Prestige",
                     "Two friends and fellow magicians become bitter enemies after a sudden tragedy. As they devote themselves to this rivalry, they make sacrifices that bring them fame but with terrible consequences.",
                     "https://i.pinimg.com/originals/86/e4/6e/86e46e4a69181bc4e71358c4bc395680.jpg",
                     "https://www.youtube.com/watch?v=ijXruSzfGEc")


dark_knight = media.Movie("The Dark Knight",
                           """After Gordon, Dent and Batman begin an assault on Gotham's organised crime,
                           the mobs hire the Joker, a psychopathic criminal mastermind, who wants to bring all the heroes down to his level.""",
                           "https://www.filmonpaper.com/site/media/2011/05/TheDarkKnight_onesheet_advance_WhySoSeriousStyle_USA-1-500x738.jpg",
                           "https://www.youtube.com/watch?v=EXeTwQWrcwY")


garden_of_words = media.Movie("The Garden of Words",
                              """"When a lonely teenager skips his morning lessons to sit in a lovely garden,
                              he meets a mysterious older woman who shares his feelings of alienation.""",
                              "https://occ-0-299-300.1.nflxso.net/art/6d1ca/7ef2124cbe2b5a411bfd282b3563794c5ec6d1ca.jpg",
                              "https://www.youtube.com/watch?v=HTTRweJ7jVs")

a_silent_voice = media.Movie("A Silent Voice",
                             """When a grade school student with impaired hearing is bullied mercilessly, she transfers to another school.
                             Years later, one of her former tormentors sets out to make amends.""",
                             "https://cdn.traileraddict.com/content/madman/a-silent-voice-poster.jpg",
                             "https://www.youtube.com/watch?v=nfK6UgLra7g")


avengers_infinity_war = media.Movie("Avengers Infinity War",
                                    """Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos.
                                    On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality.
                                    The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.""",
                                    "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/1/11/Avengers_Infinity_war_poster.jpeg/revision/latest?cb=20180316141550",
                                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# list of all movies
movies = [interstellar,prestige,dark_knight,garden_of_words,a_silent_voice,avengers_infinity_war]



# this will generate an html page of movies
fresh_tomatoes.open_movies_page(movies)
