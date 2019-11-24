# EliOS
**End goal:** Help people with mood disorders such as Bipolar, Depression, and Seasonal Affective Disorder to manage their position. 

**How we do it:** We created **EliOS**, a system for **understanding, predicting,** and **collaborating** to treat mood disorders. Through brain scanning, mood & activity tracking, and artificial intelligence, we can change what it means to have mood disorders.

## Motivation:
EliOS was built for (and named after) our great friend Eli Scott. Eli is a student of Cognitive Science and has Bipolar disorder. The idea of EliOS was born when she noticed that none of the mood tracker apps that she could find really helped her manage her condition. They didn't even visualize the trends in her mood very effectively for her doctors, let alone make predictions or recommendations. Furthermore, none of the apps had any way to make the process of building and reaching out to a support network any easier. 

## Goals:
To make sure we met the needs of our stakeholders, we conducted a **psychological literature review** and a **user consultation meeting**. These are our resultant design goals:
* Quick & clean data entry.
* Clear and concise visualization of data.
* Make effective and clear predictions.
* 


Who it’s for: Eli (case study), potentially generalized to public market or rehab centres.
## How we do it: 
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

## Questions (Preliminary):
* How was your mood today overall? `Slider` `1-7`
	* How variable was your mood over today? `Slider` `1-7`
* How much sleep did you get? `Slider` `0-24`
* How many calories did you consume? (Estimate is fine) `Slider` `0-5000`
* `Zip Code` should be known for weather
* `Google Calendar` should be integrated via google account.
* Upload your meditation EEG: `File Upload`
* How many minutes did you exercise? `0-12`
* How much did you exercise today? `1-12`
* How intense was your exercise? `1-7`

## Types of Input to Have Ready:
* 5-Button Likhert Scale
* Slider
* Rich Text Input
* Short text input (Email, Postal, etc.)
* File Upload
* Google Auth (I can handle this...)
