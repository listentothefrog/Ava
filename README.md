# Ava 

Ava stands for Advanced Voice Assitant. Her mission in life is simple it is to help me with my daily tasks. Currently she is running on my computer and only responds to my voice and the voice of my parents. She is still in production mode with great updates that will come along the way.

# Packages and abilities 

Here is how Ava works and the packages it uses,

* `speech_recognition`  Ava uses speech_recognition to detect voices. Ava uses a python package called speech_recognition, this is really popular speech recognition package and recommend using this if you wanna build your own AI bot. 
* `natural language processing`  Ava uses the google cloud natural language api to find the entity and sentiment, this is really beneficial becuase you don't wanna be hard code all of the commands. For the time being there no commands it just pronts the entity type and the sentitment.
  
#### Abilites of AVA 
* `Authentication` Before you can talk with AVA, she needs to know that if it's me (Shashank) so its sends an email to my inbox with a verification code, which s randomly generated. If my response is equal to the verification code then it will speak. This is useful because I don't want strangers to speak with because of security reasons. 

#### I have to work on this abilites but these are some ideas that I have in my mind. 
* `Sending Emails`  Ava can send emails based on certain commands that need my password, for example if you want to create a new github project it first asks your password and creates the project and sends an email to my gmail, this uses the smtplib module in python. I am still working on this and need to figure where this will be usefull
* `Playing Music` Ava can plays music using the Spotify api, Ava plays the most popular tracks and can also search for tracks. I am also planning to recommend music based on my intrests this can be done in two ways 
  * We can either do it as a csv file or just use the spotify api. I am planning to go in the csv file route because it is not limited. 

#### Thats about it I am planning to add more features to AVA until it can fully function like human. 

# Open Source 

I am planning to keep this open source, because I want to people to contribute to this repo and I also learn when expirenced programmers make code changes to my code and want to people to have this tool as a refrence if they are building there own AI system that will help them in their lives.

(Don't read this if you know open source works) Here are the steps for beginners who don't know how open source works 

* If you want to work on this project you got to clone this repo `git clone https://github.com/shashanke7y/Ava.git` on your machine.
* Then you got to create a branch and name that branch what ever you want `git checkout newBranch`
* You can make your changes in the branch and push em. `git push newBranch` 
* When you push your changes, head over to the repo and click on Pull request, then type your title and description. 
* After you are done with that you just wait for me to merge your PR, this will take one day. 

### If you are having any questions you can join the my discord server https://discord.gg/GUmxzGPTDV you can chat with other devs and ask for help. Happy Coding 

