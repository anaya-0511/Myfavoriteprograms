#Musical app
#This tells you any information about musicals like genres, composers, awards, etc.
import pandas as pd
data = pd.read_csv('broadway_musicals_90_dataset - Sheet1.csv')# uses panda library to load the data into a variable
musical_name = data["Musical Name"].tolist()#Puts the musical names from the data set in a list called "musical name"
musical_genres = data["Genre"].tolist()#Puts the genres from the data set in a list called "musical genres"
ratings = data["Rating"].tolist()#Puts the ratings from the data set in a list called "ratings"
composers = data["Composer"].tolist()#Puts the composers from the data set in a list called "composers"
recommendations = []#an array for the filtered out musicals
awards = data["Number of Tony Awards"].tolist()#Puts the number of awards from the data set in a list called "awards"
movie_musical = data["Movie Musical/show"].tolist()#Puts the info on if a musical is a movie or a tvshoe from the data set in a list called "movie_musical"

def findingshow_genre(genre):#Helps user find musicals based of off prefered genre
    for i in range (len(musical_genres)):#Filters through array
        if genre in musical_genres[i]:#If the genre the user puts in is the same as the description of the musical add it to the recommendations array
            recommendations.append(musical_name[i])
    print(f"Since you like {genre} you should watch {recommendations}.")#prints filtered list
    recommendations.clear()#clears the list


def composer_finder(composer):#Helps user find musicals based of off prefered composer
    for i in range(len(composers)):#Filters through array
        if composer == composers[i]:# If the users input is in the same as the musical's composer add it to the reccomendations array
            recommendations.append(musical_name[i])
    print(f"Since you like {composer},these are the musicals that {composer} composed music for:{recommendations}.")#prints filtered list
    recommendations.clear()#clears the list


def finding_goodratings(rating):#Helps user find musicals based of off prefered rating and higher
    for i in range(len(ratings)):#Filters through array
        if ratings[i] >= rating:# If the musical ratings are the same or higher than the users input, add the musical to the reccomendations array
            recommendations.append(musical_name[i])#appends musical name
            recommendations.append(ratings[i])#appends rating of musical
    print(f"Here are the musicals recommended with their ratings:{recommendations}.")#Prints out array


def movie_musicalfinder(musical):#Helps user find out if a musical is a movie or tvshow
    for i in range (len(musical_name)):#Filters through array
        if musical == musical_name[i]:# Sees if the input is in the list
            if movie_musical[i] == "Yes":#Sees if the musical is equal to yes in the data sheet
                print(f"{movie_musical[i]}, {musical} is a movie or TV show.")#prints yes statement
            if movie_musical[i] == "No":#Sees if the musical is equal to no in the data sheet
                print(f"{movie_musical[i]}, {musical} is not a movie or TV show.")#prints no statment
def awards_number(musical):#Helps user find out how many tony awards a musical won
    for i in range(len(musical_name)):#Filters through array
        if musical == musical_name[i]:#Sees if the input is in the list
            recommendations.append(awards[i])#Appends the number of tony awards the musical won to an array
            print(f"{musical_name[i]} won {recommendations} awards.")#prints statement
def asciiart():#Just ascii art for the menu
    print("""
                                           =@%@#
                                        ==   :=#@.
                                      %       .=*@
                                  :*.          .+%*.#@##.
                               **               :*@#+-.. .@
                            :++=                   :=*@:..     +=
       #@+--=+**++=-.                 -#=. -*#:  -*@:.         #-
      @*-                          =:     :.   .#:-@-             =*.
      @*-.                       ..  :@*::-.::-# -+##                 =@=
      @#=.        .----=-       .: :%=          -*:+@                       .:-=-===+*##+
      :%*:     :#          =    . :=:   .#-.:*:  :+-%-         ==-+                    .:#@
       @#+.  .#  :*#*+=*##-       @-  = .#@@@@#.= .:**      =-  .*..   --+              -*@
        %+:..+ .%..      :-#.    .#. * @@@@@@@@@@. :+@         %.:     *: -            .=#@
        =%+:- +-     .-:   :*+   .#.  @@+    :-:.   +%@*++**=..        .*  -           :+%+
         #*-+.=.  =   .-. # .=+   *- -+ =*:.        .+@%##=. #@.        ::  +          +#@
          @*==:  -.@@@@@@@@- :+:  +-. .              :*@@@@@@@.        %.--  +       .:#@
          :@+.. +%@@@:        =#  .-:                .+@@@@@ =. -      @#= =-  -+.  .-*%=
           +#-. :@+  -++..     ==  *:                :-%+---=  .-  *  +@@% =.:*+   +=+%*
            @+: : =:           -*   *-               :*%@-     #  :-  *:@@@= -:  -: *#%
            =*=  :             .*   ::=+*%-       .:.-*%*    .-:  +:  ==:@@@@@=.  * #@
             @*               -===   %.   *-+*#***%=.:*#=    :-   +.   +:: .==  : -#%-
             +*:            :*   *    +:*-+.  .@@+=* .*%=@:.-*   :-     :=:       +*@
              @#           .*#:::-*..#=%::   *#@# @= :*@*-  -:   #*#.            .=#-
              -#*       .=%-. ++*=**+#=    =-%@@: #= :#%-=@@=+  +.  =+           -+@
               ##**  .#%@@=             .*.:@@@@= == =%.
                .++.*@@@:@*                        :+@:
                *%*- :*==:@@@=-+*+=+**-  =@@@@@#+  .:+%-=+=-         :#         :@#
                 .@#- :-%  *@@@@@@#**@@@@@@@@@@     =@-=#%#+   .*.    %       .=@@
                   ##=  +*  :@@@@@@@@@@@@@@@@@ +   .*@@@@@@@@@@@= =   +. .  .=%%@
                     @*- :.  .-@@@@@@@@@@@@@% ::   +@@@@@@@@@@@@@@=- .=. .+=*+%*
                      :@*- -   =.=@@@@@@@@+  ==   :#*---=-:. :@@@@@=# -.  .=*@.
                        -@*:     *:        =%    :*@+=+=***#::= %@@@- =  :-%*
                          =%#-     .*%%%%+-. :-+ -@-        :=#:==@@: + -#%
                            -@+-    +:         :*#+            --:+@+ :*@
                              :@#-:=:          +##-             .. -.*%
                                 +@*=:       :#@ @#+:           :==@+
                                    *@%**##%@*     %%*+==:....-*@%
                                                       -%@@@@@-




          """)


print("Welcome to Musical Recommender!!")
asciiart()
while True:
    action = input("""What would you like to do today? A. Find shows based on genre, B. Find the number of awards a show won,
                   C. Find shows based off the composer, D.Find shows based on ratings,
                    E.See if a show was made into a movie or a TV show, or F. Leave the game:(input example:A) """)#Lists out the options for what they can do
    if action == "A":
        genre = input("What type of genres interest you: ")#input for the parameter
        findingshow_genre(genre)#runs the function
        leave = input("Would you like to leave now?  ")#asks if they would like to break
        if leave == "yes":
            break#ends code
        else:
            continue#continues
    if action == "B":
        musical = input("Musical name: ")#input for the parameter
        awards_number(musical)#runs the function
        leave = input("Would you like to leave now?  ")#asks if they would like to break
        if leave == "yes":
            break#ends code
        else:
            continue#continues
    if action == "C":
        composer = input("What composer interests you? ")#input for the parameter
        composer_finder(composer)#runs the function
        leave = input("Would you like to leave now?  ")#asks if they would like to break
        if leave == "yes":
            break#ends code
        else:
            continue#continues
    if action == "D":
        rating = input("Minimum rating(Whole numbers only): ")#input for the parameter
        finding_goodratings(int(rating))#runs the function
        leave = input("Would you like to leave now?  ")#asks if they would like to break
        if leave == "yes":
            break#ends code
        else:
            continue#continues
    else:
     if action == "E":
        musical = input("Musical Name: ")#input for the parameter
        movie_musicalfinder(musical)#runs the function
        leave = input("Would you like to leave now?  ")#asks if they would like to break
        if leave == "yes":
            break#ends code
        else:
            continue#continues
     else:
        print("Goodbye!")
        break#ends code
