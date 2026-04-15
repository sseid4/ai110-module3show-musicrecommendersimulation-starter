"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "calm",
            "target_energy": 0.25,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "angry",
            "target_energy": 0.95,
            "likes_acoustic": False,
        },
        # System Evaluation: adversarial/edge-case profiles to probe scoring behavior.
        "Adversarial Conflict (High Energy + Sad)": {
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.9,
            "likes_acoustic": True,
        },
        "Edge Case: Unknown Genre + Very Low Energy": {
            "favorite_genre": "synthwave",
            "favorite_mood": "happy",
            "target_energy": 0.0,
            "likes_acoustic": False,
        },
    }

    print("\nSystem Evaluation: Top 5 recommendations per profile\n")
    for profile_name, taste_profile in profiles.items():
        recommendations = recommend_songs(taste_profile, songs, k=5)

        print(f"=== {profile_name} ===")
        for idx, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = [reason.strip() for reason in explanation.split(",") if reason.strip()]

            print(f"{idx}. {song['title']} - {song['artist']}")
            print(f"   Final score: {score:.2f}")
            print("   Reasons:")
            for reason in reasons:
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
