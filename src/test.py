from request import SupportRequest

req = SupportRequest("My computer is not working")
print(req.description)
print(req.state) 
print(req.id)
print(req.created_at)