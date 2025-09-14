class SquatCounter:
    def __init__(self):
        self.reps = 0

    def update(self, keypoints):
        """
        keypoints: dict -> {"left_knee": (x,y,conf), ...}
        Return a dict:
            {"reps": int, "state": "UP"/"DOWN", "knee_angle": None, "form_flags": []}
        """
        return {"reps": self.reps, "state": "-", "knee_angle": None, "form_flags": []}
