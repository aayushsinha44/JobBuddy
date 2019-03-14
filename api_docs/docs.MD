Company Registration 

{
"name": "xyz",
"sector": "IT",  
"website": "www.google.com",
"about": "some text"
}
endpoint: /register_company/
sector -> 'IT', 'Finance', 'Marketing'

Company Auto Complete

{
"start_with": "abc"
}
endpoint: /get_company_autocomplete/

Recruiter Registration


curl --request POST --data '{
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "recruiter",
            "company": "1",
            "pan": "123"
        }'  http://192.168.159.206:8000/register/
        
Recruiter Login

curl --request POST --data '{"phone_number": "9203", "password": "abc", "type": "recruiter" }'  http://192.168.159.206:8000/login/

email/phone_number
