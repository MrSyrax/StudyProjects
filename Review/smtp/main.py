import smtplib

#store credentials for the email you will be using to send out the mail
my_email = 'kevinlearningpython@gmail.com'
password = '5426233Kk!!'


#open a connection to the gmail smtp server on port (587 for tls)
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        #start TLS 
        connection.starttls()
        #enter credentials stored above 
        connection.login(my_email,password)
        #send the email by using connection.sendmail()
        connection.sendmail(
            #specify who it's from
            from_addr=my_email,
            #specify who it is going to
            to_addrs='kevincarrillo89@yahoo.com',
            #write out the message Subject:subject here\n\natual message here
            msg=F'Subject:SUP BEEEETCH!\n\nstuff to email')