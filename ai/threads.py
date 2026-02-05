import openai

def generate_thread(topic, niche, region):
    prompt = f"""
Create a viral X thread (1/🧵 format)
Topic: {topic}
Niche: {niche}
Region: {region}

Rules:
- 5 tweets max
- First tweet = hook
- Short lines
- No emojis spam
"""

    r = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.85
    )

    return r.choices[0].message.content.split("\n\n")
