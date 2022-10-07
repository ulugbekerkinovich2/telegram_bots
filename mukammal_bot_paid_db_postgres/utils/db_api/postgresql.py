from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from mukammal_bot_paid_db_postgres.data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
            port=config.DB_PORT,
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def create_table_anketa(self):
        sql = """
        CREATE TABLE IF NOT EXISTS anketa (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(255) NOT NULL,
        email varchar(255) NULL,
        phone_number varchar(11) NOT NULL UNIQUE,
        telegram_id BIGINT NOT NULL UNIQUE );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args_anketa(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_anketa(self, fullname, email, phone_number, telegram_id):
        sql = "INSERT INTO anketa (fullname, email, phone_number,telegram_id) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, fullname, email, phone_number, telegram_id, fetchrow=True)

    async def select_anketa(self):
        # sql = "SELECT COUNT(*) FROM anketa"
        sql = "SELECT * FROM anketa"
        return await self.execute(sql, fetchval=True)

    async def create_table_elon_shogird(self):
        sql = """
        CREATE TABLE IF NOT EXISTS elon_shogird (
        id SERIAL PRIMARY KEY,
        ismi VARCHAR(255) NOT NULL,
        yoshi varchar(255) NOT NULL,
        texnologiya varchar(255) NOT NULL,
        aloqa varchar(255) NOT NULL,
        hudud varchar(255) NOT NULL,
        narxi varchar(255) NOT NULL,
        kasbi varchar(255) NOT NULL,
        murojaat_vaqti varchar(255) NOT NULL,
        maqsad varchar(255) NOT NULL,
        telegram_id BIGINT NOT NULL);
        """
        await self.execute(sql, execute=True)

    async def add_elon_shogird(self, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi, murojaat_vaqti, maqsad,
                               telegram_id):
        sql = "INSERT INTO elon_shogird (ismi, yoshi, texnologiya, aloqa,hudud,narxi,kasbi,murojaat_vaqti,maqsad,telegram_id) VALUES($1, $2, $3 , $4 ,$5 ,$6 ,$7 ,$8 ,$9 , $10) returning *"
        return await self.execute(sql, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi, murojaat_vaqti, maqsad,
                                  telegram_id, fetchrow=True)

    async def delete_elon_shogird(self):
        await self.execute("DELETE FROM elon_shogird WHERE TRUE", execute=True)

    async def create_table_elon_sherik(self):
        sql = """
        CREATE TABLE IF NOT EXISTS elon_sherik (
        id SERIAL PRIMARY KEY,
        ismi VARCHAR(255) NOT NULL,
        yoshi varchar(255) NOT NULL,
        texnologiya varchar(255) NOT NULL,
        aloqa varchar(255) NOT NULL,
        hudud varchar(255) NOT NULL,
        narxi varchar(255) NOT NULL,
        kasbi varchar(255) NOT NULL,
        murojaat_vaqti varchar(255) NOT NULL,
        maqsad varchar(255) NOT NULL,
        telegram_id BIGINT NOT NULL);
        """
        await self.execute(sql, execute=True)

    async def add_elon_sherik(self, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi, murojaat_vaqti, maqsad,
                              telegram_id):
        sql = "INSERT INTO elon_sherik (ismi, yoshi, texnologiya, aloqa,hudud,narxi,kasbi,murojaat_vaqti,maqsad,telegram_id) VALUES($1, $2, $3 , $4 ,$5 ,$6 ,$7 ,$8 ,$9 , $10) returning *"
        return await self.execute(sql, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi, murojaat_vaqti, maqsad,
                                  telegram_id, fetchrow=True)

    async def delete_elon_sherik(self):
        await self.execute("DELETE FROM elon_sherik WHERE TRUE", execute=True)

    async def create_table_elon_xodim(self):
        sql = """
        CREATE TABLE IF NOT EXISTS elon_xodim (
        id SERIAL PRIMARY KEY,
        idora_nomi varchar(255) NOT NULL,
        texnologiya varchar(255) NOT NULL,
        aloqa varchar(255) NOT NULL,
        hudud varchar(255) NOT NULL,
        masul_ismi varchar(255) NOT NULL,
        murojaat_vaqti varchar(255) NOT NULL,
        ish_vaqti varchar(255) NOT NULL,
        narxi varchar(255) NOT NULL,
        qoshimcha_malumot varchar(255) NOT NULL,
        telegram_id BIGINT NOT NULL);
        """
        await self.execute(sql, execute=True)

    async def add_elon_xodim(self, idora_nomi, texnologiya, aloqa, hudud, masul_ismi, murojaat_vaqti, ish_vaqti, narxi,
                             qoshimcha_malumot, telegram_id):
        sql = "INSERT INTO elon_xodim (idora_nomi, texnologiya, aloqa,hudud,masul_ismi,murojaat_vaqti,ish_vaqti,narxi,qoshimcha_malumot,telegram_id) VALUES($1, $2, $3 , $4 ,$5 ,$6 ,$7 ,$8 ,$9 , $10) returning *"
        return await self.execute(sql, idora_nomi, texnologiya, aloqa, hudud, masul_ismi, murojaat_vaqti, ish_vaqti,
                                  narxi, qoshimcha_malumot, telegram_id, fetchrow=True)

    async def delete_elon_xodim(self):
        await self.execute("DELETE FROM elon_xodim WHERE TRUE", execute=True)

    async def create_table_elon_ustoz_kerak(self):
        sql = """
           CREATE TABLE IF NOT EXISTS elon_ustoz_kerak (
           id SERIAL PRIMARY KEY,
           ismi varchar(255) NOT NULL,
           yoshi varchar(255) NOT NULL,
           texnologiya varchar(255) NOT NULL,
           aloqa varchar(255) NOT NULL,
           hudud varchar(255) NOT NULL,
           narxi varchar(255) NOT NULL,
           kasbi varchar(255) NOT NULL,
           murojaat_vaqti varchar(255) NOT NULL,
           maqsad varchar(255) NOT NULL,
           telegram_id BIGINT NOT NULL);
           """
        await self.execute(sql, execute=True)

    async def add_elon_ustoz_kerak(self, telegram_id, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi,
                                   murojaat_vaqti, maqsad):
        sql = "INSERT INTO elon_ustoz_kerak ( telegram_id, ismi,yoshi, texnologiya, aloqa, hudud,narxi, kasbi, murojaat_vaqti, maqsad,) VALUES($1, $2, $3 , $4 ,$5 ,$6 ,$7 ,$8 ,$9 , $10) returning *"
        return await self.execute(sql, telegram_id, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi,
                                  murojaat_vaqti, maqsad, fetchrow=True)

    async def delete_elon_ustoz_kerak(self):
        await self.execute("DELETE FROM elon_ustoz_kerak WHERE TRUE", execute=True)

    async def create_table_elon_Ish_joyi_kerak(self):
        sql = """
           CREATE TABLE IF NOT EXISTS elon_Ish_joyi_kerak (
           id SERIAL PRIMARY KEY,
           ismi varchar(255) NOT NULL,
           yoshi varchar(255) NOT NULL,
           texnologiya varchar(255) NOT NULL,
           aloqa varchar(255) NOT NULL,
           hudud varchar(255) NOT NULL,
           narxi varchar(255) NOT NULL,
           kasbi varchar(255) NOT NULL,
           murojaat_vaqti varchar(255) NOT NULL,
           maqsad varchar(255) NOT NULL,
           telegram_id BIGINT NOT NULL);
           """
        await self.execute(sql, execute=True)

    async def add_elon_Ish_joyi_kerak(self, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi,
                                      murojaat_vaqti,
                                      maqsad, telegram_id):
        sql = "INSERT INTO elon_Ish_joyi_kerak (ismi,yoshi, texnologiya, aloqa, hudud,narxi, kasbi, murojaat_vaqti, maqsad, telegram_id) VALUES($1, $2, $3 , $4 ,$5 ,$6 ,$7 ,$8, $9,$10) returning *"
        return await self.execute(sql, ismi, yoshi, texnologiya, aloqa, hudud, narxi, kasbi, murojaat_vaqti,
                                  maqsad, telegram_id, fetchrow=True)

    async def delete_elon_Ish_joyi_kerak(self):
        await self.execute("DELETE FROM elon_Ish_joyi_kerak WHERE TRUE", execute=True)
