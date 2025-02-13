main.py
import requests

def ask_groq_api(question, api_url, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {"question": question}
    
    try:
        response = requests.post(api_url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("answer", "No answer found.")
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def main():
    api_url = "https://api.groq.example/v1/ask"  # Replace this with the real Groq endpoint
    api_key = "YOUR_API_KEY_HERE"

    while True:
        user_input = input("Enter your question (or 'quit' to exit): ")
        if user_input.strip().lower() == "quit":
            print("Exiting...")
            break
        
        answer = ask_groq_api(user_input, api_url, api_key)
        print(f"Groq API says: {answer}")

if __name__ == "__main__":
    main()