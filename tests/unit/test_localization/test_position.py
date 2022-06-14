import pytest

from localization.position import Position2D, get_distance_between


@pytest.mark.parametrize(
    "first_position, second_position, expected_distance",
    (
        (Position2D(0, 0), Position2D(0, 1), 1),
        (Position2D(0, 1), Position2D(0, 0), 1),
        (Position2D(0, 0), Position2D(0, 5), 5),
        (Position2D(0, 0), Position2D(5, 0), 5),
        (Position2D(0, 0), Position2D(1, 1), 1.41),
        (Position2D(0, 0), Position2D(16, 15), 21.93),
    ),
)
def test_get_distance_between_returns_correct_distance(
    first_position, second_position, expected_distance
):
    # WHEN & THEN
    assert get_distance_between(first_position, second_position) == expected_distance
