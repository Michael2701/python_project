from App.Migrations.UsersMigration import UsersMigration
from App.Migrations.GeneticFileMigration import GeneticFileMigration
from App.Migrations.GeneMigration import GeneMigration
from App.Migrations.InterferenceMigration import InterferenceMigration


class MigrationsFactory:

    migrations: list

    def __init__(self):
        self.migrations = [
            [InterferenceMigration, 'interference'],
            [UsersMigration, 'users'],
            [GeneticFileMigration, 'files'],
            [GeneMigration, 'genes']
        ]

    def run_migrations(self):
        print("creating data base")
        for migration, table in self.migrations:
            print("creating "+table+" table...")
            migration()


mf = MigrationsFactory()
mf.run_migrations()
