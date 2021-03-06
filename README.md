# SongGen
A Markov Chain based dynamic song generator for over 600 artists across various genres.

## Inspiration
I was inspired to build something involving linguistics and analysis of text data, as the is a field I am extremely interested in.  I am a Computer Science major, possibly minoring in Linguistics so analysis of language is an interesting topic to me.  I started off trying to build a song recommendation system, but after running into several walls the project was scaled back to what it is today.
## What it does
My application takes in a user inputted name of an artist, and provided that the artist is in the database, a robotic voice starts singing an auto generated song generated off similar songs by that artist.
## How I built it
The end product is build using Python and several packages.  I used Pandas to deal with the Big Data from the songs.  I took the data and obtain a list of all the lyrics of all the songs by a given artist.  I then split the list into a list of words within the songs.  From there I implemented a Markov Chain to power the dynamic text production.  Then when the Markov Chain runs, it generates a new list of words that is the new song.  I then used a text to speech package to read aloud the song that was generated.  Lastly I use Flask to try to make it seem like this project can exist outside an IDE.
## Challenges I ran into
As is common in hackathons, my goal was set too high to begin with.  I intended to use machine learning to create a music recommendation system, but as I have never worked with ML before that did not go too well.  I quickly decided it would be more possible (and more fun) to do something that is within my possibility while still creating a finished product.  Also I spend 2 hours trying to fix a bug with the Indico Emotion API before I accidentally used all 25000 credits and gave up  ¯\_(ツ)_/¯ .  
## Accomplishments that I'm proud of
I had never really worked with Big Data or pandas before so that was all new to me, but I picked it up pretty quickly.   I also was not sure whether I was actually going to end this event with a finished(ish) product, as I tend to get discouraged easily, But I am happy I kept going.  Lastly its incredible to listen to the defualt Microsoft David voice rapping a made up Kanye West song.
## What I learned
Machine learning is not something you can pick up in a few hours (or I can't anyway).  Also I learned its better to do something fun then it is to try to grind out a project you think might be successful, but don't enjoy creating.  I also learned useful skills about how to deal with Big Data in python using panda, and I learned a lot about finding and installing various Python packages such as the text to speech package I used.  I also learned that coffee is really not that bad (and definitely necessary sometimes)

## What's next for SongGen
Ideally in the future I will implement some form of machine learning algorithm, as a Markov Chain is definitely not the most effective way to do what I'm doing.  Also making a better front-end for users is on the to-do list.  Lastly I want to improve the linguistic element of the project and add some algorithms that take the text and turn it into something that is more like a real song.
