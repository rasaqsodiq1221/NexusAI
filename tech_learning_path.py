import os
import base64
from dotenv import load_dotenv
import requests
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Set up Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
    exit()

genai.configure(api_key=api_key)

# Define tech interests
tech_interests = [
    "Web Development", 
    "Mobile App Development",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence",
    "Cybersecurity",
    "Cloud Computing",
    "DevOps",
    "Blockchain",
    "Internet of Things (IoT)"
    # ... (You can add more interests from the original list)
]

def get_coursera_access_token(app_key, app_secret):
    url = "https://api.coursera.com/oauth2/client_credentials/token"
    auth_string = f"{app_key}:{app_secret}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_auth}"
    }
    data = {"grant_type": "client_credentials"}
    
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.RequestException as e:
        print(f"Error obtaining Coursera access token: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Response content: {e.response.content}")
        return None

def get_coursera_courses(subject, access_token):
    url = "https://api.coursera.org/api/courses.v1"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"q": "search", "query": subject, "limit": 5, "fields": "name,slug"}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        courses = response.json().get("elements", [])
        return [{"name": course["name"], "url": f"https://www.coursera.org/learn/{course['slug']}"} for course in courses]
    except requests.RequestException as e:
        print(f"Error fetching Coursera courses: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Response content: {e.response.content}")
        return []

def get_ai_suggestions(interests):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""For someone interested in {', '.join(interests)}, please provide:

1. Overview:
   - Brief description of each selected technology
   - How these technologies relate to each other (if applicable)

2. Industry Trends:
   - Current trends in these fields
   - Emerging technologies or practices
   - Job market outlook

3. Advice:
   - Why these technologies are important
   - Potential challenges in learning these technologies
   - Tips for success in these fields

4. Personalized Learning Path:
   - Step-by-step guide to learning these technologies
   - Suggest a logical order for learning multiple technologies
   - Estimated time frame for each step
   - Key concepts to focus on for each technology
   - Suggested projects or practical applications to reinforce learning

5. Resources:
   - Types of courses or certifications that would be beneficial
   - Recommended books or online resources
   - Relevant communities or forums for support and networking

Please structure your response clearly with headers and bullet points for easy readability."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating AI suggestions: {str(e)}")
        return "Unable to generate AI suggestions at this time."

def main():
    print("Tech Learning Path Prompt System")
    print("--------------------------------")

    # Coursera API setup
    coursera_app_key = os.getenv("COURSERA_APP_KEY")
    coursera_app_secret = os.getenv("COURSERA_APP_SECRET")

    if not all([coursera_app_key, coursera_app_secret]):
        print("Coursera API credentials not found. Please set the COURSERA_APP_KEY and COURSERA_APP_SECRET environment variables.")
        exit()

    # Get Coursera access token
    coursera_access_token = get_coursera_access_token(coursera_app_key, coursera_app_secret)
    if not coursera_access_token:
        print("Failed to obtain Coursera access token.")
        exit()

    # User input
    print("Available tech interests:")
    for i, interest in enumerate(tech_interests, 1):
        print(f"{i}. {interest}")

    selected_indices = input("Enter the numbers of your interests (comma-separated): ").split(',')
    selected_interests = [tech_interests[int(i.strip()) - 1] for i in selected_indices if i.strip().isdigit() and 0 < int(i.strip()) <= len(tech_interests)]

    if selected_interests:
        print("\nGenerating personalized learning path...")
        
        # Get AI suggestions
        ai_suggestions = get_ai_suggestions(selected_interests)
        print("\nAI-Generated Learning Path:")
        print(ai_suggestions)

        # Get course recommendations
        print("\nRecommended Coursera Courses:")
        for interest in selected_interests:
            print(f"\nCourses for {interest}:")
            
            coursera_courses = get_coursera_courses(interest, coursera_access_token)
            if coursera_courses:
                for course in coursera_courses:
                    print(f"- {course['name']}")
                    print(f"  URL: {course['url']}")
            else:
                print("No courses found for this interest.")

    else:
        print("No valid interests selected.")

if __name__ == "__main__":
    main()