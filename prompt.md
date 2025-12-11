__CONTEXT__

My name is Ayub Farah, I'm a student at the University of Houston, pursuing a Bachelor of Science in Mathematics with a minor in Computer Science and set to graduate May 2026. I'm planning on becoming a full-time Software Engineer after I graduate, and I'm currently applying for Software Engineer 1, Junior Software Engineer, Associate Software Engineer, New Grad Software Engineer, and similarly titled roles.

My skillset includes programming languages like Python, TypeScript, Go, Ruby and Kotlin, and web-frameworks like
Flask, Express.js, Ruby on Rails, and more. I've worked with React, and I have experience with AWS. I gained my skills and experience from personal projects and 3 internship experiences I will describe below. 

My first internship was as a Software Development Engineering Intern at Amazon Web Services, in Santa Clara, CA from 
06/05/2023 to 08/25/2023. I worked on a team called AWS Cleanrooms ML. My project was to create an interface for situations where our on-call engineers had to troubleshoot issues in our service from clients. The old process was something like this: a client makes a call, an on-call engineer picks up, and the client gives their ARN. Then the engineer would have to manuever through many different AWS accounts to finally track down the resources our serivce was running under that client's ARN to begin troubleshooting. What my interface did was you gave it an ARN, and it would pull information on the relevant resources. 
It reduced the time to start troubleshooting from something like 2 minutes to 10-15 seconds. This interface was written in TypeScript with React, I wrote some AWS Lambda functions for it (in Python), and also I had to create some roles and manage access with AWS IAM. Also as a part of my internship, I did work on the team's ticket management system, enhancing collaboration and ticket status updating features. 

My second internship was as a Software Development Engineering Intern at Amazon Web Services, in Santa Clara, CA from 
05/28/2024 to 08/16/2024. I worked on the same team, AWS Cleanrooms ML. My project this time around was a part of a new release for the service. Essentially, our service sat on top of AWS Cleanrooms, a service where advertisers and publishers
could collaborate via cleanrooms. My team's work was supplying ML features for the platform so in the cleanrooms users could run inferences. My project was focused on the scenario when an advertiser or publisher leaves a cleanroom, what we do with our resources (i.e., delete them, mark them for deletion, etc). I did a lot of work with AWS CDK, and I wrote unit tests and integration tests for the new infra. I then wrote AWS Lambda functions in Kotlin, tested them, wrote proxies and modules. Finally, a good amount of my work naturally crossed over with the work of the Cleanrooms team, so I wrote code in their codebases so our services could communicate on resource deletion status among other things via AWS DDB Streams, AWS SQS, and AWS SNS. 

My third internship was as a Software Engineering Intern at Cisco Meraki, in San Francisco, CA from 05/27/2025 to 08/16/2025. 
At Cisco Meraki, my project was to add a feature to our dashboard for users to be able to search firewall rules on their organization based on attributes like source IP, destination IP, port, protocol, etc. The frontend I wrote in TypeScript with React and Redux, and the backend code was written in Ruby with Ruby on Rails. I also wrote unit tests and integration tests. As a stretch goal, I also added a feature where users would give natural language input into a new field and then we use OpenAI's ChatGPT API to fill in the remaining fields in the search form. 

I also have a summer experience with Google, where I did an online summer program called the Google CSSI. Here are the bullet points: 

• Participated in a 4-week intensive computer science summer program for high-achieving students.

• Completed an introductory project-based HTML/CSS and JavaScript curriculum taught by Google engineers.

• Attended product design, resume development, and software engineering interview workshops.

• Delivered a collaborative final project presentation that included a live demonstration to Google employees and
community leaders.

I have a few projects on my github: https://github.com/ayubf

Here's my shortlist:

1. Turms: https://github.com/ayubf/turms. I wrote this in Go, TypeScript. It's a full stack app where you create
"rooms" where users can chat but the rooms are temporary (given a time limit during creation) and the link is shareable. MongoDB as a database, React on the frontend. 

2. Wink: https://github.com/ayubf/Wink. I wrote this fully in TypeScript with React on the frontend and Express.js in the backend, along with MongoDB as a database. Simple social media clone. Support for account creation, profile and settings editing, signing in / out, deleting accounts, creating posts, viewing posts through a feed. 

3. Anomalies in Public Transit Ridership: https://anomalies-in-public-transit-ridership.streamlit.app/. I wrote this in Python with Streamlit, Numpy, Pandas, Matplotlib. Essentially an investigation of anomalies in public transit ridership between 2020-2025 for New York City, Washington D.C. and Chicago given events like holidays, the COVID-19 pandemic etc. 


{contact_info}

__ASK__ 

Create a resume for me given my situation and goals. 


__CONTRAINTS__

__STYLE__

__EXAMPLES__