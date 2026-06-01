# Music Library Manager
# Uses: dictionaries, lists, tuples, sets, CSV

import csv

# --- Data Setup ---

# Dictionary — album info
albums = {
    "Thriller":        {"artist": "Michael Jackson", "year": 1982, "sales_millions": 65},
    "Back in Black":   {"artist": "AC/DC",           "year": 1980, "sales_millions": 50},
    "The Bodyguard":   {"artist": "Whitney Houston", "year": 1992, "sales_millions": 50},
}

# Tuple — fixed genre categories (immutable)
genres = ("Pop", "Rock", "R&B", "Hip Hop", "Jazz")

# List — user playlist (mutable, ordered)
playlist = ["Thriller", "Back in Black"]

# Set — favourite artists (unique only)
favourite_artists = {"Michael Jackson", "Whitney Houston", "AC/DC"}


# --- Functions ---

def show_albums():
    print("\n📀 Album Library:")
    for name, info in albums.items():
        print(f"  {name} — {info['artist']} ({info['year']}) | Sales: {info['sales_millions']}M")

def add_to_playlist(album):
    if album in albums:
        playlist.append(album)
        print(f"✅ '{album}' added to playlist.")
    else:
        print(f"❌ '{album}' not found in library.")

def show_playlist():
    print("\n🎵 Your Playlist:")
    for i, track in enumerate(playlist):
        print(f"  {i+1}. {track}")

def total_sales():
    total = sum(info["sales_millions"] for info in albums.values())
    print(f"\n💰 Total Sales: {total}M albums")

def add_favourite_artist(artist):
    favourite_artists.add(artist)
    print(f"⭐ '{artist}' added to favourites.")

def show_favourites():
    print("\n⭐ Favourite Artists:")
    for artist in favourite_artists:
        print(f"  - {artist}")

def save_to_csv():
    with open("albums.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["album", "artist", "year", "sales_millions"])
        writer.writeheader()
        for name, info in albums.items():
            writer.writerow({"album": name, **info})
    print("\n💾 Library saved to albums.csv")


# --- Run ---
show_albums()
add_to_playlist("The Bodyguard")
show_playlist()
total_sales()
add_favourite_artist("Beyoncé")
show_favourites()
save_to_csv()