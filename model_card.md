# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

This recommender suggests the top 5 songs from a small catalog based on user taste settings.
It is designed for classroom exploration and learning how recommendation logic works.
It assumes a user can be represented by favorite genre, favorite mood, and target energy.

Intended use: simple demos, class experiments, and basic profile testing.
Non-intended use: real music apps, high-stakes decisions, or personalized recommendations for large and diverse audiences.

---

## 3. How the Model Works

Each song gets points based on how well it matches the user profile.
The model gives +1 if genre matches and +1 if mood matches.
It also gives up to +4 for energy closeness, so songs near the target energy score much higher.
After scoring all songs, it sorts them from highest to lowest and returns the top 5.
Compared to the starter setup, I changed the weights to make energy more important and genre less important.

---

## 4. Data

The dataset has 18 songs in `data/songs.csv`.
Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness.
Genres and moods are mixed, but the catalog is very small and uneven.
Some genres appear once, while lofi appears multiple times.
I did not add or remove rows during this checkpoint.
The data misses many music styles and does not capture lyrics, culture, or context.

---

## 5. Strengths

The system works well for users with clear energy preferences.
High-energy profiles get fast and intense songs, while low-energy profiles shift to calmer tracks.
The recommendations are easy to explain because the scoring is transparent.
This makes it useful for learning and debugging recommender behavior.

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

One weakness is that the current scoring can create an energy-based filter bubble, especially after increasing the energy weight in the sensitivity experiment. Songs with similar energy values repeatedly dominate the top results, even when the mood signal conflicts with user intent (for example, high-energy plus sad profiles still surface mostly hype tracks). This can under-serve users with mixed or nuanced tastes because the linear energy-gap formula is strong and always active for every song. The system also ignores `likes_acoustic`, so users who care about acoustic texture are not represented in ranking decisions.

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Adversarial Conflict (High Energy + Sad), and Edge Case (Unknown Genre + Very Low Energy). For each profile, I ran the system and reviewed the top 5 songs to see whether the results matched the requested vibe. I also ran a sensitivity experiment by changing the weights so energy mattered more and genre mattered less, then compared how the top 5 changed. The biggest surprise was how often "Gym Hero" stayed near the top for multiple high-energy users, even when their mood request was different. In plain terms, this happens because the model rewards energy similarity very strongly, so a very energetic pop song can keep winning even when someone asks for a different feeling.

---

## 8. Future Work

I would use `likes_acoustic` in scoring so acoustic listeners are actually represented.
I would add diversity rules so the top 5 is not dominated by near-duplicate energy matches.
I would tune weights with validation profiles instead of manual guessing.

---

## 9. Personal Reflection

My biggest learning moment was seeing how one weight change (energy from low influence to high influence) quickly changed almost every top-5 list.
AI tools helped me move faster when creating test profiles, running quick experiments, and drafting explanations, but I still had to double-check outputs by actually running `python -m src.main` and reviewing results myself.
I was surprised that a very simple scoring rule can still feel like a recommendation engine, because repeated patterns like "Gym Hero" appearing for high-energy users looked realistic even without machine learning.
At the same time, that repetition showed me the risk of bias: if one signal is too strong, the system can ignore other user intent.
If I extend this project, I would add acoustic preference into scoring, tune weights with a small validation set, and add a diversity rule so the top songs are not all near-duplicates.
