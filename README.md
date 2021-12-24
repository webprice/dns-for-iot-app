# dns-for-iot-app
windows client-side scrips and apps

the guide:
1. Point desired domain to these NS nameservers:

http://fra.rastem.com.ua

http://tor.rastem.com.ua

2. run a client-side script which will sent post requests(json format) to http://fra.rastem.com.ua/PATH with specific data.

3. The process:
   /register -for user registration
   /login - will give you a right token, that will expire in 28 days
   /add - for adding a domain to our database
   /check - check the account, see which domains already added under the account
   /delete - delete a domain from account and Database
   /update - update your domain IP address on the DNS servers, you might want to set this script as a cron job.
