# East Coast Detector:

## Inspiration 
In developing countries, livestock offer a pathway out of poverty for millions of smallholders. Milk, meat, eggs and other animal products and services provide vital nutrition, income and security for families and their communities. But productivity remains low, and poor animal health an ongoing threat. 

## What it does
Uses data science & IoT to find the origin of the contagious, tick-borne disease "East Coast Fever"
Collar collects sensory information from an individual cow - temperature, gait, location, distance traveled. At 60 second intervals, aggregates symptoms to gauge the health condition of the cow - ILL (high temperature, unsteady gait) or AT RISK (has been in close contact with a cow previously deemed ILL). Displays RED and YELLOW LED accordingly, so farmers are continuously updated on the status of their cattle. 

## How we built it
Using Python & LoPy, we made a smart collar for cows that tracks the health of cows and aims to detect whether a cow/buffalo has a East coast fever. It exploits one of the properties of the symptoms - the lymphs. The temperature in the lymphs are relatively less than the temperature in the cows. The collar looks for any difference in the temperature in a certain area of the neck and try to determine disease. It also uses LoRa network & GPS to find any other cows that were close to the sick cow to trigger a possible 

## Accomplishments that we're proud of
- We have a working thermal sensor that can detect the difference between two different areas of the cow & send an email to the farmer notifying that something's not right.
- We configured the GPS device & now we're able to map the movement of the infected cow in a large scale helping us track the origin of the disease.
- We were able to tackle the problem of illiteracy in African farmers by replacing text based communications with visual pictures.

## What we learned:
- We learnt how to use LoPy and about the LoRa network
- We learnt how we could use biological facts & use technology to use it in our advantages.

## What's next for Fever Fighters!
- Using the data we collected, we could track the origin of the disease.
- Using bluetooth & the LoRa network we could predict other cattles that could be suffering from the disease, we have a model ready, perhaps we could make the model more accurate.

## Contributers:
- Gagan Devagiri
- Jack Radford
- Clara Ng
- Yi Wang
