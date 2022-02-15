import json

Player_name = "Red"
Player_role = "Medic"

## Median cutoffs for each measure

SBSOD_MedianCutoff = 4.933
VGEM_MinecraftUSAR_MedianCutoff = 77.93
Competency_MedianCutoff = 90
PsychologicalCollectivism_MedianCutoff = 59
RMET_MedianCutoff = 27
SociableDominance_MedianCutoff = 46

TaskPotential_MustBeHighIn = 1
TeamPotential_MustBeHighIn = 1

## Assign measure response values to script variables. The competency test completion times may need to be pulled in separately depending on when that message gets published

Competency_Score = 200
##print("Competency_Score: ")
##print(Competency_Score)
## Credit note: thank you to the Gallup team for providing the question to message mappings!

##{"ImportId":"QID13_1"}
##b0_Q10_1
SBSOD_1 = 2

##{"ImportId":"QID13_2"}
##b0_Q10_2
SBSOD_2 = 4

##{"ImportId":"QID13_3"}
##b0_Q10_3
SBSOD_3 = 1

##{"ImportId":"QID13_4"}
##b0_Q10_4
SBSOD_4 = 3

##{"ImportId":"QID13_5"}
##b0_Q10_5
SBSOD_5 = 3

##{"ImportId":"QID13_6"}
##b0_Q10_6
SBSOD_6 = 4

##{"ImportId":"QID13_7"}
##b0_Q10_7
SBSOD_7 = 6

##{"ImportId":"QID13_8"}
##b0_Q10_8
SBSOD_8 = 7

##{"ImportId":"QID13_9"}
##b0_Q10_9
SBSOD_9 = 5

##{"ImportId":"QID13_10"}
##b0_Q10_10
SBSOD_10 = 4

##{"ImportId":"QID13_11"}
##b0_Q10_11
SBSOD_11 = 2

##{"ImportId":"QID13_12"}
##b0_Q10_12
SBSOD_12 = 6

##{"ImportId":"QID13_13"}
##b0_Q10_13
SBSOD_13 = 7

##{"ImportId":"QID13_14"}
##b0_Q10_14
SBSOD_14 = 1

##{"ImportId":"QID13_15"}
##b0_Q10_15
SBSOD_15 = 5


## The video game experience measure scores need to be standardized for calculation

##{"ImportId":"QID867_1"}
##b0_Q20_1
##Please indicate how many years of experience you have with the following: - Years using a computer for any purpose
VGEM_1 = 12*5

##{"ImportId":"QID867_2"}
##b0_Q20_2
##Please indicate how many years of experience you have with the following: - Years using a computer to play video games
VGEM_2 = 12*5

##{"ImportId":"QID867_4"}
##b0_Q20_4
##Please indicate how many years of experience you have with the following: - Years playing Minecraft
VGEM_3 = 12*5

##{"ImportId":"QID868_1"}
##b0_Q19_1
##For the following, please indicate how regularly you: - Use a computer
VGEM_4 = 3
if VGEM_4 == 1:
    VGEM_4 = 0
elif VGEM_4 == 2:
    VGEM_4 = 16
elif VGEM_4 == 3:
    VGEM_4 = 33
elif VGEM_4 == 4:
    VGEM_4 = 50
elif VGEM_4 == 6:
    VGEM_4 = 82
elif VGEM_4 == 7:
    VGEM_4 = 100
else:
    print("Something is wrong with the value of VGEM_4")


##{"ImportId":"QID868_3"}
##b0_Q19_3
##For the following, please indicate how regularly you: - Use a computer to play video games
VGEM_5 = 2
if VGEM_5 == 1:
    VGEM_5 = 0
elif VGEM_5 == 2:
    VGEM_5 = 16
elif VGEM_5 == 3:
    VGEM_5 = 33
elif VGEM_5 == 4:
    VGEM_5 = 50
elif VGEM_5 == 6:
    VGEM_5 = 82
elif VGEM_5 == 7:
    VGEM_5 = 100
else:
    print("Something is wrong with the value of VGEM_5")

##{"ImportId":"QID868_5"}
##b0_Q19_5
##For the following, please indicate how regularly you: - Play video games which require participation in a team
VGEM_6 = 4
if VGEM_6 == 1:
    VGEM_6 = 0
elif VGEM_6 == 2:
    VGEM_6 = 16
elif VGEM_6 == 3:
    VGEM_6 = 33
elif VGEM_6 == 4:
    VGEM_6 = 50
elif VGEM_6 == 6:
    VGEM_6 = 82
elif VGEM_6 == 7:
    VGEM_6 = 100
else:
    print("Something is wrong with the value of VGEM_6")

##{"ImportId":"QID868_6"}
##b0_Q19_6
##For the following, please indicate how regularly you: - Play Minecraft
VGEM_7 = 2
if VGEM_7 == 1:
    VGEM_7 = 0
elif VGEM_7 == 2:
    VGEM_7 = 16
elif VGEM_7 == 3:
    VGEM_7 = 33
elif VGEM_7 == 4:
    VGEM_7 = 50
elif VGEM_7 == 6:
    VGEM_7 = 82
elif VGEM_7 == 7:
    VGEM_7 = 100
else:
    print("Something is wrong with the value of VGEM_7")

##{"ImportId":"QID872_1"}
##b0_Q15_1
##Learning the layout of a new virtual environment
VGEM_8 = 80

##{"ImportId":"QID872_2"}
##b0_Q15_2
##Communicating your current location in a virtual environment to members of a team
VGEM_9 = 30

##{"ImportId":"QID872_3"}
##b0_Q15_3
##Coordinating with teammates to optimize tasks
VGEM_10 = 40

##{"ImportId":"QID872_4"}
##b0_Q15_4
##Maintaining an awareness of game/task parameters (e.g., time limits, point goals, etc)
VGEM_11 = 60

##{"ImportId":"QID872_5"}
##b0_Q15_5
##Learning the purposes of novel items, tools, or objects
VGEM_12 = 20

##{"ImportId":"QID872_6"}
##b0_Q15_6
##Remembering which places you have visited  in a virtual environment
VGEM_13 = 10

##{"ImportId":"QID872_7"}
##b0_Q15_7
##Controlling the movement of an avatar using the W, A, S, and D keys + mouse control
VGEM_14 = 90

##{"ImportId":"QID872_8"}
##b0_Q15_8
##Keeping track of where you are in a virtual environment
VGEM_15 = 40

##{"ImportId":"QID830_1"}
##b0_Q21_1
##I preferred to work in those groups rather than working alone
PsychologicalCollectivism_1 = 4

##{"ImportId":"QID830_2"}
##b0_Q21_2
##Working in those groups was better than working alone.
PsychologicalCollectivism_2 = 6

##{"ImportId":"QID830_3"}
##b0_Q21_3
##I wanted to work with those groups as opposed to working alone.
PsychologicalCollectivism_3 = 3

##{"ImportId":"QID830_4"}
##b0_Q21_4
##I felt comfortable counting on group members to do their part.
PsychologicalCollectivism_4 = 7

##{"ImportId":"QID830_5"}
##b0_Q21_5
##I was not bothered by the need to rely on group members.
PsychologicalCollectivism_5 = 1

##{"ImportId":"QID830_6"}
##b0_Q21_6
##I felt comfortable tasking group members to handle their tasks.
PsychologicalCollectivism_6 = 2

##{"ImportId":"QID830_7"}
##b0_Q21_7
##The health of those groups was important to me.
PsychologicalCollectivism_7 = 5

##{"ImportId":"QID830_8"}
##b0_Q21_8
##I cared about the well-being of those groups.
PsychologicalCollectivism_8 = 4

##{"ImportId":"QID830_9"}
##b0_Q21_9
##I was concerned about the needs of those groups.
PsychologicalCollectivism_9 = 6

##{"ImportId":"QID830_10"}
##b0_Q21_10
##I followed the norms of those groups.
PsychologicalCollectivism_10 = 2

##{"ImportId":"QID830_11"}
##b0_Q21_11
##I followed the procedures used by those groups.
PsychologicalCollectivism_11 = 4

##{"ImportId":"QID830_12"}
##b0_Q21_12
##I accepted the rules of those groups.
PsychologicalCollectivism_12 = 2

##{"ImportId":"QID830_13"}
##b0_Q21_13
##I cared more about the goals of those groups than my own goals.
PsychologicalCollectivism_13 = 4

##{"ImportId":"QID830_14"}
##b0_Q21_14
##I emphasized the goals of those groups more than my individual goals.
PsychologicalCollectivism_14 = 5

##{"ImportId":"QID830_15"}
##b0_Q21_15
##Group goals were more important to me than my personal goals.
PsychologicalCollectivism_15 = 6


##{"ImportId":"QID832_9"}
##b0_Q22_1
##I have no problems talking in front of a group.
SociableDominance_1 = 1

##{"ImportId":"QID832_16"}
##b0_Q22_2
##At school I found it easy to talk in front of the class
SociableDominance_2 = 4

##{"ImportId":"QID832_17"}
##b0_Q22_3
##No doubt I’ll make a good leader.
SociableDominance_3 = 3

##{"ImportId":"QID832_18"}
##b0_Q22_4
##I certainly have self-confidence.
SociableDominance_4 = 5

##{"ImportId":"QID832_19"}
##b0_Q22_5
##For me it is not hard to start a conversation in a group.
SociableDominance_5 = 6

##{"ImportId":"QID832_20"}
##b0_Q22_6
##I am not shy with strangers.
SociableDominance_6 = 3

##{"ImportId":"QID832_21"}
##b0_Q22_7
##I like taking responsibility.
SociableDominance_7 = 4

##{"ImportId":"QID832_22"}
##b0_Q22_8
##People turn to me for decisions
SociableDominance_8 = 5

##{"ImportId":"QID832_23"}
##b0_Q22_9
##I can look everybody in the eye, and lie with a straight face
SociableDominance_9 = 1

##{"ImportId":"QID832_24"}
##b0_Q22_10
##I can lie without anybody noticing it
SociableDominance_10 = 2

##{"ImportId":"QID832_25"}
##b0_Q22_11
##I find it important to get my way.
SociableDominance_11 = 4

##{"ImportId":"QID832_26"}
##b0_Q22_12
##I find it important to get my way, even if this causes a row
SociableDominance_12 = 5

##{"ImportId":"QID832_27"}
##b0_Q22_13
##I quickly feel aggressive with people
SociableDominance_13 = 6

##{"ImportId":"QID832_28"}
##b0_Q22_14
##I make smart, sarcastic remarks if people deserve it
SociableDominance_14 = 4

##{"ImportId":"QID832_29"}
##b0_Q22_15
##I’d rather be disliked (for being unkind) and that people look down on me (for not achieving my aims)
SociableDominance_15 = 7



##{"ImportId":"QID751"}
##b0_Q26
RMET_1 = 3

##{"ImportId":"QID753"}
##b0_Q28
RMET_2 = 2

##{"ImportId":"QID755"}
##b0_Q30
RMET_3 = 4

##{"ImportId":"QID757"}
##b0_Q32
RMET_4 = 2

##{"ImportId":"QID759"}
##b0_Q34
RMET_5 = 1

##{"ImportId":"QID761"}
##b0_Q36
RMET_6 = 3

##{"ImportId":"QID763"}
##b0_Q38
RMET_7 = 4

##{"ImportId":"QID765"}
##b0_Q40
RMET_8 = 3

##{"ImportId":"QID767"}
##b0_Q42
RMET_9 = 4

##{"ImportId":"QID769"}
##b0_Q44
RMET_10 = 2

##{"ImportId":"QID771"}
##b0_Q46
RMET_11 = 3

##{"ImportId":"QID773"}
##b0_Q48
RMET_12 = 4

##{"ImportId":"QID775"}
##b0_Q50
RMET_13 = 1

##{"ImportId":"QID777"}
##b0_Q52
RMET_14 = 1

##{"ImportId":"QID779"}
##b0_Q54
RMET_15 = 2

##{"ImportId":"QID781"}
##b0_Q56
RMET_16 = 3

##{"ImportId":"QID783"}
##b0_Q58
RMET_17 = 4

##{"ImportId":"QID785"}
##b0_Q60
RMET_18 = 3

##{"ImportId":"QID787"}
##b0_Q62
RMET_19 = 1

##{"ImportId":"QID789"}
##b0_Q64
RMET_20 = 2

##{"ImportId":"QID791"}
##b0_Q66
RMET_21 = 3

##{"ImportId":"QID793"}
##b0_Q68
RMET_22 = 4

##{"ImportId":"QID795"}
##b0_Q70
RMET_23 = 3

##{"ImportId":"QID797"}
##b0_Q72
RMET_24 = 2

##{"ImportId":"QID799"}
##b0_Q74
RMET_25 = 1

##{"ImportId":"QID801"}
##b0_Q76
RMET_26 = 3

##{"ImportId":"QID803"}
##b0_Q78
RMET_27 = 2

##{"ImportId":"QID805"}
##b0_Q80
RMET_28 = 1

##{"ImportId":"QID807"}
##b0_Q82
RMET_29 = 1

##{"ImportId":"QID809"}
##b0_Q84
RMET_30 = 2

##{"ImportId":"QID811"}
##b0_Q86
RMET_31 = 3

##{"ImportId":"QID813"}
##b0_Q88
RMET_32 = 4

##{"ImportId":"QID815"}
##b0_Q90
RMET_33 = 3

##{"ImportId":"QID817"}
##b0_Q92
RMET_34 = 3

##{"ImportId":"QID819"}
##b0_Q94
RMET_35 = 1

##{"ImportId":"QID821"}
##b0_Q96
RMET_36 = 1

## Measure score calculations

SBSOD_Score = sum([SBSOD_1, abs(SBSOD_2 - 8) , SBSOD_3 , SBSOD_4 , SBSOD_5 , abs(SBSOD_6 - 8 ) , SBSOD_7 , abs(SBSOD_8 - 8) , SBSOD_9 , abs(SBSOD_10 - 8) , abs(SBSOD_11 - 8) , abs(SBSOD_12 - 8) , abs(SBSOD_13 - 8) , SBSOD_14 , abs(SBSOD_15-8)])/15
##print("SBSOD Score: ")
##print(SBSOD_Score)

VGEM_MinecraftUSAR_Score = sum([VGEM_1 , VGEM_2 , VGEM_3 , VGEM_4 , VGEM_5 , VGEM_6 , VGEM_7 , VGEM_8 , VGEM_9 , VGEM_10 , VGEM_11 , VGEM_12 , VGEM_13 , VGEM_14 , VGEM_15])/15
##print("VGEM_MinecraftUSAR_Score: ")
##print(VGEM_MinecraftUSAR_Score)

PsychologicalCollectivism_Score = sum([PsychologicalCollectivism_1 , PsychologicalCollectivism_2 , PsychologicalCollectivism_3 , PsychologicalCollectivism_4 , PsychologicalCollectivism_5 , PsychologicalCollectivism_6 , PsychologicalCollectivism_7 , PsychologicalCollectivism_8 , PsychologicalCollectivism_9 , PsychologicalCollectivism_10 , PsychologicalCollectivism_11 , PsychologicalCollectivism_12 , PsychologicalCollectivism_13 , PsychologicalCollectivism_14 , PsychologicalCollectivism_15])/15
##print("PsychologicalCollectivism_Score: ")
##print(PsychologicalCollectivism_Score)

SociableDominance_Score = sum([SociableDominance_1 , SociableDominance_2 , SociableDominance_3 , SociableDominance_4 , SociableDominance_5 , SociableDominance_6 , SociableDominance_7 , SociableDominance_8 , SociableDominance_9 , SociableDominance_10 , SociableDominance_11 , SociableDominance_12 , SociableDominance_13 , SociableDominance_14 , SociableDominance_15])/15
##print("SociableDominance_Score: ")
##print(SociableDominance_Score)

## The correct answers for the Reading the Mind in the Eyes Test are listed here in tandem with their corresponding item number (i.e., the correct answer to RMET_1 is 1 and the correct answer to RMET_27 is 2)

RMET_Score = 0
if RMET_1 == 1:
    RMET_Score += 1
if RMET_2 == 2:
    RMET_Score += 1
if RMET_3 == 3:
    RMET_Score += 1
if RMET_4 == 2:
    RMET_Score += 1
if RMET_5 == 3:
    RMET_Score += 1
if RMET_6 == 2:
    RMET_Score += 1
if RMET_7 == 3:
    RMET_Score += 1
if RMET_8 == 1:
    RMET_Score += 1
if RMET_9 == 4:
    RMET_Score += 1
if RMET_10 == 1:
    RMET_Score += 1
if RMET_11 == 3:
    RMET_Score += 1
if RMET_12 == 3:
    RMET_Score += 1
if RMET_13 == 2:
    RMET_Score += 1
if RMET_14 == 4:
    RMET_Score += 1
if RMET_15 == 1:
    RMET_Score += 1
if RMET_16 == 2:
    RMET_Score += 1
if RMET_17 == 1:
    RMET_Score += 1
if RMET_18 == 1:
    RMET_Score += 1
if RMET_19 == 4:
    RMET_Score += 1
if RMET_20 == 2:
    RMET_Score += 1
if RMET_21 == 2:
    RMET_Score += 1
if RMET_22 == 1:
    RMET_Score += 1
if RMET_23 == 3:
    RMET_Score += 1
if RMET_24 == 1:
    RMET_Score += 1
if RMET_25 == 4:
    RMET_Score += 1
if RMET_26 == 3:
    RMET_Score += 1
if RMET_27 == 2:
    RMET_Score += 1
if RMET_28 == 1:
    RMET_Score += 1
if RMET_29 == 4:
    RMET_Score += 1
if RMET_30 == 2:
    RMET_Score += 1
if RMET_31 == 2:
    RMET_Score += 1
if RMET_32 == 1:
    RMET_Score += 1
if RMET_33 == 4:
    RMET_Score += 1
if RMET_34 == 3:
    RMET_Score += 1
if RMET_35 == 2:
    RMET_Score += 1
if RMET_36 == 3:
    RMET_Score += 1

##print("RMET_Score: ")
##print(RMET_Score)

## Measure median cutoff categorizations
## Note I’ve been using 0 = Low and 1 = High, but could go back to string values if that makes things easier

if SBSOD_Score > SBSOD_MedianCutoff:
    SBSOD_MedianSplit_Score = 1
else:
    SBSOD_MedianSplit_Score = 0
print("SBSOD_MedianSplit_Score: ")
print(SBSOD_MedianSplit_Score)


if VGEM_MinecraftUSAR_Score > VGEM_MinecraftUSAR_MedianCutoff:
    VGEM_MinecraftUSAR_MedianSplit_Score = 1
else:
    VGEM_MinecraftUSAR_MedianSplit_Score = 0
print("VGEM_MinecraftUSAR_MedianSplit_Score: ")
print(VGEM_MinecraftUSAR_MedianSplit_Score)


if Competency_Score > Competency_MedianCutoff:
    Competency_MedianSplit_Score = 1
else:
    Competency_MedianSplit_Score = 0
print("Competency_MedianSplit_Score: ")
print(Competency_MedianSplit_Score)


if PsychologicalCollectivism_Score > PsychologicalCollectivism_MedianCutoff:
    PsychologicalCollectivism_MedianSplit_Score = 1
else:
    PsychologicalCollectivism_MedianSplit_Score = 0
print("PsychologicalCollectivism_MedianSplit_Score: ")
print(PsychologicalCollectivism_MedianSplit_Score)


if RMET_Score > RMET_MedianCutoff:
    RMET_MedianSplit_Score = 1
else:
    RMET_MedianSplit_Score = 0
print("RMET_MedianSplit_Score: ")
print(RMET_MedianSplit_Score)


if SociableDominance_Score > SociableDominance_MedianCutoff:
    SociableDominance_MedianSplit_Score = 1
else:
    SociableDominance_MedianSplit_Score = 0
print("SociableDominance_MedianSplit_Score: ")
print(SociableDominance_MedianSplit_Score)


## Measure median cutoff categorizations

TaskPotential_Score = sum([SBSOD_MedianSplit_Score , VGEM_MinecraftUSAR_MedianSplit_Score , Competency_MedianSplit_Score])

TeamPotential_Score = sum([PsychologicalCollectivism_MedianSplit_Score , RMET_MedianSplit_Score , SociableDominance_MedianSplit_Score])


if TaskPotential_Score > TaskPotential_MustBeHighIn:
    TaskPotential_Category = 1
else:
    TaskPotential_Category = 0

if TeamPotential_Score > TeamPotential_MustBeHighIn:
    TeamPotential_Category = 1
else:
    TeamPotential_Category = 0

## Profile Outcome

if TaskPotential_Score == 1 and TeamPotential_Score == 1:
    PlayerProfile = "HighTaskHighTeam"
elif TaskPotential_Score == 1 and TeamPotential_Score == 0:
    PlayerProfile = "HighTaskLowTeam"
if TaskPotential_Score == 0 and TeamPotential_Score == 1:
    PlayerProfile = "LowTaskHighTeam"
if TaskPotential_Score == 0 and TeamPotential_Score == 0:
    PlayerProfile = "LowTaskLowTeam"

print("Player Profile: ")
print(PlayerProfile)
## The following variables should be published back to the message bus with appropriate tagging information

##The player’s name
##The player’s role
##The player’s TaskPotential
##The player’s TeamPotential
##The player’s PlayerProfile
