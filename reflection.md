# Reflection: Profile Pair Comparisons

These comments compare how each pair of user profiles changed the top recommendations and why that difference makes sense.

1. High-Energy Pop vs Chill Lofi: High-Energy Pop pushes songs like "Gym Hero" and "Sunrise City" to the top because they are close to 0.9 energy, while Chill Lofi favors softer tracks because its target energy is much lower (0.25).
2. High-Energy Pop vs Deep Intense Rock: Both profiles like high energy, so they share some fast songs, but the rock profile surfaces "Storm Runner" because of genre alignment while the pop profile keeps more pop songs near the top.
3. High-Energy Pop vs Adversarial Conflict (High Energy + Sad): The outputs are very similar because both profiles ask for high energy and pop; changing mood to sad does not move results much when energy is weighted strongly.
4. High-Energy Pop vs Edge Case (Unknown Genre + Very Low Energy): The edge case flips the list toward low-energy songs, showing that target energy can overpower genre when genre is rare or missing.
5. Chill Lofi vs Deep Intense Rock: These two profiles separate clearly because one asks for low-energy calm listening and the other asks for intense high-energy listening.
6. Chill Lofi vs Adversarial Conflict (High Energy + Sad): Chill Lofi produces relaxed tracks, while the adversarial profile keeps getting workout-like songs because its high-energy target dominates despite the sad mood request.
7. Chill Lofi vs Edge Case (Unknown Genre + Very Low Energy): Both profiles prefer lower energy than other users, so they overlap in softer songs, but Chill Lofi still benefits from lofi genre matches while the edge case does not.
8. Deep Intense Rock vs Adversarial Conflict (High Energy + Sad): These profiles both return very energetic songs, but rock preference helps "Storm Runner" for the rock user, while pop preference keeps "Gym Hero" strong for the adversarial user.
9. Deep Intense Rock vs Edge Case (Unknown Genre + Very Low Energy): This is the biggest contrast in behavior: one profile selects near-max energy tracks and the other selects low-energy tracks.
10. Adversarial Conflict (High Energy + Sad) vs Edge Case (Unknown Genre + Very Low Energy): The adversarial profile still gets high-energy tracks because energy is high, while the edge case gets calmer tracks because energy is set to 0.0; this shows energy target is the strongest driver.
