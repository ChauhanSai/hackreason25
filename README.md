# WanderLogic
### 🎊 [HackReason 2025](https://devpost.com/software/team-ud086l/) 3rd place prized winner 🎊

## Inspiration 🧠
We were planning a Europe trip after our study abroad this summer, but we ran into difficulty organizing it and spent countless hours trying to make it work. This experience inspired us to create WanderLogic, a tool that uses automated reasoning to simplify the process of planning a trip, saving time and eliminating stress.

## What It Does ✈️
WanderLogic takes your budget, trip duration, and desired destinations to generate:  
- Possible travel routes.  
- Total estimated costs.  
- Detailed schedules, including flight days.

## How We Built It 🛠️
- **Logic Programming**: We used S(CASP) for automated reasoning to generate travel plans.  
- **Data Collection**: Python scripts scraped flight and hotel data using Google Flights Booking Options API and Google Hotels API on SerpAPI. This data formed the "facts" for S(CASP).  
- **Frontend**: React.js powers our user-friendly website interface.  
- **Integration**: Flask serves as the backend, with Axios handling communication between the frontend and backend.

## What We Learned 🧑‍🏫
- How to use **S(CASP)** for logic programming.  
- Leveraging **SerpAPI** to scrape travel data.  
- Integrating React with Python for a seamless user experience.

## Challenges We Faced 🏔️
- Learning and debugging a new language, **S(CASP)**.  
- Resolving issues while connecting the backend and frontend.  
- Managing and formatting complex travel data.

## What’s Next? ✨
- Expand WanderLogic to include additional travel modes (trains, buses).  
- Make the results sortable in different formamts
- Allow for more user customization by specifying dates of travel

WanderLogic is just the beginning of hassle-free travel planning! 🌍

Developed by: Allen Zheng (asz230001), Cheryl Wang (cxw230017), Sai Chauhan (skc230003)
