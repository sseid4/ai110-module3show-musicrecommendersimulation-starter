# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One weakness is that the current scoring can create an energy-based filter bubble, especially after increasing the energy weight in the sensitivity experiment. Songs with similar energy values repeatedly dominate the top results, even when the mood signal conflicts with user intent (for example, high-energy plus sad profiles still surface mostly hype tracks). This can under-serve users with mixed or nuanced tastes because the linear energy-gap formula is strong and always active for every song. The system also ignores `likes_acoustic`, so users who care about acoustic texture are not represented in ranking decisions.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Adversarial Conflict (High Energy + Sad), and Edge Case (Unknown Genre + Very Low Energy). For each profile, I ran the system and reviewed the top 5 songs to see whether the results matched the requested vibe. I also ran a sensitivity experiment by changing the weights so energy mattered more and genre mattered less, then compared how the top 5 changed. The biggest surprise was how often "Gym Hero" stayed near the top for multiple high-energy users, even when their mood request was different. In plain terms, this happens because the model rewards energy similarity very strongly, so a very energetic pop song can keep winning even when someone asks for a different feeling.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
