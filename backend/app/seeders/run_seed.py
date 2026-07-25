from app.seeders.seed_data import seed_users


def run_seed() -> None:
    seed_users()
