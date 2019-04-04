Problem Statement:

Find the Merge Candidates

Create Django Project,

Consider you have following contacts in your phonebook.
user1:{
 c1 : [p1, e1]
 c2 : [p2, e2]
 c3 : [p2, e3]
 c4 : [e3, p4]
 c5 : [e2, p5]
 c6 : [p3, e4, p6]
 c7 : [e4]
 c8 : [p6, e5]
}

all "c" are contacts, "p" are phone numbers, "e" are email addresses.
Each contact can have one or more phone numbers and emails each 
contact information is stored in a json format per contact like 
{{user1, c1:[p1, e1]}, {user1,c2:[p2, e2]}}
how you model this data is important, justify your choices in data modeling.
You have to find potential merge candidates (hint try using AGPL or some python goodness)
Use 2 databases in your django project, ('default' db has information about 'authentication') , fragment user data between the 2 DBs like have 4 user's data (user_id, phone_nos, emails) in DB1 and others in DB2
make sure you use some scheme to get to the right DB rather than looking up for users in both DBs, maybe use a cache or some kind of primary key format to denote the user and the DB on which its data is kept
create a simple UI in angular4-material which will show this nicely (make it mobile friendly if possible)
I should be able to add new users and add their contacts from UI after which i should see the merge suggestions. along with which DB the user's data is stored in
feel free to choose any DBs like mysql,mongodb,redis,etc and justify your choices
use restful calls
keep in mind how a end user will might use it.
Please mention the time complexity of the solution you come up with for finding merge candidates

Solution should contain list of potential merge candidates for that user

for example for above case solution would be:
user1_merge_suggestions : [ [c1], [c2, c3, c4, c5], [c6, c7, c8] ]


Please host it on any service (AWS,GCP,etc) of your choice (bonus points if it works nicely on mobile screens).

Let me know know how much time you will need for this.

Note: Please don't use any in-line CSS. Try to follow best practices.
