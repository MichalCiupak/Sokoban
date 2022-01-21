from player import Player


def test_creat_player():
    player = Player((1, 1))
    assert player
    assert player.facing_right


def test_player_position():
    player = Player((1, 1))
    assert player.rect.topleft == (1, 1)


def test_player_animate():
    player = Player((1, 1))
    image = player.image
    assert image == player.image
    player.facing_right = False
    player.animate()
    assert image != player.image
