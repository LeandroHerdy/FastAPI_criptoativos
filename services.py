from database.models import User, Favorite
from database.connection import async_session
from sqlalchemy import delete
from sqlalchemy.future import select
from aiohttp import ClientSession
from datetime import date, timedelta


class UserService:

    async def create_user(name: str):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id==user_id))
            await session.commit()

    async def list_user():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()

    async def get_by_id(user_id):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.id==user_id))
            return result.scalars()


class FavoriteService:

    async def add_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            session.add(Favorite(user_id=user_id, symbol=symbol))
            await session.commit()

    async def remove_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            await session.execute(delete(Favorite).where(Favorite.user_id==user_id, Favorite.symbol==symbol))
            await session.commit()


class AssetService:
    async def day_summary(symbol:str):
        async with ClientSession() as session:
            yesterday = date.today() - timedelta(days=1)
            url = f'https://www.mercadobiticion.net/api/{symbol}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}/'
            response = await session.get(url)
            data = await response.json()
            return {
                'highest': data['highest'],
                'lowest': data['highest'],
                'symbol': data['symbol']
            }