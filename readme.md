## Inspiration
This project was originally inspired by a similar project, [Sherlock](https://github.com/sherlock-project/sherlock), which is a command line based tool that "hunt[s] down social media accounts by username across social networks". I was interested in this concept and the overall idea of using the immense amount of data available on the internet. However, instead of just looking for whether an account existed or not, I also wanted to show various other data on the account depending on which platform the account was on. 

## What it does
The final product is a website that takes the user's inputted username and searches various popular websites for accounts that match that username and then displays various metadata about each of the accounts associated with that username. Currently, it support searching for accounts on Instagram, Reddit, Stack Overflow, Twitter, Twitch and Youtube.

## How it was built
### Backend
The backend of the website is written in Python using the Flask framework. When a user sends a request to the backend, it uses a patchwork of different methods ranging from webscraping to official APIs to search popular websites for accounts with the provided username.

### Frontend
The frontend of our website is written in Typescript using the Next.JS framework and Tailwind and blocks.css as UI libraries. It accepts user input and displays the accounts that the server finds. Since the metadata associated with the account is different depending on which platform the account is associated with, the frontend also contains an algorithm to automatically identify what type of value a given metadata field holds. For example, it can identify URLs and format them as links as opposed to plaintext and also can guess when a number actually represents a UNIX timestamp and format it accordingly.

## What's next for Where Am I Online?
The most clear next step for this project is to continue to add to the number of websites supported so this tool can provide a more comprehensive image of a user's online data footprint.
