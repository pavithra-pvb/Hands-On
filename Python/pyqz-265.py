def get_trend_post(trending):
    if not trending:
        return "Hello, Sam!!!"
    elif "sam" not in trending.lower():
        return "Greetings, OpenAI!"
    else:
        return "OpenAI is screwed."
    
trending = "Sam lost his job"
print(get_trend_post(trending))

"""
Ans:
A) Hello, Sam!!!
B) Greetings, OpenAI!
C) OpenAI is screwed - Ans
D) Error

"""