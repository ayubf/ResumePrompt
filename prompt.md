__CONTEXT__

My name is Ayub Farah, I'm a student at the University of Houston, pursuing a Bachelor of Science in Mathematics with a minor in Computer Science and set to graduate May 2026. I'm planning on becoming a full-time Software Engineer after I graduate, and I'm currently applying for Software Engineer 1, Junior Software Engineer, Associate Software Engineer, New Grad Software Engineer, and similarly titled roles.

My skillset includes programming languages like Python, TypeScript, Go, Ruby and Kotlin, and web-frameworks like
Flask, Express.js, Ruby on Rails, and more. I've worked with React, and I have experience with AWS. I've used databases like MongoDB, Postgres, MySQL and SQLite.

I gained my skills and experience from personal projects and 3 internship experiences I will describe below. 

My first internship was as a Software Development Engineering Intern at Amazon Web Services, in Santa Clara, CA from 06/05/2023 to 08/25/2023. I worked on a team called AWS Cleanrooms ML. My project was to create an interface for situations where our on-call engineers had to troubleshoot issues in our service from clients. The old process was something like this: a client makes a call, an on-call engineer picks up, and the client gives their ARN. Then the engineer would have to manuever through many different AWS accounts to finally track down the resources our serivce was running under that client's ARN to begin troubleshooting. What my interface did was you gave it an ARN, and it would pull information on the relevant resources. It reduced the time to start troubleshooting from something like 2 minutes to 10-15 seconds. This interface was written in TypeScript with React, I wrote some AWS Lambda functions for it (in Python), and also I had to create some roles and manage access with AWS IAM. Also as a part of my internship, I did work on the team's ticket management system, enhancing collaboration and ticket status updating features.

My second internship was as a Software Development Engineering Intern at Amazon Web Services, in Santa Clara, CA from 05/28/2024 to 08/16/2024. I worked on the same team, AWS Cleanrooms ML. My project this time around was a part of a new release for the service. Essentially, our service sat on top of AWS Cleanrooms, a service where advertisers and publishers could collaborate via cleanrooms. My team's work was supplying ML features for the platform so in the cleanrooms users could run inferences. My project was focused on the scenario when an advertiser or publisher leaves a cleanroom, what we do with our resources (i.e., delete them, mark them for deletion, etc). I did a lot of work with AWS CDK, and I wrote unit tests and integration tests for the new infra. I then wrote AWS Lambda functions in Kotlin, tested them, wrote proxies and modules. Finally, a good amount of my work naturally crossed over with the work of the Cleanrooms team, so I wrote code in their codebases so our services could communicate on resource deletion status among other things via AWS DDB Streams, AWS SQS, and AWS SNS.

My third internship was as a Software Engineering Intern at Cisco Meraki, in San Francisco, CA from 05/27/2025 to 08/16/2025. At Cisco Meraki, my project was to add a feature to our dashboard for users to be able to search firewall rules on their organization based on attributes like source IP, destination IP, port, protocol, etc. The frontend I wrote in TypeScript with React and Redux, and the backend code was written in Ruby with Ruby on Rails. I also wrote unit tests and integration tests. As a stretch goal, I also added a feature where users would give natural language input into a new field and then we use OpenAI's ChatGPT API to fill in the remaining fields in the search form.

I also have a summer experience with Google, where I did an online summer program called the Google CSSI. Here are the bullet points: 

• Participated in a 4-week intensive computer science summer program for high-achieving students.

• Completed an introductory project-based HTML/CSS and JavaScript curriculum taught by Google engineers.

• Attended product design, resume development, and software engineering interview workshops.

• Delivered a collaborative final project presentation that included a live demonstration to Google employees and
community leaders.

I have a few projects on my github: https://github.com/ayubf

Here's my shortlist:

1. Turms: https://github.com/ayubf/turms. I wrote this in Go, TypeScript. It's a full stack app where you create
"rooms" where users can chat but the rooms are temporary (given a time limit during creation) and the link is shareable. MongoDB as a database, React on the frontend Implemented secure user session management with encrypted JWTs

2. Wink: https://github.com/ayubf/Wink. I wrote this fully in TypeScript with React on the frontend and Express.js in the backend, along with MongoDB as a database. Simple social media clone. Support for account creation, profile and settings editing, signing in / out, deleting accounts, creating posts, viewing posts through a feed. 

3. Anomalies in Public Transit Ridership: https://anomalies-in-public-transit-ridership.streamlit.app/. I wrote this in Python with Streamlit, Numpy, Pandas, Matplotlib. Essentially an investigation of anomalies in public transit ridership between 2020-2025 for New York City, Washington D.C. and Chicago given events like holidays, the COVID-19 pandemic etc. My conclusions include that the COVID-19 dropped NYC transit ridership more sharply than Washington D.C and Chicago, who were very close to each other in ridership, also that among the holidays, Christmas drops ridership more on average, and among the cities, Chicago sees the highest drops in ridership. 


{contact_info}

__ASK__ 

Create a resume for me given my situation and goals. 


__CONSTRAINTS__

- Response must be a valid .tex file

- Must use Jake's Resume template or similar

- Prioritize relevance: Include only experiences, projects, and skills that directly support the target role. Remove anything outdated, irrelevant, or low-impact.

- Outcome-focused: Each bullet must highlight measurable results or impact (metrics, improvements, efficiencies, revenue, scale). Avoid task-only descriptions.

- Readability first: Use short bullets, clean formatting, and scannable structure. Avoid dense paragraphs.

- Technical accuracy: All technologies, tools, and accomplishments must be truthful and correct.

- Strong signal-to-noise ratio: Maximize meaningful information per line; eliminate filler, clichés, and generic claims.

- Role-aligned narrative: Convey a coherent story tailored to the job description, showing career progression and relevant expertise.

- One-page target: Keep to one page unless you have over 10 years of experience.

- Avoid repetition: Do not restate the same skills, projects, or achievements across sections.

- ATS-compatible: Use standard section headers, simple formatting, no images or complex tables that break parsing.

- Use industry-standard wording: Keywords and phrasing should align with modern hiring expectations in software engineering.

__STYLE__

- In the project section headers, list technologies used like this for example:
```
Project Name | Technology A, Technology B, ...
```
- No links in the project headers or bullet points

- In the project section bullet points, mention the goals, purpose, and outcomes only. 

- Crisp, clear, confident tone: Direct, strong statements with no exaggeration or fluff.

- Begin bullets with strong action verbs (“Built,” “Designed,” “Optimized,” “Deployed,” “Refactored,” “Led”).

- Quantify wherever possible: Include numbers, percentages, scale, speedups, savings, or user counts.

- Problem → Action → Outcome structure: Each bullet should follow this logical progression. Be clear about impact and purpose

- Consistent formatting: Maintain the same tense, bullet style, and spacing throughout.

- Focus on personal accomplishments: Highlight individual contributions, not just team efforts, unless relevant.

- Show initiative and ownership: Demonstrate leadership, decision-making, and autonomy.

- Prefer specificity over generality: Detail concrete results rather than vague improvements.

- Modern, industry-aligned language: Use terminology and phrasing expected by engineering managers and recruiters in 2025.

- Clarity over cleverness: Make every bullet instantly understandable to a skim-reader.


__EXAMPLES__

For this example, consider only the structure not the specific content of the resume:

```tex
%-------------------------
% Resume in Latex
% Author : Jake Gutierrez
% Based off of: https://github.com/sb2nov/resume
% License : MIT
%------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%----------HEADING----------
% \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
%   \textbf{\href{http://sourabhbajaj.com/}{\Large Sourabh Bajaj}} & Email : \href{mailto:sourabh@sourabhbajaj.com}{sourabh@sourabhbajaj.com}\\
%   \href{http://sourabhbajaj.com/}{http://www.sourabhbajaj.com} & Mobile : +1-123-456-7890 \\
% \end{tabular*}

\begin{center}
    \textbf{\Huge \scshape Jake Ryan} \\ \vspace{1pt}
    \small 123-456-7890 $|$ \href{mailto:x@x.com}{\underline{jake@su.edu}} $|$ 
    \href{https://linkedin.com/in/...}{\underline{linkedin.com/in/jake}} $|$
    \href{https://github.com/...}{\underline{github.com/jake}}
\end{center}


%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Southwestern University}{Georgetown, TX}
      {Bachelor of Arts in Computer Science, Minor in Business}{Aug. 2018 -- May 2021}
    \resumeSubheading
      {Blinn College}{Bryan, TX}
      {Associate's in Liberal Arts}{Aug. 2014 -- May 2018}
  \resumeSubHeadingListEnd


%-----------EXPERIENCE-----------
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {Undergraduate Research Assistant}{June 2020 -- Present}
      {Texas A\&M University}{College Station, TX}
      \resumeItemListStart
        \resumeItem{Developed a REST API using FastAPI and PostgreSQL to store data from learning management systems}
        \resumeItem{Developed a full-stack web application using Flask, React, PostgreSQL and Docker to analyze GitHub data}
        \resumeItem{Explored ways to visualize GitHub collaboration in a classroom setting}
      \resumeItemListEnd
      
% -----------Multiple Positions Heading-----------
%    \resumeSubSubheading
%     {Software Engineer I}{Oct 2014 - Sep 2016}
%     \resumeItemListStart
%        \resumeItem{Apache Beam}
%          {Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines}
%     \resumeItemListEnd
%    \resumeSubHeadingListEnd
%-------------------------------------------

    \resumeSubheading
      {Information Technology Support Specialist}{Sep. 2018 -- Present}
      {Southwestern University}{Georgetown, TX}
      \resumeItemListStart
        \resumeItem{Communicate with managers to set up campus computers used on campus}
        \resumeItem{Assess and troubleshoot computer problems brought by students, faculty and staff}
        \resumeItem{Maintain upkeep of computers, classroom equipment, and 200 printers across campus}
    \resumeItemListEnd

    \resumeSubheading
      {Artificial Intelligence Research Assistant}{May 2019 -- July 2019}
      {Southwestern University}{Georgetown, TX}
      \resumeItemListStart
        \resumeItem{Explored methods to generate video game dungeons based off of \emph{The Legend of Zelda}}
        \resumeItem{Developed a game in Java to test the generated dungeons}
        \resumeItem{Contributed 50K+ lines of code to an established codebase via Git}
        \resumeItem{Conducted  a human subject study to determine which video game dungeon generation technique is enjoyable}
        \resumeItem{Wrote an 8-page paper and gave multiple presentations on-campus}
        \resumeItem{Presented virtually to the World Conference on Computational Intelligence}
      \resumeItemListEnd

  \resumeSubHeadingListEnd


%-----------PROJECTS-----------
\section{Projects}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{Gitlytics} $|$ \emph{Python, Flask, React, PostgreSQL, Docker}}{June 2020 -- Present}
          \resumeItemListStart
            \resumeItem{Developed a full-stack web application using with Flask serving a REST API with React as the frontend}
            \resumeItem{Implemented GitHub OAuth to get data from user’s repositories}
            \resumeItem{Visualized GitHub data to show collaboration}
            \resumeItem{Used Celery and Redis for asynchronous tasks}
          \resumeItemListEnd
      \resumeProjectHeading
          {\textbf{Simple Paintball} $|$ \emph{Spigot API, Java, Maven, TravisCI, Git}}{May 2018 -- May 2020}
          \resumeItemListStart
            \resumeItem{Developed a Minecraft server plugin to entertain kids during free time for a previous job}
            \resumeItem{Published plugin to websites gaining 2K+ downloads and an average 4.5/5-star review}
            \resumeItem{Implemented continuous delivery using TravisCI to build the plugin upon new a release}
            \resumeItem{Collaborated with Minecraft server administrators to suggest features and get feedback about the plugin}
          \resumeItemListEnd
    \resumeSubHeadingListEnd



%
%-----------PROGRAMMING SKILLS-----------
\section{Technical Skills}
 \begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
     \textbf{Languages}{: Java, Python, C/C++, SQL (Postgres), JavaScript, HTML/CSS, R} \\
     \textbf{Frameworks}{: React, Node.js, Flask, JUnit, WordPress, Material-UI, FastAPI} \\
     \textbf{Developer Tools}{: Git, Docker, TravisCI, Google Cloud Platform, VS Code, Visual Studio, PyCharm, IntelliJ, Eclipse} \\
     \textbf{Libraries}{: pandas, NumPy, Matplotlib}
    }}
 \end{itemize}


%-------------------------------------------
\end{document}
```

For these examples, focus on the structure and language, and remember to include my details in my resume, from the context section, and not from any of these examples below

```tex
%-------------------------
% Resume in Latex
% Author : Sourabh Bajaj
% Website: https://github.com/sb2nov/resume
% License : MIT
%------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[pdftex]{hyperref}
\usepackage{fancyhdr}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.375in}
\addtolength{\evensidemargin}{-0.375in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

%-------------------------
% Custom commands
\newcommand{\resumeItem}[2]{
  \item\small{
    \textbf{#1}{: #2 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-1pt}\item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-5pt}
}

\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}

\renewcommand{\labelitemii}{$\circ$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%----------HEADING-----------------
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
  \textbf{\href{http://sourabhbajaj.com/}{\Large Sourabh Bajaj}} & Email : \href{mailto:sourabh@sourabhbajaj.com}{mail@website.com}\\
  \href{http://sourabhbajaj.com/}{http://www.sourabhbajaj.com} & Mobile : +1-123-456-7890 \\
\end{tabular*}


%-----------EDUCATION-----------------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Georgia Institute of Technology}{Atlanta, GA}
      {Master of Science in Computer Science;  GPA: 4.00}{Aug. 2012 -- Dec. 2013}
    \resumeSubheading
      {Birla Institute of Technology and Science}{Pilani, India}
      {Bachelor of Engineering in Electrical and Electronics;  GPA: 3.66 (9.15/10.0)}{Aug. 2008 -- July. 2012}
  \resumeSubHeadingListEnd


%-----------EXPERIENCE-----------------
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {Google}{Mountain View, CA}
      {Software Engineer}{Oct 2016 - Present}
      \resumeItemListStart
        \resumeItem{Tensorflow}
          {TensorFlow is an open source software library for numerical computation using data flow graphs; primarily used for training deep learning models.}
        \resumeItem{Apache Beam}
          {Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines, as well as a set of language-specific SDKs for constructing pipelines and runners.}
      \resumeItemListEnd

    \resumeSubheading
      {Coursera}{Mountain View, CA}
      {Senior Software Engineer}{Jan 2014 - Oct 2016}
      \resumeItemListStart
        \resumeItem{Notifications}
          {Service for sending email, push and in-app notifications. Involved in features such as delivery time optimization, tracking, queuing and A/B testing. Built an internal app to run batch campaigns for marketing etc.}
        \resumeItem{Nostos}
          {Bulk data processing and injection service from Hadoop to Cassandra and provides a thin REST layer on top for serving offline computed data online.}
        \resumeItem{Workflows}
          {Dataduct an open source workflow framework to create and manage data pipelines leveraging reusables patterns to expedite developer productivity.}
        \resumeItem{Data Collection}
          {Designed the internal survey and crowd sourcing platfowm which allowed for creating various tasks for crowd sourding or embedding surveys across the Coursera platform.}
        \resumeItem{Dev Environment}
          {Analytics environment based on docker and AWS, standardized the python and R dependencies. Wrote the core libraries that are shared by all data scientists.}
        \resumeItem{Data Warehousing}
          {Setup, schema design and management of Amazon Redshift. Built an internal app for access to the data using a web interface. Dataduct integration for daily ETL injection into Redshift.}
        \resumeItem{Recommendations}
          {Core service for all recommendation systems at Coursesa, currently used on the homepage and throughout the content discovery process. Worked on both offline training and online serving.}
        \resumeItem{Content Discovery}
          {Improved content discovery by building a new onboarding experience on coursera. Using this to personalize the search and browse experience. Also worked on ranking and indexing improvements.}
        \resumeItem{Course Dashboards}
          {Instructor dashboards and learner surveying tools, which helped instructors run their class better by providing data on Assignments and Learner Activity.}
      \resumeItemListEnd

    \resumeSubheading
      {Lucena Research}{Atlanta, GA}
      {Data Scientist}{Summer 2012 and 2013}
      \resumeItemListStart
        \resumeItem{Portfolio Management}
          {Created models for portfolio hedging,  portfolio optimization and price forecasting. Also creating a strategy backtesting engine used for simulating and backtesting strategies.}
        \resumeItem{QuantDesk}
          {Python backend for a web application used by hedge fund managers for portfolio management.}
      \resumeItemListEnd

  \resumeSubHeadingListEnd


%-----------PROJECTS-----------------
\section{Projects}
  \resumeSubHeadingListStart
    \resumeSubItem{QuantSoftware Toolkit}
      {Open source python library for financial data analysis and machine learning for finance.}
    \resumeSubItem{Github Visualization}
      {Data Visualization of Git Log data using D3 to analyze project trends over time.}
    \resumeSubItem{Recommendation System}
      {Music and Movie recommender systems using collaborative filtering on public datasets.}
%     \resumeSubItem{Mac Setup}
%       {Book that gives step by step instructions on setting up developer environment on Mac OS.}
  \resumeSubHeadingListEnd

%
%--------PROGRAMMING SKILLS------------
\section{Programming Skills}
 \resumeSubHeadingListStart
   \item{
     \textbf{Languages}{: Scala, Python, Javascript, C++, SQL, Java}
     \hfill
     \textbf{Technologies}{: AWS, Play, React, Kafka, GCE}
   }
 \resumeSubHeadingListEnd


%-------------------------------------------
\end{document}
```

https://imgur.com/a/3B5FT7o
https://github.com/Talal916/Resume/blob/master/Talal%20Jawaid%20CS%20Engineer.pdf
https://imgur.com/5UJf5m2
https://imgur.com/a/Tu3oLpR
https://imgur.com/jtUlNME
https://imgur.com/ShyZ4Sr
https://drive.google.com/file/d/1EsK8SSB0cHePe4sb0ZjhnQvvXlHUJLo4/view
https://imgur.com/jip7WER
https://drive.google.com/file/d/1ogQ3EcGIQqjrLdq-TIlX416FSmXNtcdb/view

Here are some well-made examples/partial examples who's structure and content you can copy

```tex

    \resumeSubheading
      {Amazon Web Services}{Santa Clara, CA}
      {Software Development Engineering Intern}{Jun 2023 -- Aug 2023}
      \resumeItemListStart
        \resumeItem{Designed and built a troubleshooting interface using TypeScript and React for AWS Cleanrooms ML on-call engineers, reducing troubleshooting initiation time by 90\% (from 2 minutes to 10-15 seconds).}
        \resumeItem{Developed AWS Lambda functions (in Python) to retrieve resource information based on ARN, streamlining the troubleshooting process.}
        \resumeItem{Implemented AWS IAM roles and access management for secure and controlled access to resources.}
        \resumeItem{Enhanced the team's ticket management system, improving collaboration and ticket status tracking.}
      \resumeItemListEnd

    \resumeSubheading
      {Amazon Web Services}{Santa Clara, CA}
      {Software Development Engineering Intern}{Jun 2023 -- Aug 2023}
      \resumeItemListStart
        \resumeItem{Designed and built a troubleshooting interface using TypeScript and React for AWS Cleanrooms ML on-call engineers, reducing troubleshooting initiation time by 90\% (from 2 minutes to 10-15 seconds).}
        \resumeItem{Developed AWS Lambda functions (in Python) to retrieve resource information based on ARN, streamlining the troubleshooting process.}
        \resumeItem{Implemented AWS IAM roles and access management for secure and controlled access to resources.}
        \resumeItem{Enhanced the team's ticket management system, improving collaboration and ticket status tracking.}
      \resumeItemListEnd
```