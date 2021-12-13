# Project 4 Documentation
## By: Nathan Noack

## Introduction
**[See working site here!](https://git-committed.netlify.app/)**\
Welcome to the Backend repo! This is a full-stack (React/Python/Masonite/Postgre SQL) app implementing CRUD functionality.\
**[See frontend repo here](https://github.com/underdoggum/gitcommitted_frontend)**


## Technologies Used
#### Core
 - HTML5
 - CSS3
 - JavaScript ES6
 - Python

#### Libraries / Techniques
 - React Routing
 - MaterialUI framework (mobile-first, responsive, trendy look & feel)
 - Frontend deployed with Netlify
 - Postgre SQL as the database
 - Masonite as the ORM framework


## Backend Route Table
| Path            | HTTP Verb | Purpose                                                   |
|:---------------:|:---------:|:---------------------------------------------------------:|
| /               | GET       | Show Masonite Welcome page                                |
| /timeblocks     | GET       | Fetch All timeblock categories                            |
| /timeblocks/@id | GET       | Show a single timeblock category                          |
| /timeblocks     | POST      | Create route (primarily for seeding timeblock categories) |
| /timeblocks/@id | PUT       | Update a specific timeblock category                      |
| /reminders      | GET       | Fetch All timeblock categories                            |
| /reminders/@id  | GET       | Show a single reminder                                    |
| /reminders      | POST      | Create a new reminder                                     |
| /timeblocks/@id | PUT       | Update a specific reminder                                |
| /timeblocks/@id | DELETE    | Delete a specific reminder                                |




## Challenges
 - Problem: I initially wanted to create user authentication, but found it too time-consuming to integrate before MVP project time. Maybe in the future... [Alex M.'s tutorial on Masonite user auth](https://dev.to/alexmercedcoder/how-to-create-an-one-to-many-relationship-with-auth-in-python-with-masonite-d17)


## Known Bugs
 - No known bugs at this time


## Extra Features for the Future:
 - Add user authentication
 - Reconfigure one-to-many relationship between timeblocks <--> reminders
 - Add additional models if it makes sense in the frontend (e.g. URLs)