import faker


f = faker.Faker("ru_RU")

with open("test.txt", "w", encoding="utf-8") as file:
    for _ in range(100):
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
