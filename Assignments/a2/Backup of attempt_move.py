        current_position = self.get_player_position()

        entities = self.get_entities()  # Will return a dictionary of all the entities

        # Step 1: Check if direction is valid
        if direction not in [UP, DOWN, LEFT, RIGHT] or not DIRECTION_DELTAS:
            return False
        # Step 2: Check if position is out of bounds or blocked
        # Check for out of bounds
        if (
            current_position[0] + DIRECTION_DELTAS[direction][0] < 0
            or current_position[0] + DIRECTION_DELTAS[direction][0] >= len(self._maze)
            or current_position[1] + DIRECTION_DELTAS[direction][1] < 0
            or current_position[1] + DIRECTION_DELTAS[direction][1]
            >= len(self._maze[0])
        ):
            return False
            # Check for blocked
        if (
            self._maze[current_position[0] + DIRECTION_DELTAS[direction][0]][
                current_position[1] + DIRECTION_DELTAS[direction][1]
            ].is_blocking()
            == True
        ):
            return False
        # Step 3: Check if player is moving to an entity
        if (
            current_position[0] + DIRECTION_DELTAS[direction][0],
            current_position[1] + DIRECTION_DELTAS[direction][1],
        ) in entities:
            # Check if entity is a crate
            if (
                current_position[0] + DIRECTION_DELTAS[direction][0],
                current_position[1] + DIRECTION_DELTAS[direction][1],
            ) in self._crate_position:
                # Check if crate can be pushed
                if (
                    current_position[0]
                    + current_position[0]
                    + DIRECTION_DELTAS[direction][0],
                    current_position[1]
                    + current_position[1]
                    + DIRECTION_DELTAS[direction][1],
                ) == Tile or Entity:
                    return False
                else:
                    # Move the crate and then the player
                    # Update crate position
                    self._crate_position.remove(
                        (
                            current_position[0] + DIRECTION_DELTAS[direction][0],
                            current_position[1] + DIRECTION_DELTAS[direction][1],
                        )
                    )
                    self._crate_position.append(
                        (
                            current_position[0]
                            + current_position[0]
                            + DIRECTION_DELTAS[direction][0],
                            current_position[1]
                            + current_position[1]
                            + DIRECTION_DELTAS[direction][1],
                        )
                    )
                    # Update player position
                    self._player_position = (
                        current_position[0] + DIRECTION_DELTAS[direction][0],
                        current_position[1] + DIRECTION_DELTAS[direction][1],
                    )
            # Check if entity is a potion
            elif (
                current_position[0] + DIRECTION_DELTAS[direction][0],
                current_position[1] + DIRECTION_DELTAS[direction][1],
            ) in self._potion_position:
                # Check which potion

                # Apply effect of potion to player
                self._player.apply_effect(
                    self._entities[
                        (
                            current_position[0] + DIRECTION_DELTAS[direction][0],
                            current_position[1] + DIRECTION_DELTAS[direction][1],
                        )
                    ].effect()
                )

                # Move player
                self._player_position = (
                    current_position[0] + DIRECTION_DELTAS[direction][0],
                    current_position[1] + DIRECTION_DELTAS[direction][1],
                )
            # Check if entity is a goal
            elif (
                current_position[0] + DIRECTION_DELTAS[direction][0],
                current_position[1] + DIRECTION_DELTAS[direction][1],
            ) in self._goal_position:
                # Move player
                self._player_position = (
                    current_position[0] + DIRECTION_DELTAS[direction][0],
                    current_position[1] + DIRECTION_DELTAS[direction][1],
                )
        # Step 4: Move player
        self._player_position = (
            current_position[0] + DIRECTION_DELTAS[direction][0],
            current_position[1] + DIRECTION_DELTAS[direction][1],
        )

        # Update get_entities with crate position
        self._entities = self.get_entities()

        # Decrease player moves remaining by 1
        self._player.add_moves_remaining(-1)
        return True