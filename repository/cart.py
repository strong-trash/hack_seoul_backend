from sqlalchemy.orm import joinedload

from orm.cart import Cart
from repository.base import Repository


class CartRepository(Repository):
    model = Cart

    def get_by_user_id(self, user_id: int):
        return self.session.query(
            self.model
        ).filter(
            self.model.user_id == user_id
        ).options(
            joinedload(Cart.product)
        ).all()
