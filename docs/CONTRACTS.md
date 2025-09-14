# Contracts - agreed function signatures

| Module        | Function / Class        | Signature                                          | Notes / Example I/O |
|---------------|-------------------------|---------------------------------------------------|---------------------|
| pose_engine   | get_keypoints           | def get_keypoints(frame_bgr) -> dict              | {"left_hip": (x,y,conf), ...} |
| exercise_logic| SquatCounter.update     | def update(self, keypoints: dict) -> dict         | {"reps":int,"state":"UP"/"DOWN","knee_angle":float,"form_flags":[...]} |
| analytics     | compare_to_benchmark    | def compare_to_benchmark(user_reps:int, exercise:str, age:str, gender:str) -> dict | {"user_reps":X,"avg_reps":Y,"percent_diff":Z} |
| gamification  | award_badges            | def award_badges(history:list, latest_session:dict) -> list | ["First 10 Squats", ...] |
