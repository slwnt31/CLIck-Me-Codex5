class Developer:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.initial = kwargs["initial"]
        self.bio = kwargs["bio"]
        self.tech_stack = kwargs["tech_stack"]
        self.school = kwargs["school"]
        self.projects = kwargs["projects"]
        self.interests = kwargs["interests"]
        self.philosophy = kwargs["philosophy"]
        self.vibe_coding_experience = kwargs["vibe_coding_experience"]
