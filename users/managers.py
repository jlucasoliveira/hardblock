from typing import Any, Dict

from django.contrib.auth.base_user import BaseUserManager

from core.managers import BaseManager


class UserManager(BaseManager, BaseUserManager):
    def _create_user(
        self,
        username: str,
        email: str,
        name: str,
        password: str,
        *,
        is_staff: bool,
        is_superuser: bool,
        **kwargs: Dict[str, Any],
    ):
        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
            name=name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(
        self,
        username: str,
        email: str,
        name: str,
        password: str,
        **kwargs: Dict[str, Any],
    ):
        return self._create_user(
            username,
            email,
            name,
            password,
            **kwargs,
            is_staff=False,
            is_superuser=False,
        )

    def create_superuser(
        self,
        username: str,
        email: str,
        name: str,
        password: str,
        **kwargs: Dict[str, Any],
    ):
        return self._create_user(
            username,
            email,
            name,
            password,
            **kwargs,
            is_staff=True,
            is_superuser=True,
        )
