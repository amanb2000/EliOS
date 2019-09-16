# EliOS
End goal: predict mood episodes.
Who it’s for: Eli (case study), potentially generalized to public market or rehab centres.
How we do it: 
* What we’ll track:
    * Mood (every day) with a combination of Doctor’s forms + other methods
    * Sleep (Fitbit)
    * Diet (calories)
    * Weather
    * Daily schedule
        * Interface with google calendar
        * By which calendar it is
            * Could also do #of appointments/hours accounted for
        * If the word ‘doctor’ is used
    * EEG in meditation!
        * Eli sits and gets EEG’d while meditating for 10 minutes w/ Calm.
    * Exercise (minutes, quality on Likert scale)
    * Fitbit stuff
        * All heart rate info
        * Steps
        * Sleep!
        * GPS data
* Rough Data Pipeline:
    * Inputs:
        * Our web app interface
        * Fitbit JSON export (daily or weekly?)
        * Weather API (based on zip code)
        * EEG emotiv interface => CSV
        * Calendar => Google Calendar API, JSON
    * Aggregated into firebase/web app
    * Get a data pulling system going to download full dataset + mess around with it.
    * Integrate Caretrack ML Server (Adam can help) for inputting analytics.
* ML Stuff
    * Will discuss later...
* Misc. implementation ideas:
    * Notifications for when to track your mood (web notifications, iOS notifications later on?)
    * Have a retroactive labeling system
        * Mark manic/depressive/mixed episodes every 2 weeks.
