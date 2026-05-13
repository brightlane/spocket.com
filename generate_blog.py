import os
from datetime import datetime

AFFILIATE_LINK = "https://get.spocket.co/lj4qn74mjd1o"

# 2. Your Pre-Written Authority Content Bank
# Add as many as you want here. The script cycles through them by day.
CONTENT_BANK = [
    {
        "topic": "Why US-Based Suppliers are Winning in 2026",
        "content": "Shipping speed has become the #1 conversion factor. By switching from overseas suppliers to Spocket's US-vetted network, merchants are seeing a 40% increase in repeat customers. Local shipping reduces the 'anxiety window' for buyers."
    },
    {
        "topic": "The Death of 30-Day Shipping",
        "content": "In 2026, customers expect Amazon-level speed. If your dropshipping store takes 3 weeks to deliver, your brand is effectively dead on arrival. Spocket allows for 2-7 day delivery, making your store competitive with major retailers."
    },
    {
        "topic": "Automating Your High-Ticket Dropshipping Store",
        "content": "Manual order fulfillment is a bottleneck. High-scale sellers use Spocket to automate inventory sync and order processing. This allows you to focus on marketing and conversion rate optimization rather than logistics."
    }
]

def generate_html_block():
    today = datetime.now().strftime("%B %d, %Y")
    # This selects a post based on the day of the month so it's always "new"
    post_index = int(datetime.now().day % len(CONTENT_BANK))
    post = CONTENT_BANK[post_index]
    
    blog_html = f"""
    <div class="blog-post">
        <div class="blog-meta">{today} • Strategy Update</div>
        <h2 style="font-size: 2.5rem; margin: 1rem 0;">{post['topic']}</h2>
        <div class="blog-content">
            {post['content']}
        </div>
        <a href="{AFFILIATE_LINK}" class="btn-main" style="margin-top: 1.5rem;">Access These Suppliers →</a>
    </div>
    """
    return blog_html

def update_index(new_html):
    if not os.path.exists("index.html"):
        print("Error: index.html not found.")
        return

    with open("index.html", "r") as f:
        content = f.read()

    # Avoid duplicate posting if it ran today already
    if f"{datetime.now().strftime('%B %d, %Y')}" in content:
        print("Today's post is already live.")
        return

    # Injects the post after the BLOG_START comment
    updated_content = content.replace("<!-- BLOG_START -->", f"<!-- BLOG_START -->\n{new_html}")

    with open("index.html", "w") as f:
        f.write(updated_content)

if __name__ == "__main__":
    new_post_html = generate_html_block()
    update_index(new_post_html)
    print("Static blog post injected successfully.")
