import smtplib, ssl

#### EMAIL CONFIG ####

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "eastcoastdetector@gmail.com"  # Enter your address
receiver_email = "gagandevagiri@gmail.com"  # Enter receiver address
password = input("Type the id and press enter: ")
message = """\
Subject: Hello peasents!

Your cow died lol
."""



#### EMAIL CONFIG ####



def DeadorAlive():
    # add functions instead of the actual value.
    currentTemp = 10
    currentHeartRate = 10
    currentPace = 0
    if (currentTemp <= 15 and currentHeartRate <= 10 and currentPace < 10) :
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return "cow died"
    else:

        return "cow didn't die"
alive = DeadorAlive() # Dead or alive
print(alive)

# def main() 
# if state:
#     # heart rate not less than 20.
#     # temperature not less than 30.
#     # then declare dead 
#     return "Dead" # notify farmer that the cow is dead.
# #else:
    