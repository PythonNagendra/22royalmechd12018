import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("nagendrasr02@gmail.com", "nsr02022000") 
  
# message to be sent 
message = "Hello Prajwal"
  
# sending the mail 
s.sendmail("nagendrasr02@gmail.com", "rosethasin@gmail.com", message) 
  
# terminating the session 
s.quit() 