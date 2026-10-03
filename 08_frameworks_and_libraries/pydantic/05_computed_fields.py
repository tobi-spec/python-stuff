from pydantic import BaseModel,  ValidationError, computed_field


class SocialMediaUser(BaseModel):
    first_name: str
    last_name: str = None
    follower: int

    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.first_name}'

    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower >= 10000

try:
    user = SocialMediaUser(
        first_name='John',
        last_name='Doe',
        follower=1234
    )
    print(user)
except ValidationError as e:
    print(e)


try:
    user = SocialMediaUser(
        first_name='GamerFreak',
        follower=100000
    )
    print(user)
except ValidationError as e:
    print(e)
