
Learn How to Web Scrapping using python using Beautiful Soup  

Beautiful Soup is a Python library for pulling data out of HTML and XML files.  
https://www.crummy.com/software/BeautifulSoup/bs4/doc/


please look at following url when scrapping   
* https://news.ycombinator.com/robots.txt  
* https://www.linkedin.com/robots.txt  
* https://github.com/robots.txt  

---

# Authentication with Spotify

1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account,
    you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:  
    https://developer.spotify.com/dashboard/  
     ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_01.png?raw=true)

3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.  
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_02.png?raw=true)
    Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access a Spotify user's account  
    without giving them the username or password. We'll explore OAuth more in later modules on web development,  
    but if you want you can read more about it here: 
    https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth

    Authenticating with Spotify is quite complicated, especially when you want to access a user's account. 
    So instead, we're going to use one of the most popular Python Spotify modules - Spotipy to make things easier.      
       
4. Using the Spotipy documentation, figure out how to authenticate your Python project with Spotify using 
   your unique Client ID/ Client Secret.

5. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). 
   As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.  
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_03.png?raw=true)
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_04.png?raw=true)
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_05.png?raw=true)

    HINT 1: You need your own Spotify app Client ID and Secret, the ones in the image above won't work.      
    HINT 2: This is the method you'll need: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth      
    HINT 3: Try passing the Client ID and Secret directly into the SpotifyOAuth() constructor instead of using export or set.      
    HINT 4: You need the "playlist-modify-private" scope in order to create a private playlist on Spotify.      
    HINT 5:  If successful, you should see the page below show up automatically (be sure to click Agree):
         
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_06.png?raw=true)  
    Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar:
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_07.png?raw=true)
    Finally, you need to paste the URL into the prompt in PyCharm:
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_08.png?raw=true)  
    Now if you close PyCharm and restart, you should see a new file in this project called token.txt
    ![alt text](https://github.com/distareza/learnpython-day45-web_scrapping/raw/master/resources/authenticate_with_spotify_09.png?raw=true)

7. Get the user id of the authenticated user (your Spotify username).  
    HINT 1: You'll need this method: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user
    
    HINT 2: The output of the above method is a dictionary, look for the value of the "id" key.

