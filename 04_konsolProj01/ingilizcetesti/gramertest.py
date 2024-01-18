

verbs = {"simpPre": ["run","walk","see","watch","help"]}

subject = ["I","You","He","She","It","We","They","You"]

#i, you, we, they, don't
#he, she, it does not
#we can check the subject first
forms = {"negative" : {"simPre" : ["do not","does not"],
                       "simPas" : ["did not"],
                       "simFut" : ["will not"]},
        "positive" : {"simPre" : ["does", "do"],
            "simPas" : ["irre","regu"],
            "simFut" : ["will"]}
        }

print(forms["negative"])

#random subject sec

#random object sec