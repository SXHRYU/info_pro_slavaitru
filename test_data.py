import os
import faker


def generate_fake_data(file_path: str | os.PathLike, /, count: int) -> None:
    f = faker.Faker("ru_RU")

    with open(file_path, "w", encoding="utf-8") as file:
        for _ in range(count):
            # fmt: off
            file.write(
                (
                    f.date() + "\t"
                    + f.bban() + "\t"
                    + f.text().replace("\n", " ") + "\t"
                    + f.pricetag() + "\t"
                    + f.email() + "\t"
                    + f.phone_number() + "\t"
                    + f.address() + "\t"
                    + f.time() + "\t"
                    + f.businesses_inn() + "\n"
                )
            )
            # fmt: on
