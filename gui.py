
import tkinter as tk
import webbrowser
import requests

from io import BytesIO
from PIL import Image, ImageTk
from news_api import get_news, search_news

# ---------------- COLORS ----------------
BG = "#F4F2ED"
WHITE = "#FFFFFF"
BLACK = "#171717"
RED = "#C62828"
GREY = "#777777"
LINE = "#E0DED8"

# Keep image references alive
image_references = []

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("THE DAILY | News Magazine")
root.geometry("1250x850")
root.minsize(950, 650)
root.configure(bg=BG)

# ---------------- HEADER ----------------
topbar = tk.Frame(root, bg=BLACK, height=35)
topbar.pack(fill="x")
topbar.pack_propagate(False)

tk.Label(
    topbar,
    text="THE DAILY  |  INDEPENDENT NEWS & STORIES",
    bg=BLACK,
    fg=WHITE,
    font=("Arial", 9, "bold")
).pack(side="left", padx=25, pady=8)

tk.Label(
    topbar,
    text="YOUR DAILY EDITION",
    bg=BLACK,
    fg=WHITE,
    font=("Arial", 9)
).pack(side="right", padx=25)

# ---------------- MASTHEAD ----------------
masthead = tk.Frame(root, bg=BG)
masthead.pack(fill="x", pady=(18, 12))

tk.Label(
    masthead,
    text="THE DAILY",
    bg=BG,
    fg=BLACK,
    font=("Georgia", 34, "bold")
).pack()

tk.Label(
    masthead,
    text="NEWS THAT MATTERS. STORIES THAT INSPIRE.",
    bg=BG,
    fg=GREY,
    font=("Arial", 9, "bold")
).pack(pady=4)

tk.Frame(root, bg=BLACK, height=2).pack(
    fill="x", padx=30
)

# ---------------- NAVIGATION ----------------
nav = tk.Frame(root, bg=BG)
nav.pack(fill="x", padx=25, pady=10)

# ---------------- STATUS ----------------
status = tk.Label(
    root,
    text="Select a category to explore the latest news",
    bg=BG,
    fg=RED,
    font=("Arial", 10, "bold")
)
status.pack(anchor="w", padx=35, pady=5)

# ---------------- SEARCH BAR ----------------
search_frame = tk.Frame(root, bg=BG)
search_frame.pack(fill="x", padx=35, pady=10)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 13),
    width=45,
    bd=1,
    relief="solid"
)
search_entry.pack(side="left", ipady=8, padx=(0, 10))

search_entry.bind(
    "<Return>",
    lambda event: perform_search()
)

search_entry.insert(0, "Search news...")

search_button = tk.Button(
    search_frame,
    text="SEARCH",
    bg=RED,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=20,
    pady=9,
    cursor="hand2",
    command=lambda: perform_search()
)
search_button.pack(side="left")

# ---------------- SCROLLABLE CONTENT ----------------
container = tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True, padx=25, pady=10)

canvas = tk.Canvas(
    container,
    bg=BG,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    container,
    orient="vertical",
    command=canvas.yview
)

content = tk.Frame(canvas, bg=BG)

window_id = canvas.create_window(
    (0, 0),
    window=content,
    anchor="nw"
)

content.bind(
    "<Configure>",
    lambda event: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.bind(
    "<Configure>",
    lambda event: canvas.itemconfigure(
        window_id,
        width=event.width
    )
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# ---------------- LOAD IMAGE ----------------
def load_image(url, width, height):

    if not url:
        return None

    try:
        response = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()

        img = Image.open(
            BytesIO(response.content)
        ).convert("RGB")

        img = img.resize(
            (width, height),
            Image.Resampling.LANCZOS
        )

        return ImageTk.PhotoImage(img)

    except Exception:
        return None


# ---------------- OPEN ARTICLE ----------------
def open_article(url):

    if url:
        webbrowser.open(url)


# ---------------- FEATURED STORY ----------------
def create_featured(article):

    title = article.get("title") or "Headline unavailable"
    description = article.get("description") or "Read the full article for more details."
    source = article.get("source", {}).get("name") or "Unknown source"
    url = article.get("url")
    image_url = article.get("urlToImage")

    card = tk.Frame(
        content,
        bg=WHITE,
        padx=18,
        pady=18,
        highlightbackground=LINE,
        highlightthickness=1
    )

    card.pack(fill="x", pady=(5, 20))

    tk.Label(
        card,
        text="TOP STORY",
        bg=WHITE,
        fg=RED,
        font=("Arial", 10, "bold")
    ).pack(anchor="w", pady=(0, 12))

    photo = load_image(image_url, 1000, 300)

    if photo:
        image_label = tk.Label(card, image=photo, bg=WHITE)
        image_label.image = photo
        image_references.append(photo)
        image_label.pack(fill="x", pady=(0, 15))
    else:
        tk.Label(
            card,
            text="FEATURED NEWS",
            bg="#E8E5DE",
            fg=GREY,
            height=8,
            font=("Georgia", 20, "bold")
        ).pack(fill="x", pady=(0, 15))

    tk.Label(
        card,
        text=title,
        bg=WHITE,
        fg=BLACK,
        font=("Georgia", 24, "bold"),
        wraplength=950,
        justify="left"
    ).pack(anchor="w", pady=5)

    tk.Label(
        card,
        text=f"By {source}",
        bg=WHITE,
        fg=RED,
        font=("Arial", 10, "bold")
    ).pack(anchor="w", pady=5)

    tk.Label(
        card,
        text=description,
        bg=WHITE,
        fg=GREY,
        font=("Arial", 12),
        wraplength=950,
        justify="left"
    ).pack(anchor="w", pady=8)

    tk.Button(
        card,
        text="READ FULL STORY  →",
        bg=BLACK,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=9,
        cursor="hand2",
        command=lambda: open_article(url)
    ).pack(anchor="w", pady=8)


# ---------------- NEWS CARD ----------------
def create_news_card(article, parent):

    title = article.get("title") or "Headline unavailable"
    description = article.get("description") or "No description available."
    source = article.get("source", {}).get("name") or "Unknown source"
    url = article.get("url")
    image_url = article.get("urlToImage")

    card = tk.Frame(
        parent,
        bg=WHITE,
        padx=12,
        pady=12,
        highlightbackground=LINE,
        highlightthickness=1
    )

    card.pack(fill="both", expand=True, padx=7, pady=7)

    photo = load_image(image_url, 450, 190)

    if photo:
        image_label = tk.Label(card, image=photo, bg=WHITE)
        image_label.image = photo
        image_references.append(photo)
        image_label.pack(fill="x", pady=(0, 10))
    else:
        tk.Label(
            card,
            text="NEWS",
            bg="#E8E5DE",
            fg=GREY,
            height=5,
            font=("Georgia", 16, "bold")
        ).pack(fill="x", pady=(0, 10))

    tk.Label(
        card,
        text=source.upper(),
        bg=WHITE,
        fg=RED,
        font=("Arial", 9, "bold")
    ).pack(anchor="w")

    tk.Label(
        card,
        text=title,
        bg=WHITE,
        fg=BLACK,
        font=("Georgia", 15, "bold"),
        wraplength=420,
        justify="left"
    ).pack(anchor="w", pady=8)

    tk.Label(
        card,
        text=description,
        bg=WHITE,
        fg=GREY,
        font=("Arial", 10),
        wraplength=420,
        justify="left"
    ).pack(anchor="w", pady=5)

    tk.Button(
        card,
        text="Read More →",
        bg=WHITE,
        fg=RED,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        command=lambda: open_article(url)
    ).pack(anchor="w", pady=8)

# ---------------- PERFORM SEARCH ----------------
def perform_search():

    keyword = search_entry.get().strip()

    if not keyword or keyword == "Search news...":
        status.config(text="Please enter a news topic to search.")
        return

    global image_references
    image_references = []

    for widget in content.winfo_children():
        widget.destroy()

    status.config(text=f"Searching news about '{keyword}'...")
    root.update_idletasks()

    articles = search_news(keyword)
    print("Search completed:", len(articles), "articles found")

    if not articles:
        status.config(text="No articles found. Try another keyword.")
        return

    status.config(
        text=f"{len(articles)} search results for '{keyword}'"
    )

    create_featured(articles[0])

    tk.Label(
        content,
        text="SEARCH RESULTS",
        bg=BG,
        fg=BLACK,
        font=("Arial", 16, "bold")
    ).pack(anchor="w", pady=10)

    grid = tk.Frame(content, bg=BG)
    grid.pack(fill="both", expand=True)

    for index, article in enumerate(articles[1:]):

        row = index // 2
        column = index % 2

        grid.grid_columnconfigure(column, weight=1)

        card_holder = tk.Frame(grid, bg=BG)
        card_holder.grid(
            row=row,
            column=column,
            sticky="nsew"
        )

        create_news_card(article, card_holder)

# ---------------- DISPLAY NEWS ----------------
def show_news(category):

    global image_references

    image_references = []

    for widget in content.winfo_children():
        widget.destroy()

    status.config(
        text=f"Loading {category.title()} news..."
    )

    root.update_idletasks()

    articles = get_news(category)

    if not articles:
        status.config(text="No news found. Please try again.")
        return

    status.config(
        text=f"{len(articles)} articles available | {category.title()}"
    )

    # First article is featured
    create_featured(articles[0])

    # Remaining articles
    tk.Label(
        content,
        text="LATEST STORIES",
        bg=BG,
        fg=BLACK,
        font=("Arial", 16, "bold")
    ).pack(anchor="w", pady=10)

    grid = tk.Frame(content, bg=BG)
    grid.pack(fill="both", expand=True)

    for index, article in enumerate(articles[1:]):

        row = index // 2
        column = index % 2

        grid.grid_columnconfigure(column, weight=1)

        card_holder = tk.Frame(grid, bg=BG)
        card_holder.grid(
            row=row,
            column=column,
            sticky="nsew"
        )

        create_news_card(article, card_holder)


# ---------------- CATEGORY BUTTONS ----------------
categories = [
    ("HOME", "technology"),
    ("TECHNOLOGY", "technology"),
    ("BUSINESS", "business"),
    ("SPORTS", "sports")
]

for label, category in categories:

    tk.Button(
        nav,
        text=label,
        bg=BG,
        fg=BLACK,
        font=("Arial", 10, "bold"),
        relief="flat",
        activeforeground=RED,
        cursor="hand2",
        command=lambda c=category: show_news(c)
    ).pack(side="left", padx=12)


# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="THE DAILY  •  YOUR WORLD, YOUR NEWS",
    bg=BLACK,
    fg=WHITE,
    font=("Arial", 9),
    pady=10
)
footer.pack(fill="x")

# ---------------- START APP ----------------
show_news("technology")

root.mainloop()
