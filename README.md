# Tech Learning Path Generator

This project generates personalized tech learning paths using AI suggestions and recommends relevant Coursera courses.

## Setup Instructions

Follow these steps to set up and run the project on your local machine:

1. **Fork the repository**
   - Visit the GitHub page of this repository: https://github.com/rasaqsodiq1221/NexusAI.git
   - Click the "Fork" button in the top-right corner to create a copy in your GitHub account

2. **Clone your forked repository**
`git clone https://github.com/your-github-username/your-repo-name.git`
- change the directory to your repo
`cd your-repo-name`

*Note: Replace `your-github-username` with your actual GitHub username*


3. **Set up a virtual environment** 
`python -m venv venv`
- then
`venv\Scripts\activate`

5. **Install required packages**
`pip install -r requirements.txt`

6. **Set up API keys**
   - Create a `.env` file in the project root directory
   - Add your API keys to the `.env` file:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     COURSERA_APP_KEY=your_coursera_app_key
     COURSERA_APP_SECRET=your_coursera_app_secret
     ```
   - Replace `your_gemini_api_key`, `your_coursera_app_key`, and `your_coursera_app_secret` with your actual API keys

7. **How to obtain API keys**
   - For Gemini API:
     - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
     - Create or select a project
     - Click on "Create API Key" and copy the generated key
   - For Coursera API:
     - Visit [Coursera Developers](https://dev.coursera.com/get-started)
     - Click the Sign In button in the upper-right corner.
     - Once redirected, log in to your account at www.coursera.org and click Login With SAML.
     - If logged in on www.coursera.org, you should see the terms and conditions page.
     - You should be briefly directed to www.coursera.org and then back to the portal, with your email address shown in the upper-right corner.
     - Note: If the top-right still shows "Sign in" after logging in via SAML, click the Sign In button again. it's a bug
     - Click your email address in the upper-right corner and choose Apps from the dropdown.
     - Click +New App in the top-right corner of the "Apps" page.
     - Add a name and description for the new app.
     - Choose one or more APIs in the APIs section and click Enable to activate them for your application.
     - Click Save; you'll see "App created" and will be redirected to your app's page containing the API key and secret credentials.
     - To view an API key or secret, click the Show button in the Credentials section.

8. **Run the program**
`python tech_learning_path.py`

1. **Follow the prompts**
   - The program will display a list of tech interests
   - Enter the numbers of your interests (comma-separated)
   - The program will generate a personalized learning path and recommend Coursera courses



## Keeping Your Fork Updated

To keep your fork updated with the original repository:

1. Add the original repository as an upstream remote:
`git remote add upstream https://github.com/rasaqsodiq1221/NexusAI.git`

3. Fetch the latest changes from the upstream repository:
`git fetch upstream`

4. Merge the changes into your local main branch:
`git checkout main`
- then
`git merge upstream/main`

6. Push the updated main branch to your fork:
`git push origin main`





## Contributing

If you'd like to contribute to this project:

1. "Create a new branch for your feature or bug fix"

- This means that instead of making changes directly on the main branch, you create a separate branch for your specific contribution.
- For example: `git checkout -b fix-login-bug` or `git checkout -b add-new-feature`


2. "Make your changes and commit them with a clear commit message"

- This is where you actually make your code changes.
- After making changes, you stage them (`git add .`) and commit them (`git commit -m "Clear description of your changes"`)


3. "Push your branch to your fork on GitHub"

- This step uploads your new branch with its changes to your forked repository on GitHub.
- You'd use a command like: `git push origin fix-login-bug`


4. "Open a pull request from your branch to the original repository"

- A pull request (PR) is a way to propose your changes to the original project.
- You do this on the GitHub website. There's usually a prompt after you push a new branch.
- This allows the project maintainers to review your changes before deciding to merge them into the main project.



## Troubleshooting

- If you encounter any issues related to missing packages, ensure you've activated your virtual environment and installed all requirements.
- If you see API-related errors, double-check that your `.env` file is set up correctly with valid API keys.


