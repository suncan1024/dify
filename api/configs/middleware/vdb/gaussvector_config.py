from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings


class GaussVectorConfig(BaseSettings):
    """
    Configuration settings for GaussVector
    """

    GaussVector_HOST: str | None = Field(
        description="Hostname or IP address of the GaussVector server(e.g., 'localhost')",
        default=None,
    )

    GaussVector_PORT: PositiveInt = Field(
        description="Port number on which the GaussVector server is listening (default is 6600)",
        default=8800,
    )

    GaussVector_USER: str | None = Field(
        description="Username for authenticating with the GaussVector database",
        default=None,
    )

    GaussVector_PASSWORD: str | None = Field(
        description="Password for authenticating with the GaussVector database",
        default=None,
    )

    GaussVector_DATABASE: str | None = Field(
        description="Name of the GaussVector database to connect to",
        default=None,
    )

    GaussVector_MIN_CONNECTION: PositiveInt = Field(
        description="Min connection of the GaussVector database",
        default=1,
    )

    GaussVector_MAX_CONNECTION: PositiveInt = Field(
        description="Max connection of the GaussVector database",
        default=5,
    )

    GaussVector_ENABLE_PQ: bool = Field(
        description="Enable GaussVector PQ acceleration feature",
        default=False,
    )
