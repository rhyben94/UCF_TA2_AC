##The goal of this component would be to track (as best we can) the exchanges of information between players so that ASIs can better identify where there may be breakdowns in knowledge sharing 


MarkerBlocks_Labels_All = [red_abrasion,red_bonedamage,red_novictim,red_regularvictim,red_criticalvictim,red_rubble,red_threat,red_sos,
                           green_abrasion,green_bonedamage,green_novictim,green_regularvictim,green_criticalvictim,green_rubble,green_threat,green_sos,
                           blue_abrasion,blue_bonedamage,blue_novictim,blue_regularvictim,blue_criticalvictim,blue_rubble,blue_threat,blue_sos]

MarkerBlocks_Labels_VictimInformation = [red_abrasion,red_bonedamage,red_novictim,red_regularvictim,red_criticalvictim,
                                         green_abrasion,green_bonedamage,green_novictim,green_regularvictim,green_criticalvictim,
                                         blue_abrasion, blue_bonedamage, blue_novictim, blue_regularvictim, blue_criticalvictim]

MarkerBlocks_Labels_EnvironmentInformation = [red_novictim,red_regularvictim,red_criticalvictim,red_rubble,red_threat,
                                              green_novictim,green_regularvictim,green_criticalvictim,green_rubble,green_threat,
                                              blue_novictim,blue_regularvictim,blue_criticalvictim,blue_rubble,blue_threat]

MarkerBlocks_Labels_RequestsAlerts = [red_threat,red_sos,
                                      green_threat,green_sos,
                                      blue_threat,blue_sos]


Team_MarkerBlocks_CurrentlyOnMap = [] ##want to capture [[MarkerBlockType, X, Z, Zone], [MarkerBlockType, X, Z, Zone], [MarkerBlockType, X, Z, Zone], ...]





## at the start of the mission we'll want to start a timer
## @ mission start
##Time_start = get the current time at mission start







## All of the following would be instigated by OnMessage

## The simplest part of this will be tracking the marker blocks placed and destroyed by each player. That will mean subscribing to and monitoring the events associated with marker block placement (I’m not sure if marker destroyed events are published on the same topic, it may mean subscribing to more than one topic).
## When we see Event:MarkerPlaced we need to check the data.type to increment the correct count

##Current_Event_Data_Type = pull the data.type from the current message to identify the type of marker block

Current_BlockLocation = [] ##want the [X,Z], can determine the Zone from that






## Go down this cascade if the event is a placement
    ## All Medic placement events

    if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim or Current_Event_Data_Type == red_rubble or Current_Event_Data_Type == red_threat or Current_Event_Data_Type == red_sos:
        Externalization_PushCount_Overall_Medic += 1

    if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim:
        Externalization_VictimInformationPushes_Medic += 1

    if dCurrent_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim or Current_Event_Data_Type == red_rubble or Current_Event_Data_Type == red_threat:
        Externalization_EnvironmentInformationPushes_Medic += 1

    if Current_Event_Data_Type == red_threat or Current_Event_Data_Type == red_sos:
        Externalization_RequestsAlertsPushes_Medic += 1


    ## All Engineer placement events
    if Current_Event_Data_Type == blue_abrasion or Current_Event_Data_Type == blue_bonedamage or Current_Event_Data_Type == blue_novictim or Current_Event_Data_Type == blue_regularvictim or Current_Event_Data_Type == blue_criticalvictim or Current_Event_Data_Type == blue_rubble or Current_Event_Data_Type == blue_threat or Current_Event_Data_Type == blue_sos:
        Externalization_PushCount_Overall_Engineer += 1

    if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim:
        Externalization_VictimInformationPushes_Engineer += 1

    if dCurrent_Event_Data_Type == blue_novictim or Current_Event_Data_Type == blue_regularvictim or Current_Event_Data_Type == blue_criticalvictim or Current_Event_Data_Type == blue_rubble or Current_Event_Data_Type == blue_threat:
        Externalization_EnvironmentInformationPushes_Engineer += 1

    if Current_Event_Data_Type == blue_threat or Current_Event_Data_Type == blue_sos:
        Externalization_RequestsAlertsPushes_Engineer += 1


    ## All Transporter placement events
    if Current_Event_Data_Type == green_abrasion or Current_Event_Data_Type == green_bonedamage or Current_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim or Current_Event_Data_Type == green_rubble or Current_Event_Data_Type == green_threat or Current_Event_Data_Type == green_sos:
        Externalization_PushCount_Overall_Transporter += 1

    if Current_Event_Data_Type == green_abrasion or Current_Event_Data_Type == green_bonedamage or Current_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim:
        Externalization_VictimInformationPushes_Transporter += 1

    if dCurrent_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim or Current_Event_Data_Type == green_rubble or Current_Event_Data_Type == green_threat:
        Externalization_EnvironmentInformationPushes_Engineer += 1

    if Current_Event_Data_Type == green_threat or Current_Event_Data_Type == green_sos:
        Externalization_RequestsAlertsPushes_Transporter += 1

    ##check if Current_BlockLocation is the same as any in the Team_MarkerBlocks_CurrentlyOnMap list
    ##If so, remove the conflicting block from and add this one to Team_MarkerBlocks_CurrentlyOnMap list
    ##If not, add this one to Team_MarkerBlocks_CurrentlyOnMap list and update overlays

    ## This cascade will be needed if a marker block is placed in the same location as a MarkerBlock_CurrentlyOnMap
        ## All Marker Block Overlays
        if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim or Current_Event_Data_Type == red_rubble or Current_Event_Data_Type == red_threat or Current_Event_Data_Type == red_sos:
            Externalization_OverlaysCount_Overall_Medic += 1
            ##
        if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim:
            Externalization_VictimInformationOverlays_Medic += 1

        if dCurrent_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim or Current_Event_Data_Type == red_rubble or Current_Event_Data_Type == red_threat:
            Externalization_EnvironmentInformationOverlays_Medic += 1

        if Current_Event_Data_Type == red_threat or Current_Event_Data_Type == red_sos:
            Externalization_RequestsAlertsOverlays_Medic += 1


        ## All Engineer placement events
        if Current_Event_Data_Type == blue_abrasion or Current_Event_Data_Type == blue_bonedamage or Current_Event_Data_Type == blue_novictim or Current_Event_Data_Type == blue_regularvictim or Current_Event_Data_Type == blue_criticalvictim or Current_Event_Data_Type == blue_rubble or Current_Event_Data_Type == blue_threat or Current_Event_Data_Type == blue_sos:
            Externalization_OverlaysCount_Overall_Engineer += 1

        if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim:
            Externalization_VictimInformationOverlays_Engineer += 1

        if dCurrent_Event_Data_Type == blue_novictim or Current_Event_Data_Type == blue_regularvictim or Current_Event_Data_Type == blue_criticalvictim or Current_Event_Data_Type == blue_rubble or Current_Event_Data_Type == blue_threat:
            Externalization_EnvironmentInformationOverlays_Engineer += 1

        if Current_Event_Data_Type == blue_threat or Current_Event_Data_Type == blue_sos:
            Externalization_RequestsAlertsOverlays_Engineer += 1


        ## All Transporter placement events
        if Current_Event_Data_Type == green_abrasion or Current_Event_Data_Type == green_bonedamage or Current_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim or Current_Event_Data_Type == green_rubble or Current_Event_Data_Type == green_threat or Current_Event_Data_Type == green_sos:
            Externalization_OverlaysCount_Overall_Transporter += 1

        if Current_Event_Data_Type == green_abrasion or Current_Event_Data_Type == green_bonedamage or Current_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim:
            Externalization_VictimInformationOverlays_Transporter += 1

        if dCurrent_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim or Current_Event_Data_Type == green_rubble or Current_Event_Data_Type == green_threat:
            Externalization_EnvironmentInformationOverlays_Engineer += 1

        if Current_Event_Data_Type == green_threat or Current_Event_Data_Type == green_sos:
            Externalization_RequestsAlertsOverlays_Transporter += 1






## Go down this cascade if the event is a MarkerRemoved
    ## All Medic removal events
    if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim or Current_Event_Data_Type == red_rubble or Current_Event_Data_Type == red_threat or Current_Event_Data_Type == red_sos:
        Externalization_RemovalCount_Overall_Medic += 1

    if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim:
        Externalization_VictimInformationRemoval_Medic += 1

    if dCurrent_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim or Current_Event_Data_Type == red_rubble or Current_Event_Data_Type == red_threat:
        Externalization_EnvironmentInformationRemoval_Medic += 1

    if Current_Event_Data_Type == red_threat or Current_Event_Data_Type == red_sos:
        Externalization_RequestsAlertsRemoval_Medic += 1


    ## All Engineer placement events
    if Current_Event_Data_Type == blue_abrasion or Current_Event_Data_Type == blue_bonedamage or Current_Event_Data_Type == blue_novictim or Current_Event_Data_Type == blue_regularvictim or Current_Event_Data_Type == blue_criticalvictim or Current_Event_Data_Type == blue_rubble or Current_Event_Data_Type == blue_threat or Current_Event_Data_Type == blue_sos:
        Externalization_RemovalCount_Overall_Engineer += 1

    if Current_Event_Data_Type == red_abrasion or Current_Event_Data_Type == red_bonedamage or Current_Event_Data_Type == red_novictim or Current_Event_Data_Type == red_regularvictim or Current_Event_Data_Type == red_criticalvictim:
        Externalization_VictimInformationRemoval_Engineer += 1

    if dCurrent_Event_Data_Type == blue_novictim or Current_Event_Data_Type == blue_regularvictim or Current_Event_Data_Type == blue_criticalvictim or Current_Event_Data_Type == blue_rubble or Current_Event_Data_Type == blue_threat:
        Externalization_EnvironmentInformationRemoval_Engineer += 1

    if Current_Event_Data_Type == blue_threat or Current_Event_Data_Type == blue_sos:
        Externalization_RequestsAlertsRemoval_Engineer += 1


    ## All Transporter placement events
    if Current_Event_Data_Type == green_abrasion or Current_Event_Data_Type == green_bonedamage or Current_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim or Current_Event_Data_Type == green_rubble or Current_Event_Data_Type == green_threat or Current_Event_Data_Type == green_sos:
        Externalization_RemovalCount_Overall_Transporter += 1

    if Current_Event_Data_Type == green_abrasion or Current_Event_Data_Type == green_bonedamage or Current_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim:
        Externalization_VictimInformationRemoval_Transporter += 1

    if dCurrent_Event_Data_Type == green_novictim or Current_Event_Data_Type == green_regularvictim or Current_Event_Data_Type == green_criticalvictim or Current_Event_Data_Type == green_rubble or Current_Event_Data_Type == green_threat:
        Externalization_EnvironmentInformationRemoval_Engineer += 1

    if Current_Event_Data_Type == green_threat or Current_Event_Data_Type == green_sos:
        Externalization_RequestsAlertsRemoval_Transporter += 1

    ## Remove from Team_MarkerBlocks_CurrentlyOnMap




## For calculating the rates we are going to need to select a time window over which to calculate the rates and averages.
# For sake of argument, let’s say we’ll take a 30 second time window.
# CurrentRate will therefore be the count of externalizations/30 for that window and the “average” will actually be an average of averages for each window.

Externalization_RateAverage_Medic
Externalization_CurrentRate_Medic

Externalization_VictimInformationPushes_RateAverage_Medic
Externalization_VictimInformationPushes_CurrentRate_Medic

Externalization_RubbleInformationPushes_RateAverage_Medic
Externalization_RubbleInformationPushes_CurrentRate_Medic

Externalization_RequestsAlertsPushes_RateAverage_Medic
Externalization_RequestsAlertsPushes_CurrentRate_Medic

Externalization_RemoveBlock_RateAverage_Medic
Externalization_RemoveBlock_CurrentRate_Medic

Externalization_OverlayBlock_RateAverage_Medic
Externalization_OverlayBlock_CurrentRate_Medic




Externalization_RateAverage_Engineer
Externalization_CurrentRate_Engineer

Externalization_VictimInformationPushes_RateAverage_Engineer
Externalization_VictimInformationPushes_CurrentRate_Engineer

Externalization_RubbleInformationPushes_RateAverage_Engineer
Externalization_RubbleInformationPushes_CurrentRate_Engineer

Externalization_RequestsAlertsPushes_RateAverage_Engineer
Externalization_RequestsAlertsPushes_CurrentRate_Engineer

Externalization_RemoveBlock_RateAverage_Engineer
Externalization_RemoveBlock_CurrentRate_Engineer

Externalization_OverlayBlock_RateAverage_Engineer
Externalization_OverlayBlock_CurrentRate_Engineer




Externalization_RateAverage_Transporter
Externalization_CurrentRate_Transporter

Externalization_VictimInformationPushes_RateAverage_Transporter
Externalization_VictimInformationPushes_CurrentRate_Transporter

Externalization_RubbleInformationPushes_RateAverage_Transporter
Externalization_RubbleInformationPushes_CurrentRate_Transporter

Externalization_RequestsAlertsPushes_RateAverage_Transporter
Externalization_RequestsAlertsPushes_CurrentRate_Transporter

Externalization_RemoveBlock_RateAverage_Transporter
Externalization_RemoveBlock_CurrentRate_Transporter

Externalization_OverlayBlock_RateAverage_Transporter
Externalization_OverlayBlock_CurrentRate_Transporter



