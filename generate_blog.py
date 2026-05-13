import os
import openai
from datetime import datetime

# 1. Configuration
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
AFFILIATE_LINK = "https://get.spocket.co/lj4qn74mjd1o"

# 2. Topics to cycle through
TOPICS = [
    "Winning Dropshipping Products for Summer 2026",
    "How to find US-based suppliers for Shopify",
    "Scaling from 0 to $10k with Spocket automation",
    "Why 2-day shipping is mandatory for Ecommerce in 2026",
    "The best alternative to AliExpress for professional sellers"
]

def generate_content():
    today = datetime.now().strftime("%B %d, %Y")
    topic = TOPICS[int(datetime.now().day % len(TOPICS))]
    
    prompt = f"Write a 500-word SEO blog post about '{topic}'. Focus on why Spocket is the best solution. Use a professional, tech-focused tone. Do not use generic intros."
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    content = response.choices[0].message.content
    
    # 3. Create the HTML Block
    blog_html = f"""
    <div class="blog-post" style="margin-bottom: 4rem; border-bottom: 1px solid var(--border); padding-bottom: 2rem;">
        <div class="meta">{today} • Daily Insight</div>
        <h2 style="font-size: 2.5rem; margin: 1rem 0;">{topic}</h2>
        <div class="content" style="color: var(--muted); line-height: 1.8;">
            {content.replace('\n', '<br>')}
        </div>
        <a href="{AFFILIATE_LINK}" class="btn-main" style="margin-top: 1.5rem;">Try Spocket Free →</a>
    </div>
    """
    return blog_html

def update_index(new_html):
    with open("index.html", "r") as f:
        lines = f.readlines()

    # This inserts the new blog post right after a specific marker in your HTML
    with open("index.html", "w") as f:
        for line in lines:
            f.write(line)
            if "<!-- BLOG_START -->" in line:
                f.write(new_html)

if __name__ == "__main__":
    new_post = generate_content()
    update_index(new_post)
    print("Daily blog generated and injected.")
