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
    global currentTemp = 10
    global currentHeartRate = 10
    global currentPace = 0
    if (currentTemp <= 15 and currentHeartRate <= 10 and currentPace < 10) :
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return False
    else:
        return True

def Fever():
    global varFever = currentTemp + currentHeartRate
    if (varFever >= 130):
        return False
    else:
        return True

def EastCoastFever():
    if (Fever):
        RelativeTemp = #RelativeTemp()
        if RelativeTemp > 5:
            
            message = f"""
            Subject: East Coast Fever alert!
            
            
            Our system has diagnosed cow number {num} with possible """
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                return False
            else:
                return True

alive = DeadorAlive()

# def main() 
# if state:
#     # heart rate not less than 20.
#     # temperature not less than 30.
#     # then declare dead 
#     return "Dead" # notify farmer that the cow is dead.
# #else:
num = 2