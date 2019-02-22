import smtplib, ssl
## 
#### EMAIL CONFIG ####

port = 465  # For SSL 
smtp_server = "smtp.gmail.com"
sender_email = "eastcoastdetector@gmail.com"  # Enter your address
receiver_email = "gagandevagiri@gmail.com"  # Enter receiver address
password = input("Type the id and press enter: ")

num = 420

#### EMAIL CONFIG ####



def DeadorAlive():
    # add functions instead of the actual value.
    global currentTemp
    currentTemp = 40 #celsius
    global currentHeartRate
    currentHeartRate = 70
    if (currentTemp <= 15 and currentHeartRate <= 10) :
        message = """\
Subject: Your cow died lol!

lmao
."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return False
    else:
        return True

def Fever():
    global varFever
    varFever = currentTemp + currentHeartRate
    if (varFever >= 100):
        return True
    else:
        return False

def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        return True


def EastCoastFever(Fever):
    if (Fever):
        RelativeTemp = 10#RelativeTemp()
        if RelativeTemp > 5:
            global message
            message = f"""
            Subject: East Coast Fever alert!
            

            Our system has diagnosed cow number {num} possibility of East coast fever.
            Please take appropiate action. """
            x = sendEmail()
            return x
        else:
            global message
            message = f"""
            Subject: East Coast Fever alert!


            Our system has diagnosed cow number {num} possibility of fever & a low possibility of east coast fever.
            We reccomend that you take appropiate action immediately. """
            x = sendEmail()
            return x
    else:
        global message
        message = f"""
        Subject: Daily update! (No action required)


        Your cow's healthy.
        """


alive = DeadorAlive()
if (alive):
    fever = Fever()
else:
    fever = False
ECF = EastCoastFever(fever)
if (not fever):
    print("Cow's healthy")

def main():
    if state:
        heart rate 
# def main() 
# if state:
#     # heart rate not less than 20.
#     # temperature not less than 30.
#     # then declare dead 
#     return "Dead" # notify farmer that the cow is dead.
# #else: