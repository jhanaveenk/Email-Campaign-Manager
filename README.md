This is a Email Campaign Manager:
1. clone projectt using 'git clone https://github.com/jhanaveenk/MikeLegal.git'.
2. Download all dependencies from requirement.txt using command 'pip install -r requirements.txt".
3. Remember to replace credentials of EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.
4. To GET and POST the subscribers using this endpoint 'http://127.0.0.1:8000/api/add_subscriber/'
   ![Screenshot (52)](https://github.com/jhanaveenk/MikeLegal/assets/71990959/3b61dc2d-3ed1-45aa-a512-7b229987c466)
  ![Screenshot (53)](https://github.com/jhanaveenk/MikeLegal/assets/71990959/2a364ed6-6c62-4aa4-abe3-b168e78181d3)
5. To Unsubscriber use this endpoint with PATCH request 'http://localhost:8000/api/unsubscribe/<email>/'
     ![Screenshot (54)](https://github.com/jhanaveenk/MikeLegal/assets/71990959/a595c3bd-2392-4684-bc08-6f140c3cb78c)

6. To send daily Campaigns using SMTP use this endpoint with post-request 'http://127.0.0.1:8000/api/send_daily_campaign/'
   ![Screenshot (56)](https://github.com/jhanaveenk/MikeLegal/assets/71990959/d697a009-4ec1-4e66-a178-1b9671d75e24)
![Screenshot (57)](https://github.com/jhanaveenk/MikeLegal/assets/71990959/891e03f7-22ac-4cc7-9068-2df9d325d395)
7. Create SuperUser to have a look into the admin panel 
![Screenshot (55)](https://github.com/jhanaveenk/MikeLegal/assets/71990959/9da67dc0-7375-47ed-8686-40fb475b5637)
